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


class MessageEntityTextUrl(TLObject):  # type: ignore
    """Message entity representing a text url: for in-text urls like https://google.com use messageEntityUrl.

    Constructor of :obj:`~hydrogram.raw.base.MessageEntity`.

    Details:
        - Layer: ``181``
        - ID: ``76A6D327``

    Parameters:
        offset (``int`` ``32-bit``):
            Offset of message entity within message (in UTF-16 code units)

        length (``int`` ``32-bit``):
            Length of message entity within message (in UTF-16 code units)

        url (``str``):
            The actual URL

    """

    __slots__: List[str] = ["offset", "length", "url"]

    ID = 0x76a6d327
    QUALNAME = "types.MessageEntityTextUrl"

    def __init__(self, *, offset: int, length: int, url: str) -> None:
        self.offset = offset  # int
        self.length = length  # int
        self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityTextUrl":
        # No flags
        
        offset = Int.read(b)
        
        length = Int.read(b)
        
        url = String.read(b)
        
        return MessageEntityTextUrl(offset=offset, length=length, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        b.write(String(self.url))
        
        return b.getvalue()
