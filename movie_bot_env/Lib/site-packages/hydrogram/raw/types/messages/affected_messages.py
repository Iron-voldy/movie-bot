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


class AffectedMessages(TLObject):  # type: ignore
    """Events affected by operation

    Constructor of :obj:`~hydrogram.raw.base.messages.AffectedMessages`.

    Details:
        - Layer: ``181``
        - ID: ``84D19185``

    Parameters:
        pts (``int`` ``32-bit``):
            Event count after generation

        pts_count (``int`` ``32-bit``):
            Number of events that were generated

    Functions:
        This object can be returned by 4 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ReadHistory
            messages.DeleteMessages
            messages.ReadMessageContents
            channels.DeleteMessages
    """

    __slots__: List[str] = ["pts", "pts_count"]

    ID = 0x84d19185
    QUALNAME = "types.messages.AffectedMessages"

    def __init__(self, *, pts: int, pts_count: int) -> None:
        self.pts = pts  # int
        self.pts_count = pts_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AffectedMessages":
        # No flags
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        return AffectedMessages(pts=pts, pts_count=pts_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        return b.getvalue()
