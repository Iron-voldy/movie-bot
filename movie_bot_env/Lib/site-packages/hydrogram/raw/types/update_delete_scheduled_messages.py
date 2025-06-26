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


class UpdateDeleteScheduledMessages(TLObject):  # type: ignore
    """Some scheduled messages were deleted from the schedule queue of a chat

    Constructor of :obj:`~hydrogram.raw.base.Update`.

    Details:
        - Layer: ``181``
        - ID: ``90866CEE``

    Parameters:
        peer (:obj:`Peer <hydrogram.raw.base.Peer>`):
            Peer

        messages (List of ``int`` ``32-bit``):
            Deleted scheduled messages

    """

    __slots__: List[str] = ["peer", "messages"]

    ID = 0x90866cee
    QUALNAME = "types.UpdateDeleteScheduledMessages"

    def __init__(self, *, peer: "raw.base.Peer", messages: List[int]) -> None:
        self.peer = peer  # Peer
        self.messages = messages  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDeleteScheduledMessages":
        # No flags
        
        peer = TLObject.read(b)
        
        messages = TLObject.read(b, Int)
        
        return UpdateDeleteScheduledMessages(peer=peer, messages=messages)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Vector(self.messages, Int))
        
        return b.getvalue()
