# Subtitle Configuration

# Supported subtitle languages with their codes, names, and flags
SUPPORTED_LANGUAGES = {
    'en': {'name': 'English', 'flag': '🇺🇸', 'opensubtitles_code': 'en'},
    'es': {'name': 'Spanish', 'flag': '🇪🇸', 'opensubtitles_code': 'es'},
    'fr': {'name': 'French', 'flag': '🇫🇷', 'opensubtitles_code': 'fr'},
    'de': {'name': 'German', 'flag': '🇩🇪', 'opensubtitles_code': 'de'},
    'it': {'name': 'Italian', 'flag': '🇮🇹', 'opensubtitles_code': 'it'},
    'pt': {'name': 'Portuguese', 'flag': '🇵🇹', 'opensubtitles_code': 'pt'},
    'ru': {'name': 'Russian', 'flag': '🇷🇺', 'opensubtitles_code': 'ru'},
    'ja': {'name': 'Japanese', 'flag': '🇯🇵', 'opensubtitles_code': 'ja'},
    'ko': {'name': 'Korean', 'flag': '🇰🇷', 'opensubtitles_code': 'ko'},
    'zh': {'name': 'Chinese', 'flag': '🇨🇳', 'opensubtitles_code': 'zh'},
    'ar': {'name': 'Arabic', 'flag': '🇸🇦', 'opensubtitles_code': 'ar'},
    'hi': {'name': 'Hindi', 'flag': '🇮🇳', 'opensubtitles_code': 'hi'},
    'ta': {'name': 'Tamil', 'flag': '🇮🇳', 'opensubtitles_code': 'ta'},
    'te': {'name': 'Telugu', 'flag': '🇮🇳', 'opensubtitles_code': 'te'},
    'ml': {'name': 'Malayalam', 'flag': '🇮🇳', 'opensubtitles_code': 'ml'},
    'si': {'name': 'Sinhala', 'flag': '🇱🇰', 'opensubtitles_code': 'si'},
    'th': {'name': 'Thai', 'flag': '🇹🇭', 'opensubtitles_code': 'th'},
    'tr': {'name': 'Turkish', 'flag': '🇹🇷', 'opensubtitles_code': 'tr'},
    'nl': {'name': 'Dutch', 'flag': '🇳🇱', 'opensubtitles_code': 'nl'},
    'sv': {'name': 'Swedish', 'flag': '🇸🇪', 'opensubtitles_code': 'sv'},
    'no': {'name': 'Norwegian', 'flag': '🇳🇴', 'opensubtitles_code': 'no'},
    'da': {'name': 'Danish', 'flag': '🇩🇰', 'opensubtitles_code': 'da'},
    'fi': {'name': 'Finnish', 'flag': '🇫🇮', 'opensubtitles_code': 'fi'},
    'pl': {'name': 'Polish', 'flag': '🇵🇱', 'opensubtitles_code': 'pl'},
    'cs': {'name': 'Czech', 'flag': '🇨🇿', 'opensubtitles_code': 'cs'},
    'hu': {'name': 'Hungarian', 'flag': '🇭🇺', 'opensubtitles_code': 'hu'},
    'ro': {'name': 'Romanian', 'flag': '🇷🇴', 'opensubtitles_code': 'ro'},
    'bg': {'name': 'Bulgarian', 'flag': '🇧🇬', 'opensubtitles_code': 'bg'},
    'hr': {'name': 'Croatian', 'flag': '🇭🇷', 'opensubtitles_code': 'hr'},
    'sr': {'name': 'Serbian', 'flag': '🇷🇸', 'opensubtitles_code': 'sr'},
    'sk': {'name': 'Slovak', 'flag': '🇸🇰', 'opensubtitles_code': 'sk'},
    'sl': {'name': 'Slovenian', 'flag': '🇸🇮', 'opensubtitles_code': 'sl'},
    'lv': {'name': 'Latvian', 'flag': '🇱🇻', 'opensubtitles_code': 'lv'},
    'lt': {'name': 'Lithuanian', 'flag': '🇱🇹', 'opensubtitles_code': 'lt'},
    'et': {'name': 'Estonian', 'flag': '🇪🇪', 'opensubtitles_code': 'et'},
    'uk': {'name': 'Ukrainian', 'flag': '🇺🇦', 'opensubtitles_code': 'uk'},
    'be': {'name': 'Belarusian', 'flag': '🇧🇾', 'opensubtitles_code': 'be'},
    'he': {'name': 'Hebrew', 'flag': '🇮🇱', 'opensubtitles_code': 'he'},
    'fa': {'name': 'Persian', 'flag': '🇮🇷', 'opensubtitles_code': 'fa'},
    'ur': {'name': 'Urdu', 'flag': '🇵🇰', 'opensubtitles_code': 'ur'},
    'bn': {'name': 'Bengali', 'flag': '🇧🇩', 'opensubtitles_code': 'bn'},
    'id': {'name': 'Indonesian', 'flag': '🇮🇩', 'opensubtitles_code': 'id'},
    'ms': {'name': 'Malay', 'flag': '🇲🇾', 'opensubtitles_code': 'ms'},
    'vi': {'name': 'Vietnamese', 'flag': '🇻🇳', 'opensubtitles_code': 'vi'},
}

