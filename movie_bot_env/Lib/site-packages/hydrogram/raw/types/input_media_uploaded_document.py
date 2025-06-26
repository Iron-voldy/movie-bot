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


class InputMediaUploadedDocument(TLObject):  # type: ignore
    """New document

    Constructor of :obj:`~hydrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``181``
        - ID: ``5B38C6C1``

    Parameters:
        file (:obj:`InputFile <hydrogram.raw.base.InputFile>`):
            The uploaded file

        mime_type (``str``):
            MIME type of document

        attributes (List of :obj:`DocumentAttribute <hydrogram.raw.base.DocumentAttribute>`):
            Attributes that specify the type of the document (video, audio, voice, sticker, etc.)

        nosound_video (``bool``, *optional*):
            Whether the specified document is a video file with no audio tracks (a GIF animation (even as MPEG4), for example)

        force_file (``bool``, *optional*):
            Force the media file to be uploaded as document

        spoiler (``bool``, *optional*):
            Whether this media should be hidden behind a spoiler warning

        thumb (:obj:`InputFile <hydrogram.raw.base.InputFile>`, *optional*):
            Thumbnail of the document, uploaded as for the file

        stickers (List of :obj:`InputDocument <hydrogram.raw.base.InputDocument>`, *optional*):
            Attached stickers

        ttl_seconds (``int`` ``32-bit``, *optional*):
            Time to live in seconds of self-destructing document

    """

    __slots__: List[str] = ["file", "mime_type", "attributes", "nosound_video", "force_file", "spoiler", "thumb", "stickers", "ttl_seconds"]

    ID = 0x5b38c6c1
    QUALNAME = "types.InputMediaUploadedDocument"

    def __init__(self, *, file: "raw.base.InputFile", mime_type: str, attributes: List["raw.base.DocumentAttribute"], nosound_video: Optional[bool] = None, force_file: Optional[bool] = None, spoiler: Optional[bool] = None, thumb: "raw.base.InputFile" = None, stickers: Optional[List["raw.base.InputDocument"]] = None, ttl_seconds: Optional[int] = None) -> None:
        self.file = file  # InputFile
        self.mime_type = mime_type  # string
        self.attributes = attributes  # Vector<DocumentAttribute>
        self.nosound_video = nosound_video  # flags.3?true
        self.force_file = force_file  # flags.4?true
        self.spoiler = spoiler  # flags.5?true
        self.thumb = thumb  # flags.2?InputFile
        self.stickers = stickers  # flags.0?Vector<InputDocument>
        self.ttl_seconds = ttl_seconds  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaUploadedDocument":
        
        flags = Int.read(b)
        
        nosound_video = True if flags & (1 << 3) else False
        force_file = True if flags & (1 << 4) else False
        spoiler = True if flags & (1 << 5) else False
        file = TLObject.read(b)
        
        thumb = TLObject.read(b) if flags & (1 << 2) else None
        
        mime_type = String.read(b)
        
        attributes = TLObject.read(b)
        
        stickers = TLObject.read(b) if flags & (1 << 0) else []
        
        ttl_seconds = Int.read(b) if flags & (1 << 1) else None
        return InputMediaUploadedDocument(file=file, mime_type=mime_type, attributes=attributes, nosound_video=nosound_video, force_file=force_file, spoiler=spoiler, thumb=thumb, stickers=stickers, ttl_seconds=ttl_seconds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.nosound_video else 0
        flags |= (1 << 4) if self.force_file else 0
        flags |= (1 << 5) if self.spoiler else 0
        flags |= (1 << 2) if self.thumb is not None else 0
        flags |= (1 << 0) if self.stickers else 0
        flags |= (1 << 1) if self.ttl_seconds is not None else 0
        b.write(Int(flags))
        
        b.write(self.file.write())
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        b.write(String(self.mime_type))
        
        b.write(Vector(self.attributes))
        
        if self.stickers is not None:
            b.write(Vector(self.stickers))
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        return b.getvalue()
