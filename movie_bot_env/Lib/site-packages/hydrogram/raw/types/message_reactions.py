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


class MessageReactions(TLObject):  # type: ignore
    """Message reactions »

    Constructor of :obj:`~hydrogram.raw.base.MessageReactions`.

    Details:
        - Layer: ``181``
        - ID: ``4F2B9479``

    Parameters:
        results (List of :obj:`ReactionCount <hydrogram.raw.base.ReactionCount>`):
            Reactions

        min (``bool``, *optional*):
            Similar to min objects, used for message reaction » constructors that are the same for all users so they don't have the reactions sent by the current user (you can use messages.getMessagesReactions to get the full reaction info).

        can_see_list (``bool``, *optional*):
            Whether messages.getMessageReactionsList can be used to see how each specific peer reacted to the message

        reactions_as_tags (``bool``, *optional*):
            

        recent_reactions (List of :obj:`MessagePeerReaction <hydrogram.raw.base.MessagePeerReaction>`, *optional*):
            List of recent peers and their reactions

    """

    __slots__: List[str] = ["results", "min", "can_see_list", "reactions_as_tags", "recent_reactions"]

    ID = 0x4f2b9479
    QUALNAME = "types.MessageReactions"

    def __init__(self, *, results: List["raw.base.ReactionCount"], min: Optional[bool] = None, can_see_list: Optional[bool] = None, reactions_as_tags: Optional[bool] = None, recent_reactions: Optional[List["raw.base.MessagePeerReaction"]] = None) -> None:
        self.results = results  # Vector<ReactionCount>
        self.min = min  # flags.0?true
        self.can_see_list = can_see_list  # flags.2?true
        self.reactions_as_tags = reactions_as_tags  # flags.3?true
        self.recent_reactions = recent_reactions  # flags.1?Vector<MessagePeerReaction>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageReactions":
        
        flags = Int.read(b)
        
        min = True if flags & (1 << 0) else False
        can_see_list = True if flags & (1 << 2) else False
        reactions_as_tags = True if flags & (1 << 3) else False
        results = TLObject.read(b)
        
        recent_reactions = TLObject.read(b) if flags & (1 << 1) else []
        
        return MessageReactions(results=results, min=min, can_see_list=can_see_list, reactions_as_tags=reactions_as_tags, recent_reactions=recent_reactions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.min else 0
        flags |= (1 << 2) if self.can_see_list else 0
        flags |= (1 << 3) if self.reactions_as_tags else 0
        flags |= (1 << 1) if self.recent_reactions else 0
        b.write(Int(flags))
        
        b.write(Vector(self.results))
        
        if self.recent_reactions is not None:
            b.write(Vector(self.recent_reactions))
        
        return b.getvalue()
