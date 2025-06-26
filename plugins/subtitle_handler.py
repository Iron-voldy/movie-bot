import logging
import asyncio
from io import BytesIO
from hydrogram import Client, filters
from hydrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from hydrogram.errors import MessageNotModified
from config.subtitle_config import SUPPORTED_LANGUAGES, PRIORITY_LANGUAGES, UI_CONFIG
from database.subtitle_db import subtitle_db
from info import ENABLE_SUBTITLES
from Script import script
from utils import temp

logger = logging.getLogger(__name__)

class SubtitleKeyboardBuilder:
    """Build inline keyboards for subtitle selection"""
    
    @staticmethod
    def create_language_selection(movie_id: str, available_languages: list, 
                                request_id: int, page: int = 0):
        """Create language selection keyboard"""
        languages_per_page = UI_CONFIG['max_languages_per_page']
        languages_per_row = UI_CONFIG['languages_per_row']
        
        # Sort languages with priority ones first
        priority_langs = [lang for lang in PRIORITY_LANGUAGES if lang in available_languages]
        other_langs = [lang for lang in available_languages if lang not in PRIORITY_LANGUAGES]
        sorted_languages = priority_langs + sorted(other_langs)
        
        # Paginate languages
        start_idx = page * languages_per_page
        end_idx = start_idx + languages_per_page
        page_languages = sorted_languages[start_idx:end_idx]
        
        keyboard = []
        
        # Create language buttons
        for i in range(0, len(page_languages), languages_per_row):
            row = []
            for j in range(languages_per_row):
                if i + j < len(page_languages):
                    lang_code = page_languages[i + j]
                    lang_info = SUPPORTED_LANGUAGES.get(lang_code, {
                        'name': lang_code.upper(), 
                        'flag': '🌐'
                    })
                    
                    button_text = f"{lang_info['flag']} {lang_info['name']}"
                    callback_data = f"sub_lang:{request_id}:{movie_id}:{lang_code}"
                    
                    row.append(InlineKeyboardButton(button_text, callback_data=callback_data))
            
            if row:
                keyboard.append(row)
        
        # Navigation buttons
        nav_buttons = []
        
        # Previous page button
        if page > 0:
            nav_buttons.append(InlineKeyboardButton(
                "⬅️ Previous", 
                callback_data=f"sub_page:{request_id}:{movie_id}:{page-1}"
            ))
        
        # Next page button
        if end_idx < len(sorted_languages):
            nav_buttons.append(InlineKeyboardButton(
                "Next ➡️", 
                callback_data=f"sub_page:{request_id}:{movie_id}:{page+1}"
            ))
        
        if nav_buttons:
            keyboard.append(nav_buttons)
        
        # Control buttons
        control_buttons = [
            InlineKeyboardButton(
                "🚫 No Subtitles", 
                callback_data=f"sub_none:{request_id}:{movie_id}"
            ),
            InlineKeyboardButton(
                "⬅️ Back to Movie", 
                callback_data=f"back_movie:{request_id}:{movie_id}"
            )
        ]
        keyboard.append(control_buttons)
        
        return InlineKeyboardMarkup(keyboard)
    
    @staticmethod
    def create_subtitle_quality_selection(movie_id: str, language: str, 
                                        subtitles: list, request_id: int):
        """Create quality selection keyboard for multiple subtitle options"""
        keyboard = []
        
        for i, subtitle in enumerate(subtitles[:5]):  # Limit to top 5 options
            # Create quality indicator
            download_count = subtitle.get('download_count', 0)
            if download_count >= 1000:
                quality_emoji = '🌟'
            elif download_count >= 100:
                quality_emoji = '⭐'
            elif download_count >= 10:
                quality_emoji = '✨'
            else:
                quality_emoji = '📝'
            
            # Create button text
            release = subtitle.get('release', 'Standard')[:20]  # Limit length
            button_text = f"{quality_emoji} {release} ({download_count} DL)"
            
            callback_data = f"sub_download:{request_id}:{movie_id}:{language}:{i}"
            keyboard.append([InlineKeyboardButton(button_text, callback_data=callback_data)])
        
        # Back button
        keyboard.append([InlineKeyboardButton(
            "⬅️ Back to Languages", 
            callback_data=f"sub_back_lang:{request_id}:{movie_id}"
        )])
        
        return InlineKeyboardMarkup(keyboard)
    
    @staticmethod
    def create_download_progress_keyboard(movie_id: str, request_id: int):
        """Create keyboard shown during download"""
        keyboard = [[
            InlineKeyboardButton(
                "⏳ Downloading...", 
                callback_data="downloading"
            )
        ]]
        return InlineKeyboardMarkup(keyboard)

