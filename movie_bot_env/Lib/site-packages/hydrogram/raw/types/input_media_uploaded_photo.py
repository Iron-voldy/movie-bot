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


class InputMediaUploadedPhoto(TLObject):  # type: ignore
    """Photo

    Constructor of :obj:`~hydrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``181``
        - ID: ``1E287D04``

    Parameters:
        file (:obj:`InputFile <hydrogram.raw.base.InputFile>`):
            The uploaded file

        spoiler (``bool``, *optional*):
            Whether this media should be hidden behind a spoiler warning

        stickers (List of :obj:`InputDocument <hydrogram.raw.base.InputDocument>`, *optional*):
            Attached mask stickers

        ttl_seconds (``int`` ``32-bit``, *optional*):
            Time to live in seconds of self-destructing photo

    """

    __slots__: List[str] = ["file", "spoiler", "stickers", "ttl_seconds"]

    ID = 0x1e287d04
    QUALNAME = "types.InputMediaUploadedPhoto"

    def __init__(self, *, file: "raw.base.InputFile", spoiler: Optional[bool] = None, stickers: Optional[List["raw.base.InputDocument"]] = None, ttl_seconds: Optional[int] = None) -> None:
        self.file = file  # InputFile
        self.spoiler = spoiler  # flags.2?true
        self.stickers = stickers  # flags.0?Vector<InputDocument>
        self.ttl_seconds = ttl_seconds  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaUploadedPhoto":
        
        flags = Int.read(b)
        
        spoiler = True if flags & (1 << 2) else False
        file = TLObject.read(b)
        
        stickers = TLObject.read(b) if flags & (1 << 0) else []
        
        ttl_seconds = Int.read(b) if flags & (1 << 1) else None
        return InputMediaUploadedPhoto(file=file, spoiler=spoiler, stickers=stickers, ttl_seconds=ttl_seconds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.spoiler else 0
        flags |= (1 << 0) if self.stickers else 0
        flags |= (1 << 1) if self.ttl_seconds is not None else 0
        b.write(Int(flags))
        
        b.write(self.file.write())
        
        if self.stickers is not None:
            b.write(Vector(self.stickers))
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        return b.getvalue()
