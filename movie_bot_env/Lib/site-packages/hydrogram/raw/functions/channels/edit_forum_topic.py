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


class EditForumTopic(TLObject):  # type: ignore
    """Edit forum topic; requires manage_topics rights.


    Details:
        - Layer: ``181``
        - ID: ``F4DFA185``

    Parameters:
        channel (:obj:`InputChannel <hydrogram.raw.base.InputChannel>`):
            Supergroup

        topic_id (``int`` ``32-bit``):
            Topic ID

        title (``str``, *optional*):
            If present, will update the topic title (maximum UTF-8 length: 128).

        icon_emoji_id (``int`` ``64-bit``, *optional*):
            If present, updates the custom emoji used as topic icon. Telegram Premium users can use any custom emoji, other users can only use the custom emojis contained in the inputStickerSetEmojiDefaultTopicIcons emoji pack. Pass 0 to switch to the fallback topic icon.

        closed (``bool``, *optional*):
            If present, will update the open/closed status of the topic.

        hidden (``bool``, *optional*):
            If present, will hide/unhide the topic (only valid for the "General" topic, id=1).

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "topic_id", "title", "icon_emoji_id", "closed", "hidden"]

    ID = 0xf4dfa185
    QUALNAME = "functions.channels.EditForumTopic"

    def __init__(self, *, channel: "raw.base.InputChannel", topic_id: int, title: Optional[str] = None, icon_emoji_id: Optional[int] = None, closed: Optional[bool] = None, hidden: Optional[bool] = None) -> None:
        self.channel = channel  # InputChannel
        self.topic_id = topic_id  # int
        self.title = title  # flags.0?string
        self.icon_emoji_id = icon_emoji_id  # flags.1?long
        self.closed = closed  # flags.2?Bool
        self.hidden = hidden  # flags.3?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditForumTopic":
        
        flags = Int.read(b)
        
        channel = TLObject.read(b)
        
        topic_id = Int.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        icon_emoji_id = Long.read(b) if flags & (1 << 1) else None
        closed = Bool.read(b) if flags & (1 << 2) else None
        hidden = Bool.read(b) if flags & (1 << 3) else None
        return EditForumTopic(channel=channel, topic_id=topic_id, title=title, icon_emoji_id=icon_emoji_id, closed=closed, hidden=hidden)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.icon_emoji_id is not None else 0
        flags |= (1 << 2) if self.closed is not None else 0
        flags |= (1 << 3) if self.hidden is not None else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(Int(self.topic_id))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.icon_emoji_id is not None:
            b.write(Long(self.icon_emoji_id))
        
        if self.closed is not None:
            b.write(Bool(self.closed))
        
        if self.hidden is not None:
            b.write(Bool(self.hidden))
        
        return b.getvalue()
