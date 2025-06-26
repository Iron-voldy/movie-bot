import logging
from hydrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid
from info import AUTH_CHANNEL, LONG_IMDB_DESCRIPTION, MAX_LIST_ELM, ENABLE_SUBTITLES
from imdb import Cinemagoer
import asyncio
from hydrogram.types import Message, InlineKeyboardButton
from hydrogram import enums
from typing import Union, List, Dict, Optional, Tuple
import re
import os
from datetime import datetime
from database.users_chats_db import db

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

imdb = Cinemagoer() 

# temp db for banned 
class temp(object):
    BANNED_USERS = []
    BANNED_CHATS = []
    ME = None
    CURRENT = int(os.environ.get("SKIP", 2))
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None
    SETTINGS = {}
    AUTH_CHANNEL = []
    # Subtitle system references
    SUBTITLE_SYSTEM = None
    ADMINS = []

async def delete_messages(time, msgs):
    """Delete messages after specified time"""
    await asyncio.sleep(time)
    for msg in msgs:
        try:
            await msg.delete()
        except Exception as e:
            logger.error(f"Error deleting message: {e}")

def remove_username_from_filename(filename):
    """Remove username mentions from filename"""
    # Pattern to match @username (with letters, numbers, underscores)
    pattern = r'\s*@[a-zA-Z0-9_]+\s*'
    
    # Remove the username and clean up extra spaces
    new_name = re.sub(pattern, ' ', filename).strip()
    
    # Replace multiple spaces with single space
    new_name = re.sub(r'\s+', ' ', new_name)
    
    return new_name

def format_size(size_str):
    """Format file size string for better display"""
    if "MB" in size_str:
        # Remove decimal part for MB and spaces
        size_num = size_str.split()[0]
        if '.' in size_num:
            size_num = size_num.split('.')[0]
        return f"{size_num}MB"  # No space
    elif "GB" in size_str:
        # Remove spaces for GB
        size_num = size_str.split()[0]
        return f"{size_num}GB"  # No space
    else:
        return size_str.replace(" ", "")  # Fallback (remove spaces if any)

# ============== SUBTITLE UTILITY FUNCTIONS ==============

