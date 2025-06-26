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


class HighScore(TLObject):  # type: ignore
    """Game highscore

    Constructor of :obj:`~hydrogram.raw.base.HighScore`.

    Details:
        - Layer: ``181``
        - ID: ``73A379EB``

    Parameters:
        pos (``int`` ``32-bit``):
            Position in highscore list

        user_id (``int`` ``64-bit``):
            User ID

        score (``int`` ``32-bit``):
            Score

    """

    __slots__: List[str] = ["pos", "user_id", "score"]

    ID = 0x73a379eb
    QUALNAME = "types.HighScore"

    def __init__(self, *, pos: int, user_id: int, score: int) -> None:
        self.pos = pos  # int
        self.user_id = user_id  # long
        self.score = score  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "HighScore":
        # No flags
        
        pos = Int.read(b)
        
        user_id = Long.read(b)
        
        score = Int.read(b)
        
        return HighScore(pos=pos, user_id=user_id, score=score)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.pos))
        
        b.write(Long(self.user_id))
        
        b.write(Int(self.score))
        
        return b.getvalue()
