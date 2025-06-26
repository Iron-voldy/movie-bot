import logging
import gridfs
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Any, Tuple
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorGridFS
from pymongo.errors import DuplicateKeyError, OperationFailure, ServerSelectionTimeoutError
from pymongo import ASCENDING, DESCENDING, TEXT
from config.subtitle_config import CACHE_CONFIG, SUBTITLE_SETTINGS
from info import SUBTITLE_DB_URI, SUBTITLE_DB_NAME
import gzip
import json
import asyncio

logger = logging.getLogger(__name__)

class SubtitleStorage:
    """Handles subtitle storage operations using MongoDB and GridFS"""
    
    def __init__(self, db_uri: str = None, db_name: str = None):
        self.db_uri = db_uri or SUBTITLE_DB_URI
        self.db_name = db_name or SUBTITLE_DB_NAME
        self.client = None
        self.db = None
        self.fs = None
        self.subtitles_collection = None
        self.movies_collection = None
        self.usage_stats_collection = None
        self.api_logs_collection = None
        self.cache_duration = SUBTITLE_SETTINGS['cache_duration']
        self._connection_lock = asyncio.Lock()
        self._connected = False
        
    async def connect(self):
        """Initialize database connection with retry logic"""
        async with self._connection_lock:
            if self._connected:
                return
                
            max_retries = 3
            retry_delay = 2
            
            for attempt in range(max_retries):
                try:
                    self.client = AsyncIOMotorClient(
                        self.db_uri,
                        serverSelectionTimeoutMS=5000,
                        connectTimeoutMS=10000,
                        socketTimeoutMS=10000,
                        maxPoolSize=50,
                        minPoolSize=5
                    )
                    
                    # Test connection
                    await self.client.admin.command('ping')
                    
                    self.db = self.client[self.db_name]
                    self.fs = AsyncIOMotorGridFS(self.db)
                    self.subtitles_collection = self.db.subtitles_metadata
                    self.movies_collection = self.db.movies_subtitles
                    self.usage_stats_collection = self.db.usage_statistics
                    self.api_logs_collection = self.db.api_logs
                    
                    # Create indexes for better performance
                    await self._create_indexes()
                    
                    self._connected = True
                    logger.info("Connected to subtitle database successfully")
                    return
                    
                except (ServerSelectionTimeoutError, OperationFailure) as e:
                    logger.warning(f"Connection attempt {attempt + 1} failed: {e}")
                    if attempt < max_retries - 1:
                        await asyncio.sleep(retry_delay * (attempt + 1))
                    else:
                        logger.error(f"Failed to connect to subtitle database after {max_retries} attempts")
                        raise
                except Exception as e:
                    logger.error(f"Unexpected error connecting to subtitle database: {e}")
                    raise
    
    async def _create_indexes(self):
        """Create necessary database indexes for optimal performance"""
        try:
            # Indexes for subtitle metadata
            index_operations = [
                # Unique index for movie-language combination
                (self.subtitles_collection, [("movie_id", ASCENDING), ("language", ASCENDING)], {"unique": True, "background": True}),
                
                # TTL index for automatic cleanup
                (self.subtitles_collection, [("expires_at", ASCENDING)], {"expireAfterSeconds": 0, "background": True}),
                
                # Performance indexes
                (self.subtitles_collection, [("created_at", DESCENDING)], {"background": True}),
                (self.subtitles_collection, [("quality_score", DESCENDING)], {"background": True}),
                (self.subtitles_collection, [("provider", ASCENDING)], {"background": True}),
                (self.subtitles_collection, [("language", ASCENDING)], {"background": True}),
                (self.subtitles_collection, [("cached_content", ASCENDING)], {"background": True}),
                
                # Compound indexes for common queries
                (self.subtitles_collection, [("movie_id", ASCENDING), ("quality_score", DESCENDING)], {"background": True}),
                (self.subtitles_collection, [("language", ASCENDING), ("quality_score", DESCENDING)], {"background": True}),
                
                # Indexes for movie-subtitle relationships
                (self.movies_collection, [("imdb_id", ASCENDING)], {"unique": True, "sparse": True, "background": True}),
                (self.movies_collection, [("title", TEXT)], {"background": True}),
                (self.movies_collection, [("last_checked", DESCENDING)], {"background": True}),
                (self.movies_collection, [("subtitle_count", DESCENDING)], {"background": True}),
                
                # Indexes for usage statistics
                (self.usage_stats_collection, [("date", DESCENDING)], {"background": True}),
                (self.usage_stats_collection, [("movie_id", ASCENDING), ("date", DESCENDING)], {"background": True}),
                (self.usage_stats_collection, [("language", ASCENDING), ("date", DESCENDING)], {"background": True}),
                
                # Indexes for API logs
                (self.api_logs_collection, [("timestamp", DESCENDING)], {"background": True}),
                (self.api_logs_collection, [("provider", ASCENDING), ("timestamp", DESCENDING)], {"background": True}),
                (self.api_logs_collection, [("status", ASCENDING)], {"background": True})
            ]
            
            # Create indexes concurrently
            tasks = []
            for collection, index_spec, options in index_operations:
                task = collection.create_index(index_spec, **options)
                tasks.append(task)
            
            await asyncio.gather(*tasks, return_exceptions=True)
            logger.info("Database indexes created successfully")
            
        except Exception as e:
            logger.error(f"Error creating indexes: {e}")
    
    async def store_subtitle_metadata(self, movie_id: str, language: str, 
                                    subtitle_data: Dict[str, Any]) -> bool:
        """Store subtitle metadata with comprehensive information"""
        try:
            if not self._connected:
                await self.connect()
                
            document = {
                "movie_id": movie_id,
                "language": language,
                "provider": subtitle_data.get('provider', 'unknown'),
                "subtitle_id": subtitle_data.get('id'),
                "download_count": subtitle_data.get('download_count', 0),
                "quality_score": subtitle_data.get('quality_score', 0),
                "format": subtitle_data.get('format', 'srt'),
                "filename": subtitle_data.get('filename', ''),
                "release": subtitle_data.get('release', ''),
                "file_size": subtitle_data.get('file_size', 0),
                "encoding": subtitle_data.get('encoding', 'utf-8'),
                "fps": subtitle_data.get('fps', None),
                "cd_count": subtitle_data.get('cd_count', 1),
                "hearing_impaired": subtitle_data.get('hearing_impaired', False),
                "machine_translated": subtitle_data.get('machine_translated', False),
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow(),
                "expires_at": datetime.utcnow() + timedelta(seconds=self.cache_duration),
                "download_url": subtitle_data.get('url', ''),
                "cached_content": False,
                "gridfs_file_id": None,
                "local_downloads": 0,
                "last_downloaded": None,
                "verification_status": "pending",  # pending, verified, failed
                "user_ratings": [],
                "sync_offset": 0.0  # Time offset in seconds
            }
            
            # Use upsert to update existing records
            result = await self.subtitles_collection.replace_one(
                {"movie_id": movie_id, "language": language},
                document,
                upsert=True
            )
            
            # Update movie subtitle info
            await self._update_movie_subtitle_count(movie_id)
            
            logger.info(f"Stored subtitle metadata for {movie_id} ({language})")
            return True
            
        except Exception as e:
            logger.error(f"Error storing subtitle metadata: {e}")
            return False
    
    async def get_subtitle_metadata(self, movie_id: str, language: str) -> Optional[Dict]:
        """Get subtitle metadata with automatic cleanup of expired entries"""
        try:
            if not self._connected:
                await self.connect()
                
            result = await self.subtitles_collection.find_one({
                "movie_id": movie_id,
                "language": language,
                "expires_at": {"$gt": datetime.utcnow()}
            })
            
            if result:
                # Convert ObjectId to string
                result['_id'] = str(result['_id'])
                logger.debug(f"Found subtitle metadata for {movie_id} ({language})")
                
                # Update access statistics
                await self._record_access(movie_id, language)
            
            return result
            
        except Exception as e:
            logger.error(f"Error getting subtitle metadata: {e}")
            return None
    
    async def cache_subtitle_content(self, movie_id: str, language: str, 
                                   content: str, compress: bool = True) -> Optional[str]:
        """Cache subtitle content in GridFS with optional compression"""
        try:
            if not self._connected:
                await self.connect()
                
            filename = f"{movie_id}_{language}.srt"
            
            # Prepare content for storage
            if compress:
                content_bytes = gzip.compress(content.encode('utf-8'))
                content_type = "application/gzip"
            else:
                content_bytes = content.encode('utf-8')
                content_type = "text/plain"
            
            # Delete existing file if it exists
            async for grid_file in self.fs.find({"filename": filename}):
                await self.fs.delete(grid_file._id)
            
            # Upload new content
            file_id = await self.fs.upload_from_stream(
                filename,
                content_bytes,
                metadata={
                    "movie_id": movie_id,
                    "language": language,
                    "cached_at": datetime.utcnow(),
                    "compressed": compress,
                    "content_type": content_type,
                    "original_size": len(content),
                    "compressed_size": len(content_bytes),
                    "encoding": "utf-8",
                    "version": "1.0"
                }
            )
            
            # Update metadata to indicate content is cached
            await self.subtitles_collection.update_one(
                {"movie_id": movie_id, "language": language},
                {
                    "$set": {
                        "cached_content": True,
                        "gridfs_file_id": str(file_id),
                        "cache_size": len(content_bytes),
                        "updated_at": datetime.utcnow()
                    }
                }
            )
            
            logger.info(f"Cached subtitle content for {movie_id} ({language}) - {len(content_bytes)} bytes")
            return str(file_id)
            
        except Exception as e:
            logger.error(f"Error caching subtitle content: {e}")
            return None
    
    async def get_cached_subtitle_content(self, movie_id: str, language: str) -> Optional[str]:
        """Get cached subtitle content from GridFS with decompression support"""
        try:
            if not self._connected:
                await self.connect()
                
            filename = f"{movie_id}_{language}.srt"
            
            # Find the file in GridFS
            grid_file = await self.fs.find_one({"filename": filename})
            if not grid_file:
                return None
            
            # Download the content
            content_bytes = await grid_file.read()
            metadata = grid_file.metadata or {}
            
            # Decompress if necessary
            if metadata.get('compressed', False):
                try:
                    content = gzip.decompress(content_bytes).decode('utf-8')
                except:
                    # Fallback if decompression fails
                    content = content_bytes.decode('utf-8', errors='replace')
            else:
                content = content_bytes.decode('utf-8', errors='replace')
            
            # Record cache hit
            await self._record_cache_hit(movie_id, language)
            
            logger.debug(f"Retrieved cached subtitle content for {movie_id} ({language})")
            return content
            
        except Exception as e:
            logger.error(f"Error getting cached subtitle content: {e}")
            return None
    
    async def store_movie_subtitle_info(self, imdb_id: str, title: str, 
                                      available_languages: List[str], 
                                      additional_info: Dict[str, Any] = None) -> bool:
        """Store comprehensive movie subtitle availability information"""
        try:
            if not self._connected:
                await self.connect()
                
            document = {
                "imdb_id": imdb_id,
                "title": title,
                "normalized_title": title.lower().strip(),
                "available_languages": available_languages,
                "last_checked": datetime.utcnow(),
                "subtitle_count": len(available_languages),
                "check_count": 1,
                "created_at": datetime.utcnow(),
                "updated_at": datetime.utcnow()
            }
            
            # Add additional information if provided
            if additional_info:
                document.update({
                    "year": additional_info.get('year'),
                    "genre": additional_info.get('genre', []),
                    "runtime": additional_info.get('runtime'),
                    "rating": additional_info.get('rating'),
                    "plot": additional_info.get('plot', ''),
                    "poster_url": additional_info.get('poster_url'),
                    "is_series": additional_info.get('is_series', False),
                    "season": additional_info.get('season'),
                    "episode": additional_info.get('episode')
                })
            
            # Upsert with increment of check_count
            result = await self.movies_collection.update_one(
                {"imdb_id": imdb_id},
                {
                    "$set": document,
                    "$inc": {"check_count": 1}
                },
                upsert=True
            )
            
            logger.info(f"Stored movie subtitle info for {imdb_id} - {len(available_languages)} languages")
            return True
            
        except Exception as e:
            logger.error(f"Error storing movie subtitle info: {e}")
            return False
    
    async def get_movie_subtitle_info(self, imdb_id: str = None, title: str = None) -> Optional[Dict]:
        """Get movie subtitle availability information by IMDB ID or title"""
        try:
            if not self._connected:
                await self.connect()
                
            query = {}
            if imdb_id:
                query["imdb_id"] = imdb_id
            elif title:
                query["normalized_title"] = title.lower().strip()
            else:
                return None
                
            result = await self.movies_collection.find_one(query)
            
            if result:
                result['_id'] = str(result['_id'])
                logger.debug(f"Found movie subtitle info for {imdb_id or title}")
            
            return result
            
        except Exception as e:
            logger.error(f"Error getting movie subtitle info: {e}")
            return None
    
    async def search_movies_by_title(self, title: str, limit: int = 10) -> List[Dict]:
        """Search for movies by title with fuzzy matching"""
        try:
            if not self._connected:
                await self.connect()
                
            # Try exact text search first
            cursor = self.movies_collection.find(
                {"$text": {"$search": title}},
                {"_id": 0, "imdb_id": 1, "title": 1, "available_languages": 1, 
                 "subtitle_count": 1, "year": 1, "genre": 1, "rating": 1}
            ).sort([("subtitle_count", DESCENDING)]).limit(limit)
            
            results = await cursor.to_list(length=limit)
            
            # If no exact matches, try partial matching
            if not results:
                normalized_title = title.lower().strip()
                cursor = self.movies_collection.find(
                    {"normalized_title": {"$regex": normalized_title, "$options": "i"}},
                    {"_id": 0, "imdb_id": 1, "title": 1, "available_languages": 1, 
                     "subtitle_count": 1, "year": 1, "genre": 1, "rating": 1}
                ).sort([("subtitle_count", DESCENDING)]).limit(limit)
                
                results = await cursor.to_list(length=limit)
            
            logger.info(f"Found {len(results)} movies matching '{title}'")
            return results
            
        except Exception as e:
            logger.error(f"Error searching movies by title: {e}")
            return []
    
    async def get_popular_languages(self, limit: int = 20) -> List[Dict]:
        """Get most popular subtitle languages with detailed statistics"""
        try:
            if not self._connected:
                await self.connect()
                
            pipeline = [
                {
                    "$group": {
                        "_id": "$language",
                        "count": {"$sum": 1},
                        "avg_quality": {"$avg": "$quality_score"},
                        "total_downloads": {"$sum": "$download_count"},
                        "avg_local_downloads": {"$avg": "$local_downloads"},
                        "providers": {"$addToSet": "$provider"},
                        "last_updated": {"$max": "$updated_at"}
                    }
                },
                {
                    "$addFields": {
                        "popularity_score": {
                            "$add": [
                                {"$multiply": ["$count", 1]},
                                {"$multiply": ["$avg_quality", 0.1]},
                                {"$multiply": ["$total_downloads", 0.001]}
                            ]
                        }
                    }
                },
                {"$sort": {"popularity_score": DESCENDING}},
                {"$limit": limit}
            ]
            
            cursor = self.subtitles_collection.aggregate(pipeline)
            results = await cursor.to_list(length=limit)
            
            logger.info(f"Retrieved {len(results)} popular languages")
            return results
            
        except Exception as e:
            logger.error(f"Error getting popular languages: {e}")
            return []
    
    async def cleanup_expired_subtitles(self) -> Dict[str, int]:
        """Clean up expired subtitle entries and orphaned files"""
        try:
            if not self._connected:
                await self.connect()
                
            cleanup_stats = {
                "expired_metadata": 0,
                "orphaned_files": 0,
                "total_size_freed": 0
            }
            
            # Delete expired metadata
            expired_cursor = self.subtitles_collection.find({
                "expires_at": {"$lt": datetime.utcnow()}
            }, {"gridfs_file_id": 1})
            
            expired_file_ids = []
            async for doc in expired_cursor:
                if doc.get("gridfs_file_id"):
                    expired_file_ids.append(doc["gridfs_file_id"])
            
            # Delete expired metadata entries
            result = await self.subtitles_collection.delete_many({
                "expires_at": {"$lt": datetime.utcnow()}
            })
            cleanup_stats["expired_metadata"] = result.deleted_count
            
            # Clean up orphaned GridFS files
            orphaned_count, size_freed = await self._cleanup_orphaned_gridfs_files(expired_file_ids)
            cleanup_stats["orphaned_files"] = orphaned_count
            cleanup_stats["total_size_freed"] = size_freed
            
            # Update movie subtitle counts
            await self._update_all_movie_subtitle_counts()
            
            logger.info(f"Cleanup completed: {cleanup_stats}")
            return cleanup_stats
            
        except Exception as e:
            logger.error(f"Error cleaning up expired subtitles: {e}")
            return {"expired_metadata": 0, "orphaned_files": 0, "total_size_freed": 0}
    
    async def _cleanup_orphaned_gridfs_files(self, expired_file_ids: List[str] = None) -> Tuple[int, int]:
        """Clean up GridFS files that no longer have metadata references"""
        try:
            orphaned_count = 0
            total_size_freed = 0
            
            # Get all GridFS file IDs
            gridfs_files = {}
            async for grid_file in self.fs.find():
                gridfs_files[str(grid_file._id)] = grid_file.length
            
            # Get all referenced file IDs from metadata
            referenced_files = set()
            async for doc in self.subtitles_collection.find(
                {"gridfs_file_id": {"$exists": True, "$ne": None}},
                {"gridfs_file_id": 1}
            ):
                file_id = doc.get("gridfs_file_id")
                if file_id:
                    referenced_files.add(str(file_id))
            
            # Add expired file IDs to cleanup list
            if expired_file_ids:
                referenced_files.difference_update(expired_file_ids)
            
            # Delete orphaned files
            for file_id, file_size in gridfs_files.items():
                if file_id not in referenced_files:
                    try:
                        await self.fs.delete(file_id)
                        orphaned_count += 1
                        total_size_freed += file_size
                    except Exception as e:
                        logger.error(f"Error deleting orphaned file {file_id}: {e}")
            
            if orphaned_count > 0:
                logger.info(f"Cleaned up {orphaned_count} orphaned GridFS files, freed {total_size_freed} bytes")
                
            return orphaned_count, total_size_freed
            
        except Exception as e:
            logger.error(f"Error cleaning up orphaned GridFS files: {e}")
            return 0, 0
    
    async def get_database_stats(self) -> Dict[str, Any]:
        """Get comprehensive database statistics"""
        try:
            if not self._connected:
                await self.connect()
                
            # Get collection stats
            subtitle_count = await self.subtitles_collection.count_documents({})
            movie_count = await self.movies_collection.count_documents({})
            cached_subtitle_count = await self.subtitles_collection.count_documents({"cached_content": True})
            
            # Get database size
            stats = await self.db.command("dbStats")
            
            # Get GridFS stats
            gridfs_files = []
            total_gridfs_size = 0
            async for f in self.fs.find():
                gridfs_files.append(f)
                total_gridfs_size += f.length
            
            # Get language distribution
            language_stats = await self.get_popular_languages(15)
            
            # Get provider distribution
            provider_pipeline = [
                {"$group": {"_id": "$provider", "count": {"$sum": 1}}},
                {"$sort": {"count": DESCENDING}}
            ]
            provider_cursor = self.subtitles_collection.aggregate(provider_pipeline)
            provider_stats = await provider_cursor.to_list(length=10)
            
            # Get quality distribution
            quality_pipeline = [
                {
                    "$bucket": {
                        "groupBy": "$quality_score",
                        "boundaries": [0, 50, 100, 500, 1000, float('inf')],
                        "default": "unknown",
                        "output": {"count": {"$sum": 1}}
                    }
                }
            ]
            quality_cursor = self.subtitles_collection.aggregate(quality_pipeline)
            quality_stats = await quality_cursor.to_list(length=10)
            
            # Calculate cache efficiency
            cache_efficiency = (cached_subtitle_count / subtitle_count * 100) if subtitle_count > 0 else 0
            
            return {
                "subtitle_entries": subtitle_count,
                "movie_entries": movie_count,
                "cached_subtitles": cached_subtitle_count,
                "cache_efficiency": round(cache_efficiency, 2),
                "database_size": stats.get("dataSize", 0),
                "storage_size": stats.get("storageSize", 0),
                "index_size": stats.get("indexSize", 0),
                "gridfs_files": len(gridfs_files),
                "gridfs_size": total_gridfs_size,
                "collections": stats.get("collections", 0),
                "languages": language_stats,
                "providers": provider_stats,
                "quality_distribution": quality_stats,
                "avg_subtitle_size": total_gridfs_size // len(gridfs_files) if gridfs_files else 0
            }
            
        except Exception as e:
            logger.error(f"Error getting database stats: {e}")
            return {}
    
    async def get_subtitle_by_quality(self, movie_id: str, language: str, 
                                    min_quality_score: int = 50) -> Optional[Dict]:
        """Get best quality subtitle for a movie and language"""
        try:
            if not self._connected:
                await self.connect()
                
            result = await self.subtitles_collection.find_one({
                "movie_id": movie_id,
                "language": language,
                "quality_score": {"$gte": min_quality_score},
                "expires_at": {"$gt": datetime.utcnow()}
            }, sort=[("quality_score", DESCENDING), ("download_count", DESCENDING)])
            
            if result:
                result['_id'] = str(result['_id'])
                logger.debug(f"Found quality subtitle for {movie_id} ({language})")
            
            return result
            
        except Exception as e:
            logger.error(f"Error getting quality subtitle: {e}")
            return None
    
    async def get_subtitles_by_movie(self, movie_id: str, include_expired: bool = False) -> List[Dict]:
        """Get all available subtitles for a movie"""
        try:
            if not self._connected:
                await self.connect()
                
            query = {"movie_id": movie_id}
            if not include_expired:
                query["expires_at"] = {"$gt": datetime.utcnow()}
                
            cursor = self.subtitles_collection.find(query).sort([
                ("quality_score", DESCENDING),
                ("download_count", DESCENDING)
            ])
            
            results = await cursor.to_list(length=None)
            
            for result in results:
                result['_id'] = str(result['_id'])
            
            logger.debug(f"Found {len(results)} subtitles for movie {movie_id}")
            return results
            
        except Exception as e:
            logger.error(f"Error getting subtitles by movie: {e}")
            return []
    
    async def update_download_stats(self, movie_id: str, language: str, 
                                  user_id: str = None) -> bool:
        """Update download statistics with user tracking"""
        try:
            if not self._connected:
                await self.connect()
                
            # Update subtitle metadata
            await self.subtitles_collection.update_one(
                {"movie_id": movie_id, "language": language},
                {
                    "$inc": {"local_downloads": 1},
                    "$set": {"last_downloaded": datetime.utcnow()},
                    "$push": {
                        "download_history": {
                            "user_id": user_id,
                            "timestamp": datetime.utcnow(),
                            "ip_hash": None  # Could be added for analytics
                        }
                    }
                }
            )
            
            # Record usage statistics
            await self._record_download(movie_id, language, user_id)
            
            logger.debug(f"Updated download stats for {movie_id} ({language})")
            return True
            
        except Exception as e:
            logger.error(f"Error updating download stats: {e}")
            return False
    
    async def bulk_store_subtitles(self, subtitle_data_list: List[Dict]) -> int:
        """Bulk store multiple subtitle metadata entries efficiently"""
        try:
            if not self._connected:
                await self.connect()
                
            if not subtitle_data_list:
                return 0
            
            operations = []
            for data in subtitle_data_list:
                movie_id = data.get('movie_id')
                language = data.get('language')
                
                if not movie_id or not language:
                    continue
                
                document = {
                    "movie_id": movie_id,
                    "language": language,
                    "provider": data.get('provider', 'unknown'),
                    "subtitle_id": data.get('id'),
                    "download_count": data.get('download_count', 0),
                    "quality_score": data.get('quality_score', 0),
                    "format": data.get('format', 'srt'),
                    "filename": data.get('filename', ''),
                    "release": data.get('release', ''),
                    "file_size": data.get('file_size', 0),
                    "created_at": datetime.utcnow(),
                    "updated_at": datetime.utcnow(),
                    "expires_at": datetime.utcnow() + timedelta(seconds=self.cache_duration),
                    "cached_content": False,
                    "local_downloads": 0,
                    "verification_status": "pending"
                }
                
                operations.append({
                    "replaceOne": {
                        "filter": {"movie_id": movie_id, "language": language},
                        "replacement": document,
                        "upsert": True
                    }
                })
            
            if operations:
                # Process in batches to avoid memory issues
                batch_size = 100
                total_processed = 0
                
                for i in range(0, len(operations), batch_size):
                    batch = operations[i:i + batch_size]
                    result = await self.subtitles_collection.bulk_write(batch)
                    total_processed += result.upserted_count + result.modified_count
                
                logger.info(f"Bulk stored {total_processed} subtitle entries")
                return total_processed
            
            return 0
            
        except Exception as e:
            logger.error(f"Error in bulk store: {e}")
            return 0
    
    async def get_usage_statistics(self, days: int = 30) -> Dict[str, Any]:
        """Get usage statistics for the specified number of days"""
        try:
            if not self._connected:
                await self.connect()
                
            start_date = datetime.utcnow() - timedelta(days=days)
            
            # Downloads per day
            daily_pipeline = [
                {"$match": {"timestamp": {"$gte": start_date}}},
                {
                    "$group": {
                        "_id": {
                            "$dateToString": {
                                "format": "%Y-%m-%d",
                                "date": "$timestamp"
                            }
                        },
                        "downloads": {"$sum": 1},
                        "unique_users": {"$addToSet": "$user_id"},
                        "languages": {"$addToSet": "$language"}
                    }
                },
                {"$sort": {"_id": 1}}
            ]
            
            daily_cursor = self.usage_stats_collection.aggregate(daily_pipeline)
            daily_stats = await daily_cursor.to_list(length=days)
            
            # Language popularity
            lang_pipeline = [
                {"$match": {"timestamp": {"$gte": start_date}}},
                {
                    "$group": {
                        "_id": "$language",
                        "downloads": {"$sum": 1},
                        "unique_users": {"$addToSet": "$user_id"}
                    }
                },
                {"$sort": {"downloads": -1}},
                {"$limit": 10}
            ]
            
            lang_cursor = self.usage_stats_collection.aggregate(lang_pipeline)
            language_stats = await lang_cursor.to_list(length=10)
            
            # Top movies
            movie_pipeline = [
                {"$match": {"timestamp": {"$gte": start_date}}},
                {
                    "$group": {
                        "_id": "$movie_id",
                        "downloads": {"$sum": 1},
                        "languages": {"$addToSet": "$language"}
                    }
                },
                {"$sort": {"downloads": -1}},
                {"$limit": 10}
            ]
            
            movie_cursor = self.usage_stats_collection.aggregate(movie_pipeline)
            movie_stats = await movie_cursor.to_list(length=10)
            
            # Overall statistics
            total_downloads = await self.usage_stats_collection.count_documents({
                "timestamp": {"$gte": start_date}
            })
            
            unique_users = await self.usage_stats_collection.distinct(
                "user_id", {"timestamp": {"$gte": start_date}}
            )
            
            return {
                "period_days": days,
                "total_downloads": total_downloads,
                "unique_users": len(unique_users),
                "daily_stats": daily_stats,
                "language_stats": language_stats,
                "movie_stats": movie_stats,
                "avg_downloads_per_day": total_downloads / days if days > 0 else 0
            }
            
        except Exception as e:
            logger.error(f"Error getting usage statistics: {e}")
            return {}
    
    async def verify_subtitle_integrity(self, movie_id: str, language: str) -> Dict[str, Any]:
        """Verify the integrity of cached subtitle content"""
        try:
            if not self._connected:
                await self.connect()
                
            # Get metadata
            metadata = await self.get_subtitle_metadata(movie_id, language)
            if not metadata:
                return {"status": "not_found", "message": "Subtitle metadata not found"}
            
            # Check if content is cached
            if not metadata.get('cached_content'):
                return {"status": "not_cached", "message": "Subtitle content not cached"}
            
            # Try to retrieve content
            content = await self.get_cached_subtitle_content(movie_id, language)
            if not content:
                return {"status": "content_missing", "message": "Cached content could not be retrieved"}
            
            # Basic content validation
            line_count = len([line for line in content.split('\n') if line.strip()])
            has_timecode = bool(re.search(r'\d{2}:\d{2}:\d{2}', content))
            
            verification_result = {
                "status": "verified",
                "content_length": len(content),
                "line_count": line_count,
                "has_timecode": has_timecode,
                "verified_at": datetime.utcnow()
            }
            
            # Update verification status
            await self.subtitles_collection.update_one(
                {"movie_id": movie_id, "language": language},
                {"$set": {"verification_status": "verified", "last_verified": datetime.utcnow()}}
            )
            
            return verification_result
            
        except Exception as e:
            logger.error(f"Error verifying subtitle integrity: {e}")
            return {"status": "error", "message": str(e)}
    
    async def get_subtitle_recommendations(self, movie_id: str, user_language_preferences: List[str] = None) -> List[Dict]:
        """Get subtitle recommendations based on quality and user preferences"""
        try:
            if not self._connected:
                await self.connect()
                
            # Get all subtitles for the movie
            subtitles = await self.get_subtitles_by_movie(movie_id)
            if not subtitles:
                return []
            
            # Score subtitles based on various factors
            scored_subtitles = []
            for subtitle in subtitles:
                score = 0
                
                # Quality score (normalized to 0-40)
                quality_score = min(subtitle.get('quality_score', 0), 1000)
                score += (quality_score / 1000) * 40
                
                # Download count (normalized to 0-30)
                download_count = min(subtitle.get('download_count', 0), 10000)
                score += (download_count / 10000) * 30
                
                # Language preference bonus (0-20)
                if user_language_preferences and subtitle.get('language') in user_language_preferences:
                    preference_index = user_language_preferences.index(subtitle.get('language'))
                    score += max(20 - (preference_index * 5), 5)
                
                # Cached content bonus (0-5)
                if subtitle.get('cached_content'):
                    score += 5
                
                # Verification status bonus (0-5)
                if subtitle.get('verification_status') == 'verified':
                    score += 5
                
                subtitle['recommendation_score'] = score
                scored_subtitles.append(subtitle)
            
            # Sort by recommendation score
            scored_subtitles.sort(key=lambda x: x['recommendation_score'], reverse=True)
            
            return scored_subtitles
            
        except Exception as e:
            logger.error(f"Error getting subtitle recommendations: {e}")
            return []
    
    async def export_statistics_csv(self, days: int = 30) -> str:
        """Export usage statistics as CSV format"""
        try:
            stats = await self.get_usage_statistics(days)
            
            csv_lines = ["Date,Downloads,Unique_Users,Languages"]
            
            for day_stat in stats.get('daily_stats', []):
                date = day_stat['_id']
                downloads = day_stat['downloads']
                unique_users = len(day_stat.get('unique_users', []))
                languages = len(day_stat.get('languages', []))
                
                csv_lines.append(f"{date},{downloads},{unique_users},{languages}")
            
            return '\n'.join(csv_lines)
            
        except Exception as e:
            logger.error(f"Error exporting statistics: {e}")
            return ""
    
    async def backup_metadata(self) -> Dict[str, Any]:
        """Create a backup of subtitle metadata"""
        try:
            if not self._connected:
                await self.connect()
                
            # Get all subtitle metadata
            subtitles_cursor = self.subtitles_collection.find({})
            subtitles = await subtitles_cursor.to_list(length=None)
            
            # Get all movie info
            movies_cursor = self.movies_collection.find({})
            movies = await movies_cursor.to_list(length=None)
            
            backup_data = {
                "created_at": datetime.utcnow().isoformat(),
                "version": "1.0",
                "subtitle_count": len(subtitles),
                "movie_count": len(movies),
                "subtitles": [
                    {k: (v.isoformat() if isinstance(v, datetime) else v) 
                     for k, v in subtitle.items() if k != '_id'}
                    for subtitle in subtitles
                ],
                "movies": [
                    {k: (v.isoformat() if isinstance(v, datetime) else v) 
                     for k, v in movie.items() if k != '_id'}
                    for movie in movies
                ]
            }
            
            logger.info(f"Created backup with {len(subtitles)} subtitles and {len(movies)} movies")
            return backup_data
            
        except Exception as e:
            logger.error(f"Error creating backup: {e}")
            return {}
    
    async def restore_from_backup(self, backup_data: Dict[str, Any]) -> bool:
        """Restore subtitle metadata from backup"""
        try:
            if not self._connected:
                await self.connect()
                
            if not backup_data or 'subtitles' not in backup_data:
                logger.error("Invalid backup data")
                return False
            
            # Restore subtitles
            subtitles = backup_data['subtitles']
            if subtitles:
                # Convert datetime strings back to datetime objects
                for subtitle in subtitles:
                    for key in ['created_at', 'updated_at', 'expires_at', 'last_downloaded', 'last_verified']:
                        if key in subtitle and isinstance(subtitle[key], str):
                            try:
                                subtitle[key] = datetime.fromisoformat(subtitle[key])
                            except:
                                subtitle[key] = datetime.utcnow()
                
                await self.subtitles_collection.insert_many(subtitles, ordered=False)
            
            # Restore movies
            movies = backup_data.get('movies', [])
            if movies:
                for movie in movies:
                    for key in ['created_at', 'updated_at', 'last_checked']:
                        if key in movie and isinstance(movie[key], str):
                            try:
                                movie[key] = datetime.fromisoformat(movie[key])
                            except:
                                movie[key] = datetime.utcnow()
                
                await self.movies_collection.insert_many(movies, ordered=False)
            
            logger.info(f"Restored {len(subtitles)} subtitles and {len(movies)} movies from backup")
            return True
            
        except Exception as e:
            logger.error(f"Error restoring from backup: {e}")
            return False
    
    # Private helper methods
    
    async def _update_movie_subtitle_count(self, movie_id: str):
        """Update subtitle count for a movie"""
        try:
            count = await self.subtitles_collection.count_documents({
                "movie_id": movie_id,
                "expires_at": {"$gt": datetime.utcnow()}
            })
            
            languages = await self.subtitles_collection.distinct(
                "language", 
                {"movie_id": movie_id, "expires_at": {"$gt": datetime.utcnow()}}
            )
            
            await self.movies_collection.update_one(
                {"$or": [{"imdb_id": movie_id}, {"title": movie_id}]},
                {
                    "$set": {
                        "subtitle_count": count,
                        "available_languages": languages,
                        "last_checked": datetime.utcnow()
                    }
                },
                upsert=True
            )
            
        except Exception as e:
            logger.error(f"Error updating movie subtitle count: {e}")
    
    async def _update_all_movie_subtitle_counts(self):
        """Update subtitle counts for all movies"""
        try:
            # Get unique movie IDs
            movie_ids = await self.subtitles_collection.distinct("movie_id")
            
            # Update counts in batches
            batch_size = 50
            for i in range(0, len(movie_ids), batch_size):
                batch = movie_ids[i:i + batch_size]
                tasks = [self._update_movie_subtitle_count(movie_id) for movie_id in batch]
                await asyncio.gather(*tasks, return_exceptions=True)
            
        except Exception as e:
            logger.error(f"Error updating all movie subtitle counts: {e}")
    
    async def _record_access(self, movie_id: str, language: str):
        """Record subtitle access for analytics"""
        try:
            await self.usage_stats_collection.insert_one({
                "type": "access",
                "movie_id": movie_id,
                "language": language,
                "timestamp": datetime.utcnow()
            })
        except Exception as e:
            logger.debug(f"Error recording access: {e}")
    
    async def _record_download(self, movie_id: str, language: str, user_id: str = None):
        """Record subtitle download for analytics"""
        try:
            await self.usage_stats_collection.insert_one({
                "type": "download",
                "movie_id": movie_id,
                "language": language,
                "user_id": user_id,
                "timestamp": datetime.utcnow()
            })
        except Exception as e:
            logger.debug(f"Error recording download: {e}")
    
    async def _record_cache_hit(self, movie_id: str, language: str):
        """Record cache hit for analytics"""
        try:
            await self.usage_stats_collection.insert_one({
                "type": "cache_hit",
                "movie_id": movie_id,
                "language": language,
                "timestamp": datetime.utcnow()
            })
        except Exception as e:
            logger.debug(f"Error recording cache hit: {e}")
    
    async def log_api_request(self, provider: str, endpoint: str, status: str, 
                            response_time: float, error_message: str = None):
        """Log API requests for monitoring"""
        try:
            if not self._connected:
                await self.connect()
                
            await self.api_logs_collection.insert_one({
                "provider": provider,
                "endpoint": endpoint,
                "status": status,
                "response_time": response_time,
                "error_message": error_message,
                "timestamp": datetime.utcnow()
            })
            
        except Exception as e:
            logger.debug(f"Error logging API request: {e}")
    
    async def get_api_health_stats(self, hours: int = 24) -> Dict[str, Any]:
        """Get API health statistics"""
        try:
            if not self._connected:
                await self.connect()
                
            start_time = datetime.utcnow() - timedelta(hours=hours)
            
            pipeline = [
                {"$match": {"timestamp": {"$gte": start_time}}},
                {
                    "$group": {
                        "_id": {
                            "provider": "$provider",
                            "status": "$status"
                        },
                        "count": {"$sum": 1},
                        "avg_response_time": {"$avg": "$response_time"},
                        "max_response_time": {"$max": "$response_time"}
                    }
                }
            ]
            
            cursor = self.api_logs_collection.aggregate(pipeline)
            results = await cursor.to_list(length=None)
            
            # Process results into a more readable format
            stats = {}
            for result in results:
                provider = result['_id']['provider']
                status = result['_id']['status']
                
                if provider not in stats:
                    stats[provider] = {}
                
                stats[provider][status] = {
                    "count": result['count'],
                    "avg_response_time": round(result['avg_response_time'], 3),
                    "max_response_time": round(result['max_response_time'], 3)
                }
            
            return stats
            
        except Exception as e:
            logger.error(f"Error getting API health stats: {e}")
            return {}
    
    async def optimize_database(self) -> Dict[str, Any]:
        """Perform database optimization tasks"""
        try:
            if not self._connected:
                await self.connect()
                
            optimization_results = {}
            
            # Reindex collections
            reindex_results = await asyncio.gather(
                self.subtitles_collection.reindex(),
                self.movies_collection.reindex(),
                self.usage_stats_collection.reindex(),
                return_exceptions=True
            )
            
            optimization_results['reindex_completed'] = all(
                not isinstance(result, Exception) for result in reindex_results
            )
            
            # Cleanup old usage statistics (keep only 90 days)
            old_stats_date = datetime.utcnow() - timedelta(days=90)
            deleted_stats = await self.usage_stats_collection.delete_many({
                "timestamp": {"$lt": old_stats_date}
            })
            optimization_results['deleted_old_stats'] = deleted_stats.deleted_count
            
            # Cleanup old API logs (keep only 30 days)
            old_logs_date = datetime.utcnow() - timedelta(days=30)
            deleted_logs = await self.api_logs_collection.delete_many({
                "timestamp": {"$lt": old_logs_date}
            })
            optimization_results['deleted_old_logs'] = deleted_logs.deleted_count
            
            # Update all movie subtitle counts
            await self._update_all_movie_subtitle_counts()
            optimization_results['updated_movie_counts'] = True
            
            logger.info(f"Database optimization completed: {optimization_results}")
            return optimization_results
            
        except Exception as e:
            logger.error(f"Error optimizing database: {e}")
            return {"error": str(e)}
    
    async def close(self):
        """Close database connection and cleanup resources"""
        try:
            if self.client:
                self.client.close()
                self._connected = False
                logger.info("Closed subtitle database connection")
        except Exception as e:
            logger.error(f"Error closing database connection: {e}")
    
    def __del__(self):
        """Destructor to ensure connection is closed"""
        try:
            if hasattr(self, 'client') and self.client:
                # Note: In async context, this should be handled properly
                # This is just a fallback for cleanup
                pass
        except:
            pass