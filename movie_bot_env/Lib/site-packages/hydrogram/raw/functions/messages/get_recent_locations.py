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


class GetRecentLocations(TLObject):  # type: ignore
    """Get live location history of a certain user


    Details:
        - Layer: ``181``
        - ID: ``702A40E0``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            User

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

    Returns:
        :obj:`messages.Messages <hydrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["peer", "limit", "hash"]

    ID = 0x702a40e0
    QUALNAME = "functions.messages.GetRecentLocations"

    def __init__(self, *, peer: "raw.base.InputPeer", limit: int, hash: int) -> None:
        self.peer = peer  # InputPeer
        self.limit = limit  # int
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetRecentLocations":
        # No flags
        
        peer = TLObject.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetRecentLocations(peer=peer, limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