def extract_movie_info_from_filename(filename: str) -> Dict[str, any]:
    """Extract comprehensive movie information from filename for subtitle search"""
    info = {
        'original_filename': filename,
        'clean_title': '',
        'year': None,
        'quality': None,
        'format': None,
        'is_series': False,
        'season': None,
        'episode': None,
        'language_indicators': [],
        'release_group': None,
        'source': None,
        'codec': None,
        'audio': None
    }
    
    # Extract year (prioritize 4-digit years)
    year_matches = re.findall(r'\b(19|20)\d{2}\b', filename)
    if year_matches:
        # Take the last year found (usually the release year)
        info['year'] = year_matches[-1]
    
    # Extract quality/resolution
    quality_patterns = [
        r'\b(2160p|4K|UHD)\b',
        r'\b(1080p|FullHD|FHD)\b', 
        r'\b(720p|HD)\b',
        r'\b(480p|SD)\b',
        r'\b(540p)\b'
    ]
    
    for pattern in quality_patterns:
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            info['quality'] = match.group(1).upper()
            break
    
    # Extract source/format
    source_patterns = [
        r'\b(BluRay|Blu-Ray|BRRip|BDRip)\b',
        r'\b(WebRip|Web-Rip|WEBRip)\b',
        r'\b(WEB-DL|WebDL|WEB)\b',
        r'\b(DVDRip|DVD-Rip)\b',
        r'\b(HDRip|HD-Rip)\b',
        r'\b(CAMRip|CAM|TS|TC)\b',
        r'\b(HDTV|PDTV|SDTV)\b'
    ]
    
    for pattern in source_patterns:
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            info['source'] = match.group(1)
            break
    
    # Extract codec information
    codec_patterns = [
        r'\b(x264|H\.264|AVC)\b',
        r'\b(x265|H\.265|HEVC)\b',
        r'\b(XviD|DivX)\b',
        r'\b(AV1)\b'
    ]
    
    for pattern in codec_patterns:
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            info['codec'] = match.group(1)
            break
    
    # Extract audio information
    audio_patterns = [
        r'\b(DTS-HD|DTS-X|DTS)\b',
        r'\b(TrueHD|Atmos)\b',
        r'\b(AC3|DD|EAC3)\b',
        r'\b(AAC|MP3)\b',
        r'\b(FLAC|PCM)\b'
    ]
    
    for pattern in audio_patterns:
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            info['audio'] = match.group(1)
            break
    
    # Check if it's a series with comprehensive patterns
    series_patterns = [
        r'[Ss](\d{1,3})[Ee](\d{1,3})',  # S01E01 format
        r'Season[\s\.](\d{1,2})[\s\.]Episode[\s\.](\d{1,3})',  # Season 1 Episode 1
        r'(\d{1,2})x(\d{1,3})',  # 1x01 format
        r'Episode[\s\.](\d{1,3})',  # Episode 1
        r'Ep[\s\.](\d{1,3})',  # Ep 1
        r'Part[\s\.](\d{1,3})'   # Part 1
    ]
    
    for pattern in series_patterns:
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            info['is_series'] = True
            groups = match.groups()
            if len(groups) >= 2:
                info['season'] = int(groups[0])
                info['episode'] = int(groups[1])
            elif len(groups) == 1:
                info['episode'] = int(groups[0])
            break
    
    # Extract language indicators
    language_patterns = {
        'english': [r'\b(English|Eng|EN)\b', r'\b(ENGLISH)\b'],
        'hindi': [r'\b(Hindi|Hin|HI)\b', r'\b(HINDI)\b'],
        'tamil': [r'\b(Tamil|Tam|TA)\b', r'\b(TAMIL)\b'],
        'telugu': [r'\b(Telugu|Tel|TE)\b', r'\b(TELUGU)\b'],
        'malayalam': [r'\b(Malayalam|Mal|ML)\b', r'\b(MALAYALAM)\b'],
        'kannada': [r'\b(Kannada|Kan|KN)\b', r'\b(KANNADA)\b'],
        'spanish': [r'\b(Spanish|Spa|ES)\b', r'\b(SPANISH|Espanol)\b'],
        'french': [r'\b(French|Fra|FR)\b', r'\b(FRENCH|Francais)\b'],
        'german': [r'\b(German|Ger|DE)\b', r'\b(GERMAN|Deutsch)\b'],
        'italian': [r'\b(Italian|Ita|IT)\b', r'\b(ITALIAN|Italiano)\b'],
        'russian': [r'\b(Russian|Rus|RU)\b', r'\b(RUSSIAN)\b'],
        'japanese': [r'\b(Japanese|Jap|JP)\b', r'\b(JAPANESE)\b'],
        'korean': [r'\b(Korean|Kor|KR)\b', r'\b(KOREAN)\b'],
        'chinese': [r'\b(Chinese|Chi|CN|Mandarin|Cantonese)\b', r'\b(CHINESE)\b'],
        'arabic': [r'\b(Arabic|Ara|AR)\b', r'\b(ARABIC)\b'],
        'portuguese': [r'\b(Portuguese|Por|PT)\b', r'\b(PORTUGUESE)\b'],
        'dutch': [r'\b(Dutch|Dut|NL)\b', r'\b(DUTCH)\b'],
        'turkish': [r'\b(Turkish|Tur|TR)\b', r'\b(TURKISH)\b']
    }
    
    for lang, patterns in language_patterns.items():
        for pattern in patterns:
            if re.search(pattern, filename, re.IGNORECASE):
                info['language_indicators'].append(lang)
                break
    
    # Extract release group (usually at the end in brackets or after a dash)
    release_group_patterns = [
        r'-([A-Z0-9]+)(?:\.[a-zA-Z0-9]+)*$',  # -GROUP.ext
        r'\[([A-Z0-9]+)\]',  # [GROUP]
        r'\(([A-Z0-9]+)\)'   # (GROUP)
    ]
    
    for pattern in release_group_patterns:
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            potential_group = match.group(1)
            # Filter out common extensions and quality indicators
            if not re.match(r'^(mkv|mp4|avi|srt|mp3|1080p|720p|480p)$', potential_group, re.IGNORECASE):
                info['release_group'] = potential_group
                break
    
    # Clean title (remove all extracted information)
    clean_title = filename
    
    # Remove year
    if info['year']:
        clean_title = re.sub(rf'\b{info["year"]}\b', '', clean_title)
    
    # Remove quality, source, codec, audio
    removal_items = [info['quality'], info['source'], info['codec'], info['audio'], info['release_group']]
    for item in removal_items:
        if item:
            clean_title = re.sub(rf'\b{re.escape(item)}\b', '', clean_title, flags=re.IGNORECASE)
    
    # Remove series information
    if info['is_series']:
        series_removal_patterns = [
            r'[Ss]\d{1,3}[Ee]\d{1,3}',
            r'Season[\s\.]?\d{1,2}',
            r'Episode[\s\.]?\d{1,3}',
            r'\d{1,2}x\d{1,3}',
            r'Ep[\s\.]?\d{1,3}',
            r'Part[\s\.]?\d{1,3}'
        ]
        for pattern in series_removal_patterns:
            clean_title = re.sub(pattern, '', clean_title, flags=re.IGNORECASE)
    
    # Remove language indicators
    for lang_list in language_patterns.values():
        for pattern in lang_list:
            clean_title = re.sub(pattern, '', clean_title, flags=re.IGNORECASE)
    
    # Remove common brackets and their contents
    clean_title = re.sub(r'\[[^\]]*\]', '', clean_title)  # Remove [content]
    clean_title = re.sub(r'\([^)]*\)', '', clean_title)   # Remove (content) - but be careful with years
    clean_title = re.sub(r'\{[^}]*\}', '', clean_title)   # Remove {content}
    
    # Remove common separators and clean up
    clean_title = re.sub(r'[._\-\+\[\](){}\|]', ' ', clean_title)
    clean_title = re.sub(r'\s+', ' ', clean_title).strip()
    
    # Remove common keywords that aren't part of the title
    removal_keywords = [
        'download', 'free', 'full', 'movie', 'film', 'watch', 'online',
        'streaming', 'hd', 'quality', 'rip', 'dual', 'audio', 'subtitle',
        'sub', 'dubbed', 'org', 'mkv', 'mp4', 'avi', 'www', 'com', 'net',
        'complete', 'uncut', 'extended', 'directors', 'cut', 'remastered',
        'limited', 'theatrical', 'imax', 'proper', 'repack', 'internal'
    ]
    
    words = clean_title.split()
    filtered_words = [word for word in words if word.lower() not in removal_keywords and len(word) > 1]
    clean_title = ' '.join(filtered_words).strip()
    
    # Final cleanup - remove any remaining single characters or numbers at the end
    clean_title = re.sub(r'\s+[a-zA-Z0-9]\s*$', '', clean_title).strip()
    
    info['clean_title'] = clean_title
    
    return info

