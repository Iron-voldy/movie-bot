import os
import logging
import random
import asyncio
from Script import script
from hydrogram import Client, filters, enums
from hydrogram.errors import ChatAdminRequired, FloodWait
from hydrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import get_file_details, unpack_new_file_id, get_delete_results
from database.users_chats_db import db
from info import CHANNELS, ADMINS, AUTH_CHANNEL, LOG_CHANNEL, NON_AUTH_GROUPS, PICS, BATCH_FILE_CAPTION, CUSTOM_FILE_CAPTION, PROTECT_CONTENT
from utils import get_size, is_subscribed, temp, delete_messages
import re
import json
import base64
logger = logging.getLogger(__name__)
from os import environ
import time, psutil


@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        buttons = [
            [
                InlineKeyboardButton('Uᴘᴅᴀᴛᴇѕ', url='https://t.me/SECL4U')
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(script.START_TXT.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
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
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return
    btn = []
    for channel in temp.AUTH_CHANNEL:
        if not await is_subscribed(client, message, channel):
            invite_link = await client.create_chat_invite_link(channel, creates_join_request=True)
            chat = await client.get_chat(channel)
            btn.append(
                [InlineKeyboardButton(f"✇ Jᴏɪɴ {chat.title} ✇", url=invite_link.invite_link)]
            )

    if btn and message.command[1] != "subscribe":
        btn.append([InlineKeyboardButton(" 🔄 Try Again", url=f"https://t.me/{temp.U_NAME}?start={message.command[1]}")])
    if btn:
        await client.send_message(
            chat_id=message.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode=enums.ParseMode.MARKDOWN
        )
        return
    if len(message.command) == 2 and message.command[1] in ["subscribe", "error", "okay", "help"]:
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
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return
    
    file_id = message.command[1]
    files_ = await get_file_details(file_id)           
    if not files_:
        return await message.reply('No such file exist.')
    files = files_
    title = files['file_name']
    size=get_size(files['file_size'])
    f_caption=""
    if CUSTOM_FILE_CAPTION:
        try:
            f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
        except Exception as e:
            logger.exception(e)
            f_caption=f_caption
    if f_caption is None:
        f_caption = f"{files['file_name']}"
    m=await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption
        )
    asyncio.create_task(delete_messages(300, [m]))
                    

@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
           
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)



@Client.on_message(filters.command('setchannel') & filters.user(ADMINS))
async def save_channel(client, message):
    try:
        _ids = message.text.split(" ", 1)[1]
    except:
        return await message.reply("No Input!!")
    txt = 'Saved Channels:\n'
    try:
        ids = _ids.split()
        for id in ids:
            chat = await client.get_chat(int(id))
            txt += '\n' + chat.title
    except Exception as e:
        return await message.reply(f"Error: {e}")

    temp.AUTH_CHANNEL = list(map(int, _ids.split()))
    stg = {'AUTH_CHANNEL': _ids}
    await db.update_sttg(stg)
    await message.reply(txt)
    

@Client.on_message(filters.command('getchannel') & filters.user(ADMINS))
async def get_channel(client, message):
    ids = temp.AUTH_CHANNEL
    txt = 'Channels:\n'
    try:
        for id in ids:
            chat = await client.get_chat(int(id))
            txt += '\n' + chat.title
        await message.reply(txt)
    except Exception as e:
        await message.reply(f"Error: {e}")


@Client.on_message(filters.command("delete_files") & filters.user(ADMINS))
async def delete_files(bot, message):
    try:
        keyword = message.text.split(" ", 1)[1]
    except:
        return await message.reply_text("No Input!!")
    files, total_results = await get_delete_results(keyword)
    btn = [[
        InlineKeyboardButton('YES', callback_data=f'del_files#{keyword}')
    ],[
        InlineKeyboardButton('NO', callback_data='close_data')
    ]]
    await message.reply(f'Total {total_results} files found, Do you want to delete?', reply_markup=InlineKeyboardMarkup(btn))
    
    
@Client.on_message(filters.command('ping'))
async def ping(client, message):
    start_time = time.monotonic()
    msg = await message.reply("👀")
    end_time = time.monotonic()
    await msg.edit(f'{round((end_time - start_time) * 1000)} ms')
