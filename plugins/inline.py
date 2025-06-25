import logging
from hydrogram import Client, filters
from hydrogram.errors.exceptions.bad_request_400 import QueryIdInvalid
from hydrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultCachedDocument, InlineQuery
from database.ia_filterdb import get_search_results
from utils import is_subscribed, get_size, temp
from info import CACHE_TIME, AUTH_USERS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION
from plugins.pm_filter import next_back

logger = logging.getLogger(__name__)
cache_time = 0 if AUTH_USERS or AUTH_CHANNEL else CACHE_TIME

@Client.on_inline_query()
async def answer(bot, query):
    """Show search results for given inline query"""
    for channel in temp.AUTH_CHANNEL:
        if not await is_subscribed(bot, query, channel):
            await query.answer(results=[],
                               cache_time=0,
                               switch_pm_text='You have to subscribe my channel to use the bot',
                               switch_pm_parameter="subscribe")
            return

    results = []
    if '|' in query.query:
        string, file_type = query.query.split('|', maxsplit=1)
        string = string.strip()
        file_type = file_type.strip().lower()
    else:
        string = query.query.strip()
        file_type = None

    offset = int(query.offset or 0)
    reply_markup = get_reply_markup(query=string)
    all_total = await get_search_results(string)
    files, next_offset, total = await next_back(all_total, max_results=10, offset=offset)

    for file in files:
        title=file['file_name']
        size=get_size(file['file_size'])
        f_caption=""
        if CUSTOM_FILE_CAPTION:
            try:
                f_caption=CUSTOM_FILE_CAPTION.format(file_name= '' if title is None else title, file_size='' if size is None else size, file_caption='' if f_caption is None else f_caption)
            except Exception as e:
                logger.exception(e)
                f_caption=f_caption
        if f_caption is None:
            f_caption = f"{file['file_name']}"
        results.append(
            InlineQueryResultCachedDocument(
                title=file['file_name'],
                document_file_id=file['_id'],
                caption=f_caption,
                description =f'Size:{get_size(file["file_size"])}',
                reply_markup=reply_markup))

    if results:
        switch_pm_text = f"Results - {total}"
        if string:
            switch_pm_text += f" for {string}"
        try:
            await query.answer(results=results,
                           is_personal = True,
                           cache_time=cache_time,
                           switch_pm_text=switch_pm_text,
                           switch_pm_parameter="start",
                           next_offset=str(next_offset))
        except QueryIdInvalid:
            pass
        except Exception as e:
            logging.exception(str(e))
    else:
        switch_pm_text = f'No results'
        if string:
            switch_pm_text += f' for "{string}"'

        await query.answer(results=[],
                           is_personal = True,
                           cache_time=cache_time,
                           switch_pm_text=switch_pm_text,
                           switch_pm_parameter="okay")


def get_reply_markup(query):
    buttons = [
        [
            InlineKeyboardButton('Search again', switch_inline_query_current_chat=query)
        ]
        ]
    return InlineKeyboardMarkup(buttons)