@Client.on_callback_query(filters.regex(r"^sub_lang:"))
async def handle_subtitle_language_selection(client: Client, callback_query: CallbackQuery):
    """Handle subtitle language selection"""
    try:
        _, request_id, movie_id, language = callback_query.data.split(":")
        
        if int(request_id) != callback_query.from_user.id:
            await callback_query.answer("❌ This is not for you!", show_alert=True)
            return
        
        # Show loading state
        await callback_query.answer("🔍 Searching for subtitles...")
        
        # Get movie info (you'll need to implement this based on your existing system)
        movie_title = await get_movie_title_by_id(movie_id)
        imdb_id = await get_imdb_id_by_movie_id(movie_id)
        
        # Search for subtitles
        subtitles = await subtitle_db.search_and_cache_subtitles(
            movie_title, imdb_id, language
        )
        
        if not subtitles:
            lang_info = SUPPORTED_LANGUAGES.get(language, {'name': language.upper()})
            await callback_query.edit_message_text(
                script.NO_SUBTITLE_TXT.format(movie_title=movie_title),
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        "⬅️ Try Another Language", 
                        callback_data=f"sub_back_lang:{request_id}:{movie_id}"
                    ),
                    InlineKeyboardButton(
                        "🎬 Download Without Subs", 
                        callback_data=f"files#{movie_id}"
                    )
                ]])
            )
            return
        
        # If only one subtitle option, download directly
        if len(subtitles) == 1:
            await download_and_send_subtitle(
                client, callback_query, movie_id, language, subtitles[0], request_id
            )
        else:
            # Show quality selection
            lang_info = SUPPORTED_LANGUAGES.get(language, {'name': language.upper()})
            keyboard = SubtitleKeyboardBuilder.create_subtitle_quality_selection(
                movie_id, language, subtitles, int(request_id)
            )
            
            await callback_query.edit_message_text(
                f"🎬 **{movie_title}**\n\n"
                f"📝 **{lang_info['name']} Subtitles**\n\n"
                f"Found {len(subtitles)} subtitle options. "
                f"Choose the best quality for your needs:",
                reply_markup=keyboard
            )
            
    except Exception as e:
        logger.error(f"Error in subtitle language selection: {e}")
        await callback_query.answer("❌ An error occurred. Please try again.", show_alert=True)

@Client.on_callback_query(filters.regex(r"^sub_download:"))
async def handle_subtitle_download(client: Client, callback_query: CallbackQuery):
    """Handle subtitle download"""
    try:
        _, request_id, movie_id, language, subtitle_index = callback_query.data.split(":")
        
        if int(request_id) != callback_query.from_user.id:
            await callback_query.answer("❌ This is not for you!", show_alert=True)
            return
        
        # Get subtitle info from cache/storage
        movie_title = await get_movie_title_by_id(movie_id)
        imdb_id = await get_imdb_id_by_movie_id(movie_id)
        
        subtitles = await subtitle_db.search_and_cache_subtitles(
            movie_title, imdb_id, language
        )
        
        if not subtitles or int(subtitle_index) >= len(subtitles):
            await callback_query.answer("❌ Subtitle not found!", show_alert=True)
            return
        
        subtitle_info = subtitles[int(subtitle_index)]
        await download_and_send_subtitle(
            client, callback_query, movie_id, language, subtitle_info, int(request_id)
        )
        
    except Exception as e:
        logger.error(f"Error in subtitle download: {e}")
        await callback_query.answer("❌ Download failed. Please try again.", show_alert=True)

@Client.on_callback_query(filters.regex(r"^sub_page:"))
async def handle_subtitle_page_navigation(client: Client, callback_query: CallbackQuery):
    """Handle subtitle language page navigation"""
    try:
        _, request_id, movie_id, page = callback_query.data.split(":")
        
        if int(request_id) != callback_query.from_user.id:
            await callback_query.answer("❌ This is not for you!", show_alert=True)
            return
        
        # Get available languages (this should be cached)
        available_languages = await subtitle_db.get_available_languages(movie_id)
        
        if not available_languages:
            await callback_query.answer("❌ No languages available!", show_alert=True)
            return
        
        movie_title = await get_movie_title_by_id(movie_id)
        keyboard = SubtitleKeyboardBuilder.create_language_selection(
            movie_id, available_languages, int(request_id), int(page)
        )
        
        await callback_query.edit_message_text(
            script.SUBTITLE_SELECTION_TXT.format(movie_title=movie_title),
            reply_markup=keyboard
        )
        
    except MessageNotModified:
        await callback_query.answer()
    except Exception as e:
        logger.error(f"Error in page navigation: {e}")
        await callback_query.answer("❌ Navigation failed!", show_alert=True)

