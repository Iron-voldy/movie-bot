class script(object):
    START_TXT = """𝙷𝚎𝚕𝚕𝚊𝚘𝚠 <b>{}</b>, 
𝙸𝚖 𝚈𝚘𝚞𝚛 𝙵𝚛𝚒𝚎𝚗𝚍𝚕𝚢 <a href=https://t.me/{}>{}</a>.
    
- 𝚈𝚘𝚞 𝙲𝚊𝚗 𝙶𝚎𝚝 𝚈𝚘𝚞𝚛 𝙵𝚒𝚕𝚖 𝙰𝚗𝚍 𝚂𝚎𝚛𝚒𝚎𝚜 𝚏𝚒𝚕𝚎𝚜 𝚄𝚜𝚒𝚗𝚐 𝚝𝚑𝚒𝚜 𝚋𝚘𝚝. 
- 𝙰𝚍𝚍 𝚋𝚘𝚝 𝚝𝚘 𝚈𝚘𝚞𝚛 𝙶𝚛𝚘𝚞𝚙 𝚘𝚛 𝚁𝚎𝚚𝚞𝚎𝚜𝚝 𝙷𝚎𝚛𝚎. 😍
- 🎬 𝙽𝚘𝚠 𝚠𝚒𝚝𝚑 𝚜𝚞𝚋𝚝𝚒𝚝𝚕𝚎 𝚜𝚞𝚙𝚙𝚘𝚛𝚝! 📝"""

    
    HELP_TXT = """Hello {}!
    
Here αre тнe αvαιlαвle coммαɴdѕ.
    
I'м нere тo αѕѕιѕт yoυ! Feel ғree тo αѕĸ ғor αɴy ɢυιdαɴce or coммαɴdѕ yoυ мαy ɴeed.
Leт'ѕ мαĸe тнιɴɢѕ eαѕιer ғor yoυ!

🎬 **Movie Search**: Search for movies and get subtitles in multiple languages
📝 **Subtitle Support**: Available languages include English, Spanish, French, German, Tamil, Sinhala, Hindi, Korean, and many more!"""


    ABOUT_TXT = """Here αre ѕoмe deтαιlѕ yoυ ɴeed тo ĸɴow.

✯ 𝙱𝙾𝚃 𝚃𝚈𝙿𝙴: 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝚅𝟹 + 𝚂𝚄𝙱𝚃𝙸𝚃𝙻𝙴𝚂	
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href="https://t.me/ImSahanSBot">Sahan</a>
✯ 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁: <a href="https://t.me/Iron_voldy">Hasindu</a> 
✯ 𝚂𝙾𝚄𝚁𝙲𝙴: 𝙿𝚛𝚒𝚟𝚊𝚝𝚎 (ᴅᴍ ᴅᴇᴠᴇʟᴏᴘᴇʀ) 
✯ 𝚂𝚄𝙱𝚃𝙸𝚃𝙻𝙴𝚂: 𝙴𝚗𝚊𝚋𝚕𝚎𝚍 📝
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴𝚂: 40+ languages supported
✯ 𝚀𝚄𝙰𝙻𝙸𝚃𝚈: High quality subtitles from multiple sources"""  

      
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Fιlтerѕ αllow υѕerѕ тo ѕeт αυтoмαтed replιeѕ ғor ѕpecιғιc ĸeywordѕ, αɴd тнe вoт wιll reѕpoɴd wнeɴever α ĸeyword ιѕ ғoυɴd ιɴ тнe мeѕѕαɢe.

<b>NOTE:</b>
1. Tнιѕ вoт ѕнoυld нαve αdмιɴ prιvιleɢeѕ тo ғυɴcтιoɴ properly.  
2. Oɴly αdмιɴѕ cαɴ αdd ғιlтerѕ ιɴ α cнαт.  
3. Alerт вυттoɴѕ нαve α lιмιт oғ 64 cнαrαcтerѕ.

