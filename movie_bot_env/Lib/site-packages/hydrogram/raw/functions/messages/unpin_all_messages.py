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


class UnpinAllMessages(TLObject):  # type: ignore
    """Unpin all pinned messages


    Details:
        - Layer: ``181``
        - ID: ``EE22B9A8``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Chat where to unpin

        top_msg_id (``int`` ``32-bit``, *optional*):
            Forum topic where to unpin

    Returns:
        :obj:`messages.AffectedHistory <hydrogram.raw.base.messages.AffectedHistory>`
    """

    __slots__: List[str] = ["peer", "top_msg_id"]

    ID = 0xee22b9a8
    QUALNAME = "functions.messages.UnpinAllMessages"

    def __init__(self, *, peer: "raw.base.InputPeer", top_msg_id: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.top_msg_id = top_msg_id  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UnpinAllMessages":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        return UnpinAllMessages(peer=peer, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        return b.getvalue()