@Client.on_callback_query(filters.regex(r"^sub_back_lang:"))
async def handle_back_to_languages(client: Client, callback_query: CallbackQuery):
    """Handle back to language selection"""
    try:
        _, request_id, movie_id = callback_query.data.split(":")
        
        if int(request_id) != callback_query.from_user.id:
            await callback_query.answer("❌ This is not for you!", show_alert=True)
            return
        
        # Get available languages
        available_languages = await subtitle_db.get_available_languages(movie_id)
        
        if not available_languages:
            # Search for available languages
            movie_title = await get_movie_title_by_id(movie_id)
            imdb_id = await get_imdb_id_by_movie_id(movie_id)
            
            if subtitle_db.api_manager:
                available_languages = await subtitle_db.api_manager.get_available_languages(
                    movie_title, imdb_id
                )
                
                if available_languages:
                    await subtitle_db.cache.set_available_languages(movie_id, available_languages)
        
        if not available_languages:
            await callback_query.answer("❌ No subtitles available for this movie!", show_alert=True)
            return
        
        movie_title = await get_movie_title_by_id(movie_id)
        keyboard = SubtitleKeyboardBuilder.create_language_selection(
            movie_id, available_languages, int(request_id)
        )
        
        await callback_query.edit_message_text(
            script.SUBTITLE_SELECTION_TXT.format(movie_title=movie_title),
            reply_markup=keyboard
        )
        
    except Exception as e:
        logger.error(f"Error going back to languages: {e}")
        await callback_query.answer("❌ An error occurred!", show_alert=True)

@Client.on_callback_query(filters.regex(r"^sub_none:"))
async def handle_no_subtitles(client: Client, callback_query: CallbackQuery):
    """Handle no subtitles selection - proceed with movie download"""
    try:
        _, request_id, movie_id = callback_query.data.split(":")
        
        if int(request_id) != callback_query.from_user.id:
            await callback_query.answer("❌ This is not for you!", show_alert=True)
            return
        
        # Redirect to file download
        await callback_query.answer("🎬 Proceeding without subtitles...")
        
        # Trigger the original file callback
        callback_query.data = f"files#{movie_id}"
        
        # Import and call the original file handler
        from plugins.pm_filter import cb_handler
        await cb_handler(client, callback_query)
        
    except Exception as e:
        logger.error(f"Error in no subtitles handler: {e}")
        await callback_query.answer("❌ An error occurred!", show_alert=True)

async def download_and_send_subtitle(client: Client, callback_query: CallbackQuery, 
                                   movie_id: str, language: str, subtitle_info: dict, 
                                   request_id: int):
    """Download subtitle and send to user"""
    try:
        # Show downloading state
        await callback_query.edit_message_text(
            "📥 Downloading subtitle...\n\n"
            "⏳ This may take a few seconds",
            reply_markup=SubtitleKeyboardBuilder.create_download_progress_keyboard(
                movie_id, request_id
            )
        )
        
        # Download and process subtitle
        subtitle_content = await subtitle_db.download_and_process_subtitle(
            movie_id, language, subtitle_info
        )
        
        if not subtitle_content:
            await callback_query.edit_message_text(
                "❌ **Download Failed**\n\n"
                "Unable to download the subtitle file. "
                "Please try another option or proceed without subtitles.",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(
                        "⬅️ Try Another", 
                        callback_data=f"sub_back_lang:{request_id}:{movie_id}"
                    ),
                    InlineKeyboardButton(
                        "🎬 Movie Only", 
                        callback_data=f"files#{movie_id}"
                    )
                ]])
            )
            return
        
        # Prepare subtitle file
        lang_info = SUPPORTED_LANGUAGES.get(language, {'name': language.upper()})
        movie_title = await get_movie_title_by_id(movie_id)
        
        # Clean movie title for filename
        clean_title = "".join(c for c in movie_title if c.isalnum() or c in (' ', '-', '_')).strip()
        filename = f"{clean_title}_{lang_info['name']}.srt"
        
        # Create BytesIO object for the subtitle file
        subtitle_file = BytesIO(subtitle_content.encode('utf-8'))
        subtitle_file.name = filename
        
        # Send subtitle file
        await client.send_document(
            chat_id=callback_query.from_user.id,
            document=subtitle_file,
            caption=f"📝 **{lang_info['name']} Subtitles**\n\n"
                   f"🎬 Movie: {movie_title}\n"
                   f"📊 Quality: {subtitle_info.get('download_count', 0)} downloads\n"
                   f"📁 Format: SRT\n\n"
                   f"**How to use:**\n"
                   f"1. Download both movie and subtitle files\n"
                   f"2. Keep them in the same folder\n"
                   f"3. Make sure they have similar names\n"
                   f"4. Open with any video player that supports subtitles",
            reply_to_message_id=callback_query.message.id
        )
        
        # Update message with success and movie download option
        await callback_query.edit_message_text(
            f"✅ **Subtitle Downloaded Successfully!**\n\n"
            f"📝 Language: {lang_info['name']}\n"
            f"🎬 Movie: {movie_title}\n\n"
            f"The subtitle file has been sent above. "
            f"Now download the movie file:",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    "🎬 Download Movie", 
                    callback_data=f"files#{movie_id}"
                ),
                InlineKeyboardButton(
                    "📝 Get Another Language", 
                    callback_data=f"sub_back_lang:{request_id}:{movie_id}"
                )
            ]])
        )
        
    except Exception as e:
        logger.error(f"Error downloading and sending subtitle: {e}")
        await callback_query.edit_message_text(
            "❌ **Download Failed**\n\n"
            "An error occurred while processing the subtitle. "
            "Please try again or proceed without subtitles.",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    "🔄 Try Again", 
                    callback_data=f"sub_back_lang:{request_id}:{movie_id}"
                ),
                InlineKeyboardButton(
                    "🎬 Movie Only", 
                    callback_data=f"files#{movie_id}"
                )
            ]])
        )

