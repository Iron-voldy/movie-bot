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


class GetStoriesArchive(TLObject):  # type: ignore
    """Fetch the story archive » of a peer we control.


    Details:
        - Layer: ``181``
        - ID: ``B4352016``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Peer whose archived stories should be fetched

        offset_id (``int`` ``32-bit``):
            Offsets for pagination, for more info click here

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

    Returns:
        :obj:`stories.Stories <hydrogram.raw.base.stories.Stories>`
    """

    __slots__: List[str] = ["peer", "offset_id", "limit"]

    ID = 0xb4352016
    QUALNAME = "functions.stories.GetStoriesArchive"

    def __init__(self, *, peer: "raw.base.InputPeer", offset_id: int, limit: int) -> None:
        self.peer = peer  # InputPeer
        self.offset_id = offset_id  # int
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStoriesArchive":
        # No flags
        
        peer = TLObject.read(b)
        
        offset_id = Int.read(b)
        
        limit = Int.read(b)
        
        return GetStoriesArchive(peer=peer, offset_id=offset_id, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