def is_movie_file(filename: str) -> bool:
    """Enhanced check if filename appears to be a movie/video file"""
    video_extensions = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.3gp', '.ogv']
    
    # Check file extension
    filename_lower = filename.lower()
    if any(filename_lower.endswith(ext) for ext in video_extensions):
        return True
    
    # Check for video quality indicators
    quality_indicators = ['2160p', '4K', '1080p', '720p', '480p', 'HDRip', 'BluRay', 'WebRip', 'BRRip']
    if any(indicator.lower() in filename_lower for indicator in quality_indicators):
        return True
    
    # Check for video source indicators
    source_indicators = ['bluray', 'webrip', 'web-dl', 'brrip', 'dvdrip', 'hdtv', 'cam', 'ts', 'tc']
    if any(indicator in filename_lower for indicator in source_indicators):
        return True
    
    # Check for codec indicators
    codec_indicators = ['x264', 'x265', 'h.264', 'h.265', 'hevc', 'xvid', 'divx']
    if any(indicator in filename_lower for indicator in codec_indicators):
        return True
    
    # Check for movie/series patterns
    movie_patterns = [
        r'\b(19|20)\d{2}\b',  # Year
        r'[Ss]\d{1,2}[Ee]\d{1,2}',  # Series pattern
        r'\d{1,2}x\d{1,2}'  # Episode pattern
    ]
    
    for pattern in movie_patterns:
        if re.search(pattern, filename):
            return True
    
    return False

def clean_search_query(query: str) -> str:
    """Clean and normalize search query for better subtitle matching"""
    # Remove common prefixes/suffixes
    query = re.sub(r'^(the|a|an)\s+', '', query, flags=re.IGNORECASE)
    query = re.sub(r'\s+(movie|film|series|season|episode)$', '', query, flags=re.IGNORECASE)
    
    # Remove year in parentheses
    query = re.sub(r'\s*\(\d{4}\)\s*', ' ', query)
    
    # Remove quality indicators
    quality_patterns = ['720p', '1080p', '480p', '2160p', '4K', 'HD', 'CAM', 'TS', 'BluRay', 'WebRip']
    for pattern in quality_patterns:
        query = re.sub(rf'\b{pattern}\b', '', query, flags=re.IGNORECASE)
    
    # Remove extra spaces and normalize
    query = re.sub(r'\s+', ' ', query).strip()
    
    return query

def format_subtitle_filename(movie_title: str, language: str, quality: str = None) -> str:
    """Generate a proper subtitle filename"""
    # Clean movie title for filename
    clean_title = "".join(c for c in movie_title if c.isalnum() or c in (' ', '-', '_', '.')).strip()
    clean_title = re.sub(r'\s+', '_', clean_title)
    
    # Remove common video extensions if present
    clean_title = re.sub(r'\.(mp4|mkv|avi|mov|wmv)$', '', clean_title, flags=re.IGNORECASE)
    
    # Add language
    filename = f"{clean_title}_{language}"
    
    # Add quality if provided
    if quality:
        filename += f"_{quality}"
    
    # Add extension
    filename += ".srt"
    
    return filename

def detect_content_type(filename: str) -> Dict[str, any]:
    """Enhanced detection of content type (movie, series, documentary, etc.)"""
    result = {
        'type': 'unknown',
        'subtype': None,
        'is_video': False,
        'title': filename,
        'confidence': 0.0,
        'metadata': {}
    }
    
    # Check if it's a video file
    result['is_video'] = is_movie_file(filename)
    
    # Extract detailed info
    movie_info = extract_movie_info_from_filename(filename)
    result['metadata'] = movie_info
    
    # Series detection with high confidence
    if movie_info['is_series']:
        result['type'] = 'series'
        result['confidence'] = 0.95
        
        # Determine series subtype
        if movie_info['season'] and movie_info['episode']:
            result['subtype'] = 'episode'
        elif movie_info['season']:
            result['subtype'] = 'season'
        else:
            result['subtype'] = 'series'
        
        return result
    
    # Documentary detection
    doc_indicators = ['documentary', 'docu', 'national.geographic', 'discovery', 'bbc', 'nova']
    if any(indicator in filename.lower() for indicator in doc_indicators):
        result['type'] = 'documentary'
        result['confidence'] = 0.8
        return result
    
    # Animation detection
    animation_indicators = ['animated', 'cartoon', 'anime', 'animation', 'pixar', 'disney', 'dreamworks']
    if any(indicator in filename.lower() for indicator in animation_indicators):
        result['type'] = 'movie'
        result['subtype'] = 'animation'
        result['confidence'] = 0.7
        return result
    
    # Movie detection
    movie_score = 0
    movie_indicators = [
        (r'\b(19|20)\d{2}\b', 2),  # Year (strong indicator)
        (r'\b(BluRay|BRRip|DVDRip|WebRip|HDRip|CAMRip)\b', 2),  # Source format
        (r'\b(720p|1080p|480p|2160p|4K)\b', 1),  # Quality
        (r'\b(x264|x265|HEVC|H\.264|H\.265)\b', 1),  # Codec
    ]
    
    for pattern, score in movie_indicators:
        if re.search(pattern, filename, re.IGNORECASE):
            movie_score += score
    
    if movie_score >= 3 or (movie_score >= 2 and result['is_video']):
        result['type'] = 'movie'
        result['confidence'] = min(0.9, 0.5 + (movie_score * 0.1))
    elif result['is_video'] and movie_score >= 1:
        result['type'] = 'movie'
        result['confidence'] = 0.6
    elif result['is_video']:
        result['type'] = 'movie'  # Default video files to movie
        result['confidence'] = 0.4
    
    return result

