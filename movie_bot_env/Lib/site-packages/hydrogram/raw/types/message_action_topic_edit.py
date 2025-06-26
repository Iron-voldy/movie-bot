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


class MessageActionTopicEdit(TLObject):  # type: ignore
    """Forum topic information was edited.

    Constructor of :obj:`~hydrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``C0944820``

    Parameters:
        title (``str``, *optional*):
            New topic title.

        icon_emoji_id (``int`` ``64-bit``, *optional*):
            ID of the new custom emoji used as topic icon, or if it was removed.

        closed (``bool``, *optional*):
            Whether the topic was opened or closed.

        hidden (``bool``, *optional*):
            Whether the topic was hidden or unhidden (only valid for the "General" topic, id=1).

    """

    __slots__: List[str] = ["title", "icon_emoji_id", "closed", "hidden"]

    ID = 0xc0944820
    QUALNAME = "types.MessageActionTopicEdit"

    def __init__(self, *, title: Optional[str] = None, icon_emoji_id: Optional[int] = None, closed: Optional[bool] = None, hidden: Optional[bool] = None) -> None:
        self.title = title  # flags.0?string
        self.icon_emoji_id = icon_emoji_id  # flags.1?long
        self.closed = closed  # flags.2?Bool
        self.hidden = hidden  # flags.3?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionTopicEdit":
        
        flags = Int.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        icon_emoji_id = Long.read(b) if flags & (1 << 1) else None
        closed = Bool.read(b) if flags & (1 << 2) else None
        hidden = Bool.read(b) if flags & (1 << 3) else None
        return MessageActionTopicEdit(title=title, icon_emoji_id=icon_emoji_id, closed=closed, hidden=hidden)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.icon_emoji_id is not None else 0
        flags |= (1 << 2) if self.closed is not None else 0
        flags |= (1 << 3) if self.hidden is not None else 0
        b.write(Int(flags))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.icon_emoji_id is not None:
            b.write(Long(self.icon_emoji_id))
        
        if self.closed is not None:
            b.write(Bool(self.closed))
        
        if self.hidden is not None:
            b.write(Bool(self.hidden))
        
        return b.getvalue()