# Default subtitle languages to show first
PRIORITY_LANGUAGES = ['en', 'es', 'fr', 'de', 'hi', 'ta', 'si', 'ar', 'ru', 'zh']

# OpenSubtitles API configuration
OPENSUBTITLES_CONFIG = {
    'base_url': 'https://api.opensubtitles.com',
    'api_version': 'v1',
    'user_agent': 'TelegramBot v1.0.0',
    'rate_limit': {
        'requests_per_10_seconds': 40,
        'daily_downloads_free': 20,
        'daily_downloads_vip': 1000
    }
}

# SubDB API configuration (fallback)
SUBDB_CONFIG = {
    'base_url': 'http://api.thesubdb.com',
    'user_agent': 'SubDB/1.0 (TelegramBot/1.0; https://telegram.org/)',
    'supported_formats': ['srt', 'vtt']
}

# Subtitle file settings
SUBTITLE_SETTINGS = {
    'max_file_size': 5 * 1024 * 1024,  # 5MB
    'supported_formats': ['.srt', '.vtt', '.ass', '.ssa', '.sub'],
    'default_format': 'srt',
    'encoding': 'utf-8',
    'cache_duration': 24 * 60 * 60,  # 24 hours in seconds
}

# Rate limiting settings
RATE_LIMIT_CONFIG = {
    'api_calls_per_minute': 60,
    'api_calls_per_hour': 1000,
    'concurrent_requests': 5,
    'retry_attempts': 3,
    'retry_delay': 1,  # seconds
}

# Cache settings
CACHE_CONFIG = {
    'redis_prefix': 'subtitle:',
    'metadata_ttl': 3600,  # 1 hour
    'content_ttl': 86400,  # 24 hours
    'search_results_ttl': 1800,  # 30 minutes
    'max_cache_size': 100 * 1024 * 1024,  # 100MB
}

# UI Configuration
UI_CONFIG = {
    'languages_per_row': 2,
    'max_languages_per_page': 10,
    'show_download_count': True,
    'show_quality_info': True,
    'timeout_seconds': 300,  # 5 minutes
}

# Quality indicators for subtitles
QUALITY_INDICATORS = {
    'excellent': {'min_downloads': 1000, 'emoji': '🌟'},
    'good': {'min_downloads': 100, 'emoji': '⭐'},
    'average': {'min_downloads': 10, 'emoji': '✨'},
    'basic': {'min_downloads': 0, 'emoji': '📝'}
}

# Movie identification patterns
MOVIE_PATTERNS = {
    'year_pattern': r'\b(19|20)\d{2}\b',
    'quality_pattern': r'\b(720p|1080p|480p|2160p|4K)\b',
    'format_pattern': r'\b(BluRay|BRRip|DVDRip|WebRip|HDRip|CAMRip)\b',
    'season_episode_pattern': r'[Ss](\d{1,2})[Ee](\d{1,2})'
}

# Error messages
ERROR_MESSAGES = {
    'api_unavailable': "Subtitle service is temporarily unavailable. Please try again later.",
    'no_subtitles_found': "No subtitles found for this movie in the selected language.",
    'download_failed': "Failed to download subtitles. Please try again.",
    'invalid_format': "Unsupported subtitle format.",
    'file_too_large': "Subtitle file is too large to process.",
    'rate_limit_exceeded': "Too many requests. Please wait a moment and try again.",
    'network_error': "Network error occurred. Please check your connection."
}

# Success messages
SUCCESS_MESSAGES = {
    'subtitles_found': "✅ Found {count} subtitle(s) for {movie_title}",
    'download_started': "📥 Downloading subtitles...",
    'download_completed': "✅ Subtitles downloaded successfully!",
    'cache_hit': "⚡ Loaded from cache"
}