def extract_imdb_id_from_filename(filename: str) -> Optional[str]:
    """Try to extract IMDB ID from filename if present"""
    # Look for IMDB ID patterns
    imdb_patterns = [
        r'imdb[_\-]?(tt\d{7,})',
        r'(tt\d{7,})',
        r'imdb\.com/title/(tt\d{7,})'
    ]
    
    for pattern in imdb_patterns:
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            return match.group(1) if match.group(1).startswith('tt') else f"tt{match.group(1)}"
    
    return None

def suggest_alternative_titles(title: str) -> List[str]:
    """Suggest alternative title variations for better search results"""
    alternatives = [title]
    
    # Remove year if present
    no_year = re.sub(r'\s*\(\d{4}\)\s*', '', title)
    if no_year != title:
        alternatives.append(no_year)
    
    # Add common article variations
    if title.lower().startswith('the '):
        alternatives.append(title[4:])  # Remove "The "
    else:
        alternatives.append(f"The {title}")
    
    # Replace common symbols
    symbol_replacements = [
        ('&', 'and'),
        ('and', '&'),
        (':', ' '),
        ('-', ' '),
        ('_', ' ')
    ]
    
    for old, new in symbol_replacements:
        if old in title:
            alternatives.append(title.replace(old, new))
    
    # Remove duplicates while preserving order
    unique_alternatives = []
    for alt in alternatives:
        alt_clean = alt.strip()
        if alt_clean and alt_clean not in unique_alternatives:
            unique_alternatives.append(alt_clean)
    
    return unique_alternatives

def calculate_filename_similarity(filename1: str, filename2: str) -> float:
    """Calculate similarity between two filenames for subtitle matching"""
    # Normalize both filenames
    def normalize(fname):
        return re.sub(r'[^\w\s]', '', fname.lower())
    
    norm1 = normalize(filename1)
    norm2 = normalize(filename2)
    
    # Simple similarity based on common words
    words1 = set(norm1.split())
    words2 = set(norm2.split())
    
    if not words1 or not words2:
        return 0.0
    
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    
    return len(intersection) / len(union) if union else 0.0

def validate_subtitle_filename(subtitle_filename: str, movie_filename: str) -> bool:
    """Validate if subtitle filename matches movie filename"""
    similarity = calculate_filename_similarity(subtitle_filename, movie_filename)
    return similarity >= 0.3  # 30% similarity threshold

def get_subtitle_language_from_filename(filename: str) -> Optional[str]:
    """Try to detect subtitle language from filename"""
    language_patterns = {
        'en': [r'\.en\.', r'\.eng\.', r'\.english\.', r'_en_', r'_eng_', r'_english_'],
        'es': [r'\.es\.', r'\.spa\.', r'\.spanish\.', r'_es_', r'_spa_', r'_spanish_'],
        'fr': [r'\.fr\.', r'\.fre\.', r'\.french\.', r'_fr_', r'_fre_', r'_french_'],
        'de': [r'\.de\.', r'\.ger\.', r'\.german\.', r'_de_', r'_ger_', r'_german_'],
        'it': [r'\.it\.', r'\.ita\.', r'\.italian\.', r'_it_', r'_ita_', r'_italian_'],
        'pt': [r'\.pt\.', r'\.por\.', r'\.portuguese\.', r'_pt_', r'_por_', r'_portuguese_'],
        'ru': [r'\.ru\.', r'\.rus\.', r'\.russian\.', r'_ru_', r'_rus_', r'_russian_'],
        'ja': [r'\.ja\.', r'\.jap\.', r'\.japanese\.', r'_ja_', r'_jap_', r'_japanese_'],
        'ko': [r'\.ko\.', r'\.kor\.', r'\.korean\.', r'_ko_', r'_kor_', r'_korean_'],
        'zh': [r'\.zh\.', r'\.chi\.', r'\.chinese\.', r'_zh_', r'_chi_', r'_chinese_'],
        'ar': [r'\.ar\.', r'\.ara\.', r'\.arabic\.', r'_ar_', r'_ara_', r'_arabic_'],
        'hi': [r'\.hi\.', r'\.hin\.', r'\.hindi\.', r'_hi_', r'_hin_', r'_hindi_'],
        'ta': [r'\.ta\.', r'\.tam\.', r'\.tamil\.', r'_ta_', r'_tam_', r'_tamil_'],
        'te': [r'\.te\.', r'\.tel\.', r'\.telugu\.', r'_te_', r'_tel_', r'_telugu_'],
        'ml': [r'\.ml\.', r'\.mal\.', r'\.malayalam\.', r'_ml_', r'_mal_', r'_malayalam_'],
        'si': [r'\.si\.', r'\.sin\.', r'\.sinhala\.', r'_si_', r'_sin_', r'_sinhala_']
    }
    
    filename_lower = filename.lower()
    
    for lang_code, patterns in language_patterns.items():
        for pattern in patterns:
            if re.search(pattern, filename_lower):
                return lang_code
    
    return None

