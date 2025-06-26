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


class EmojiKeyword(TLObject):  # type: ignore
    """Emoji keyword

    Constructor of :obj:`~hydrogram.raw.base.EmojiKeyword`.

    Details:
        - Layer: ``181``
        - ID: ``D5B3B9F9``

    Parameters:
        keyword (``str``):
            Keyword

        emoticons (List of ``str``):
            Emojis associated to keyword

    """

    __slots__: List[str] = ["keyword", "emoticons"]

    ID = 0xd5b3b9f9
    QUALNAME = "types.EmojiKeyword"

    def __init__(self, *, keyword: str, emoticons: List[str]) -> None:
        self.keyword = keyword  # string
        self.emoticons = emoticons  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiKeyword":
        # No flags
        
        keyword = String.read(b)
        
        emoticons = TLObject.read(b, String)
        
        return EmojiKeyword(keyword=keyword, emoticons=emoticons)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.keyword))
        
        b.write(Vector(self.emoticons, String))
        
        return b.getvalue()
