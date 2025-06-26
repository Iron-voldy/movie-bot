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


class PeerColorSet(TLObject):  # type: ignore
    """Represents a color palette that can be used in message accents ».

    Constructor of :obj:`~hydrogram.raw.base.help.PeerColorSet`.

    Details:
        - Layer: ``181``
        - ID: ``26219A58``

    Parameters:
        colors (List of ``int`` ``32-bit``):
            A list of 1-3 colors in RGB format, describing the accent color.

    """

    __slots__: List[str] = ["colors"]

    ID = 0x26219a58
    QUALNAME = "types.help.PeerColorSet"

    def __init__(self, *, colors: List[int]) -> None:
        self.colors = colors  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerColorSet":
        # No flags
        
        colors = TLObject.read(b, Int)
        
        return PeerColorSet(colors=colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.colors, Int))
        
        return b.getvalue()
