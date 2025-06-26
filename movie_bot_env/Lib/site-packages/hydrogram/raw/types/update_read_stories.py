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


class UpdateReadStories(TLObject):  # type: ignore
    """Stories of a specific peer were marked as read.

    Constructor of :obj:`~hydrogram.raw.base.Update`.

    Details:
        - Layer: ``181``
        - ID: ``F74E932B``

    Parameters:
        peer (:obj:`Peer <hydrogram.raw.base.Peer>`):
            The peer

        max_id (``int`` ``32-bit``):
            ID of the last story that was marked as read

    """

    __slots__: List[str] = ["peer", "max_id"]

    ID = 0xf74e932b
    QUALNAME = "types.UpdateReadStories"

    def __init__(self, *, peer: "raw.base.Peer", max_id: int) -> None:
        self.peer = peer  # Peer
        self.max_id = max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateReadStories":
        # No flags
        
        peer = TLObject.read(b)
        
        max_id = Int.read(b)
        
        return UpdateReadStories(peer=peer, max_id=max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.max_id))
        
        return b.getvalue()
