import logging
import asyncio
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
from subtitle.storage import SubtitleStorage
from subtitle.cache_manager import CacheManager
from subtitle.api_manager import SubtitleAPIManager
from subtitle.processor import SubtitleProcessor
from config.subtitle_config import SUPPORTED_LANGUAGES, PRIORITY_LANGUAGES, ERROR_MESSAGES
from info import SUBTITLE_DB_URI, SUBTITLE_DB_NAME, REDIS_URL, ENABLE_SUBTITLES

logger = logging.getLogger(__name__)

class SubtitleDatabase:
    """Main interface for subtitle database operations"""
    
    def __init__(self):
        self.storage = None
        self.cache = None
        self.api_manager = None
        self.processor = None
        self._initialized = False
        self._initialization_lock = asyncio.Lock()
        self._error_count = 0
        self._last_error = None
        
    async def initialize(self):
        """Initialize all subtitle system components"""
        if self._initialized:
            return True
            
        async with self._initialization_lock:
            if self._initialized:  # Double-check after acquiring lock
                return True
                
            try:
                logger.info("Initializing subtitle database system...")
                
                # Initialize storage
                self.storage = SubtitleStorage(SUBTITLE_DB_URI, SUBTITLE_DB_NAME)
                await self.storage.connect()
                logger.info("✅ Storage initialized")
                
                # Initialize cache
                self.cache = CacheManager(REDIS_URL)
                await self.cache.connect()
                logger.info("✅ Cache initialized")
                
                # Initialize API manager
                self.api_manager = SubtitleAPIManager()
                logger.info("✅ API manager initialized")
                
                # Initialize processor
                self.processor = SubtitleProcessor()
                logger.info("✅ Processor initialized")
                
                self._initialized = True
                self._error_count = 0
                self._last_error = None
                
                logger.info("🎉 Subtitle database system initialized successfully")
                return True
                
            except Exception as e:
                self._error_count += 1
                self._last_error = str(e)
                logger.error(f"❌ Failed to initialize subtitle database system: {e}")
                
                # Cleanup partially initialized components
                await self._cleanup_partial_initialization()
                raise
    
    async def _cleanup_partial_initialization(self):
        """Clean up partially initialized components"""
        try:
            if self.storage:
                await self.storage.close()
                self.storage = None
            if self.cache:
                await self.cache.close()
                self.cache = None
            if self.api_manager:
                await self.api_manager.close()
                self.api_manager = None
            self.processor = None
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")
    
    async def ensure_initialized(self):
        """Ensure the system is initialized before operations"""
        if not self._initialized:
            await self.initialize()
        return self._initialized
    
    async def get_subtitle_info(self, movie_id: str, language: str) -> Optional[Dict]:
        """Get subtitle information with caching"""
        if not await self.ensure_initialized():
            return None
            
        try:
            # Try cache first
            cached_info = await self.cache.get_subtitle_metadata(movie_id, language)
            if cached_info:
                logger.debug(f"Cache hit for subtitle info: {movie_id} ({language})")
                return cached_info
            
            # Try storage
            stored_info = await self.storage.get_subtitle_metadata(movie_id, language)
            if stored_info:
                # Cache the result
                await self.cache.set_subtitle_metadata(movie_id, language, stored_info)
                logger.debug(f"Storage hit for subtitle info: {movie_id} ({language})")
                return stored_info
            
            return None
            
        except Exception as e:
            logger.error(f"Error getting subtitle info: {e}")
            return None
    
    async def get_subtitle_content(self, movie_id: str, language: str) -> Optional[str]:
        """Get subtitle content with caching"""
        if not await self.ensure_initialized():
            return None
            
        try:
            # Try cache first
            cached_content = await self.cache.get_subtitle_content(movie_id, language)
            if cached_content:
                logger.debug(f"Cache hit for subtitle content: {movie_id} ({language})")
                return cached_content
            
            # Try storage
            stored_content = await self.storage.get_cached_subtitle_content(movie_id, language)
            if stored_content:
                # Cache the result
                await self.cache.set_subtitle_content(movie_id, language, stored_content)
                logger.debug(f"Storage hit for subtitle content: {movie_id} ({language})")
                return stored_content
            
            return None
            
        except Exception as e:
            logger.error(f"Error getting subtitle content: {e}")
            return None
    
    async def search_and_cache_subtitles(self, movie_title: str, imdb_id: str = None, 
                                       language: str = 'en', file_hash: str = None) -> List[Dict]:
        """Search for subtitles and cache results"""
        if not await self.ensure_initialized():
            return []
            
        try:
            # Create cache key
            cache_key = f"{movie_title.lower()}_{language}"
            
            # Check cache first
            cached_results = await self.cache.get_search_results(movie_title, language)
            if cached_results:
                logger.debug(f"Cache hit for search results: {movie_title} ({language})")
                return cached_results
            
            # Search using API
            logger.info(f"Searching subtitles for: {movie_title} ({language})")
            results = await self.api_manager.search_subtitles(
                movie_title, imdb_id, language, file_hash
            )
            
            if results:
                logger.info(f"Found {len(results)} subtitle(s) for {movie_title} ({language})")
                
                # Store metadata for each result
                for result in results:
                    await self.storage.store_subtitle_metadata(
                        imdb_id or movie_title, language, result
                    )
                
                # Cache search results
                await self.cache.set_search_results(movie_title, language, results)
                
                # Update movie subtitle info
                if imdb_id:
                    await self.storage.store_movie_subtitle_info(
                        imdb_id, movie_title, [language]
                    )
            else:
                logger.info(f"No subtitles found for {movie_title} ({language})")
            
            return results
            
        except Exception as e:
            logger.error(f"Error searching subtitles: {e}")
            return []
    
    async def download_and_process_subtitle(self, movie_id: str, language: str, 
                                          subtitle_info: Dict) -> Optional[str]:
        """Download subtitle content and process it"""
        if not await self.ensure_initialized():
            return None
            
        try:
            logger.info(f"Downloading subtitle: {movie_id} ({language})")
            
            # Check if already cached
            cached_content = await self.get_subtitle_content(movie_id, language)
            if cached_content:
                logger.info(f"Subtitle already cached: {movie_id} ({language})")
                return cached_content
            
            # Download content
            content_bytes = await self.api_manager.download_subtitle_content(subtitle_info)
            if not content_bytes:
                logger.error(f"Failed to download subtitle content: {movie_id} ({language})")
                return None
            
            # Process content
            processed_content, error_msg = self.processor.process_subtitle_file(content_bytes)
            if not processed_content:
                logger.error(f"Failed to process subtitle: {error_msg}")
                return None
            
            logger.info(f"Successfully processed subtitle: {movie_id} ({language})")
            
            # Cache processed content
            await self.cache.set_subtitle_content(movie_id, language, processed_content)
            await self.storage.cache_subtitle_content(movie_id, language, processed_content)
            
            # Update download stats
            await self.storage.update_download_stats(movie_id, language)
            
            return processed_content
            
        except Exception as e:
            logger.error(f"Error downloading and processing subtitle: {e}")
            return None
    
    async def get_available_languages(self, movie_id: str, movie_title: str = None) -> List[str]:
        """Get available subtitle languages for a movie"""
        if not await self.ensure_initialized():
            return []
            
        try:
            # Check cache first
            cached_languages = await self.cache.get_available_languages(movie_id)
            if cached_languages:
                logger.debug(f"Cache hit for available languages: {movie_id}")
                return cached_languages
            
            # Check storage
            subtitles = await self.storage.get_subtitles_by_movie(movie_id)
            if subtitles:
                languages = list(set(sub['language'] for sub in subtitles))
                await self.cache.set_available_languages(movie_id, languages)
                logger.debug(f"Storage hit for available languages: {movie_id}")
                return languages
            
            # If no cached data and we have a title, search popular languages
            if movie_title and self.api_manager:
                logger.info(f"Searching available languages for: {movie_title}")
                languages = await self.api_manager.get_available_languages(movie_title)
                if languages:
                    await self.cache.set_available_languages(movie_id, languages)
                    logger.info(f"Found {len(languages)} languages for {movie_title}")
                return languages
            
            return []
            
        except Exception as e:
            logger.error(f"Error getting available languages: {e}")
            return []
    
    async def get_subtitle_by_quality(self, movie_id: str, language: str, 
                                    min_quality_score: int = 50) -> Optional[Dict]:
        """Get best quality subtitle for a movie and language"""
        if not await self.ensure_initialized():
            return None
            
        try:
            return await self.storage.get_subtitle_by_quality(
                movie_id, language, min_quality_score
            )
        except Exception as e:
            logger.error(f"Error getting quality subtitle: {e}")
            return None
    
    async def search_movies_by_title(self, title: str, limit: int = 10) -> List[Dict]:
        """Search for movies by title"""
        if not await self.ensure_initialized():
            return []
            
        try:
            return await self.storage.search_movies_by_title(title, limit)
        except Exception as e:
            logger.error(f"Error searching movies by title: {e}")
            return []
    
    async def get_popular_languages(self, limit: int = 20) -> List[Dict]:
        """Get most popular subtitle languages"""
        if not await self.ensure_initialized():
            return []
            
        try:
            return await self.storage.get_popular_languages(limit)
        except Exception as e:
            logger.error(f"Error getting popular languages: {e}")
            return []
    
    async def get_database_statistics(self) -> Dict[str, Any]:
        """Get comprehensive database statistics"""
        try:
            stats = {
                "status": "operational" if self._initialized else "not_initialized",
                "initialized": self._initialized,
                "error_count": self._error_count,
                "last_error": self._last_error
            }
            
            if self._initialized:
                # Get storage stats
                if self.storage:
                    storage_stats = await self.storage.get_database_stats()
                    stats["storage"] = storage_stats
                
                # Get cache stats
                if self.cache:
                    cache_stats = await self.cache.get_cache_stats()
                    stats["cache"] = cache_stats
                
                # Get API manager info
                if self.api_manager:
                    stats["api"] = {
                        "opensubtitles_configured": bool(self.api_manager.opensubtitles),
                        "subdb_configured": bool(self.api_manager.subdb)
                    }
            
            return stats
            
        except Exception as e:
            logger.error(f"Error getting database statistics: {e}")
            return {
                "status": "error",
                "error": str(e),
                "initialized": self._initialized
            }
    
    async def cleanup_system(self) -> Dict[str, int]:
        """Perform system cleanup"""
        if not await self.ensure_initialized():
            return {"storage_cleaned": 0, "cache_cleaned": 0}
            
        try:
            # Cleanup expired entries
            storage_cleaned = 0
            cache_cleaned = 0
            
            if self.storage:
                storage_cleaned = await self.storage.cleanup_expired_subtitles()
            
            if self.cache:
                cache_cleaned = await self.cache.cleanup_expired_keys()
            
            logger.info(f"Cleanup completed: {storage_cleaned} storage entries, {cache_cleaned} cache keys")
            
            return {
                "storage_cleaned": storage_cleaned,
                "cache_cleaned": cache_cleaned
            }
            
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")
            return {"storage_cleaned": 0, "cache_cleaned": 0}
    
    async def bulk_import_subtitles(self, subtitle_data_list: List[Dict]) -> int:
        """Bulk import subtitle metadata"""
        if not await self.ensure_initialized():
            return 0
            
        try:
            if self.storage:
                return await self.storage.bulk_store_subtitles(subtitle_data_list)
            return 0
        except Exception as e:
            logger.error(f"Error in bulk import: {e}")
            return 0
    
    async def invalidate_movie_cache(self, movie_id: str):
        """Invalidate all cache entries for a movie"""
        if not await self.ensure_initialized():
            return
            
        try:
            if self.cache:
                await self.cache.invalidate_movie_cache(movie_id)
        except Exception as e:
            logger.error(f"Error invalidating cache: {e}")
    
    async def test_api_connectivity(self) -> Dict[str, bool]:
        """Test API connectivity"""
        if not await self.ensure_initialized():
            return {"opensubtitles": False, "subdb": False}
            
        try:
            results = {"opensubtitles": False, "subdb": False}
            
            if self.api_manager:
                # Test with a simple search
                test_results = await self.api_manager.search_subtitles(
                    "Avengers", None, "en"
                )
                results["opensubtitles"] = len(test_results) > 0
                results["subdb"] = True  # SubDB doesn't need auth, assume working
            
            return results
            
        except Exception as e:
            logger.error(f"Error testing API connectivity: {e}")
            return {"opensubtitles": False, "subdb": False}
    
    async def get_system_health(self) -> Dict[str, Any]:
        """Get comprehensive system health information"""
        try:
            health = {
                "timestamp": datetime.utcnow().isoformat(),
                "overall_status": "unknown",
                "components": {}
            }
            
            # Check initialization
            health["components"]["initialization"] = {
                "status": "healthy" if self._initialized else "unhealthy",
                "error_count": self._error_count,
                "last_error": self._last_error
            }
            
            if self._initialized:
                # Check storage
                try:
                    storage_stats = await self.storage.get_database_stats()
                    health["components"]["storage"] = {
                        "status": "healthy",
                        "entries": storage_stats.get("subtitle_entries", 0)
                    }
                except Exception as e:
                    health["components"]["storage"] = {
                        "status": "unhealthy",
                        "error": str(e)
                    }
                
                # Check cache
                try:
                    cache_stats = await self.cache.get_cache_stats()
                    health["components"]["cache"] = {
                        "status": "healthy" if cache_stats.get("status") == "connected" else "degraded",
                        "total_keys": cache_stats.get("total_keys", 0)
                    }
                except Exception as e:
                    health["components"]["cache"] = {
                        "status": "unhealthy",
                        "error": str(e)
                    }
                
                # Check API
                try:
                    api_tests = await self.test_api_connectivity()
                    health["components"]["api"] = {
                        "status": "healthy" if any(api_tests.values()) else "degraded",
                        "opensubtitles": api_tests.get("opensubtitles", False),
                        "subdb": api_tests.get("subdb", False)
                    }
                except Exception as e:
                    health["components"]["api"] = {
                        "status": "unhealthy",
                        "error": str(e)
                    }
            
            # Determine overall status
            component_statuses = [comp.get("status") for comp in health["components"].values()]
            if all(status == "healthy" for status in component_statuses):
                health["overall_status"] = "healthy"
            elif any(status == "healthy" for status in component_statuses):
                health["overall_status"] = "degraded"
            else:
                health["overall_status"] = "unhealthy"
            
            return health
            
        except Exception as e:
            logger.error(f"Error getting system health: {e}")
            return {
                "timestamp": datetime.utcnow().isoformat(),
                "overall_status": "error",
                "error": str(e)
            }
    
    async def get_language_statistics(self) -> Dict[str, Any]:
        """Get language usage statistics"""
        if not await self.ensure_initialized():
            return {}
            
        try:
            popular_languages = await self.storage.get_popular_languages(40)
            
            # Format for better display
            language_stats = []
            for lang_stat in popular_languages:
                lang_code = lang_stat.get('_id', 'unknown')
                lang_info = SUPPORTED_LANGUAGES.get(lang_code, {
                    'name': lang_code.upper(), 
                    'flag': '🌐'
                })
                
                language_stats.append({
                    'code': lang_code,
                    'name': lang_info['name'],
                    'flag': lang_info['flag'],
                    'count': lang_stat.get('count', 0),
                    'avg_quality': lang_stat.get('avg_quality', 0)
                })
            
            return {
                'total_languages': len(language_stats),
                'supported_languages': len(SUPPORTED_LANGUAGES),
                'popular_languages': language_stats,
                'priority_languages': PRIORITY_LANGUAGES
            }
            
        except Exception as e:
            logger.error(f"Error getting language statistics: {e}")
            return {}
    
    async def search_with_filters(self, movie_title: str, filters: Dict[str, Any]) -> List[Dict]:
        """Search subtitles with advanced filters"""
        if not await self.ensure_initialized():
            return []
            
        try:
            language = filters.get('language', 'en')
            min_quality = filters.get('min_quality', 0)
            provider = filters.get('provider', None)
            
            # Basic search
            results = await self.search_and_cache_subtitles(
                movie_title, filters.get('imdb_id'), language
            )
            
            # Apply filters
            filtered_results = []
            for result in results:
                # Quality filter
                if result.get('quality_score', 0) < min_quality:
                    continue
                
                # Provider filter
                if provider and result.get('provider') != provider:
                    continue
                
                filtered_results.append(result)
            
            return filtered_results
            
        except Exception as e:
            logger.error(f"Error in filtered search: {e}")
            return []
    
    async def get_subtitle_preview(self, movie_id: str, language: str, 
                                 max_lines: int = 5) -> Optional[str]:
        """Get a preview of subtitle content"""
        if not await self.ensure_initialized():
            return None
            
        try:
            content = await self.get_subtitle_content(movie_id, language)
            if content and self.processor:
                return self.processor.create_subtitle_preview(content, max_lines)
            return None
            
        except Exception as e:
            logger.error(f"Error getting subtitle preview: {e}")
            return None
    
    async def convert_subtitle_format(self, movie_id: str, language: str, 
                                    target_format: str) -> Optional[str]:
        """Convert subtitle to different format"""
        if not await self.ensure_initialized():
            return None
            
        try:
            content = await self.get_subtitle_content(movie_id, language)
            if content and self.processor:
                return self.processor.convert_format(content, 'srt', target_format)
            return None
            
        except Exception as e:
            logger.error(f"Error converting subtitle format: {e}")
            return None
    
    async def close(self):
        """Close all connections and cleanup"""
        try:
            logger.info("Closing subtitle database system...")
            
            if self.storage:
                await self.storage.close()
                self.storage = None
                
            if self.cache:
                await self.cache.close()
                self.cache = None
                
            if self.api_manager:
                await self.api_manager.close()
                self.api_manager = None
                
            self.processor = None
            self._initialized = False
            
            logger.info("Subtitle database system closed successfully")
            
        except Exception as e:
            logger.error(f"Error closing subtitle database system: {e}")
    
    def __del__(self):
        """Destructor to ensure cleanup"""
        if self._initialized:
            try:
                # Try to schedule cleanup, but don't block
                import asyncio
                loop = asyncio.get_event_loop()
                if not loop.is_closed():
                    loop.create_task(self.close())
            except:
                pass

