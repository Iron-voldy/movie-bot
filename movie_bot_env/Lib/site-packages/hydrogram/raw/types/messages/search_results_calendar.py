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


class SearchResultsCalendar(TLObject):  # type: ignore
    """Information about found messages sent on a specific day

    Constructor of :obj:`~hydrogram.raw.base.messages.SearchResultsCalendar`.

    Details:
        - Layer: ``181``
        - ID: ``147EE23C``

    Parameters:
        count (``int`` ``32-bit``):
            Total number of results matching query

        min_date (``int`` ``32-bit``):
            Starting timestamp of attached messages

        min_msg_id (``int`` ``32-bit``):
            Ending timestamp of attached messages

        periods (List of :obj:`SearchResultsCalendarPeriod <hydrogram.raw.base.SearchResultsCalendarPeriod>`):
            Used to split the messages by days: multiple SearchResultsCalendarPeriod constructors are returned, each containing information about the first, last and total number of messages matching the filter that were sent on a specific day.  This information can be easily used to split the returned messages by day.

        messages (List of :obj:`Message <hydrogram.raw.base.Message>`):
            Messages

        chats (List of :obj:`Chat <hydrogram.raw.base.Chat>`):
            Mentioned chats

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            Mentioned users

        inexact (``bool``, *optional*):
            If set, indicates that the results may be inexact

        offset_id_offset (``int`` ``32-bit``, *optional*):
            Indicates the absolute position of messages[0] within the total result set with count count. This is useful, for example, if we need to display a progress/total counter (like photo 134 of 200, for all media in a chat, we could simply use photo ${offset_id_offset} of ${count}.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSearchResultsCalendar
    """

    __slots__: List[str] = ["count", "min_date", "min_msg_id", "periods", "messages", "chats", "users", "inexact", "offset_id_offset"]

    ID = 0x147ee23c
    QUALNAME = "types.messages.SearchResultsCalendar"

    def __init__(self, *, count: int, min_date: int, min_msg_id: int, periods: List["raw.base.SearchResultsCalendarPeriod"], messages: List["raw.base.Message"], chats: List["raw.base.Chat"], users: List["raw.base.User"], inexact: Optional[bool] = None, offset_id_offset: Optional[int] = None) -> None:
        self.count = count  # int
        self.min_date = min_date  # int
        self.min_msg_id = min_msg_id  # int
        self.periods = periods  # Vector<SearchResultsCalendarPeriod>
        self.messages = messages  # Vector<Message>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.inexact = inexact  # flags.0?true
        self.offset_id_offset = offset_id_offset  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchResultsCalendar":
        
        flags = Int.read(b)
        
        inexact = True if flags & (1 << 0) else False
        count = Int.read(b)
        
        min_date = Int.read(b)
        
        min_msg_id = Int.read(b)
        
        offset_id_offset = Int.read(b) if flags & (1 << 1) else None
        periods = TLObject.read(b)
        
        messages = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return SearchResultsCalendar(count=count, min_date=min_date, min_msg_id=min_msg_id, periods=periods, messages=messages, chats=chats, users=users, inexact=inexact, offset_id_offset=offset_id_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.inexact else 0
        flags |= (1 << 1) if self.offset_id_offset is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Int(self.min_date))
        
        b.write(Int(self.min_msg_id))
        
        if self.offset_id_offset is not None:
            b.write(Int(self.offset_id_offset))
        
        b.write(Vector(self.periods))
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
