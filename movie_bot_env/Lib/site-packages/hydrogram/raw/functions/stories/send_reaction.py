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


class SendReaction(TLObject):  # type: ignore
    """React to a story.


    Details:
        - Layer: ``181``
        - ID: ``7FD736B2``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            The peer that sent the story

        story_id (``int`` ``32-bit``):
            ID of the story to react to

        reaction (:obj:`Reaction <hydrogram.raw.base.Reaction>`):
            Reaction

        add_to_recent (``bool``, *optional*):
            Whether to add this reaction to the recent reactions list ».

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "story_id", "reaction", "add_to_recent"]

    ID = 0x7fd736b2
    QUALNAME = "functions.stories.SendReaction"

    def __init__(self, *, peer: "raw.base.InputPeer", story_id: int, reaction: "raw.base.Reaction", add_to_recent: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.story_id = story_id  # int
        self.reaction = reaction  # Reaction
        self.add_to_recent = add_to_recent  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendReaction":
        
        flags = Int.read(b)
        
        add_to_recent = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        story_id = Int.read(b)
        
        reaction = TLObject.read(b)
        
        return SendReaction(peer=peer, story_id=story_id, reaction=reaction, add_to_recent=add_to_recent)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.add_to_recent else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.story_id))
        
        b.write(self.reaction.write())
        
        return b.getvalue()
