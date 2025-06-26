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


class StoryReactionPublicRepost(TLObject):  # type: ignore
    """A certain peer has reposted the story.

    Constructor of :obj:`~hydrogram.raw.base.StoryReaction`.

    Details:
        - Layer: ``181``
        - ID: ``CFCD0F13``

    Parameters:
        peer_id (:obj:`Peer <hydrogram.raw.base.Peer>`):
            The peer that reposted the story.

        story (:obj:`StoryItem <hydrogram.raw.base.StoryItem>`):
            The reposted story.

    """

    __slots__: List[str] = ["peer_id", "story"]

    ID = 0xcfcd0f13
    QUALNAME = "types.StoryReactionPublicRepost"

    def __init__(self, *, peer_id: "raw.base.Peer", story: "raw.base.StoryItem") -> None:
        self.peer_id = peer_id  # Peer
        self.story = story  # StoryItem

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryReactionPublicRepost":
        # No flags
        
        peer_id = TLObject.read(b)
        
        story = TLObject.read(b)
        
        return StoryReactionPublicRepost(peer_id=peer_id, story=story)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer_id.write())
        
        b.write(self.story.write())
        
        return b.getvalue()