# Helper functions (implement these based on your existing system)
async def get_movie_title_by_id(movie_id: str) -> str:
    """Get movie title by file ID - implement based on your existing system"""
    # This should integrate with your existing file database
    from database.ia_filterdb import get_file_details
    
    file_details = await get_file_details(movie_id)
    if file_details:
        return file_details.get('file_name', 'Unknown Movie')
    return 'Unknown Movie'

async def get_imdb_id_by_movie_id(movie_id: str) -> str:
    """Get IMDB ID by movie file ID - implement based on your existing system"""
    # This might require additional database fields or external API calls
    # For now, return None and rely on title-based search
    return None

# Admin command for subtitle statistics
@Client.on_message(filters.command("subtitle_stats") & filters.private & filters.user(temp.ADMINS if hasattr(temp, 'ADMINS') else []))
async def subtitle_stats_command(client: Client, message):
    """Show subtitle system statistics"""
    try:
        if not ENABLE_SUBTITLES:
            await message.reply("❌ Subtitle system is disabled.")
            return
        
        stats = await subtitle_db.get_database_statistics()
        
        storage_stats = stats.get('storage', {})
        cache_stats = stats.get('cache', {})
        
        stats_text = f"""📊 **Subtitle System Statistics**

**📁 Storage:**
• Subtitle Entries: {storage_stats.get('subtitle_entries', 0)}
• Movie Entries: {storage_stats.get('movie_entries', 0)}
• Database Size: {storage_stats.get('database_size', 0)} bytes
• GridFS Files: {storage_stats.get('gridfs_files', 0)}
• GridFS Size: {storage_stats.get('gridfs_size', 0)} bytes

**⚡ Cache:**
• Status: {cache_stats.get('status', 'Unknown')}
• Total Keys: {cache_stats.get('total_keys', 0)}
• Memory Usage: {cache_stats.get('memory_usage', 'Unknown')}
• Connected Clients: {cache_stats.get('connected_clients', 0)}

**🌐 Popular Languages:**
"""
        
        # Add language statistics
        languages = storage_stats.get('languages', [])[:5]
        for i, lang_stat in enumerate(languages, 1):
            lang_code = lang_stat.get('_id', 'unknown')
            lang_info = SUPPORTED_LANGUAGES.get(lang_code, {'name': lang_code.upper(), 'flag': '🌐'})
            count = lang_stat.get('count', 0)
            stats_text += f"{i}. {lang_info['flag']} {lang_info['name']}: {count} subtitles\n"
        
        await message.reply(stats_text)
        
    except Exception as e:
        logger.error(f"Error getting subtitle stats: {e}")
        await message.reply(f"❌ Error getting statistics: {str(e)}")

# Admin command for subtitle cleanup
@Client.on_message(filters.command("subtitle_cleanup") & filters.private & filters.user(temp.ADMINS if hasattr(temp, 'ADMINS') else []))
async def subtitle_cleanup_command(client: Client, message):
    """Clean up subtitle system"""
    try:
        if not ENABLE_SUBTITLES:
            await message.reply("❌ Subtitle system is disabled.")
            return
        
        status_msg = await message.reply("🧹 Starting cleanup...")
        
        cleanup_stats = await subtitle_db.cleanup_system()
        
        await status_msg.edit_text(
            f"✅ **Cleanup Completed**\n\n"
            f"🗑️ Storage entries cleaned: {cleanup_stats.get('storage_cleaned', 0)}\n"
            f"⚡ Cache keys cleaned: {cleanup_stats.get('cache_cleaned', 0)}"
        )
        
    except Exception as e:
        logger.error(f"Error during cleanup: {e}")
        await message.reply(f"❌ Cleanup failed: {str(e)}")