# Global instance
subtitle_db = SubtitleDatabase()

# Convenience functions for easy access
async def initialize_subtitle_system():
    """Initialize the subtitle system"""
    if ENABLE_SUBTITLES:
        try:
            await subtitle_db.initialize()
            return True
        except Exception as e:
            logger.error(f"Failed to initialize subtitle system: {e}")
            return False
    return False

async def search_subtitles(movie_title: str, language: str = 'en', 
                         imdb_id: str = None) -> List[Dict]:
    """Search for subtitles"""
    return await subtitle_db.search_and_cache_subtitles(movie_title, imdb_id, language)

async def get_available_subtitle_languages(movie_id: str, 
                                         movie_title: str = None) -> List[str]:
    """Get available subtitle languages"""
    return await subtitle_db.get_available_languages(movie_id, movie_title)

async def download_subtitle(movie_id: str, language: str, 
                          subtitle_info: Dict) -> Optional[str]:
    """Download and process subtitle"""
    return await subtitle_db.download_and_process_subtitle(movie_id, language, subtitle_info)

async def get_subtitle_statistics() -> Dict[str, Any]:
    """Get subtitle system statistics"""
    return await subtitle_db.get_database_statistics()

async def cleanup_subtitle_system() -> Dict[str, int]:
    """Cleanup subtitle system"""
    return await subtitle_db.cleanup_system()

