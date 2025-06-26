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


class BusinessIntro(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.BusinessIntro`.

    Details:
        - Layer: ``181``
        - ID: ``5A0A066D``

    Parameters:
        title (``str``):
            

        description (``str``):
            

        sticker (:obj:`Document <hydrogram.raw.base.Document>`, *optional*):
            

    """

    __slots__: List[str] = ["title", "description", "sticker"]

    ID = 0x5a0a066d
    QUALNAME = "types.BusinessIntro"

    def __init__(self, *, title: str, description: str, sticker: "raw.base.Document" = None) -> None:
        self.title = title  # string
        self.description = description  # string
        self.sticker = sticker  # flags.0?Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BusinessIntro":
        
        flags = Int.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        sticker = TLObject.read(b) if flags & (1 << 0) else None
        
        return BusinessIntro(title=title, description=description, sticker=sticker)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.sticker is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.sticker is not None:
            b.write(self.sticker.write())
        
        return b.getvalue()