# ============== EXISTING UTILITY FUNCTIONS (Enhanced) ==============

async def is_subscribed(bot, query, channel):
    """Check if user is subscribed to channel"""
    if await db.find_join_req(query.from_user.id):
        return True
    try:
        user = await bot.get_chat_member(channel, query.from_user.id)
        return True
    except UserNotParticipant:
        return False

async def get_poster(query, bulk=False, id=False, file=None):
    """Get movie poster and information from IMDB"""
    if not id:
        # https://t.me/GetTGLink/4183
        query = (query.strip()).lower()
        title = query
        year = re.findall(r'[1-2]\d{3}$', query, re.IGNORECASE)
        if year:
            year = list_to_str(year[:1])
            title = (query.replace(year, "")).strip()
        elif file is not None:
            year = re.findall(r'[1-2]\d{3}', file, re.IGNORECASE)
            if year:
                year = list_to_str(year[:1]) 
        else:
            year = None
        movieid = imdb.search_movie(title.lower(), results=10)
        if not movieid:
            return None
        if year:
            filtered=list(filter(lambda k: str(k.get('year')) == str(year), movieid))
            if not filtered:
                filtered = movieid
        else:
            filtered = movieid
        movieid=list(filter(lambda k: k.get('kind') in ['movie', 'tv series'], filtered))
        if not movieid:
            movieid = filtered
        if bulk:
            return movieid
        movieid = movieid[0].movieID
    else:
        movieid = query
    movie = imdb.get_movie(movieid)
    if movie.get("original air date"):
        date = movie["original air date"]
    elif movie.get("year"):
        date = movie.get("year")
    else:
        date = "N/A"
    plot = ""
    if not LONG_IMDB_DESCRIPTION:
        plot = movie.get('plot')
        if plot and len(plot) > 0:
            plot = plot[0]
    else:
        plot = movie.get('plot outline')
    if plot and len(plot) > 800:
        plot = plot[0:800] + "..."

    return {
        'title': movie.get('title'),
        'votes': movie.get('votes'),
        "aka": list_to_str(movie.get("akas")),
        "seasons": movie.get("number of seasons"),
        "box_office": movie.get('box office'),
        'localized_title': movie.get('localized title'),
        'kind': movie.get("kind"),
        "imdb_id": f"tt{movie.get('imdbID')}",
        "cast": list_to_str(movie.get("cast")),
        "runtime": list_to_str(movie.get("runtimes")),
        "countries": list_to_str(movie.get("countries")),
        "certificates": list_to_str(movie.get("certificates")),
        "languages": list_to_str(movie.get("languages")),
        "director": list_to_str(movie.get("director")),
        "writer":list_to_str(movie.get("writer")),
        "producer":list_to_str(movie.get("producer")),
        "composer":list_to_str(movie.get("composer")) ,
        "cinematographer":list_to_str(movie.get("cinematographer")),
        "music_team": list_to_str(movie.get("music department")),
        "distributors": list_to_str(movie.get("distributors")),
        'release_date': date,
        'year': movie.get('year'),
        'genres': list_to_str(movie.get("genres")),
        'poster': movie.get('full-size cover url'),
        'plot': plot,
        'rating': str(movie.get("rating")),
        'url':f'https://www.imdb.com/title/tt{movieid}'
    }

# https://github.com/odysseusmax/animated-lamp/blob/2ef4730eb2b5f0596ed6d03e7b05243d93e3415b/bot/utils/broadcast.py#L37

async def broadcast_messages(user_id, message):
    """Broadcast message to user with error handling"""
    try:
        await message.copy(chat_id=user_id)
        return True, "Success"
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await broadcast_messages(user_id, message)
    except InputUserDeactivated:
        await db.delete_user(int(user_id))
        logging.info(f"{user_id}-Removed from Database, since deleted account.")
        return False, "Deleted"
    except UserIsBlocked:
        logging.info(f"{user_id} -Blocked the bot.")
        return False, "Blocked"
    except PeerIdInvalid:
        await db.delete_user(int(user_id))
        logging.info(f"{user_id} - PeerIdInvalid")
        return False, "Error"
    except Exception as e:
        return False, "Error"

def get_size(size):
    """Get size in readable format"""
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

def get_file_id(msg: Message):
    """Extract file ID from message"""
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            "sticker"
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

def extract_user(message: Message) -> Union[int, str]:
    """Extract user information from message"""
    # https://github.com/SpEcHiDe/PyroGramBot/blob/f30e2cca12002121bad1982f68cd0ff9814ce027/pyrobot/helper_functions/extract_user.py#L7
    user_id = None
    user_first_name = None
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        user_first_name = message.reply_to_message.from_user.first_name

    elif len(message.command) > 1:
        if (
            len(message.entities) > 1 and
            message.entities[1].type == enums.MessageEntityType.TEXT_MENTION
        ):
           
            required_entity = message.entities[1]
            user_id = required_entity.user.id
            user_first_name = required_entity.user.first_name
        else:
            user_id = message.command[1]
            # don't want to make a request -_-
            user_first_name = user_id
        try:
            user_id = int(user_id)
        except ValueError:
            pass
    else:
        user_id = message.from_user.id
        user_first_name = message.from_user.first_name
    return (user_id, user_first_name)

