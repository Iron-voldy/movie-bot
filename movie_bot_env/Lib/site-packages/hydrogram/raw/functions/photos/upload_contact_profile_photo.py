#  Hydrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2023-present Hydrogram <https://hydrogram.org>
#
#  This file is part of Hydrogram.
#
#  Hydrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Hydrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Hydrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from hydrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hydrogram.raw.core import TLObject
from hydrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class UploadContactProfilePhoto(TLObject):  # type: ignore
    """Upload a custom profile picture for a contact, or suggest a new profile picture to a contact.


    Details:
        - Layer: ``181``
        - ID: ``E14C4A71``

    Parameters:
        user_id (:obj:`InputUser <hydrogram.raw.base.InputUser>`):
            The contact

        suggest (``bool``, *optional*):
            If set, will send a messageActionSuggestProfilePhoto service message to user_id, suggesting them to use the specified profile picture; otherwise, will set a personal profile picture for the user (only visible to the current user).

        save (``bool``, *optional*):
            If set, removes a previously set personal profile picture (does not affect suggested profile pictures, to remove them simply deleted the messageActionSuggestProfilePhoto service message with messages.deleteMessages).

        file (:obj:`InputFile <hydrogram.raw.base.InputFile>`, *optional*):
            Profile photo

        video (:obj:`InputFile <hydrogram.raw.base.InputFile>`, *optional*):
            Animated profile picture video

        video_start_ts (``float`` ``64-bit``, *optional*):
            Floating point UNIX timestamp in seconds, indicating the frame of the video/sticker that should be used as static preview; can only be used if video or video_emoji_markup is set.

        video_emoji_markup (:obj:`VideoSize <hydrogram.raw.base.VideoSize>`, *optional*):
            Animated sticker profile picture, must contain either a videoSizeEmojiMarkup or a videoSizeStickerMarkup constructor.

    Returns:
        :obj:`photos.Photo <hydrogram.raw.base.photos.Photo>`
    """

    __slots__: List[str] = ["user_id", "suggest", "save", "file", "video", "video_start_ts", "video_emoji_markup"]

    ID = 0xe14c4a71
    QUALNAME = "functions.photos.UploadContactProfilePhoto"

    def __init__(self, *, user_id: "raw.base.InputUser", suggest: Optional[bool] = None, save: Optional[bool] = None, file: "raw.base.InputFile" = None, video: "raw.base.InputFile" = None, video_start_ts: Optional[float] = None, video_emoji_markup: "raw.base.VideoSize" = None) -> None:
        self.user_id = user_id  # InputUser
        self.suggest = suggest  # flags.3?true
        self.save = save  # flags.4?true
        self.file = file  # flags.0?InputFile
        self.video = video  # flags.1?InputFile
        self.video_start_ts = video_start_ts  # flags.2?double
        self.video_emoji_markup = video_emoji_markup  # flags.5?VideoSize

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadContactProfilePhoto":
        
        flags = Int.read(b)
        
        suggest = True if flags & (1 << 3) else False
        save = True if flags & (1 << 4) else False
        user_id = TLObject.read(b)
        
        file = TLObject.read(b) if flags & (1 << 0) else None
        
        video = TLObject.read(b) if flags & (1 << 1) else None
        
        video_start_ts = Double.read(b) if flags & (1 << 2) else None
        video_emoji_markup = TLObject.read(b) if flags & (1 << 5) else None
        
        return UploadContactProfilePhoto(user_id=user_id, suggest=suggest, save=save, file=file, video=video, video_start_ts=video_start_ts, video_emoji_markup=video_emoji_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.suggest else 0
        flags |= (1 << 4) if self.save else 0
        flags |= (1 << 0) if self.file is not None else 0
        flags |= (1 << 1) if self.video is not None else 0
        flags |= (1 << 2) if self.video_start_ts is not None else 0
        flags |= (1 << 5) if self.video_emoji_markup is not None else 0
        b.write(Int(flags))
        
        b.write(self.user_id.write())
        
        if self.file is not None:
            b.write(self.file.write())
        
        if self.video is not None:
            b.write(self.video.write())
        
        if self.video_start_ts is not None:
            b.write(Double(self.video_start_ts))
        
        if self.video_emoji_markup is not None:
            b.write(self.video_emoji_markup.write())
        
        return b.getvalue()
