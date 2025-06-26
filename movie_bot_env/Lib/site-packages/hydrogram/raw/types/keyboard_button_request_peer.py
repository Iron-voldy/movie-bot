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


class KeyboardButtonRequestPeer(TLObject):  # type: ignore
    """Prompts the user to select and share one or more peers with the bot using messages.sendBotRequestedPeer

    Constructor of :obj:`~hydrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``181``
        - ID: ``53D7BFD8``

    Parameters:
        text (``str``):
            Button text

        button_id (``int`` ``32-bit``):
            Button ID, to be passed to messages.sendBotRequestedPeer.

        peer_type (:obj:`RequestPeerType <hydrogram.raw.base.RequestPeerType>`):
            Filtering criteria to use for the peer selection list shown to the user. The list should display all existing peers of the specified type, and should also offer an option for the user to create and immediately use one or more (up to max_quantity) peers of the specified type, if needed.

        max_quantity (``int`` ``32-bit``):
            Maximum number of peers that can be chosne.

    """

    __slots__: List[str] = ["text", "button_id", "peer_type", "max_quantity"]

    ID = 0x53d7bfd8
    QUALNAME = "types.KeyboardButtonRequestPeer"

    def __init__(self, *, text: str, button_id: int, peer_type: "raw.base.RequestPeerType", max_quantity: int) -> None:
        self.text = text  # string
        self.button_id = button_id  # int
        self.peer_type = peer_type  # RequestPeerType
        self.max_quantity = max_quantity  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonRequestPeer":
        # No flags
        
        text = String.read(b)
        
        button_id = Int.read(b)
        
        peer_type = TLObject.read(b)
        
        max_quantity = Int.read(b)
        
        return KeyboardButtonRequestPeer(text=text, button_id=button_id, peer_type=peer_type, max_quantity=max_quantity)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(Int(self.button_id))
        
        b.write(self.peer_type.write())
        
        b.write(Int(self.max_quantity))
        
        return b.getvalue()
