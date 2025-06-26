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


class ChatForbidden(TLObject):  # type: ignore
    """A group to which the user has no access. E.g., because the user was kicked from the group.

    Constructor of :obj:`~hydrogram.raw.base.Chat`.

    Details:
        - Layer: ``181``
        - ID: ``6592A1A7``

    Parameters:
        id (``int`` ``64-bit``):
            User identifier

        title (``str``):
            Group name

    """

    __slots__: List[str] = ["id", "title"]

    ID = 0x6592a1a7
    QUALNAME = "types.ChatForbidden"

    def __init__(self, *, id: int, title: str) -> None:
        self.id = id  # long
        self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatForbidden":
        # No flags
        
        id = Long.read(b)
        
        title = String.read(b)
        
        return ChatForbidden(id=id, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(String(self.title))
        
        return b.getvalue()
