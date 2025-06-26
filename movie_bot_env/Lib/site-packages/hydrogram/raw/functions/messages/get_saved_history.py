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


class GetSavedHistory(TLObject):  # type: ignore
    """Returns saved messages » forwarded from a specific peer


    Details:
        - Layer: ``181``
        - ID: ``3D9A414D``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Target peer

        offset_id (``int`` ``32-bit``):
            Only return messages starting from the specified message ID

        offset_date (``int`` ``32-bit``):
            Only return messages sent before the specified date

        add_offset (``int`` ``32-bit``):
            Number of list elements to be skipped, negative values are also accepted.

        limit (``int`` ``32-bit``):
            Number of results to return

        max_id (``int`` ``32-bit``):
            If a positive value was transferred, the method will return only messages with IDs less than max_id

        min_id (``int`` ``32-bit``):
            If a positive value was transferred, the method will return only messages with IDs more than min_id

        hash (``int`` ``64-bit``):
            Result hash

    Returns:
        :obj:`messages.Messages <hydrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["peer", "offset_id", "offset_date", "add_offset", "limit", "max_id", "min_id", "hash"]

    ID = 0x3d9a414d
    QUALNAME = "functions.messages.GetSavedHistory"

    def __init__(self, *, peer: "raw.base.InputPeer", offset_id: int, offset_date: int, add_offset: int, limit: int, max_id: int, min_id: int, hash: int) -> None:
        self.peer = peer  # InputPeer
        self.offset_id = offset_id  # int
        self.offset_date = offset_date  # int
        self.add_offset = add_offset  # int
        self.limit = limit  # int
        self.max_id = max_id  # int
        self.min_id = min_id  # int
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSavedHistory":
        # No flags
        
        peer = TLObject.read(b)
        
        offset_id = Int.read(b)
        
        offset_date = Int.read(b)
        
        add_offset = Int.read(b)
        
        limit = Int.read(b)
        
        max_id = Int.read(b)
        
        min_id = Int.read(b)
        
        hash = Long.read(b)
        
        return GetSavedHistory(peer=peer, offset_id=offset_id, offset_date=offset_date, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.offset_date))
        
        b.write(Int(self.add_offset))
        
        b.write(Int(self.limit))
        
        b.write(Int(self.max_id))
        
        b.write(Int(self.min_id))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
