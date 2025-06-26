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


class GetSearchResultsCalendar(TLObject):  # type: ignore
    """Returns information about the next messages of the specified type in the chat split by days.


    Details:
        - Layer: ``181``
        - ID: ``6AA3F6BD``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Peer where to search

        filter (:obj:`MessagesFilter <hydrogram.raw.base.MessagesFilter>`):
            Message filter, inputMessagesFilterEmpty, inputMessagesFilterMyMentions filters are not supported by this method.

        offset_id (``int`` ``32-bit``):
            Offsets for pagination, for more info click here

        offset_date (``int`` ``32-bit``):
            Offsets for pagination, for more info click here

        saved_peer_id (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`, *optional*):
            Search within the saved message dialog » with this ID.

    Returns:
        :obj:`messages.SearchResultsCalendar <hydrogram.raw.base.messages.SearchResultsCalendar>`
    """

    __slots__: List[str] = ["peer", "filter", "offset_id", "offset_date", "saved_peer_id"]

    ID = 0x6aa3f6bd
    QUALNAME = "functions.messages.GetSearchResultsCalendar"

    def __init__(self, *, peer: "raw.base.InputPeer", filter: "raw.base.MessagesFilter", offset_id: int, offset_date: int, saved_peer_id: "raw.base.InputPeer" = None) -> None:
        self.peer = peer  # InputPeer
        self.filter = filter  # MessagesFilter
        self.offset_id = offset_id  # int
        self.offset_date = offset_date  # int
        self.saved_peer_id = saved_peer_id  # flags.2?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSearchResultsCalendar":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        saved_peer_id = TLObject.read(b) if flags & (1 << 2) else None
        
        filter = TLObject.read(b)
        
        offset_id = Int.read(b)
        
        offset_date = Int.read(b)
        
        return GetSearchResultsCalendar(peer=peer, filter=filter, offset_id=offset_id, offset_date=offset_date, saved_peer_id=saved_peer_id)

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
        
        b.write(Int(self.offset_date))
        
        return b.getvalue()
