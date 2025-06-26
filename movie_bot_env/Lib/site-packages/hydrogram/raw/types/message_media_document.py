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


class MessageMediaDocument(TLObject):  # type: ignore
    """Document (video, audio, voice, sticker, any media type except photo)

    Constructor of :obj:`~hydrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``181``
        - ID: ``4CF4D72D``

    Parameters:
        nopremium (``bool``, *optional*):
            Whether this is a normal sticker, if not set this is a premium sticker and a premium sticker animation must be played.

        spoiler (``bool``, *optional*):
            Whether this media should be hidden behind a spoiler warning

        video (``bool``, *optional*):
            Whether this is a video.

        round (``bool``, *optional*):
            Whether this is a round video.

        voice (``bool``, *optional*):
            Whether this is a voice message.

        document (:obj:`Document <hydrogram.raw.base.Document>`, *optional*):
            Attached document

        alt_document (:obj:`Document <hydrogram.raw.base.Document>`, *optional*):
            Currently only used for story videos, may contain an alternative version of the story video, explicitly encoded using H.264 (in MPEG4 transport) at a lower resolution than document.

        ttl_seconds (``int`` ``32-bit``, *optional*):
            Time to live of self-destructing document

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetWebPagePreview
            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["nopremium", "spoiler", "video", "round", "voice", "document", "alt_document", "ttl_seconds"]

    ID = 0x4cf4d72d
    QUALNAME = "types.MessageMediaDocument"

    def __init__(self, *, nopremium: Optional[bool] = None, spoiler: Optional[bool] = None, video: Optional[bool] = None, round: Optional[bool] = None, voice: Optional[bool] = None, document: "raw.base.Document" = None, alt_document: "raw.base.Document" = None, ttl_seconds: Optional[int] = None) -> None:
        self.nopremium = nopremium  # flags.3?true
        self.spoiler = spoiler  # flags.4?true
        self.video = video  # flags.6?true
        self.round = round  # flags.7?true
        self.voice = voice  # flags.8?true
        self.document = document  # flags.0?Document
        self.alt_document = alt_document  # flags.5?Document
        self.ttl_seconds = ttl_seconds  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaDocument":
        
        flags = Int.read(b)
        
        nopremium = True if flags & (1 << 3) else False
        spoiler = True if flags & (1 << 4) else False
        video = True if flags & (1 << 6) else False
        round = True if flags & (1 << 7) else False
        voice = True if flags & (1 << 8) else False
        document = TLObject.read(b) if flags & (1 << 0) else None
        
        alt_document = TLObject.read(b) if flags & (1 << 5) else None
        
        ttl_seconds = Int.read(b) if flags & (1 << 2) else None
        return MessageMediaDocument(nopremium=nopremium, spoiler=spoiler, video=video, round=round, voice=voice, document=document, alt_document=alt_document, ttl_seconds=ttl_seconds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.nopremium else 0
        flags |= (1 << 4) if self.spoiler else 0
        flags |= (1 << 6) if self.video else 0
        flags |= (1 << 7) if self.round else 0
        flags |= (1 << 8) if self.voice else 0
        flags |= (1 << 0) if self.document is not None else 0
        flags |= (1 << 5) if self.alt_document is not None else 0
        flags |= (1 << 2) if self.ttl_seconds is not None else 0
        b.write(Int(flags))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.alt_document is not None:
            b.write(self.alt_document.write())
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        return b.getvalue()
