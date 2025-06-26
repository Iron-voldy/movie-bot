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


class GetGameHighScores(TLObject):  # type: ignore
    """Get highscores of a game


    Details:
        - Layer: ``181``
        - ID: ``E822649D``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Where was the game sent

        id (``int`` ``32-bit``):
            ID of message with game media attachment

        user_id (:obj:`InputUser <hydrogram.raw.base.InputUser>`):
            Get high scores made by a certain user

    Returns:
        :obj:`messages.HighScores <hydrogram.raw.base.messages.HighScores>`
    """

    __slots__: List[str] = ["peer", "id", "user_id"]

    ID = 0xe822649d
    QUALNAME = "functions.messages.GetGameHighScores"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, user_id: "raw.base.InputUser") -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.user_id = user_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGameHighScores":
        # No flags
        
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        user_id = TLObject.read(b)
        
        return GetGameHighScores(peer=peer, id=id, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        b.write(self.user_id.write())
        
        return b.getvalue()
