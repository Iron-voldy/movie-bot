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


class MessageMediaStory(TLObject):  # type: ignore
    """Represents a forwarded story or a story mention.

    Constructor of :obj:`~hydrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``181``
        - ID: ``68CB6283``

    Parameters:
        peer (:obj:`Peer <hydrogram.raw.base.Peer>`):
            Peer that posted the story.

        id (``int`` ``32-bit``):
            Story ID

        via_mention (``bool``, *optional*):
            If set, indicates that this someone has mentioned us in this story (i.e. by tagging us in the description) or vice versa, we have mentioned the other peer (if the message is outgoing).

        story (:obj:`StoryItem <hydrogram.raw.base.StoryItem>`, *optional*):
            The story itself, if absent fetch it using stories.getStoriesByID and the peer/id parameters specified above.

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetWebPagePreview
            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["peer", "id", "via_mention", "story"]

    ID = 0x68cb6283
    QUALNAME = "types.MessageMediaStory"

    def __init__(self, *, peer: "raw.base.Peer", id: int, via_mention: Optional[bool] = None, story: "raw.base.StoryItem" = None) -> None:
        self.peer = peer  # Peer
        self.id = id  # int
        self.via_mention = via_mention  # flags.1?true
        self.story = story  # flags.0?StoryItem

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaStory":
        
        flags = Int.read(b)
        
        via_mention = True if flags & (1 << 1) else False
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        story = TLObject.read(b) if flags & (1 << 0) else None
        
        return MessageMediaStory(peer=peer, id=id, via_mention=via_mention, story=story)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.via_mention else 0
        flags |= (1 << 0) if self.story is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.story is not None:
            b.write(self.story.write())
        
        return b.getvalue()
