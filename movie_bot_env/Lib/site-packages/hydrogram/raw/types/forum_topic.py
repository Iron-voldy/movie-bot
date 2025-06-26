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


class ForumTopic(TLObject):  # type: ignore
    """Represents a forum topic.

    Constructor of :obj:`~hydrogram.raw.base.ForumTopic`.

    Details:
        - Layer: ``181``
        - ID: ``71701DA9``

    Parameters:
        id (``int`` ``32-bit``):
            Topic ID

        date (``int`` ``32-bit``):
            Topic creation date

        title (``str``):
            Topic title

        icon_color (``int`` ``32-bit``):
            If no custom emoji icon is specified, specifies the color of the fallback topic icon (RGB), one of 0x6FB9F0, 0xFFD67E, 0xCB86DB, 0x8EEE98, 0xFF93B2, or 0xFB6F5F.

        top_message (``int`` ``32-bit``):
            ID of the last message that was sent to this topic

        read_inbox_max_id (``int`` ``32-bit``):
            Position up to which all incoming messages are read.

        read_outbox_max_id (``int`` ``32-bit``):
            Position up to which all outgoing messages are read.

        unread_count (``int`` ``32-bit``):
            Number of unread messages

        unread_mentions_count (``int`` ``32-bit``):
            Number of unread mentions

        unread_reactions_count (``int`` ``32-bit``):
            Number of unread reactions to messages you sent

        from_id (:obj:`Peer <hydrogram.raw.base.Peer>`):
            ID of the peer that created the topic

        notify_settings (:obj:`PeerNotifySettings <hydrogram.raw.base.PeerNotifySettings>`):
            Notification settings

        my (``bool``, *optional*):
            Whether the topic was created by the current user

        closed (``bool``, *optional*):
            Whether the topic is closed (no messages can be sent to it)

        pinned (``bool``, *optional*):
            Whether the topic is pinned

        short (``bool``, *optional*):
            Whether this constructor is a reduced version of the full topic information. If set, only the my, closed, id, date, title, icon_color, icon_emoji_id and from_id parameters will contain valid information. Reduced info is usually only returned in topic-related admin log events » and in the messages.channelMessages constructor: if needed, full information can be fetched using channels.getForumTopicsByID.

        hidden (``bool``, *optional*):
            Whether the topic is hidden (only valid for the "General" topic, id=1)

        icon_emoji_id (``int`` ``64-bit``, *optional*):
            ID of the custom emoji used as topic icon.

        draft (:obj:`DraftMessage <hydrogram.raw.base.DraftMessage>`, *optional*):
            Message draft

    """

    __slots__: List[str] = ["id", "date", "title", "icon_color", "top_message", "read_inbox_max_id", "read_outbox_max_id", "unread_count", "unread_mentions_count", "unread_reactions_count", "from_id", "notify_settings", "my", "closed", "pinned", "short", "hidden", "icon_emoji_id", "draft"]

    ID = 0x71701da9
    QUALNAME = "types.ForumTopic"

    def __init__(self, *, id: int, date: int, title: str, icon_color: int, top_message: int, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, unread_mentions_count: int, unread_reactions_count: int, from_id: "raw.base.Peer", notify_settings: "raw.base.PeerNotifySettings", my: Optional[bool] = None, closed: Optional[bool] = None, pinned: Optional[bool] = None, short: Optional[bool] = None, hidden: Optional[bool] = None, icon_emoji_id: Optional[int] = None, draft: "raw.base.DraftMessage" = None) -> None:
        self.id = id  # int
        self.date = date  # int
        self.title = title  # string
        self.icon_color = icon_color  # int
        self.top_message = top_message  # int
        self.read_inbox_max_id = read_inbox_max_id  # int
        self.read_outbox_max_id = read_outbox_max_id  # int
        self.unread_count = unread_count  # int
        self.unread_mentions_count = unread_mentions_count  # int
        self.unread_reactions_count = unread_reactions_count  # int
        self.from_id = from_id  # Peer
        self.notify_settings = notify_settings  # PeerNotifySettings
        self.my = my  # flags.1?true
        self.closed = closed  # flags.2?true
        self.pinned = pinned  # flags.3?true
        self.short = short  # flags.5?true
        self.hidden = hidden  # flags.6?true
        self.icon_emoji_id = icon_emoji_id  # flags.0?long
        self.draft = draft  # flags.4?DraftMessage

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ForumTopic":
        
        flags = Int.read(b)
        
        my = True if flags & (1 << 1) else False
        closed = True if flags & (1 << 2) else False
        pinned = True if flags & (1 << 3) else False
        short = True if flags & (1 << 5) else False
        hidden = True if flags & (1 << 6) else False
        id = Int.read(b)
        
        date = Int.read(b)
        
        title = String.read(b)
        
        icon_color = Int.read(b)
        
        icon_emoji_id = Long.read(b) if flags & (1 << 0) else None
        top_message = Int.read(b)
        
        read_inbox_max_id = Int.read(b)
        
        read_outbox_max_id = Int.read(b)
        
        unread_count = Int.read(b)
        
        unread_mentions_count = Int.read(b)
        
        unread_reactions_count = Int.read(b)
        
        from_id = TLObject.read(b)
        
        notify_settings = TLObject.read(b)
        
        draft = TLObject.read(b) if flags & (1 << 4) else None
        
        return ForumTopic(id=id, date=date, title=title, icon_color=icon_color, top_message=top_message, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, unread_mentions_count=unread_mentions_count, unread_reactions_count=unread_reactions_count, from_id=from_id, notify_settings=notify_settings, my=my, closed=closed, pinned=pinned, short=short, hidden=hidden, icon_emoji_id=icon_emoji_id, draft=draft)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.my else 0
        flags |= (1 << 2) if self.closed else 0
        flags |= (1 << 3) if self.pinned else 0
        flags |= (1 << 5) if self.short else 0
        flags |= (1 << 6) if self.hidden else 0
        flags |= (1 << 0) if self.icon_emoji_id is not None else 0
        flags |= (1 << 4) if self.draft is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(Int(self.date))
        
        b.write(String(self.title))
        
        b.write(Int(self.icon_color))
        
        if self.icon_emoji_id is not None:
            b.write(Long(self.icon_emoji_id))
        
        b.write(Int(self.top_message))
        
        b.write(Int(self.read_inbox_max_id))
        
        b.write(Int(self.read_outbox_max_id))
        
        b.write(Int(self.unread_count))
        
        b.write(Int(self.unread_mentions_count))
        
        b.write(Int(self.unread_reactions_count))
        
        b.write(self.from_id.write())
        
        b.write(self.notify_settings.write())
        
        if self.draft is not None:
            b.write(self.draft.write())
        
        return b.getvalue()
