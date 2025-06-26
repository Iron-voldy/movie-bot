import json
import logging
import asyncio
from typing import Optional, Dict, List, Any
from datetime import datetime, timedelta
import redis.asyncio as redis
from config.subtitle_config import CACHE_CONFIG, RATE_LIMIT_CONFIG
from info import REDIS_URL

logger = logging.getLogger(__name__)

class CacheManager:
    """Manages Redis-based caching for subtitle system"""
    
    def __init__(self, redis_url: str = None):
        self.redis_url = redis_url or REDIS_URL
        self.redis_client = None
        self.prefix = CACHE_CONFIG['redis_prefix']
        self.metadata_ttl = CACHE_CONFIG['metadata_ttl']
        self.content_ttl = CACHE_CONFIG['content_ttl']
        self.search_ttl = CACHE_CONFIG['search_results_ttl']
        self._lock = asyncio.Lock()
        
    async def connect(self):
        """Initialize Redis connection"""
        try:
            self.redis_client = redis.from_url(
                self.redis_url,
                encoding='utf-8',
                decode_responses=True,
                socket_connect_timeout=5,
                socket_timeout=5
            )
            
            # Test connection
            await self.redis_client.ping()
            logger.info("Connected to Redis cache successfully")
            
        except Exception as e:
            logger.error(f"Failed to connect to Redis: {e}")
            self.redis_client = None
            # Continue without cache - degraded mode
    
    def _make_key(self, *parts: str) -> str:
        """Create a cache key with prefix"""
        return f"{self.prefix}{':'.join(parts)}"
    
    async def get_subtitle_metadata(self, movie_id: str, language: str) -> Optional[Dict]:
        """Get cached subtitle metadata"""
        if not self.redis_client:
            return None
            
        try:
            key = self._make_key("metadata", movie_id, language)
            data = await self.redis_client.get(key)
            
            if data:
                logger.info(f"Cache hit for subtitle metadata: {movie_id} ({language})")
                return json.loads(data)
            
            return None
            
        except Exception as e:
            logger.error(f"Error getting cached metadata: {e}")
            return None
    
    async def set_subtitle_metadata(self, movie_id: str, language: str, 
                                  metadata: Dict, ttl: int = None) -> bool:
        """Cache subtitle metadata"""
        if not self.redis_client:
            return False
            
        try:
            key = self._make_key("metadata", movie_id, language)
            ttl = ttl or self.metadata_ttl
            
            # Ensure datetime objects are serializable
            serializable_metadata = self._prepare_for_serialization(metadata)
            
            await self.redis_client.setex(
                key, 
                ttl, 
                json.dumps(serializable_metadata, default=str)
            )
            
            logger.info(f"Cached subtitle metadata: {movie_id} ({language})")
            return True
            
        except Exception as e:
            logger.error(f"Error caching metadata: {e}")
            return False
    
    async def get_subtitle_content(self, movie_id: str, language: str) -> Optional[str]:
        """Get cached subtitle content"""
        if not self.redis_client:
            return None
            
        try:
            key = self._make_key("content", movie_id, language)
            content = await self.redis_client.get(key)
            
            if content:
                logger.info(f"Cache hit for subtitle content: {movie_id} ({language})")
                return content
            
            return None
            
        except Exception as e:
            logger.error(f"Error getting cached content: {e}")
            return None
    
    async def set_subtitle_content(self, movie_id: str, language: str, 
                                 content: str, ttl: int = None) -> bool:
        """Cache subtitle content"""
        if not self.redis_client:
            return False
            
        try:
            key = self._make_key("content", movie_id, language)
            ttl = ttl or self.content_ttl
            
            # Check content size
            content_size = len(content.encode('utf-8'))
            max_size = CACHE_CONFIG.get('max_cache_size', 100 * 1024 * 1024)
            
            if content_size > max_size:
                logger.warning(f"Content too large to cache: {content_size} bytes")
                return False
            
            await self.redis_client.setex(key, ttl, content)
            
            logger.info(f"Cached subtitle content: {movie_id} ({language}) - {content_size} bytes")
            return True
            
        except Exception as e:
            logger.error(f"Error caching content: {e}")
            return False
    
    async def get_search_results(self, query: str, language: str) -> Optional[List[Dict]]:
        """Get cached search results"""
        if not self.redis_client:
            return None
            
        try:
            key = self._make_key("search", query.lower(), language)
            data = await self.redis_client.get(key)
            
            if data:
                logger.info(f"Cache hit for search results: {query} ({language})")
                return json.loads(data)
            
            return None
            
        except Exception as e:
            logger.error(f"Error getting cached search results: {e}")
            return None
    
    async def set_search_results(self, query: str, language: str, 
                               results: List[Dict], ttl: int = None) -> bool:
        """Cache search results"""
        if not self.redis_client:
            return False
            
        try:
            key = self._make_key("search", query.lower(), language)
            ttl = ttl or self.search_ttl
            
            # Prepare results for serialization
            serializable_results = [
                self._prepare_for_serialization(result) for result in results
            ]
            
            await self.redis_client.setex(
                key, 
                ttl, 
                json.dumps(serializable_results, default=str)
            )
            
            logger.info(f"Cached search results: {query} ({language}) - {len(results)} results")
            return True
            
        except Exception as e:
            logger.error(f"Error caching search results: {e}")
            return False
    
    async def get_available_languages(self, movie_id: str) -> Optional[List[str]]:
        """Get cached available languages for a movie"""
        if not self.redis_client:
            return None
            
        try:
            key = self._make_key("languages", movie_id)
            data = await self.redis_client.get(key)
            
            if data:
                logger.info(f"Cache hit for available languages: {movie_id}")
                return json.loads(data)
            
            return None
            
        except Exception as e:
            logger.error(f"Error getting cached languages: {e}")
            return None
    
    async def set_available_languages(self, movie_id: str, languages: List[str], 
                                    ttl: int = None) -> bool:
        """Cache available languages for a movie"""
        if not self.redis_client:
            return False
            
        try:
            key = self._make_key("languages", movie_id)
            ttl = ttl or self.metadata_ttl
            
            await self.redis_client.setex(key, ttl, json.dumps(languages))
            
            logger.info(f"Cached available languages: {movie_id} - {len(languages)} languages")
            return True
            
        except Exception as e:
            logger.error(f"Error caching languages: {e}")
            return False
    
    async def invalidate_movie_cache(self, movie_id: str):
        """Invalidate all cache entries for a movie"""
        if not self.redis_client:
            return
            
        try:
            # Find all keys related to this movie
            patterns = [
                self._make_key("metadata", movie_id, "*"),
                self._make_key("content", movie_id, "*"),
                self._make_key("languages", movie_id)
            ]
            
            for pattern in patterns:
                keys = await self.redis_client.keys(pattern)
                if keys:
                    await self.redis_client.delete(*keys)
            
            logger.info(f"Invalidated cache for movie: {movie_id}")
            
        except Exception as e:
            logger.error(f"Error invalidating movie cache: {e}")
    
    async def get_rate_limit_count(self, identifier: str, window: str) -> int:
        """Get current rate limit count"""
        if not self.redis_client:
            return 0
            
        try:
            key = self._make_key("rate_limit", window, identifier)
            count = await self.redis_client.get(key)
            return int(count) if count else 0
            
        except Exception as e:
            logger.error(f"Error getting rate limit count: {e}")
            return 0
    
    async def increment_rate_limit(self, identifier: str, window: str, 
                                 ttl: int, max_requests: int) -> tuple[bool, int]:
        """Increment rate limit counter and check if limit exceeded"""
        if not self.redis_client:
            return True, 0  # Allow if cache is unavailable
            
        try:
            key = self._make_key("rate_limit", window, identifier)
            
            async with self._lock:
                # Get current count
                current = await self.redis_client.get(key)
                current_count = int(current) if current else 0
                
                if current_count >= max_requests:
                    return False, current_count
                
                # Increment counter
                pipe = self.redis_client.pipeline()
                pipe.incr(key)
                if current_count == 0:  # First request in window
                    pipe.expire(key, ttl)
                results = await pipe.execute()
                
                new_count = results[0]
                return True, new_count
                
        except Exception as e:
            logger.error(f"Error checking rate limit: {e}")
            return True, 0  # Allow on error
    
    async def get_cache_stats(self) -> Dict[str, Any]:
        """Get cache statistics"""
        if not self.redis_client:
            return {"status": "disconnected"}
            
        try:
            # Get Redis info
            info = await self.redis_client.info()
            
            # Count keys by type
            key_patterns = {
                "metadata": self._make_key("metadata", "*"),
                "content": self._make_key("content", "*"),
                "search": self._make_key("search", "*"),
                "languages": self._make_key("languages", "*"),
                "rate_limit": self._make_key("rate_limit", "*")
            }
            
            key_counts = {}
            total_keys = 0
            
            for key_type, pattern in key_patterns.items():
                keys = await self.redis_client.keys(pattern)
                count = len(keys)
                key_counts[key_type] = count
                total_keys += count
            
            return {
                "status": "connected",
                "total_keys": total_keys,
                "key_counts": key_counts,
                "memory_usage": info.get("used_memory_human", "unknown"),
                "connected_clients": info.get("connected_clients", 0),
                "uptime": info.get("uptime_in_seconds", 0)
            }
            
        except Exception as e:
            logger.error(f"Error getting cache stats: {e}")
            return {"status": "error", "error": str(e)}
    
    async def cleanup_expired_keys(self) -> int:
        """Clean up expired keys (manual cleanup for debugging)"""
        if not self.redis_client:
            return 0
            
        try:
            # Get all our keys
            pattern = self._make_key("*")
            keys = await self.redis_client.keys(pattern)
            
            expired_count = 0
            batch_size = 100
            
            for i in range(0, len(keys), batch_size):
                batch = keys[i:i + batch_size]
                
                # Check TTL for each key
                pipe = self.redis_client.pipeline()
                for key in batch:
                    pipe.ttl(key)
                ttls = await pipe.execute()
                
                # Collect expired keys (TTL = -2 means expired)
                expired_keys = [key for key, ttl in zip(batch, ttls) if ttl == -2]
                
                if expired_keys:
                    await self.redis_client.delete(*expired_keys)
                    expired_count += len(expired_keys)
            
            if expired_count > 0:
                logger.info(f"Cleaned up {expired_count} expired cache keys")
            
            return expired_count
            
        except Exception as e:
            logger.error(f"Error cleaning up expired keys: {e}")
            return 0
    
    def _prepare_for_serialization(self, obj: Any) -> Any:
        """Prepare object for JSON serialization"""
        if isinstance(obj, dict):
            return {k: self._prepare_for_serialization(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._prepare_for_serialization(item) for item in obj]
        elif isinstance(obj, datetime):
            return obj.isoformat()
        elif hasattr(obj, '__dict__'):
            return self._prepare_for_serialization(obj.__dict__)
        else:
            return obj
    
    async def close(self):
        """Close Redis connection"""
        if self.redis_client:
            await self.redis_client.close()
            logger.info("Closed Redis connection")