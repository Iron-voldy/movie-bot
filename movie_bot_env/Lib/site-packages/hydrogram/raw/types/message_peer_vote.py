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


class MessagePeerVote(TLObject):  # type: ignore
    """How a peer voted in a poll

    Constructor of :obj:`~hydrogram.raw.base.MessagePeerVote`.

    Details:
        - Layer: ``181``
        - ID: ``B6CC2D5C``

    Parameters:
        peer (:obj:`Peer <hydrogram.raw.base.Peer>`):
            Peer ID

        option (``bytes``):
            The option chosen by the peer

        date (``int`` ``32-bit``):
            When did the peer cast the vote

    """

    __slots__: List[str] = ["peer", "option", "date"]

    ID = 0xb6cc2d5c
    QUALNAME = "types.MessagePeerVote"

    def __init__(self, *, peer: "raw.base.Peer", option: bytes, date: int) -> None:
        self.peer = peer  # Peer
        self.option = option  # bytes
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessagePeerVote":
        # No flags
        
        peer = TLObject.read(b)
        
        option = Bytes.read(b)
        
        date = Int.read(b)
        
        return MessagePeerVote(peer=peer, option=option, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Bytes(self.option))
        
        b.write(Int(self.date))
        
        return b.getvalue()