<b>Coммαɴdѕ αɴd Uѕαɢe:</b>
/filter - <code>Add a filter in a chat.</code>  
/filters - <code>List all the filters in a chat.</code>  
/del - <code>Delete a specific filter in a chat.</code>  
/delall - <code>Delete all filters in a chat (chat owner only).</code>"""


    BUTTON_TXT = """Help: <b>Buttons</b>
- Tнe вoт ѕυpporтѕ вoтн URL αɴd αlerт ιɴlιɴe вυттoɴѕ.

<b>NOTE:</b>
1. Teleɢrαм wιll ɴoт αllow yoυ тo ѕeɴd вυттoɴѕ wιтнoυт αɴy coɴтeɴт, ѕo coɴтeɴт ιѕ мαɴdαтory.  
2. Tнe вoт ѕυpporтѕ вυттoɴѕ wιтн αɴy тype oғ Teleɢrαм мedια.  
3. Bυттoɴѕ ѕнoυld вe properly pαrѕed ιɴ мαrĸdowɴ ғorмαт.

<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/SECLK)</code>

<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:This is an alert message, You should use @NETFLIXLKBOT to get Movies)</code>"""


    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Mαĸe мe тнe αdмιɴ oғ yoυr cнαɴɴel ιғ ιт'ѕ prιvαтe.  
2. Mαĸe ѕυre тнαт yoυr cнαɴɴel doeѕ ɴoт coɴтαιɴ cαмrιpѕ, porɴ, or ғαĸe ғιleѕ.  
3. Forwαrd тнe lαѕт мeѕѕαɢe тo мe wιтн qυoтeѕ.

I'll αdd αll тнe ғιleѕ ιɴ тнαт cнαɴɴel тo мy dαтαвαѕe.

<b>🎬 Subtitle Features:</b>
- Search for movies with available subtitles
- Select subtitle language before download
- Automatic subtitle quality detection  
- Support for multiple subtitle formats (.srt, .vtt, .ass)
- High-quality subtitles from OpenSubtitles and SubDB
- 40+ languages including English, Spanish, French, German, Hindi, Tamil, Sinhala, Korean, Japanese, Chinese, Arabic and more!"""

    
    CONNECTION_TXT = """Help: <b>Connections</b>

- Uѕed тo coɴɴecт тнe вoт тo PM ғor мαɴαɢιɴɢ ғιlтerѕ.
- Helpѕ αvoιd ѕpαммιɴɢ ιɴ ɢroυpѕ.

<b>NOTE:</b>
1. Oɴly αdмιɴѕ cαɴ αdd α coɴɴecтιoɴ.
2. Seɴd <code>/connect</code> ғor coɴɴecтιɴɢ мe тo yoυr PM.

<b>Commands and Usage:</b>
/connect  - <code>Connect a particular chat to your PM</code>
/disconnect  - <code>Disconnect from a chat</code>
/connections  - <code>List all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
Tнeѕe αre αddιтιoɴαl ғeαтυreѕ oғ тнe вoт тo eɴнαɴce yoυr eхperιeɴce.

<b>Commands and Usage:</b>
/id - <code>Retrieve the ID of a specified user.</code>
/info - <code>Get detailed information about a user.</code>
/imdb - <code>Fetch film information from IMDb.</code>
/search - <code>Search for film details across multiple sources.</code>
/ping - <code>To check bot speed.</code>
/subtitle - <code>Get subtitle information for a movie.</code>

<b>🎬 Subtitle Commands:</b>
/subtitle_stats - <code>View subtitle system statistics (Admin only)</code>
/subtitle_cleanup - <code>Clean up expired subtitle cache (Admin only)</code>

Feel ғree тo υѕe тнeѕe coммαɴdѕ тo eхplore тнe вoт'ѕ cαpαвιlιтιeѕ ғυrтнer! 📚"""


    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
Tнιѕ мodυle ιѕ eхclυѕιvely ғor вoт αdмιɴιѕтrαтorѕ oɴly. Uѕe тнeѕe coммαɴdѕ тo мαɴαɢe υѕerѕ αɴd cнαт operαтιoɴѕ eғғecтιvely.

