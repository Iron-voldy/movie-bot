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


class ChannelMessages(TLObject):  # type: ignore
    """Channel messages

    Constructor of :obj:`~hydrogram.raw.base.messages.Messages`.

    Details:
        - Layer: ``181``
        - ID: ``C776BA4E``

    Parameters:
        pts (``int`` ``32-bit``):
            Event count after generation

        count (``int`` ``32-bit``):
            Total number of results were found server-side (may not be all included here)

        messages (List of :obj:`Message <hydrogram.raw.base.Message>`):
            Found messages

        topics (List of :obj:`ForumTopic <hydrogram.raw.base.ForumTopic>`):
            Forum topic information

        chats (List of :obj:`Chat <hydrogram.raw.base.Chat>`):
            Chats

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            Users

        inexact (``bool``, *optional*):
            If set, returned results may be inexact

        offset_id_offset (``int`` ``32-bit``, *optional*):
            Indicates the absolute position of messages[0] within the total result set with count count. This is useful, for example, if the result was fetched using offset_id, and we need to display a progress/total counter (like photo 134 of 200, for all media in a chat, we could simply use photo ${offset_id_offset} of ${count}.

    Functions:
        This object can be returned by 15 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetMessages
            messages.GetHistory
            messages.Search
            messages.SearchGlobal
            messages.GetUnreadMentions
            messages.GetRecentLocations
            messages.GetScheduledHistory
            messages.GetScheduledMessages
            messages.GetReplies
            messages.GetUnreadReactions
            messages.SearchSentMedia
            messages.GetSavedHistory
            messages.GetQuickReplyMessages
            channels.GetMessages
            channels.SearchPosts
    """

    __slots__: List[str] = ["pts", "count", "messages", "topics", "chats", "users", "inexact", "offset_id_offset"]

    ID = 0xc776ba4e
    QUALNAME = "types.messages.ChannelMessages"

    def __init__(self, *, pts: int, count: int, messages: List["raw.base.Message"], topics: List["raw.base.ForumTopic"], chats: List["raw.base.Chat"], users: List["raw.base.User"], inexact: Optional[bool] = None, offset_id_offset: Optional[int] = None) -> None:
        self.pts = pts  # int
        self.count = count  # int
        self.messages = messages  # Vector<Message>
        self.topics = topics  # Vector<ForumTopic>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.inexact = inexact  # flags.1?true
        self.offset_id_offset = offset_id_offset  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelMessages":
        
        flags = Int.read(b)
        
        inexact = True if flags & (1 << 1) else False
        pts = Int.read(b)
        
        count = Int.read(b)
        
        offset_id_offset = Int.read(b) if flags & (1 << 2) else None
        messages = TLObject.read(b)
        
        topics = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ChannelMessages(pts=pts, count=count, messages=messages, topics=topics, chats=chats, users=users, inexact=inexact, offset_id_offset=offset_id_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.inexact else 0
        flags |= (1 << 2) if self.offset_id_offset is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.pts))
        
        b.write(Int(self.count))
        
        if self.offset_id_offset is not None:
            b.write(Int(self.offset_id_offset))
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.topics))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
