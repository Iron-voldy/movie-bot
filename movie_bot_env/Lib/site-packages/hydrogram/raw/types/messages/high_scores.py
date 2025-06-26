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


class HighScores(TLObject):  # type: ignore
    """Highscores in a game

    Constructor of :obj:`~hydrogram.raw.base.messages.HighScores`.

    Details:
        - Layer: ``181``
        - ID: ``9A3BFD99``

    Parameters:
        scores (List of :obj:`HighScore <hydrogram.raw.base.HighScore>`):
            Highscores

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            Users, associated to the highscores

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetGameHighScores
            messages.GetInlineGameHighScores
    """

    __slots__: List[str] = ["scores", "users"]

    ID = 0x9a3bfd99
    QUALNAME = "types.messages.HighScores"

    def __init__(self, *, scores: List["raw.base.HighScore"], users: List["raw.base.User"]) -> None:
        self.scores = scores  # Vector<HighScore>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "HighScores":
        # No flags
        
        scores = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return HighScores(scores=scores, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.scores))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