<b>Commands and Usage:</b>
/users - <code>Retrieve a list of all users and their IDs.</code>
/chats - <code>Get a list of all chats and their IDs.</code>
/leave - <code>Leave a specified chat.</code>
/channel - <code>Get a list of all connected channels.</code>
/broadcast - <code>Broadcast a message to all users.</code>

<b>🎬 Subtitle Admin Commands:</b>
/subtitle_stats - <code>Get subtitle database statistics</code>
/subtitle_cleanup - <code>Clean up expired subtitle entries</code>
/reset_subtitle_cache - <code>Reset subtitle cache completely</code>
/subtitle_languages - <code>View supported subtitle languages</code>

Uѕe тнeѕe αdмιɴ coммαɴdѕ тo мαɴαɢe yoυr вoт eғғecтιvely αɴd ĸeep everyтнιɴɢ rυɴɴιɴɢ ѕмooтнly! 📊"""

    
    STATUS_TXT = """- 𝙵𝚒𝚕𝚎 𝙳𝚊𝚝𝚊𝚋𝚊𝚜𝚎 𝟷.𝟶 -
★ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ: <code>{}</code>
★ ᴜꜱᴇᴅ ꜱᴛᴏʀᴀɢᴇ: <code>{}</code>

- 𝙵𝚒𝚕𝚎 𝙳𝚊𝚝𝚊𝚋𝚊𝚜𝚎 𝟸.𝟶 -
★ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ: <code>{}</code>
★ ᴜꜱᴇᴅ ꜱᴛᴏʀᴀɢᴇ: <code>{}</code>

- 𝚄𝚜𝚎𝚛 𝙳𝚊𝚝𝚊𝚋𝚊𝚜𝚎 𝟷.𝟶 -
★ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{}</code>
★ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: <code>{}</code>
★ ᴜꜱᴇᴅ ꜱᴛᴏʀᴀɢᴇ: <code>{}</code>

- 𝚂𝚞𝚋𝚝𝚒𝚝𝚕𝚎 𝙳𝚊𝚝𝚊𝚋𝚊𝚜𝚎 -
★ ᴄᴀᴄʜᴇᴅ ꜱᴜʙᴛɪᴛʟᴇꜱ: <code>{}</code>
★ ᴀᴄᴛɪᴠᴇ ʟᴀɴɢᴜᴀɢᴇꜱ: <code>{}</code>

- 𝚂𝚎𝚛𝚟𝚎𝚛 𝚁𝚎𝚜𝚘𝚞𝚛𝚌𝚎𝚜 -
★ ᴛᴏᴛᴀʟ ʀᴀᴍ: <code>{}</code>
★ ᴜsᴇᴅ ʀᴀᴍ: <code>{}</code>"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    
    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, 
ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ᴏʀ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ

📝 𝚂𝚄𝙱𝚃𝙸𝚃𝙻𝙴 𝚂𝚄𝙿𝙿𝙾𝚁𝚃: Available in multiple languages including English, Spanish, French, German, Tamil, Hindi, Korean, Sinhala, Arabic, Russian, Japanese, Chinese and more!

🌟 𝚀𝚄𝙰𝙻𝙸𝚃𝚈 𝙸𝙽𝙳𝙸𝙲𝙰𝚃𝙾𝚁𝚂:
🌟 = Excellent (1000+ downloads)
⭐ = Good (100+ downloads)  
✨ = Average (10+ downloads)
📝 = Basic quality"""

    MINFO = """
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴀ ᴍᴏᴠɪᴇ ғᴏʟʟᴏᴡ ᴛʜᴇ ғᴏʀᴍᴀᴛ ʙᴇʟᴏᴡ
𝐔𝐧𝐜𝐡𝐚𝐫𝐭𝐞𝐝 | 𝐃𝐮𝐧𝐞 𝟐𝟎𝟐𝟏 | 𝐓𝐫𝐨𝐥𝐥 𝟐𝟎𝟐𝟐 𝟕𝟐𝟎𝐩

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)

