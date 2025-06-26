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


class SetChatAvailableReactions(TLObject):  # type: ignore
    """Change the set of message reactions » that can be used in a certain group, supergroup or channel


    Details:
        - Layer: ``181``
        - ID: ``5A150BD4``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Group where to apply changes

        available_reactions (:obj:`ChatReactions <hydrogram.raw.base.ChatReactions>`):
            Allowed reaction emojis

        reactions_limit (``int`` ``32-bit``, *optional*):
            

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "available_reactions", "reactions_limit"]

    ID = 0x5a150bd4
    QUALNAME = "functions.messages.SetChatAvailableReactions"

    def __init__(self, *, peer: "raw.base.InputPeer", available_reactions: "raw.base.ChatReactions", reactions_limit: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.available_reactions = available_reactions  # ChatReactions
        self.reactions_limit = reactions_limit  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetChatAvailableReactions":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        available_reactions = TLObject.read(b)
        
        reactions_limit = Int.read(b) if flags & (1 << 0) else None
        return SetChatAvailableReactions(peer=peer, available_reactions=available_reactions, reactions_limit=reactions_limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.reactions_limit is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(self.available_reactions.write())
        
        if self.reactions_limit is not None:
            b.write(Int(self.reactions_limit))
        
        return b.getvalue()
