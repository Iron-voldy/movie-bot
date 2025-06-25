# Kanged From @TroJanZheX
import asyncio
import re
import ast
import math
from hydrogram.errors.exceptions.bad_request_400 import MediaEmpty, PhotoInvalidDimensions, WebpageMediaEmpty
from Script import script
import hydrogram
from info import ADMINS, P_TTI_SHOW_OFF, AUTH_CHANNEL, NON_AUTH_GROUPS, AUTH_USERS, CUSTOM_FILE_CAPTION, AUTH_GROUPS, P_TTI_SHOW_OFF, IMDB, \
    SINGLE_BUTTON, SPELL_CHECK_REPLY, IMDB_TEMPLATE, LOG_CHANNEL, PICS
from hydrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from hydrogram import Client, filters, enums
from hydrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from utils import format_size, remove_username_from_filename, get_size, is_subscribed, get_poster, temp, delete_messages
from database.users_chats_db import db
from database.ia_filterdb import delete_func, get_database_count, get_file_details, get_search_results, get_delete_results, get_database_size
import logging, random, psutil

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

BUTTONS = {}
SPELL_CHECK = {}
ORIGINAL_FILES = {}
SELECTIONS = {}
FILES = {}
RESOLUTIONS = ['480p', '540p', '720p', '1080p', '2160p']
LANGUAGES = ['english', 'tamil', 'hindi', 'malayalam', 'telugu', 'korean']



async def next_back(data, offset=0, max_results=0):
    out_data = data[offset:][:max_results]
    total_results = len(data)
    next_offset = offset + max_results
    if next_offset >= total_results:
        next_offset = ''
    return out_data, next_offset, total_results


@Client.on_message((filters.group | filters.private) & filters.text & filters.incoming)
async def give_filter(client, message):
    await auto_filter(client, message)
        

@Client.on_message(filters.private & filters.text & filters.incoming)
async def pm_text(bot, message):
    content = message.text
    user = message.from_user.first_name
    user_id = message.from_user.id
    if content.startswith("/") or content.startswith("#"): return  # ignore commands and hashtags
    if user_id in ADMINS: return # ignore admins
    await bot.send_message(
        chat_id=LOG_CHANNEL,
        text=f"#PM_Message\nUser: {user} ({user_id})\nMessage: {content}"
    )        

@Client.on_callback_query(filters.regex(r"^next"))
async def next_page(bot, query, cd=None):
    if cd:
        req, key, offset = cd
    else:
        ident, req, key, offset = query.data.split("_")

    if int(req) not in [query.from_user.id, 0]:
        return await query.answer("not for you", show_alert=True)
    try:
        offset = int(offset)
    except:
        offset = 0
    search = BUTTONS.get(key)
    if not search:
        await query.answer("You are using one of my old messages, please send the request again.", show_alert=True)
        return
    
    selections = SELECTIONS.get(key)
    files, n_offset, total = await next_back(FILES.get(key), max_results=10, offset=offset)

    try:
        n_offset = int(n_offset)
    except:
        n_offset = 0

    if not files:
        return
    
    btn = [[
        InlineKeyboardButton(
            text=f"{format_size(get_size(file['file_size']))} - {remove_username_from_filename(file['file_name'])}",
            callback_data=f'files#{file["_id"]}'),
        ] 
           for file in files
        ]


    if 0 < offset <= 10:
        off_set = 0
    elif offset == 0:
        off_set = None
    else:
        off_set = offset - 10

    btn.insert(0,
        [InlineKeyboardButton("🗣 ʟᴀɴɢᴜᴀɢᴇ" if selections.get('language') == 'any' else selections.get('language').title(), callback_data=f"language#{req}#{key}"),
         InlineKeyboardButton("▶️ ʀᴇꜱᴏʟᴜᴛɪᴏɴ" if selections.get('resolution') == 'any' else selections.get('resolution'), callback_data=f"resolution#{req}#{key}")]
    )
    btn.insert(1,
        [InlineKeyboardButton({"any": "🎦 ᴄᴀᴛᴇɢᴏʀʏ", "movie": "Movie", "series": "TV Series"}[selections.get('category')], callback_data=f"category#{req}#{key}")])


    if total <= 10:
        btn.append(
            [InlineKeyboardButton(text="𝙽𝙾 𝙼𝙾𝚁𝙴 𝙿𝙰𝙶𝙴𝚂 𝙰𝚅𝙰𝙸𝙻𝙰𝙱𝙻𝙴", callback_data="pages")]
        )
    elif n_offset == 0:
        btn.append(
            [InlineKeyboardButton("⏪ BACK", callback_data=f"next_{req}_{key}_{off_set}"),
             InlineKeyboardButton(f"📃 Pages {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}",
                                  callback_data="pages")]
        )
    elif off_set is None:
        btn.append(
            [InlineKeyboardButton(f"🗓 {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}", callback_data="pages"),
             InlineKeyboardButton("NEXT ⏩", callback_data=f"next_{req}_{key}_{n_offset}")])
    else:
        btn.append(
            [
                InlineKeyboardButton("⏪ BACK", callback_data=f"next_{req}_{key}_{off_set}"),
                InlineKeyboardButton(f"🗓 {math.ceil(int(offset) / 10) + 1} / {math.ceil(total / 10)}", callback_data="pages"),
                InlineKeyboardButton("NEXT ⏩", callback_data=f"next_{req}_{key}_{n_offset}")
            ],
        )

    try:
        await query.message.edit(f"""<b>"{search}"</b><b> ιѕ ɴow reαdy ғor yoυ!</b> ✨\n\n<b>Cнooѕe yoυr preғerred opтιoɴѕ вelow тo ғιɴd тнe вeѕт мαтcн ғor yoυr ɴeedѕ</b> 🔻\n\n🗣 ʟᴀɴ... | ▶️ ʀᴇꜱ... | 🎦 ᴄᴀᴛ...""", reply_markup=InlineKeyboardMarkup(btn))
    except MessageNotModified:
        pass




