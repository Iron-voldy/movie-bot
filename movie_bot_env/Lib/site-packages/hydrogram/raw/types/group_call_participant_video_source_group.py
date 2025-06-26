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


class GroupCallParticipantVideoSourceGroup(TLObject):  # type: ignore
    """Describes a group of video synchronization source identifiers

    Constructor of :obj:`~hydrogram.raw.base.GroupCallParticipantVideoSourceGroup`.

    Details:
        - Layer: ``181``
        - ID: ``DCB118B7``

    Parameters:
        semantics (``str``):
            SDP semantics

        sources (List of ``int`` ``32-bit``):
            Source IDs

    """

    __slots__: List[str] = ["semantics", "sources"]

    ID = 0xdcb118b7
    QUALNAME = "types.GroupCallParticipantVideoSourceGroup"

    def __init__(self, *, semantics: str, sources: List[int]) -> None:
        self.semantics = semantics  # string
        self.sources = sources  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallParticipantVideoSourceGroup":
        # No flags
        
        semantics = String.read(b)
        
        sources = TLObject.read(b, Int)
        
        return GroupCallParticipantVideoSourceGroup(semantics=semantics, sources=sources)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.semantics))
        
        b.write(Vector(self.sources, Int))
        
        return b.getvalue()
