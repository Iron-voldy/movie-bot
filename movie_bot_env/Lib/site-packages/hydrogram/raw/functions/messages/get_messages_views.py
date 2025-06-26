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


class GetMessagesViews(TLObject):  # type: ignore
    """Get and increase the view counter of a message sent or forwarded from a channel


    Details:
        - Layer: ``181``
        - ID: ``5784D3E1``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Peer where the message was found

        id (List of ``int`` ``32-bit``):
            ID of message

        increment (``bool``):
            Whether to mark the message as viewed and increment the view counter

    Returns:
        :obj:`messages.MessageViews <hydrogram.raw.base.messages.MessageViews>`
    """

    __slots__: List[str] = ["peer", "id", "increment"]

    ID = 0x5784d3e1
    QUALNAME = "functions.messages.GetMessagesViews"

    def __init__(self, *, peer: "raw.base.InputPeer", id: List[int], increment: bool) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # Vector<int>
        self.increment = increment  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessagesViews":
        # No flags
        
        peer = TLObject.read(b)
        
        id = TLObject.read(b, Int)
        
        increment = Bool.read(b)
        
        return GetMessagesViews(peer=peer, id=id, increment=increment)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Vector(self.id, Int))
        
        b.write(Bool(self.increment))
        
        return b.getvalue()
