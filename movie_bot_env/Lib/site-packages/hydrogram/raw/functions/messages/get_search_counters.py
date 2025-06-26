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


class GetSearchCounters(TLObject):  # type: ignore
    """Get the number of results that would be found by a messages.search call with the same parameters


    Details:
        - Layer: ``181``
        - ID: ``1BBCF300``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Peer where to search

        filters (List of :obj:`MessagesFilter <hydrogram.raw.base.MessagesFilter>`):
            Search filters

        saved_peer_id (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`, *optional*):
            Search within the saved message dialog » with this ID.

        top_msg_id (``int`` ``32-bit``, *optional*):
            If set, consider only messages within the specified forum topic

    Returns:
        List of :obj:`messages.SearchCounter <hydrogram.raw.base.messages.SearchCounter>`
    """

    __slots__: List[str] = ["peer", "filters", "saved_peer_id", "top_msg_id"]

    ID = 0x1bbcf300
    QUALNAME = "functions.messages.GetSearchCounters"

    def __init__(self, *, peer: "raw.base.InputPeer", filters: List["raw.base.MessagesFilter"], saved_peer_id: "raw.base.InputPeer" = None, top_msg_id: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.filters = filters  # Vector<MessagesFilter>
        self.saved_peer_id = saved_peer_id  # flags.2?InputPeer
        self.top_msg_id = top_msg_id  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSearchCounters":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        saved_peer_id = TLObject.read(b) if flags & (1 << 2) else None
        
        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        filters = TLObject.read(b)
        
        return GetSearchCounters(peer=peer, filters=filters, saved_peer_id=saved_peer_id, top_msg_id=top_msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.saved_peer_id is not None else 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.saved_peer_id is not None:
            b.write(self.saved_peer_id.write())
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        b.write(Vector(self.filters))
        
        return b.getvalue()
