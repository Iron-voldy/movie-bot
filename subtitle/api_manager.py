import asyncio
import aiohttp
import hashlib
import logging
import re
from typing import List, Dict, Optional, Any
from datetime import datetime, timedelta
from config.subtitle_config import (
    OPENSUBTITLES_CONFIG, SUBDB_CONFIG, RATE_LIMIT_CONFIG, 
    SUPPORTED_LANGUAGES, ERROR_MESSAGES
)
from info import OPENSUBTITLES_API_KEY, OPENSUBTITLES_USERNAME, OPENSUBTITLES_PASSWORD

logger = logging.getLogger(__name__)

class RateLimiter:
    def __init__(self, max_calls: int, time_window: int):
        self.max_calls = max_calls
        self.time_window = time_window
        self.calls = []
        self.lock = asyncio.Lock()
    
    async def acquire(self):
        async with self.lock:
            now = datetime.now()
            # Remove old calls outside the time window
            self.calls = [call_time for call_time in self.calls 
                         if (now - call_time).total_seconds() < self.time_window]
            
            if len(self.calls) >= self.max_calls:
                sleep_time = self.time_window - (now - self.calls[0]).total_seconds()
                if sleep_time > 0:
                    await asyncio.sleep(sleep_time)
                    return await self.acquire()
            
            self.calls.append(now)

