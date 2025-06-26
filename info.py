import re
from Script import script
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information 
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID','3135143'))
API_HASH = environ.get('API_HASH','24f97a7491f6fc888eeff31694c061bf')
BOT_TOKEN = environ.get('BOT_TOKEN','8064076565:AAHD9rkZh2AsoHiNthaho2mz2H78mb0Bu44')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://i.postimg.cc/8C15CQ5y/1.png https://i.postimg.cc/gcNtrv0m/2.png https://i.postimg.cc/cHD71BBz/3.png https://i.postimg.cc/F1XYhY8q/4.png https://i.postimg.cc/1tNwGVxC/5.png https://i.postimg.cc/dtW30QpL/6.png https://i.postimg.cc/139dvs3c/7.png https://i.postimg.cc/QtXVtB8K/8.png https://i.postimg.cc/y8j8G1XV/9.png https://i.postimg.cc/zDF6KyJX/10.png https://i.postimg.cc/fyycVqzd/11.png https://i.postimg.cc/26ZBtBZr/13.png https://i.postimg.cc/PJn8nrWZ/14.png https://i.postimg.cc/cC7txyhz/15.png https://i.postimg.cc/kX9tjGXP/16.png https://i.postimg.cc/zXjH4NVb/17.png https://i.postimg.cc/sggGrLhn/18.png https://i.postimg.cc/y8pgYTh7/19.png')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7374454591 1573108290 1234523543').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002080383910 -1001396095544 -1001620200646 -1001732737927 -1001551816705 -1001690448036 -1001622478032 -1001566642237 -1001705433155 -1001584832671 -1001519694012 -1001565676692 -1001586913070 -1001784709266 -1001793950262 -1001645647150 -1001509224438 -1001537303459 -1001797222352 -1001634044892 -1001588529187 -1001661067577 -1001566642237 -1001280303317 -1001594099259 -1001210825788 -1002454612042 -1002266146125').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('AUTH_CHANNEL', '').split()]
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
NON_AUTH_GROUPS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('NON_AUTH_GROUPS', '').split()]

# MongoDB information
DATABASE_NAME = environ.get('DATABASE_NAME', "sahan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://sahan:sahan@cluster0.dkyoun5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
FILES_DB_URL = environ.get('FILES_DB_URL', "mongodb+srv://sahan:sahan@cluster0.lgnnw8u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
SECONDARY_DB_URL = 'mongodb+srv://sahan:sahan@cluster0.ccqwaah.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

# Subtitle Database (NEW - Separate database for subtitles)
SUBTITLE_DB_NAME = environ.get('SUBTITLE_DB_NAME', "subtitle_db")
SUBTITLE_DB_URI = environ.get('SUBTITLE_DB_URI', "mongodb+srv://sahan:sahan@cluster0.subtitle.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Redis Cache (NEW)
REDIS_URL = environ.get('REDIS_URL', 'redis://localhost:6379')

# Subtitle API Configuration (NEW)
OPENSUBTITLES_API_KEY = environ.get('OPENSUBTITLES_API_KEY', 'Z7wZXFOP8Nty4UrefAdCoidFVPvTBnTy')
OPENSUBTITLES_USERNAME = environ.get('OPENSUBTITLES_USERNAME', '')
OPENSUBTITLES_PASSWORD = environ.get('OPENSUBTITLES_PASSWORD', '')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002281952451'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'TeamEvamaria')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", script.FILE_CAPTION)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), True)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Subtitle Settings (NEW)
ENABLE_SUBTITLES = is_enabled((environ.get('ENABLE_SUBTITLES', "True")), True)
DEFAULT_SUBTITLE_LANGUAGE = environ.get('DEFAULT_SUBTITLE_LANGUAGE', 'en')
MAX_SUBTITLE_FILE_SIZE = int(environ.get('MAX_SUBTITLE_FILE_SIZE', 5242880))  # 5MB