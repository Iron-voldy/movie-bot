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


class MessageActionGameScore(TLObject):  # type: ignore
    """Someone scored in a game

    Constructor of :obj:`~hydrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``92A72876``

    Parameters:
        game_id (``int`` ``64-bit``):
            Game ID

        score (``int`` ``32-bit``):
            Score

    """

    __slots__: List[str] = ["game_id", "score"]

    ID = 0x92a72876
    QUALNAME = "types.MessageActionGameScore"

    def __init__(self, *, game_id: int, score: int) -> None:
        self.game_id = game_id  # long
        self.score = score  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGameScore":
        # No flags
        
        game_id = Long.read(b)
        
        score = Int.read(b)
        
        return MessageActionGameScore(game_id=game_id, score=score)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.game_id))
        
        b.write(Int(self.score))
        
        return b.getvalue()