class OpenSubtitlesAPI:
    def __init__(self, api_key: str, username: str, password: str):
        self.api_key = api_key
        self.username = username
        self.password = password
        self.base_url = OPENSUBTITLES_CONFIG['base_url']
        self.session = None
        self.token = None
        self.token_expires = None
        self.rate_limiter = RateLimiter(
            RATE_LIMIT_CONFIG['api_calls_per_minute'], 60
        )
        
    async def _get_session(self) -> aiohttp.ClientSession:
        if not self.session:
            timeout = aiohttp.ClientTimeout(total=30)
            self.session = aiohttp.ClientSession(
                timeout=timeout,
                headers={
                    'User-Agent': OPENSUBTITLES_CONFIG['user_agent'],
                    'Api-Key': self.api_key,
                    'Content-Type': 'application/json'
                }
            )
        return self.session
    
    async def _login(self) -> bool:
        """Login to OpenSubtitles API and get authentication token"""
        if not self.api_key or not self.username or not self.password:
            logger.warning("OpenSubtitles credentials not provided")
            return False
            
        try:
            session = await self._get_session()
            login_data = {
                'username': self.username,
                'password': self.password
            }
            
            async with session.post(
                f"{self.base_url}/api/v1/login",
                json=login_data
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    self.token = data.get('token')
                    # Token typically expires in 24 hours
                    self.token_expires = datetime.now() + timedelta(hours=23)
                    logger.info("Successfully logged in to OpenSubtitles")
                    return True
                else:
                    logger.error(f"Login failed: {response.status}")
                    return False
                    
        except Exception as e:
            logger.error(f"Login error: {e}")
            return False
    
    async def _ensure_authenticated(self) -> bool:
        """Ensure we have a valid authentication token"""
        if not self.token or (self.token_expires and datetime.now() >= self.token_expires):
            return await self._login()
        return True
    
    async def search_subtitles(self, imdb_id: str, language: str, query: str = None) -> List[Dict]:
        """Search for subtitles using IMDB ID or query"""
        await self.rate_limiter.acquire()
        
        if not await self._ensure_authenticated():
            logger.error("Authentication failed")
            return []
        
        try:
            session = await self._get_session()
            
            # Prepare search parameters
            params = {
                'languages': SUPPORTED_LANGUAGES.get(language, {}).get('opensubtitles_code', language),
                'order_by': 'download_count',
                'order_direction': 'desc'
            }
            
            if imdb_id:
                # Remove 'tt' prefix if present
                clean_imdb_id = imdb_id.replace('tt', '')
                params['imdb_id'] = clean_imdb_id
            elif query:
                params['query'] = query
            else:
                return []
            
            headers = {'Authorization': f'Bearer {self.token}'}
            
            async with session.get(
                f"{self.base_url}/api/v1/subtitles",
                params=params,
                headers=headers
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    return self._process_search_results(data.get('data', []))
                elif response.status == 429:
                    logger.warning("Rate limit exceeded")
                    await asyncio.sleep(60)  # Wait 1 minute
                    return []
                else:
                    logger.error(f"Search failed: {response.status}")
                    return []
                    
        except Exception as e:
            logger.error(f"Search error: {e}")
            return []
    
    def _process_search_results(self, results: List[Dict]) -> List[Dict]:
        """Process and normalize search results"""
        processed = []
        for item in results:
            try:
                attributes = item.get('attributes', {})
                processed.append({
                    'id': item.get('id'),
                    'language': attributes.get('language'),
                    'download_count': attributes.get('download_count', 0),
                    'release': attributes.get('release', ''),
                    'filename': attributes.get('files', [{}])[0].get('file_name', ''),
                    'url': attributes.get('url', ''),
                    'format': 'srt',  # OpenSubtitles primarily uses SRT
                    'provider': 'opensubtitles',
                    'quality_score': self._calculate_quality_score(attributes)
                })
            except Exception as e:
                logger.error(f"Error processing result: {e}")
                continue
        
        # Sort by quality score (download count is primary factor)
        return sorted(processed, key=lambda x: x['quality_score'], reverse=True)
    
    def _calculate_quality_score(self, attributes: Dict) -> int:
        """Calculate quality score based on various factors"""
        score = 0
        
        # Download count is the primary factor
        download_count = attributes.get('download_count', 0)
        score += download_count * 10
        
        # Bonus for certain releases
        release = attributes.get('release', '').lower()
        if any(term in release for term in ['bluray', 'web-dl', 'webrip']):
            score += 100
        
        return score
    
    async def download_subtitle(self, subtitle_id: str) -> Optional[bytes]:
        """Download subtitle content"""
        await self.rate_limiter.acquire()
        
        if not await self._ensure_authenticated():
            logger.error("Authentication failed")
            return None
        
        try:
            session = await self._get_session()
            headers = {'Authorization': f'Bearer {self.token}'}
            
            # Request download
            download_data = {'file_id': subtitle_id}
            async with session.post(
                f"{self.base_url}/api/v1/download",
                json=download_data,
                headers=headers
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    download_link = data.get('link')
                    
                    if download_link:
                        # Download the actual file
                        async with session.get(download_link) as file_response:
                            if file_response.status == 200:
                                return await file_response.read()
                
                logger.error(f"Download failed: {response.status}")
                return None
                
        except Exception as e:
            logger.error(f"Download error: {e}")
            return None
    
    async def close(self):
        """Close the session"""
        if self.session:
            await self.session.close()

class SubDBAPI:
    def __init__(self):
        self.base_url = SUBDB_CONFIG['base_url']
        self.session = None
        
    async def _get_session(self) -> aiohttp.ClientSession:
        if not self.session:
            timeout = aiohttp.ClientTimeout(total=30)
            self.session = aiohttp.ClientSession(
                timeout=timeout,
                headers={'User-Agent': SUBDB_CONFIG['user_agent']}
            )
        return self.session
    
    def _calculate_file_hash(self, file_path: str) -> Optional[str]:
        """Calculate SubDB hash for a video file"""
        try:
            readsize = 64 * 1024  # 64KB
            with open(file_path, 'rb') as f:
                data = f.read(readsize)
                f.seek(-readsize, 2)  # Seek to end - 64KB
                data += f.read(readsize)
            
            return hashlib.md5(data).hexdigest()
        except Exception as e:
            logger.error(f"Hash calculation error: {e}")
            return None
    
    async def search_by_hash(self, file_hash: str, language: str) -> List[Dict]:
        """Search subtitles by file hash"""
        try:
            session = await self._get_session()
            
            params = {
                'action': 'search',
                'hash': file_hash,
                'language': language
            }
            
            async with session.get(self.base_url, params=params) as response:
                if response.status == 200:
                    languages = await response.text()
                    if language in languages.split(','):
                        return [{
                            'id': file_hash,
                            'language': language,
                            'provider': 'subdb',
                            'format': 'srt',
                            'download_count': 0,
                            'quality_score': 50  # Medium quality score
                        }]
                return []
                
        except Exception as e:
            logger.error(f"SubDB search error: {e}")
            return []
    
    async def download_subtitle(self, file_hash: str, language: str) -> Optional[bytes]:
        """Download subtitle by hash and language"""
        try:
            session = await self._get_session()
            
            params = {
                'action': 'download',
                'hash': file_hash,
                'language': language
            }
            
            async with session.get(self.base_url, params=params) as response:
                if response.status == 200:
                    return await response.read()
                return None
                
        except Exception as e:
            logger.error(f"SubDB download error: {e}")
            return None
    
    async def close(self):
        """Close the session"""
        if self.session:
            await self.session.close()

class SubtitleAPIManager:
    """Main API manager that handles both OpenSubtitles and SubDB"""
    
    def __init__(self, api_key: str = None, username: str = None, password: str = None):
        self.opensubtitles = OpenSubtitlesAPI(
            api_key or OPENSUBTITLES_API_KEY,
            username or OPENSUBTITLES_USERNAME,
            password or OPENSUBTITLES_PASSWORD
        ) if (api_key or OPENSUBTITLES_API_KEY) else None
        
        self.subdb = SubDBAPI()
        self.retry_attempts = RATE_LIMIT_CONFIG['retry_attempts']
        self.retry_delay = RATE_LIMIT_CONFIG['retry_delay']
    
    async def search_subtitles(self, movie_title: str, imdb_id: str = None, 
                             language: str = 'en', file_hash: str = None) -> List[Dict]:
        """Search for subtitles using multiple providers"""
        all_results = []
        
        # Try OpenSubtitles first
        if self.opensubtitles:
            try:
                os_results = await self._retry_operation(
                    self.opensubtitles.search_subtitles,
                    imdb_id, language, movie_title
                )
                all_results.extend(os_results)
                logger.info(f"OpenSubtitles found {len(os_results)} results")
            except Exception as e:
                logger.error(f"OpenSubtitles search failed: {e}")
        
        # Try SubDB as fallback if we have a file hash
        if file_hash and len(all_results) < 3:  # Only if we need more results
            try:
                subdb_results = await self._retry_operation(
                    self.subdb.search_by_hash,
                    file_hash, language
                )
                all_results.extend(subdb_results)
                logger.info(f"SubDB found {len(subdb_results)} results")
            except Exception as e:
                logger.error(f"SubDB search failed: {e}")
        
        # Remove duplicates and sort by quality
        unique_results = self._deduplicate_results(all_results)
        return sorted(unique_results, key=lambda x: x.get('quality_score', 0), reverse=True)
    
    async def download_subtitle_content(self, subtitle_info: Dict) -> Optional[bytes]:
        """Download subtitle content based on provider"""
        provider = subtitle_info.get('provider', 'opensubtitles')
        
        try:
            if provider == 'opensubtitles' and self.opensubtitles:
                return await self._retry_operation(
                    self.opensubtitles.download_subtitle,
                    subtitle_info['id']
                )
            elif provider == 'subdb':
                return await self._retry_operation(
                    self.subdb.download_subtitle,
                    subtitle_info['id'],
                    subtitle_info['language']
                )
            else:
                logger.error(f"Unknown provider: {provider}")
                return None
                
        except Exception as e:
            logger.error(f"Download failed for {provider}: {e}")
            return None
    
    async def get_available_languages(self, movie_title: str, imdb_id: str = None) -> List[str]:
        """Get list of available subtitle languages for a movie"""
        available_languages = set()
        
        # Check multiple popular languages
        check_languages = ['en', 'es', 'fr', 'de', 'hi', 'ta', 'si', 'ar', 'ru', 'zh']
        
        # Use semaphore to limit concurrent requests
        semaphore = asyncio.Semaphore(RATE_LIMIT_CONFIG['concurrent_requests'])
        
        async def check_language(lang):
            async with semaphore:
                try:
                    results = await self.search_subtitles(movie_title, imdb_id, lang)
                    if results:
                        available_languages.add(lang)
                except Exception as e:
                    logger.error(f"Error checking language {lang}: {e}")
        
        # Check languages concurrently
        tasks = [check_language(lang) for lang in check_languages]
        await asyncio.gather(*tasks, return_exceptions=True)
        
        return sorted(list(available_languages))
    
    def _deduplicate_results(self, results: List[Dict]) -> List[Dict]:
        """Remove duplicate results based on filename and language"""
        seen = set()
        unique_results = []
        
        for result in results:
            # Create a unique key based on filename and language
            key = f"{result.get('filename', '')}_{result.get('language', '')}"
            if key not in seen:
                seen.add(key)
                unique_results.append(result)
        
        return unique_results
    
    async def _retry_operation(self, operation, *args, **kwargs):
        """Retry an operation with exponential backoff"""
        last_exception = None
        
        for attempt in range(self.retry_attempts):
            try:
                return await operation(*args, **kwargs)
            except Exception as e:
                last_exception = e
                if attempt < self.retry_attempts - 1:
                    wait_time = self.retry_delay * (2 ** attempt)
                    logger.warning(f"Attempt {attempt + 1} failed, retrying in {wait_time}s: {e}")
                    await asyncio.sleep(wait_time)
                else:
                    logger.error(f"All {self.retry_attempts} attempts failed: {e}")
        
        raise last_exception
    
    def extract_movie_info(self, filename: str) -> Dict[str, Any]:
        """Extract movie information from filename"""
        info = {
            'title': filename,
            'year': None,
            'quality': None,
            'format': None,
            'is_series': False,
            'season': None,
            'episode': None
        }
        
        # Extract year
        year_match = re.search(r'\b(19|20)\d{2}\b', filename)
        if year_match:
            info['year'] = year_match.group()
        
        # Extract quality
        quality_match = re.search(r'\b(720p|1080p|480p|2160p|4K)\b', filename, re.IGNORECASE)
        if quality_match:
            info['quality'] = quality_match.group()
        
        # Extract format
        format_match = re.search(r'\b(BluRay|BRRip|DVDRip|WebRip|HDRip|CAMRip)\b', filename, re.IGNORECASE)
        if format_match:
            info['format'] = format_match.group()
        
        # Check if it's a series
        series_match = re.search(r'[Ss](\d{1,2})[Ee](\d{1,2})', filename)
        if series_match:
            info['is_series'] = True
            info['season'] = int(series_match.group(1))
            info['episode'] = int(series_match.group(2))
        
        # Clean title (remove year, quality, format indicators)
        clean_title = filename
        for pattern in [r'\b(19|20)\d{2}\b', r'\b(720p|1080p|480p|2160p|4K)\b', 
                       r'\b(BluRay|BRRip|DVDRip|WebRip|HDRip|CAMRip)\b', 
                       r'[Ss]\d{1,2}[Ee]\d{1,2}']:
            clean_title = re.sub(pattern, '', clean_title, flags=re.IGNORECASE)
        
        # Remove common separators and clean up
        clean_title = re.sub(r'[._\-\[\]()]', ' ', clean_title)
        clean_title = re.sub(r'\s+', ' ', clean_title).strip()
        info['title'] = clean_title
        
        return info
    
    async def close(self):
        """Close all API connections"""
        if self.opensubtitles:
            await self.opensubtitles.close()
        if self.subdb:
            await self.subdb.close()