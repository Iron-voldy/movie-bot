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


class GetStoryReactionsList(TLObject):  # type: ignore
    """Get the reaction and interaction list of a story posted to a channel, along with the sender of each reaction.


    Details:
        - Layer: ``181``
        - ID: ``B9B2881F``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Channel

        id (``int`` ``32-bit``):
            Story ID

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

        forwards_first (``bool``, *optional*):
            If set, returns forwards and reposts first, then reactions, then other views; otherwise returns interactions sorted just by interaction date.

        reaction (:obj:`Reaction <hydrogram.raw.base.Reaction>`, *optional*):
            Get only reactions of this type

        offset (``str``, *optional*):
            Offset for pagination (taken from the next_offset field of the returned stories.StoryReactionsList); empty in the first request.

    Returns:
        :obj:`stories.StoryReactionsList <hydrogram.raw.base.stories.StoryReactionsList>`
    """

    __slots__: List[str] = ["peer", "id", "limit", "forwards_first", "reaction", "offset"]

    ID = 0xb9b2881f
    QUALNAME = "functions.stories.GetStoryReactionsList"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, limit: int, forwards_first: Optional[bool] = None, reaction: "raw.base.Reaction" = None, offset: Optional[str] = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.limit = limit  # int
        self.forwards_first = forwards_first  # flags.2?true
        self.reaction = reaction  # flags.0?Reaction
        self.offset = offset  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStoryReactionsList":
        
        flags = Int.read(b)
        
        forwards_first = True if flags & (1 << 2) else False
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        reaction = TLObject.read(b) if flags & (1 << 0) else None
        
        offset = String.read(b) if flags & (1 << 1) else None
        limit = Int.read(b)
        
        return GetStoryReactionsList(peer=peer, id=id, limit=limit, forwards_first=forwards_first, reaction=reaction, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.forwards_first else 0
        flags |= (1 << 0) if self.reaction is not None else 0
        flags |= (1 << 1) if self.offset is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.reaction is not None:
            b.write(self.reaction.write())
        
        if self.offset is not None:
            b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