async def get_system_health() -> Dict[str, Any]:
    """Get system health status"""
    return await subtitle_db.get_system_health()

# Utility functions
def is_subtitle_system_enabled() -> bool:
    """Check if subtitle system is enabled"""
    return ENABLE_SUBTITLES

def is_subtitle_system_initialized() -> bool:
    """Check if subtitle system is initialized"""
    return subtitle_db._initialized

def get_supported_languages() -> Dict[str, Dict]:
    """Get all supported languages"""
    return SUPPORTED_LANGUAGES

def get_error_message(error_key: str) -> str:
    """Get localized error message"""
    return ERROR_MESSAGES.get(error_key, "Unknown error occurred")

# Context manager for subtitle operations
class SubtitleOperationContext:
    """Context manager for subtitle operations with automatic cleanup"""
    
    def __init__(self, operation_name: str):
        self.operation_name = operation_name
        self.start_time = None
    
    async def __aenter__(self):
        self.start_time = datetime.utcnow()
        logger.debug(f"Starting subtitle operation: {self.operation_name}")
        
        if not subtitle_db._initialized:
            await subtitle_db.initialize()
        
        return subtitle_db
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        duration = (datetime.utcnow() - self.start_time).total_seconds()
        
        if exc_type:
            logger.error(f"Subtitle operation '{self.operation_name}' failed after {duration:.2f}s: {exc_val}")
        else:
            logger.debug(f"Subtitle operation '{self.operation_name}' completed in {duration:.2f}s")
        
        return False  # Don't suppress exceptions

# Usage example:
# async with SubtitleOperationContext("search_subtitles") as db:
#     results = await db.search_and_cache_subtitles("Avengers", None, "en")