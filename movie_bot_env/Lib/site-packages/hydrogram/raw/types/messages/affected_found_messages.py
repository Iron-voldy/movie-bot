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


class AffectedFoundMessages(TLObject):  # type: ignore
    """Messages found and affected by changes

    Constructor of :obj:`~hydrogram.raw.base.messages.AffectedFoundMessages`.

    Details:
        - Layer: ``181``
        - ID: ``EF8D3E6C``

    Parameters:
        pts (``int`` ``32-bit``):
            Event count after generation

        pts_count (``int`` ``32-bit``):
            Number of events that were generated

        offset (``int`` ``32-bit``):
            If bigger than zero, the request must be repeated to remove more messages

        messages (List of ``int`` ``32-bit``):
            Affected message IDs

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.DeletePhoneCallHistory
    """

    __slots__: List[str] = ["pts", "pts_count", "offset", "messages"]

    ID = 0xef8d3e6c
    QUALNAME = "types.messages.AffectedFoundMessages"

    def __init__(self, *, pts: int, pts_count: int, offset: int, messages: List[int]) -> None:
        self.pts = pts  # int
        self.pts_count = pts_count  # int
        self.offset = offset  # int
        self.messages = messages  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AffectedFoundMessages":
        # No flags
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        offset = Int.read(b)
        
        messages = TLObject.read(b, Int)
        
        return AffectedFoundMessages(pts=pts, pts_count=pts_count, offset=offset, messages=messages)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        b.write(Int(self.offset))
        
        b.write(Vector(self.messages, Int))
        
        return b.getvalue()