📝 𝚂𝚄𝙱𝚃𝙸𝚃𝙻𝙴 𝙽𝙾𝚃𝙴: After movie selection, you can choose subtitle language from available options. We support 40+ languages with high-quality subtitles!

🎬 𝙼𝙾𝚅𝙸𝙴 + 𝚂𝚄𝙱𝚃𝙸𝚃𝙻𝙴 𝙿𝚁𝙾𝙲𝙴𝚂𝚂:
1. Search for movie name
2. Select movie from results  
3. Choose subtitle language
4. Download both movie and subtitle files
5. Keep them in same folder with similar names
6. Enjoy with subtitles! 🍿"""

    SINFO = """
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴀ sᴇʀɪᴇs ғᴏʟʟᴏᴡ ᴛʜᴇ ғᴏʀᴍᴀᴛ ʙᴇʟᴏᴡ
𝐋𝐨𝐤𝐢 𝐒𝟎𝟏𝐄𝟎𝟏 | 𝐘𝐨𝐮 𝐒𝟎𝟑 | 𝐖𝐞𝐝𝐧𝐞𝐬𝐝𝐚𝐲 𝐒𝟎𝟏 𝟕𝟐𝟎𝐩

🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)

📝 𝚂𝚄𝙱𝚃𝙸𝚃𝙻𝙴 𝙽𝙾𝚃𝙴: Episodes also support subtitle selection in multiple languages. Each episode can have different subtitle options!