@Client.on_callback_query(filters.regex(r"^language"))
async def language(bot, query):
    ident, req, key = query.data.split("#")
    if int(req) != query.from_user.id:
        return await query.answer("not for you", show_alert=True)

    search = BUTTONS.get(key)
    selections = SELECTIONS.get(key)
    if not search:
        await query.answer("request again", show_alert=True)
        return
    btn = [[
        InlineKeyboardButton(text=f"» {lang.title()} «" if selections.get('language') == lang else lang.title(), callback_data=f"lang_select#{req}#{key}#{lang}")
    ]
        for lang in LANGUAGES
    ]
    btn.append(
        [InlineKeyboardButton("» Any Language «" if selections.get('language') == "any" else "Any Language", callback_data=f"lang_select#{req}#{key}#any")]
    )
    await query.message.edit(f'Select you want <b>" {search} "</b> language.', reply_markup=InlineKeyboardMarkup(btn))


@Client.on_callback_query(filters.regex(r"^lang_select"))
async def lang_select(bot, query):
    ident, req, key, lang = query.data.split("#")
    if int(req) != query.from_user.id:
        return await query.answer("not for you", show_alert=True)

    original_files = ORIGINAL_FILES.get(key)
    if not original_files:
        await query.answer("request again", show_alert=True)
        return
    
    files = original_files  # Filtered files will be original files
    if lang != 'any' and not any([file for file in files if lang in file['file_name'].lower()]):
        return await query.answer('results not found for this language', show_alert=True)
    SELECTIONS[key]['language'] = lang
    selections = SELECTIONS.get(key)
    filtered_files = [
        file for file in files
        if (selections.get('language') == 'any' or selections.get('language') in file['file_name'].lower()) and
           (selections.get('resolution') == 'any' or selections.get('resolution') in file['file_name'].lower()) and
           (selections.get('category') == 'any' or
            (selections.get('category') == 'series' and re.search(r's\d{1,2}e\d{1,2}', file['file_name'].lower())) or
            (selections.get('category') == 'movie' and not re.search(r's\d{1,2}e\d{1,2}', file['file_name'].lower())))
    ]
    if not filtered_files:
        return await query.answer('results not found with the currently selected filters', show_alert=True)
    FILES[key] = filtered_files

    cd = (req, key, 0)
    await next_page(bot, query, cd=cd)
    

