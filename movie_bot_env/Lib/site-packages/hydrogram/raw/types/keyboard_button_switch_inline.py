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


class KeyboardButtonSwitchInline(TLObject):  # type: ignore
    """Button to force a user to switch to inline mode: pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field.

    Constructor of :obj:`~hydrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``181``
        - ID: ``93B9FBB5``

    Parameters:
        text (``str``):
            Button label

        query (``str``):
            The inline query to use

        same_peer (``bool``, *optional*):
            If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field.

        peer_types (List of :obj:`InlineQueryPeerType <hydrogram.raw.base.InlineQueryPeerType>`, *optional*):
            Filter to use when selecting chats.

    """

    __slots__: List[str] = ["text", "query", "same_peer", "peer_types"]

    ID = 0x93b9fbb5
    QUALNAME = "types.KeyboardButtonSwitchInline"

    def __init__(self, *, text: str, query: str, same_peer: Optional[bool] = None, peer_types: Optional[List["raw.base.InlineQueryPeerType"]] = None) -> None:
        self.text = text  # string
        self.query = query  # string
        self.same_peer = same_peer  # flags.0?true
        self.peer_types = peer_types  # flags.1?Vector<InlineQueryPeerType>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonSwitchInline":
        
        flags = Int.read(b)
        
        same_peer = True if flags & (1 << 0) else False
        text = String.read(b)
        
        query = String.read(b)
        
        peer_types = TLObject.read(b) if flags & (1 << 1) else []
        
        return KeyboardButtonSwitchInline(text=text, query=query, same_peer=same_peer, peer_types=peer_types)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.same_peer else 0
        flags |= (1 << 1) if self.peer_types else 0
        b.write(Int(flags))
        
        b.write(String(self.text))
        
        b.write(String(self.query))
        
        if self.peer_types is not None:
            b.write(Vector(self.peer_types))
        
        return b.getvalue()
