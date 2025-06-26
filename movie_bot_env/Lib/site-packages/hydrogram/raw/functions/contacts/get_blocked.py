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


class GetBlocked(TLObject):  # type: ignore
    """Returns the list of blocked users.


    Details:
        - Layer: ``181``
        - ID: ``9A868F80``

    Parameters:
        offset (``int`` ``32-bit``):
            The number of list elements to be skipped

        limit (``int`` ``32-bit``):
            The number of list elements to be returned

        my_stories_from (``bool``, *optional*):
            Whether to fetch the story blocklist; if not set, will fetch the main blocklist. See here » for differences between the two.

    Returns:
        :obj:`contacts.Blocked <hydrogram.raw.base.contacts.Blocked>`
    """

    __slots__: List[str] = ["offset", "limit", "my_stories_from"]

    ID = 0x9a868f80
    QUALNAME = "functions.contacts.GetBlocked"

    def __init__(self, *, offset: int, limit: int, my_stories_from: Optional[bool] = None) -> None:
        self.offset = offset  # int
        self.limit = limit  # int
        self.my_stories_from = my_stories_from  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBlocked":
        
        flags = Int.read(b)
        
        my_stories_from = True if flags & (1 << 0) else False
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        return GetBlocked(offset=offset, limit=limit, my_stories_from=my_stories_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.my_stories_from else 0
        b.write(Int(flags))
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