@Client.on_callback_query(filters.regex(r"^resolution"))
async def resolution(bot, query):
    ident, req, key = query.data.split("#")
    if int(req) != query.from_user.id:
        return await query.answer("not for you", show_alert=True)

    search = BUTTONS.get(key)
    selections = SELECTIONS.get(key)
    if not search:
        await query.answer("request again", show_alert=True)
        return
    btn = [[
        InlineKeyboardButton(text=f"» {resltn} «" if selections.get('resolution') == resltn else resltn, callback_data=f"resltn_select#{req}#{key}#{resltn}")
    ]
        for resltn in RESOLUTIONS
    ]
    btn.append(
        [InlineKeyboardButton("» Any Resolution «" if selections.get('resolution') == "any" else "Any Resolution", callback_data=f"resltn_select#{req}#{key}#any")]
    )
    await query.message.edit(f'Select you want <b>" {search} "</b> resolution.', reply_markup=InlineKeyboardMarkup(btn))


@Client.on_callback_query(filters.regex(r"^resltn_select"))
async def resltn_select(bot, query):
    ident, req, key, resltn = query.data.split("#")
    if int(req) != query.from_user.id:
        return await query.answer("not for you", show_alert=True)

    search = BUTTONS.get(key)
    original_files = ORIGINAL_FILES.get(key)
    if not search:
        await query.answer("request again", show_alert=True)
        return
    
    files = original_files  # Filtered files will be original files
    if resltn != 'any' and not any([file for file in files if resltn in file['file_name'].lower()]):
        return await query.answer('results not found for this resolution', show_alert=True)
    SELECTIONS[key]['resolution'] = resltn
    selections = SELECTIONS.get(key)
    filtered_files = [
        file for file in files
        if (selections.get('language') == 'any' or selections.get('language') in file['file_name'].lower()) and
           (selections.get('resolution') == 'any' or selections.get('resolution') in file['file_name'].lower()) and
           (selections.get('category') == 'any' or
            (selections.get('category') == 'series' and re.search(r's\d{1,2}e\d{1,2}', file['file_name'].lower())) or
            (selections.get('category') == 'movie' and not re.search(r's\d{1,2}e\d{1,2}', file['file_name'].lower())))
    ]
    if not filtered_files:
        return await query.answer('results not found with the currently selected filters', show_alert=True)
    FILES[key] = filtered_files

    cd = (req, key, 0)
    await next_page(bot, query, cd=cd)
    

@Client.on_callback_query(filters.regex(r"^category"))
async def category(bot, query):
    ident, req, key = query.data.split("#")
    if int(req) != query.from_user.id:
        return await query.answer("not for you", show_alert=True)

    search = BUTTONS.get(key)
    selections = SELECTIONS.get(key)
    if not search:
        await query.answer("request again", show_alert=True)
        return
    btn = [[
        InlineKeyboardButton(text="» Movie «" if selections.get('category') == 'movie' else 'Movie', callback_data=f"catgry_select#{req}#{key}#movie")
    ],[
        InlineKeyboardButton(text="» TV Series «" if selections.get('category') == 'series' else 'TV Series', callback_data=f"catgry_select#{req}#{key}#series")
    ],[
        InlineKeyboardButton(text="» Any Category «" if selections.get('category') == 'any' else 'Any Category', callback_data=f"catgry_select#{req}#{key}#any")
    ]]
    await query.message.edit(f'Select you want <b>" {search} "</b> category.', reply_markup=InlineKeyboardMarkup(btn))