def list_to_str(k):
    """Convert list to string with proper formatting"""
    if not k:
        return "N/A"
    elif len(k) == 1:
        return str(k[0])
    elif MAX_LIST_ELM:
        k = k[:int(MAX_LIST_ELM)]
        return ' '.join(f'{elem}, ' for elem in k)
    else:
        return ' '.join(f'{elem}, ' for elem in k)

def last_online(from_user):
    """Get user's last online status"""
    time = ""
    if from_user.is_bot:
        time += "🤖 Bot :("
    elif from_user.status == enums.UserStatus.RECENTLY:
        time += "Recently"
    elif from_user.status == enums.UserStatus.LAST_WEEK:
        time += "Within the last week"
    elif from_user.status == enums.UserStatus.LAST_MONTH:
        time += "Within the last month"
    elif from_user.status == enums.UserStatus.LONG_AGO:
        time += "A long time ago :("
    elif from_user.status == enums.UserStatus.ONLINE:
        time += "Currently Online"
    elif from_user.status == enums.UserStatus.OFFLINE:
        time += from_user.last_online_date.strftime("%a, %d %b %Y, %H:%M:%S")
    return time

# ============== ADVANCED SUBTITLE UTILITY FUNCTIONS ==============

def create_movie_search_variants(title: str) -> List[str]:
    """Create multiple search variants for better subtitle matching"""
    variants = []
    
    # Original title
    variants.append(title)
    
    # Remove common words
    common_words = ['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from']
    words = title.split()
    filtered_words = [word for word in words if word.lower() not in common_words]
    if len(filtered_words) != len(words):
        variants.append(' '.join(filtered_words))
    
    # Replace special characters
    special_char_variants = title
    replacements = [
        (':', ''),
        ('-', ' '),
        ('_', ' '),
        ('&', 'and'),
        ('and', '&'),
        ('.', ' '),
        ("'", ''),
        ('"', ''),
        ('!', ''),
        ('?', ''),
        (',', ''),
        (';', ''),
        ('(', ''),
        (')', ''),
        ('[', ''),
        (']', ''),
        ('{', ''),
        ('}', '')
    ]
    
    for old, new in replacements:
        if old in title:
            variant = title.replace(old, new)
            variant = re.sub(r'\s+', ' ', variant).strip()
            if variant and variant not in variants:
                variants.append(variant)
    
    # Add variants with Roman numerals converted
    roman_numerals = {
        'II': '2', 'III': '3', 'IV': '4', 'V': '5', 'VI': '6', 
        'VII': '7', 'VIII': '8', 'IX': '9', 'X': '10'
    }
    
    for roman, arabic in roman_numerals.items():
        if roman in title:
            variants.append(title.replace(roman, arabic))
        if arabic in title:
            variants.append(title.replace(arabic, roman))
    
    # Remove duplicates while preserving order
    unique_variants = []
    for variant in variants:
        if variant and variant not in unique_variants:
            unique_variants.append(variant)
    
    return unique_variants

def calculate_subtitle_relevance_score(subtitle_info: Dict, movie_info: Dict) -> float:
    """Calculate relevance score for subtitle based on movie information"""
    score = 0.0
    
    # Base score for having subtitle
    score += 10.0
    
    # Download count factor (logarithmic scaling)
    download_count = subtitle_info.get('download_count', 0)
    if download_count > 0:
        import math
        score += min(20.0, math.log10(download_count + 1) * 5)
    
    # Release match scoring
    subtitle_release = subtitle_info.get('release', '').lower()
    movie_quality = movie_info.get('quality', '').lower()
    movie_source = movie_info.get('source', '').lower()
    
    if movie_quality and movie_quality in subtitle_release:
        score += 15.0
    
    if movie_source and movie_source in subtitle_release:
        score += 10.0
    
    # Year match
    if movie_info.get('year') and str(movie_info['year']) in subtitle_release:
        score += 5.0
    
    # Format preference (SRT is most compatible)
    subtitle_format = subtitle_info.get('format', '').lower()
    format_scores = {'srt': 10.0, 'vtt': 8.0, 'ass': 6.0, 'ssa': 5.0, 'sub': 4.0}
    score += format_scores.get(subtitle_format, 0.0)
    
    # Provider reliability
    provider = subtitle_info.get('provider', '').lower()
    provider_scores = {'opensubtitles': 10.0, 'subdb': 8.0, 'subscene': 7.0}
    score += provider_scores.get(provider, 5.0)
    
    return score

def normalize_movie_title_for_search(title: str) -> str:
    """Normalize movie title for more effective subtitle search"""
    # Convert to lowercase
    normalized = title.lower()
    
    # Remove articles from beginning
    normalized = re.sub(r'^(the|a|an)\s+', '', normalized)
    
    # Replace special characters with spaces
    normalized = re.sub(r'[^\w\s]', ' ', normalized)
    
    # Remove extra whitespace
    normalized = re.sub(r'\s+', ' ', normalized).strip()
    
    # Remove common movie keywords
    movie_keywords = [
        'movie', 'film', 'cinema', 'picture', 'flick',
        'remastered', 'extended', 'directors', 'cut',
        'unrated', 'theatrical', 'special', 'edition'
    ]
    
    words = normalized.split()
    filtered_words = [word for word in words if word not in movie_keywords]
    normalized = ' '.join(filtered_words)
    
    return normalized

