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


class GetLeftChannels(TLObject):  # type: ignore
    """Get a list of channels/supergroups we left, requires a takeout session, see here » for more info.


    Details:
        - Layer: ``181``
        - ID: ``8341ECC0``

    Parameters:
        offset (``int`` ``32-bit``):
            Offset for pagination

    Returns:
        :obj:`messages.Chats <hydrogram.raw.base.messages.Chats>`
    """

    __slots__: List[str] = ["offset"]

    ID = 0x8341ecc0
    QUALNAME = "functions.channels.GetLeftChannels"

    def __init__(self, *, offset: int) -> None:
        self.offset = offset  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetLeftChannels":
        # No flags
        
        offset = Int.read(b)
        
        return GetLeftChannels(offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.offset))
        
        return b.getvalue()
