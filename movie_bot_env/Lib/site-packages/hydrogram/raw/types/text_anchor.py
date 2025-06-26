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


class TextAnchor(TLObject):  # type: ignore
    """Text linking to another section of the page

    Constructor of :obj:`~hydrogram.raw.base.RichText`.

    Details:
        - Layer: ``181``
        - ID: ``35553762``

    Parameters:
        text (:obj:`RichText <hydrogram.raw.base.RichText>`):
            Text

        name (``str``):
            Section name

    """

    __slots__: List[str] = ["text", "name"]

    ID = 0x35553762
    QUALNAME = "types.TextAnchor"

    def __init__(self, *, text: "raw.base.RichText", name: str) -> None:
        self.text = text  # RichText
        self.name = name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TextAnchor":
        # No flags
        
        text = TLObject.read(b)
        
        name = String.read(b)
        
        return TextAnchor(text=text, name=name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.text.write())
        
        b.write(String(self.name))
        
        return b.getvalue()
