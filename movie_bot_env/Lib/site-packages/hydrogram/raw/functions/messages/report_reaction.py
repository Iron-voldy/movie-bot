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


class ReportReaction(TLObject):  # type: ignore
    """Report a message reaction


    Details:
        - Layer: ``181``
        - ID: ``3F64C076``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Peer where the message was sent

        id (``int`` ``32-bit``):
            Message ID

        reaction_peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Peer that sent the reaction

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "id", "reaction_peer"]

    ID = 0x3f64c076
    QUALNAME = "functions.messages.ReportReaction"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, reaction_peer: "raw.base.InputPeer") -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.reaction_peer = reaction_peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportReaction":
        # No flags
        
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        reaction_peer = TLObject.read(b)
        
        return ReportReaction(peer=peer, id=id, reaction_peer=reaction_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        b.write(self.reaction_peer.write())
        
        return b.getvalue()
