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


class StoryViews(TLObject):  # type: ignore
    """Aggregated view and reaction information of a story.

    Constructor of :obj:`~hydrogram.raw.base.StoryViews`.

    Details:
        - Layer: ``181``
        - ID: ``8D595CD6``

    Parameters:
        views_count (``int`` ``32-bit``):
            View counter of the story

        has_viewers (``bool``, *optional*):
            If set, indicates that the viewers list is currently viewable, and was not yet deleted because the story has expired while the user didn't have a Premium account.

        forwards_count (``int`` ``32-bit``, *optional*):
            Forward counter of the story

        reactions (List of :obj:`ReactionCount <hydrogram.raw.base.ReactionCount>`, *optional*):
            All reactions sent to this story

        reactions_count (``int`` ``32-bit``, *optional*):
            Number of reactions added to the story

        recent_viewers (List of ``int`` ``64-bit``, *optional*):
            User IDs of some recent viewers of the story

    """

    __slots__: List[str] = ["views_count", "has_viewers", "forwards_count", "reactions", "reactions_count", "recent_viewers"]

    ID = 0x8d595cd6
    QUALNAME = "types.StoryViews"

    def __init__(self, *, views_count: int, has_viewers: Optional[bool] = None, forwards_count: Optional[int] = None, reactions: Optional[List["raw.base.ReactionCount"]] = None, reactions_count: Optional[int] = None, recent_viewers: Optional[List[int]] = None) -> None:
        self.views_count = views_count  # int
        self.has_viewers = has_viewers  # flags.1?true
        self.forwards_count = forwards_count  # flags.2?int
        self.reactions = reactions  # flags.3?Vector<ReactionCount>
        self.reactions_count = reactions_count  # flags.4?int
        self.recent_viewers = recent_viewers  # flags.0?Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryViews":
        
        flags = Int.read(b)
        
        has_viewers = True if flags & (1 << 1) else False
        views_count = Int.read(b)
        
        forwards_count = Int.read(b) if flags & (1 << 2) else None
        reactions = TLObject.read(b) if flags & (1 << 3) else []
        
        reactions_count = Int.read(b) if flags & (1 << 4) else None
        recent_viewers = TLObject.read(b, Long) if flags & (1 << 0) else []
        
        return StoryViews(views_count=views_count, has_viewers=has_viewers, forwards_count=forwards_count, reactions=reactions, reactions_count=reactions_count, recent_viewers=recent_viewers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.has_viewers else 0
        flags |= (1 << 2) if self.forwards_count is not None else 0
        flags |= (1 << 3) if self.reactions else 0
        flags |= (1 << 4) if self.reactions_count is not None else 0
        flags |= (1 << 0) if self.recent_viewers else 0
        b.write(Int(flags))
        
        b.write(Int(self.views_count))
        
        if self.forwards_count is not None:
            b.write(Int(self.forwards_count))
        
        if self.reactions is not None:
            b.write(Vector(self.reactions))
        
        if self.reactions_count is not None:
            b.write(Int(self.reactions_count))
        
        if self.recent_viewers is not None:
            b.write(Vector(self.recent_viewers, Long))
        
        return b.getvalue()