def extract_quality_info_from_filename(filename: str) -> Dict[str, str]:
    """Extract detailed quality information from filename"""
    quality_info = {
        'resolution': None,
        'source': None,
        'codec': None,
        'audio': None,
        'hdr': None,
        'bit_depth': None
    }
    
    # Resolution detection
    resolution_patterns = [
        (r'\b(2160p|4K|UHD)\b', '2160p'),
        (r'\b(1080p|FullHD|FHD)\b', '1080p'),
        (r'\b(720p|HD)\b', '720p'),
        (r'\b(480p|SD)\b', '480p'),
        (r'\b(360p)\b', '360p'),
        (r'\b(240p)\b', '240p')
    ]
    
    for pattern, resolution in resolution_patterns:
        if re.search(pattern, filename, re.IGNORECASE):
            quality_info['resolution'] = resolution
            break
    
    # Source detection
    source_patterns = [
        (r'\b(BluRay|Blu-Ray|BRRip|BDRip)\b', 'BluRay'),
        (r'\b(WEB-DL|WebDL)\b', 'WEB-DL'),
        (r'\b(WebRip|Web-Rip|WEBRip)\b', 'WebRip'),
        (r'\b(DVDRip|DVD-Rip)\b', 'DVDRip'),
        (r'\b(HDRip|HD-Rip)\b', 'HDRip'),
        (r'\b(HDTV)\b', 'HDTV'),
        (r'\b(CAMRip|CAM|TS|TC)\b', 'CAM')
    ]
    
    for pattern, source in source_patterns:
        if re.search(pattern, filename, re.IGNORECASE):
            quality_info['source'] = source
            break
    
    # Codec detection
    codec_patterns = [
        (r'\b(x265|H\.265|HEVC)\b', 'HEVC'),
        (r'\b(x264|H\.264|AVC)\b', 'AVC'),
        (r'\b(AV1)\b', 'AV1'),
        (r'\b(XviD)\b', 'XviD'),
        (r'\b(DivX)\b', 'DivX')
    ]
    
    for pattern, codec in codec_patterns:
        if re.search(pattern, filename, re.IGNORECASE):
            quality_info['codec'] = codec
            break
    
    # Audio detection
    audio_patterns = [
        (r'\b(Atmos|DTS-X)\b', 'Atmos'),
        (r'\b(TrueHD)\b', 'TrueHD'),
        (r'\b(DTS-HD)\b', 'DTS-HD'),
        (r'\b(DTS)\b', 'DTS'),
        (r'\b(DD\+|EAC3)\b', 'DD+'),
        (r'\b(DD|AC3)\b', 'DD'),
        (r'\b(AAC)\b', 'AAC'),
        (r'\b(MP3)\b', 'MP3')
    ]
    
    for pattern, audio in audio_patterns:
        if re.search(pattern, filename, re.IGNORECASE):
            quality_info['audio'] = audio
            break
    
    # HDR detection
    hdr_patterns = [
        (r'\b(HDR10\+|HDR10Plus)\b', 'HDR10+'),
        (r'\b(HDR10)\b', 'HDR10'),
        (r'\b(DolbyVision|DoVi)\b', 'Dolby Vision'),
        (r'\b(HDR)\b', 'HDR')
    ]
    
    for pattern, hdr in hdr_patterns:
        if re.search(pattern, filename, re.IGNORECASE):
            quality_info['hdr'] = hdr
            break
    
    # Bit depth detection
    if re.search(r'\b10bit\b', filename, re.IGNORECASE):
        quality_info['bit_depth'] = '10bit'
    elif re.search(r'\b8bit\b', filename, re.IGNORECASE):
        quality_info['bit_depth'] = '8bit'
    
    return quality_info

def format_file_info_for_display(file_info: Dict) -> str:
    """Format file information for user-friendly display"""
    parts = []
    
    # Add file size
    if 'file_size' in file_info:
        size = get_size(file_info['file_size'])
        parts.append(f"📁 {size}")
    
    # Add quality info
    quality_info = extract_quality_info_from_filename(file_info.get('file_name', ''))
    
    if quality_info['resolution']:
        parts.append(f"🎬 {quality_info['resolution']}")
    
    if quality_info['source']:
        parts.append(f"📀 {quality_info['source']}")
    
    if quality_info['codec']:
        parts.append(f"🔧 {quality_info['codec']}")
    
    if quality_info['audio']:
        parts.append(f"🔊 {quality_info['audio']}")
    
    if quality_info['hdr']:
        parts.append(f"🌈 {quality_info['hdr']}")
    
    return " | ".join(parts) if parts else "📁 File"

def smart_title_match(search_title: str, file_title: str) -> float:
    """Smart matching algorithm for titles"""
    # Normalize both titles
    search_norm = normalize_movie_title_for_search(search_title)
    file_norm = normalize_movie_title_for_search(file_title)
    
    # Exact match
    if search_norm == file_norm:
        return 1.0
    
    # Word-based matching
    search_words = set(search_norm.split())
    file_words = set(file_norm.split())
    
    if not search_words or not file_words:
        return 0.0
    
    # Calculate Jaccard similarity
    intersection = search_words.intersection(file_words)
    union = search_words.union(file_words)
    jaccard = len(intersection) / len(union)
    
    # Boost score if all search words are found
    if search_words.issubset(file_words):
        jaccard += 0.2
    
    # Boost score for similar length
    length_diff = abs(len(search_norm) - len(file_norm))
    length_bonus = max(0, 0.1 - (length_diff * 0.01))
    
    return min(1.0, jaccard + length_bonus)

