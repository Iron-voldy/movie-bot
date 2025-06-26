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


class GetUnreadReactions(TLObject):  # type: ignore
    """Get unread reactions to messages you sent


    Details:
        - Layer: ``181``
        - ID: ``3223495B``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Peer

        offset_id (``int`` ``32-bit``):
            Offsets for pagination, for more info click here

        add_offset (``int`` ``32-bit``):
            Offsets for pagination, for more info click here

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

        max_id (``int`` ``32-bit``):
            Only return reactions for messages up until this message ID

        min_id (``int`` ``32-bit``):
            Only return reactions for messages starting from this message ID

        top_msg_id (``int`` ``32-bit``, *optional*):
            If set, considers only reactions to messages within the specified forum topic

    Returns:
        :obj:`messages.Messages <hydrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["peer", "offset_id", "add_offset", "limit", "max_id", "min_id", "top_msg_id"]

    ID = 0x3223495b
    QUALNAME = "functions.messages.GetUnreadReactions"

    def __init__(self, *, peer: "raw.base.InputPeer", offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int, top_msg_id: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.offset_id = offset_id  # int
        self.add_offset = add_offset  # int
        self.limit = limit  # int
        self.max_id = max_id  # int
        self.min_id = min_id  # int
        self.top_msg_id = top_msg_id  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetUnreadReactions":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        offset_id = Int.read(b)
        
        add_offset = Int.read(b)
        
        limit = Int.read(b)
        
        max_id = Int.read(b)
        
        min_id = Int.read(b)
        
        return GetUnreadReactions(peer=peer, offset_id=offset_id, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.add_offset))
        
        b.write(Int(self.limit))
        
        b.write(Int(self.max_id))
        
        b.write(Int(self.min_id))
        
        return b.getvalue()
