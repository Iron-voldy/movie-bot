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


class TopPeer(TLObject):  # type: ignore
    """Top peer

    Constructor of :obj:`~hydrogram.raw.base.TopPeer`.

    Details:
        - Layer: ``181``
        - ID: ``EDCDC05B``

    Parameters:
        peer (:obj:`Peer <hydrogram.raw.base.Peer>`):
            Peer

        rating (``float`` ``64-bit``):
            Rating as computed in top peer rating »

    """

    __slots__: List[str] = ["peer", "rating"]

    ID = 0xedcdc05b
    QUALNAME = "types.TopPeer"

    def __init__(self, *, peer: "raw.base.Peer", rating: float) -> None:
        self.peer = peer  # Peer
        self.rating = rating  # double

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TopPeer":
        # No flags
        
        peer = TLObject.read(b)
        
        rating = Double.read(b)
        
        return TopPeer(peer=peer, rating=rating)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Double(self.rating))
        
        return b.getvalue()