📺 𝚂𝙴𝚁𝙸𝙴𝚂 + 𝚂𝚄𝙱𝚃𝙸𝚃𝙻𝙴 𝙿𝚁𝙾𝙲𝙴𝚂𝚂:
1. Search for series name with season/episode
2. Select episode from results
3. Choose subtitle language  
4. Download episode and subtitle files
5. Rename subtitle to match episode filename
6. Binge-watch with subtitles! 📺"""
    
    
    OWNER_INFO = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯    
• ꜰᴜʟʟ ɴᴀᴍᴇ : 𝚂𝚊𝚑𝚊𝚗 𝚂𝚊𝚗𝚍𝚊𝚛𝚞𝚠𝚊𝚗
• ᴀʙᴏᴜᴛ : <a href='https://t.me/About_Sandaruwan'>𝙰𝚋𝚘𝚞𝚝 𝚂𝚊𝚗𝚍𝚊𝚛𝚞𝚠𝚊𝚗</a>
• ᴅᴍ ʟɪɴᴋ : <a href='https://t.me/Sandaruwan_Feedback_Bot'>𝚂𝚊𝚑𝚊𝚗𝚂</a>

📝 𝚂𝚄𝙱𝚃𝙸𝚃𝙻𝙴 𝚂𝚈𝚂𝚃𝙴𝙼 𝙸𝙽𝙵𝙾:
• 40+ Languages supported
• High-quality subtitles from multiple sources
• Automatic format conversion
• Smart caching for faster access</b>"""

    IMDB_TEMPLATE = """
🎬 <b><a href={url}>{title}</a> ({year})</b>  
‌‌‌‌<b>{runtime}min | {release_date}</b>  

‌‌‌‌<b>⭐️ IMDB</b> ➠ <b><i>{rating}/10 ({votes})</i></b>  
‌‌‌‌<b>🌏 Country</b> ➠ <b><i>{countries}</i></b>  
<b>🔉 Language</b> ➠ <b><i>{languages}</i></b>  
‌‌‌‌‌‌‌‌‌‌‌‌<b>⚙️ Genres</b> ➠ <b><i>{genres}</i></b>  

📝 <b>Subtitle Support:</b> Available in 40+ languages
‌‌‌‌®️ <b><a href='https://t.me/SECL4U'>Mαιɴ Cнαɴɴel</a></b>
"""

    FILE_CAPTION = """➥ 𝗙𝗶𝗹𝗲 𝗡𝗮𝗺𝗲: <b>@SECL4U </b><code>{file_name}</code>

<b><i>⚠️ Warning:</b> This file will be deleted within 5 minutes. Please make sure to forward it to your <b>"Saved Messages"</b> before downloading.</i>

📝 <b>Subtitle Available:</b> Check our subtitle support for this movie!

➠ 𝗛𝗮𝘃𝗶𝗻𝗴 𝗶𝘀𝘀𝘂𝗲: <a href='https://t.me/SECL4U/54'>𝙏𝙧𝙮 𝙖𝙣𝙤𝙩𝙝𝙚𝙧 𝙗𝙤𝙩</a>
➠ 𝗡𝗲𝘄 𝘁𝗼 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁: <a href='https://t.me/SECOfficial_Bot'>𝙒𝙖𝙩𝙘𝙝 𝙩𝙝𝙚 𝙜𝙪𝙞𝙙𝙚</a>
━━━━━━━━━━━━━━‌‌
🪫 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗯𝘆: 
<b>- @SECLK | @CeylonCryptoSL -</b>"""

    SUBTITLE_SELECTION_TXT = """
🎬 <b>{movie_title}</b>

📝 <b>Choose Subtitle Language:</b>

Please select your preferred subtitle language from the options below:

🔹 High quality subtitles from multiple sources
🔹 Multiple format support (.srt, .vtt, .ass)  
🔹 Synchronized with movie timing
🔹 Quality indicators show download popularity

<b>Quality Indicators:</b>
🌟 = Excellent (1000+ downloads)
⭐ = Good (100+ downloads)
✨ = Average (10+ downloads)
📝 = Basic quality

<b>Supported Languages:</b> English, Spanish, French, German, Hindi, Tamil, Telugu, Malayalam, Kannada, Sinhala, Arabic, Russian, Japanese, Korean, Chinese, Italian, Portuguese, Dutch, Swedish, Norwegian, Danish, Finnish, Polish, Czech, Hungarian, Romanian, Bulgarian, Croatian, Serbian, Slovak, Slovenian, Ukrainian, Turkish, Thai, Vietnamese, Indonesian, Malay, Bengali, Urdu, Persian, Hebrew and more!
"""

    NO_SUBTITLE_TXT = """
🎬 <b>{movie_title}</b>

❌ <b>No subtitles found</b>

Unfortunately, subtitles are not available for this movie in the requested language. 

🔄 <b>You can try:</b>
• Searching with the original movie title
• Checking for alternative releases  
• Trying a different language
• Requesting subtitles from our community

The movie file is still available for download without subtitles.

<b>Tip:</b> Popular movies usually have subtitles in major languages like English, Spanish, French, German, Hindi, etc.
"""

    SUBTITLE_DOWNLOAD_SUCCESS_TXT = """
✅ <b>Subtitle Downloaded Successfully!</b>

🎬 <b>Movie:</b> {movie_title}
📝 <b>Language:</b> {language_name} {language_flag}
📊 <b>Quality:</b> {download_count} downloads
📁 <b>Format:</b> SRT (SubRip Text)
💾 <b>Size:</b> {file_size}

<b>📖 How to use subtitles:</b>
1. Download both movie and subtitle files
3. Make sure they have similar names (movie.mp4 & movie.srt)
4. Open with any video player that supports subtitles
5. Enable subtitles in player settings if needed

<b>📱 Recommended Players:</b>
• VLC Media Player (PC/Mobile)
• MX Player (Android)
• Infuse (iOS)
• Kodi (All platforms)
• PotPlayer (Windows)

The subtitle file has been sent above. Now you can download the movie file!
"""

    SUBTITLE_DOWNLOADING_TXT = """
📥 <b>Downloading Subtitle...</b>

🎬 <b>Movie:</b> {movie_title}
📝 <b>Language:</b> {language_name} {language_flag}
📊 <b>Quality:</b> {download_count} downloads

⏳ Please wait while we fetch and process your subtitle file...

<b>Processing steps:</b>
1. 🔍 Searching subtitle database...
2. 📥 Downloading from source...
3. 🔧 Processing and converting...
4. ✅ Preparing for delivery...

This usually takes 10-30 seconds depending on file size and server load.
"""

    SUBTITLE_ERROR_TXT = """
❌ <b>Subtitle Download Failed</b>

🎬 <b>Movie:</b> {movie_title}
📝 <b>Language:</b> {language_name}

<b>Possible reasons:</b>
• Source server temporarily unavailable
• Subtitle file corrupted or removed
• Network connectivity issues
• Rate limit exceeded

<b>🔄 What you can do:</b>
• Try again in a few minutes
• Select a different subtitle option
• Choose another language
• Download movie without subtitles

We apologize for the inconvenience. Our system automatically tries multiple sources to ensure best availability.
"""

    SUBTITLE_STATS_TXT = """
📊 <b>Subtitle System Statistics</b>

<b>📁 Database Storage:</b>
• Cached Subtitles: {subtitle_entries}
• Movie Entries: {movie_entries}
• Database Size: {database_size}
• GridFS Files: {gridfs_files}
• Storage Used: {storage_size}

<b>⚡ Cache Performance:</b>
• Status: {cache_status}
• Active Keys: {total_keys}
• Memory Usage: {memory_usage}
• Hit Rate: {hit_rate}%

<b>🌐 Language Distribution:</b>
{language_stats}

<b>📈 Usage Statistics:</b>
• Total Downloads: {total_downloads}
• Active Languages: {active_languages}
• Average Quality Score: {avg_quality}
• Cache Efficiency: {cache_efficiency}%

<b>🔧 System Health:</b>
• API Status: {api_status}
• Database: {db_status}
• Cache: {cache_status}
• Uptime: {uptime}
"""

    SUBTITLE_LANGUAGES_TXT = """
🌐 <b>Supported Subtitle Languages</b>

<b>📝 40+ Languages Available:</b>

<b>🇪🇺 European Languages:</b>
🇺🇸 English • 🇪🇸 Spanish • 🇫🇷 French • 🇩🇪 German • 🇮🇹 Italian • 🇵🇹 Portuguese • 🇷🇺 Russian • 🇳🇱 Dutch • 🇸🇪 Swedish • 🇳🇴 Norwegian • 🇩🇰 Danish • 🇫🇮 Finnish • 🇵🇱 Polish • 🇨🇿 Czech • 🇭🇺 Hungarian • 🇷🇴 Romanian • 🇧🇬 Bulgarian • 🇭🇷 Croatian • 🇷🇸 Serbian • 🇸🇰 Slovak • 🇸🇮 Slovenian • 🇱🇻 Latvian • 🇱🇹 Lithuanian • 🇪🇪 Estonian • 🇺🇦 Ukrainian • 🇧🇾 Belarusian

<b>🇦🇸 Asian Languages:</b>
🇮🇳 Hindi • 🇮🇳 Tamil • 🇮🇳 Telugu • 🇮🇳 Malayalam • 🇮🇳 Kannada • 🇱🇰 Sinhala • 🇯🇵 Japanese • 🇰🇷 Korean • 🇨🇳 Chinese • 🇹🇭 Thai • 🇻🇳 Vietnamese • 🇮🇩 Indonesian • 🇲🇾 Malay • 🇧🇩 Bengali • 🇵🇰 Urdu

<b>🌍 Other Languages:</b>
🇸🇦 Arabic • 🇮🇷 Persian • 🇮🇱 Hebrew • 🇹🇷 Turkish

<b>✨ Quality Features:</b>
• Multiple sources for better availability
• Automatic format conversion (SRT, VTT, ASS)
• Quality scoring based on downloads
• Smart caching for faster access
• Regular updates from subtitle databases

<b>🔍 Search Tips:</b>
• Use original movie title for better results
• Include release year if available
• Try alternative spellings
• Check multiple language options
"""

    SOURCE_TXT = """
<b>🔗 Source Code Information</b>

<b>🤖 Bot Details:</b>
• Type: Advanced AutoFilter Bot V3 + Subtitles
• Framework: Hydrogram (Pyrogram Fork)
• Language: Python 3.13
• Database: MongoDB with GridFS
• Cache: Redis
• Subtitle APIs: OpenSubtitles & SubDB

<b>📦 Main Components:</b>
• Movie/Series File Management
• Advanced Search & Filtering
• Multi-language Subtitle Support
• User Management System
• Admin Control Panel
• Broadcasting System
• Statistics & Analytics

<b>🎬 Subtitle System:</b>
• 40+ Language Support
• Multiple Format Support
• Quality Scoring System
• Smart Caching Layer
• Fallback API Support
• Automatic Processing

<b>🔧 Technical Stack:</b>
• Python 3.13+
• Hydrogram Library
• MongoDB Atlas
• Redis Cache
• Docker Support
• Heroku Compatible

<b>📝 License:</b>
This project is licensed under GNU General Public License v2.0

<b>👨‍💻 Developer:</b>
Created by: @Iron_voldy
Maintained by: @ImSahanSBot

<b>⚠️ Note:</b>
Source code is private. Contact developer for licensing inquiries.
"""

    SUBTITLE_HELP_TXT = """
<b>📝 Subtitle System Help</b>

<b>🎬 How to Get Subtitles:</b>
1. Search for a movie/series
2. Select the file you want
3. Choose subtitle language
4. Download both movie and subtitle files
5. Keep them in same folder with similar names

<b>📱 Supported Players:</b>
• <b>Mobile:</b> MX Player, VLC, BSPlayer
• <b>PC:</b> VLC, PotPlayer, Media Player Classic
• <b>Smart TV:</b> Kodi, Plex, Emby
• <b>Web:</b> Most HTML5 players

<b>📁 File Naming:</b>
Correct:
• Movie.mp4 + Movie.srt ✅
• Avengers.2019.720p.mkv + Avengers.2019.720p.srt ✅

Incorrect:
• Movie.mp4 + Subtitle.srt ❌
• Film.mkv + Movie.srt ❌

<b>🔧 Troubleshooting:</b>
<b>Subtitles not showing?</b>
• Check file names match
• Enable subtitles in player
• Try different subtitle format
• Update your media player

<b>Wrong timing?</b>
• Download different quality subtitle
• Use subtitle delay adjustment in player
• Try subtitle from different source

<b>Character encoding issues?</b>
• Change subtitle encoding to UTF-8
• Try different language subtitle
• Use player with better encoding support

<b>🌟 Quality Indicators:</b>
🌟 = Excellent (1000+ downloads)
⭐ = Good (100+ downloads)
✨ = Average (10+ downloads)
📝 = Basic quality

<b>💡 Pro Tips:</b>
• Popular movies have better subtitle quality
• Try multiple languages for better options
• English subtitles usually have highest quality
• Download subtitles before movie for faster access
• Keep subtitle files organized in folders

<b>❓ Need Help?</b>
Contact: @Iron_voldy
"""

    MAINTENANCE_TXT = """
<b>🔧 System Under Maintenance</b>

<b>🛠️ Subtitle System Maintenance</b>

We're currently performing maintenance on our subtitle system to improve your experience.

<b>⏰ Estimated Duration:</b> 15-30 minutes

<b>🔄 What's being updated:</b>
• Database optimization
• Cache system refresh  
• API endpoint updates
• Performance improvements
• Bug fixes and enhancements

<b>✅ Available Services:</b>
• Movie/Series search and download
• Basic bot commands
• User management

<b>❌ Temporarily Unavailable:</b>
• Subtitle search and download
• Language selection
• Subtitle statistics

<b>📱 Stay Updated:</b>
Join our channel for real-time updates: @SECL4U

We apologize for any inconvenience. Thank you for your patience!

<b>🔔 Tip:</b> You can still download movies without subtitles during maintenance.
"""