async def enhanced_movie_search_with_subtitle_info(query: str) -> Dict:
    """Enhanced movie search that includes subtitle availability"""
    from database.ia_filterdb import get_search_results
    
    try:
        # Get movie files
        files = await get_search_results(query)
        
        enhanced_results = []
        
        for file in files:
            file_info = {
                'file_data': file,
                'movie_info': extract_movie_info_from_filename(file.get('file_name', '')),
                'quality_info': extract_quality_info_from_filename(file.get('file_name', '')),
                'display_info': format_file_info_for_display(file),
                'subtitle_available': False,
                'subtitle_languages': []
            }
            
            # Check subtitle availability if enabled
            if ENABLE_SUBTITLES:
                try:
                    from database.subtitle_db import subtitle_db
                    if subtitle_db and subtitle_db._initialized:
                        movie_title = file_info['movie_info']['clean_title']
                        available_langs = await subtitle_db.get_available_languages(
                            file.get('_id', '')
                        )
                        
                        if available_langs:
                            file_info['subtitle_available'] = True
                            file_info['subtitle_languages'] = available_langs[:5]  # Limit to 5 languages
                
                except Exception as e:
                    logger.error(f"Error checking subtitle availability: {e}")
            
            enhanced_results.append(file_info)
        
        return {
            'query': query,
            'total_results': len(enhanced_results),
            'files': enhanced_results,
            'subtitle_enabled': ENABLE_SUBTITLES
        }
        
    except Exception as e:
        logger.error(f"Error in enhanced movie search: {e}")
        # Fallback to basic search
        files = await get_search_results(query)
        return {
            'query': query,
            'total_results': len(files),
            'files': [{'file_data': f, 'subtitle_available': False} for f in files],
            'subtitle_enabled': False
        }

def create_subtitle_download_url(movie_id: str, language: str, quality: str = None) -> str:
    """Create a download URL for subtitle (for future use with web interface)"""
    base_url = "https://your-bot-domain.com/subtitle"  # Replace with actual domain
    params = [f"movie_id={movie_id}", f"lang={language}"]
    
    if quality:
        params.append(f"quality={quality}")
    
    return f"{base_url}?{'&'.join(params)}"

def validate_movie_year(year_str: str) -> bool:
    """Validate if year string is a valid movie year"""
    try:
        year = int(year_str)
        current_year = datetime.now().year
        return 1888 <= year <= current_year + 2  # First motion picture to 2 years in future
    except ValueError:
        return False

def extract_episode_info(filename: str) -> Dict[str, any]:
    """Extract detailed episode information from filename"""
    episode_info = {
        'is_episode': False,
        'season': None,
        'episode': None,
        'episode_title': None,
        'series_title': None,
        'total_episodes': None,
        'episode_range': None
    }
    
    # Standard patterns
    patterns = [
        # S01E01 or S1E1 format
        r'[Ss](\d{1,3})[Ee](\d{1,3})(?:-[Ee](\d{1,3}))?',
        # 1x01 format  
        r'(\d{1,2})x(\d{1,3})(?:-(\d{1,3}))?',
        # Season 1 Episode 1 format
        r'Season[\s\.](\d{1,2})[\s\.]Episode[\s\.](\d{1,3})',
        # Episode 1 format
        r'Episode[\s\.](\d{1,3})',
        # Ep 1 format
        r'Ep[\s\.](\d{1,3})',
        # Part 1 format
        r'Part[\s\.](\d{1,3})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            episode_info['is_episode'] = True
            groups = match.groups()
            
            if len(groups) >= 2 and groups[0] and groups[1]:
                episode_info['season'] = int(groups[0])
                episode_info['episode'] = int(groups[1])
                if len(groups) > 2 and groups[2]:
                    episode_info['episode_range'] = (int(groups[1]), int(groups[2]))
            elif len(groups) == 1 and groups[0]:
                episode_info['episode'] = int(groups[0])
            
            break
    
    # Extract series title (everything before season/episode info)
    if episode_info['is_episode']:
        # Find the position of season/episode pattern
        for pattern in patterns:
            match = re.search(pattern, filename, re.IGNORECASE)
            if match:
                series_part = filename[:match.start()].strip()
                # Clean up the series title
                series_part = re.sub(r'[._\-\+]', ' ', series_part)
                series_part = re.sub(r'\s+', ' ', series_part).strip()
                episode_info['series_title'] = series_part
                break
    
    return episode_info

# Helper function for debugging
def debug_movie_info_extraction(filename: str) -> str:
    """Debug function to show extracted movie information"""
    info = extract_movie_info_from_filename(filename)
    quality = extract_quality_info_from_filename(filename)
    episode = extract_episode_info(filename)
    
    debug_info = f"""
🔍 **Debug Info for:** `{filename}`

**🎬 Movie Info:**
• Clean Title: {info['clean_title']}
• Year: {info['year']}
• Quality: {info['quality']}
• Source: {info['source']}
• Codec: {info['codec']}
• Audio: {info['audio']}
• Languages: {', '.join(info['language_indicators']) if info['language_indicators'] else 'None'}
• Release Group: {info['release_group']}

**📺 Episode Info:**
• Is Series: {episode['is_episode']}
• Season: {episode['season']}
• Episode: {episode['episode']}
• Series Title: {episode['series_title']}

**🎥 Quality Details:**
• Resolution: {quality['resolution']}
• Source: {quality['source']}
• Codec: {quality['codec']}
• Audio: {quality['audio']}
• HDR: {quality['hdr']}
• Bit Depth: {quality['bit_depth']}
"""
    
    return debug_info