@Client.on_callback_query(filters.regex(r"^catgry_select"))
async def catgry_select(bot, query):
    ident, req, key, catgry = query.data.split("#")
    if int(req) != query.from_user.id:
        return await query.answer("not for you", show_alert=True)

    search = BUTTONS.get(key)
    original_files = ORIGINAL_FILES.get(key)
    if not search:
        await query.answer("request again", show_alert=True)
        return
    
    files = original_files  # Filtered files will be original files
    if catgry != 'any' and not any(
        (catgry == 'series' and re.search(r's\d{1,2}e\d{1,2}', file['file_name'].lower())) or
        (catgry == 'movie' and not re.search(r's\d{1,2}e\d{1,2}', file['file_name'].lower()))
        for file in files):
        return await query.answer('results not found for this category', show_alert=True)
    SELECTIONS[key]['category'] = catgry
    selections = SELECTIONS.get(key)
    filtered_files = [
        file for file in files
        if (selections.get('language') == 'any' or selections.get('language') in file['file_name'].lower()) and
           (selections.get('resolution') == 'any' or selections.get('resolution') in file['file_name'].lower()) and
           (selections.get('category') == 'any' or
            (selections.get('category') == 'series' and re.search(r's\d{1,2}e\d{1,2}', file['file_name'].lower())) or
            (selections.get('category') == 'movie' and not re.search(r's\d{1,2}e\d{1,2}', file['file_name'].lower())))
    ]
    if not filtered_files:
        return await query.answer('results not found with the currently selected filters', show_alert=True)
    FILES[key] = filtered_files

    cd = (req, key, 0)
    await next_page(bot, query, cd=cd)
    

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "close_data":
        await query.message.delete()

    elif query.data.startswith("file"):
        ident, file_id = query.data.split("#")
        await query.answer(url=f"https://t.me/{temp.U_NAME}?start={file_id}")

    elif query.data == "reqinfo":
        await query.answer(text=script.REQINFO, show_alert=True)
    elif query.data == "sinfo":
        await query.answer(text=script.SINFO, show_alert=True)
    elif query.data == "minfo":
        await query.answer(text=script.MINFO, show_alert=True)
    elif query.data == "pages":
        await query.answer()

    elif query.data == "start":
        buttons = [[
                    InlineKeyboardButton('➕ Add Me To Your Group ➕', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
                ],[
                    InlineKeyboardButton('🧩 Updates', url='https://t.me/SECL4U'),
                    InlineKeyboardButton('📚 How To Use', url='https://t.me/SECOfficial_Bot')
                ],[
                    InlineKeyboardButton('🛠 Help', callback_data='help'),
                    InlineKeyboardButton('📞 Contact', callback_data='about')
                ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer('Piracy Is Crime')
    elif query.data == "help":
        buttons = [[
            InlineKeyboardButton('Aυтo Fιlтer', callback_data='autofilter'),
            InlineKeyboardButton('Eхтrα Modѕ', callback_data='extra')
        ], [
            InlineKeyboardButton('🏠 Hoмe', callback_data='start'),
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "about":
        buttons = [[
            InlineKeyboardButton('Owner', url='https://t.me/ImSahanSBot'),
            InlineKeyboardButton('Developer', url='https://t.me/Hansaka_Anuhas')
        ], [
            InlineKeyboardButton('🏠 Hoмe', callback_data='start'),
            InlineKeyboardButton('📊 Sтαтυѕ', callback_data='stats')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ABOUT_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "source":
        buttons = [[
            InlineKeyboardButton('🔙 Bαcĸ', callback_data='about')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.SOURCE_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "manuelfilter":
        buttons = [[
            InlineKeyboardButton('🔙 Bαcĸ', callback_data='help'),
            InlineKeyboardButton('Bυттoɴѕ', callback_data='button')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.MANUELFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "button":
        buttons = [[
            InlineKeyboardButton('🔙 Bαcĸ', callback_data='manuelfilter')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.BUTTON_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "autofilter":
        buttons = [[
            InlineKeyboardButton('🔙 Bαcĸ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.AUTOFILTER_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "coct":
        buttons = [[
            InlineKeyboardButton('🔙 Bαcĸ', callback_data='help')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.CONNECTION_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "extra":
        buttons = [[
            InlineKeyboardButton('🔙 Bαcĸ', callback_data='help'),
            InlineKeyboardButton('Adмιɴ', callback_data='admin')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.EXTRAMOD_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "admin":
        buttons = [[
            InlineKeyboardButton('🔙 Bαcĸ', callback_data='extra')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=script.ADMIN_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "stats":
        await query.message.edit_text('Loading...')
        buttons = [[
            InlineKeyboardButton('🔙 Bαcĸ', callback_data='about'),
            InlineKeyboardButton('🔄 ReFreѕн', callback_data='stats')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        primary_count, secondary_count= get_database_count()
        users = await db.total_users_count()
        chats = await db.total_chat_count()
        db_size = get_size(await db.get_db_size())
        primary_size, secondary_size = get_database_size()
        await query.message.edit_text(
            text=script.STATUS_TXT.format(primary_count, get_size(primary_size), secondary_count, get_size(secondary_size), users, chats, db_size, get_size(psutil.virtual_memory().total), get_size(psutil.virtual_memory().used)),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )

    elif query.data == "owner_info":
            buttons = [[
                    InlineKeyboardButton('🔙 Bαcĸ', callback_data="start"),
                    InlineKeyboardButton('📞 Coɴтαcт', url="t.me/ImSahanSBot")
                  ]]
            reply_markup = InlineKeyboardMarkup(buttons)
            await query.message.edit_text(
                text=script.OWNER_INFO,
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
                                         
    elif query.data.startswith("del_files"):
        ident, keyword = query.data.split("#")
        await query.message.edit('Deleting...')
        deleted = 0
        files, total_results = await get_delete_results(keyword)
        for file in files:
            await delete_func(file)
            deleted += 1
        await query.message.edit(f'Deleted files: {deleted}')
        
    await query.answer('🔄')


async def auto_filter(client, msg, spoll=False):
    message = msg
    if message.text.startswith("/"): return  # ignore commands

    search = re.sub(r"(_|\-|\.|\+)", " ", message.text.strip())
    all_files = await get_search_results(search)
    if not all_files:
        btn = [[
                InlineKeyboardButton("🔍 Search Google", url=f"https://www.google.com/search?q={search.replace(' ', '+')}")
        ]]
        v = await msg.reply('I cant find this in my database', reply_markup=InlineKeyboardMarkup(btn))
        asyncio.create_task(delete_messages(120, [v]))
        return
    

    files, offset, total_results = await next_back(all_files, max_results=10)

    btn = [[
        InlineKeyboardButton(
            text=f"{format_size(get_size(file['file_size']))} - {remove_username_from_filename(file['file_name'])}",
            callback_data=f'files#{file["_id"]}'),
        ] 
           for file in files
        ]


    key = f"{message.chat.id}-{message.id}"
    BUTTONS[key] = search
    req = message.from_user.id if message.from_user else 0
    ORIGINAL_FILES[key] = all_files
    FILES[key] = all_files
    SELECTIONS[key] = {'language': 'any', 'resolution': 'any', 'category': 'any'}
    

    if offset != "":
        btn.append(
            [InlineKeyboardButton(text=f"🗓 1/{math.ceil(int(total_results) / 10)}", callback_data="pages"),
             InlineKeyboardButton(text="NEXT ⏩", callback_data=f"next_{req}_{key}_{offset}")]
        )
    else:
         btn.append(
             [InlineKeyboardButton(text="𝙽𝙾 𝙼𝙾𝚁𝙴 𝙿𝙰𝙶𝙴𝚂 𝙰𝚅𝙰𝙸𝙻𝙰𝙱𝙻𝙴", callback_data="pages")]
         )
    
    btn.insert(0,
        [InlineKeyboardButton('🗣 ʟᴀɴɢᴜᴀɢᴇ', callback_data=f"language#{req}#{key}"),
         InlineKeyboardButton('▶️ ʀᴇꜱᴏʟᴜᴛɪᴏɴ', callback_data=f"resolution#{req}#{key}")]
        )
    
    btn.insert(1,
        [InlineKeyboardButton('🎦 ᴄᴀᴛᴇɢᴏʀʏ', callback_data=f"category#{req}#{key}")])


    cap = f"""<b>"{search}"</b><b> ιѕ ɴow reαdy ғor yoυ!</b> ✨\n\n<b>Cнooѕe yoυr preғerred opтιoɴѕ вelow тo ғιɴd тнe вeѕт мαтcн ғor yoυr ɴeedѕ</b> 🔻\n\n🗣 ʟᴀɴ... | ▶️ ʀᴇꜱ... | 🎦 ᴄᴀᴛ..."""
    m=await message.reply_photo(photo=random.choice(PICS), caption=cap, reply_markup=InlineKeyboardMarkup(btn))
    asyncio.create_task(delete_messages(300, [m]))
