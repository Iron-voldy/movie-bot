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


class GetSearchResultsPositions(TLObject):  # type: ignore
    """Returns sparse positions of messages of the specified type in the chat to be used for shared media scroll implementation.


    Details:
        - Layer: ``181``
        - ID: ``9C7F2F10``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Peer where to search

        filter (:obj:`MessagesFilter <hydrogram.raw.base.MessagesFilter>`):
            Message filter, inputMessagesFilterEmpty, inputMessagesFilterMyMentions filters are not supported by this method.

        offset_id (``int`` ``32-bit``):
            Offsets for pagination, for more info click here

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

        saved_peer_id (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`, *optional*):
            Search within the saved message dialog » with this ID.

    Returns:
        :obj:`messages.SearchResultsPositions <hydrogram.raw.base.messages.SearchResultsPositions>`
    """

    __slots__: List[str] = ["peer", "filter", "offset_id", "limit", "saved_peer_id"]

    ID = 0x9c7f2f10
    QUALNAME = "functions.messages.GetSearchResultsPositions"

    def __init__(self, *, peer: "raw.base.InputPeer", filter: "raw.base.MessagesFilter", offset_id: int, limit: int, saved_peer_id: "raw.base.InputPeer" = None) -> None:
        self.peer = peer  # InputPeer
        self.filter = filter  # MessagesFilter
        self.offset_id = offset_id  # int
        self.limit = limit  # int
        self.saved_peer_id = saved_peer_id  # flags.2?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSearchResultsPositions":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        saved_peer_id = TLObject.read(b) if flags & (1 << 2) else None
        
        filter = TLObject.read(b)
        
        offset_id = Int.read(b)
        
        limit = Int.read(b)
        
        return GetSearchResultsPositions(peer=peer, filter=filter, offset_id=offset_id, limit=limit, saved_peer_id=saved_peer_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.saved_peer_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.saved_peer_id is not None:
            b.write(self.saved_peer_id.write())
        
        b.write(self.filter.write())
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
