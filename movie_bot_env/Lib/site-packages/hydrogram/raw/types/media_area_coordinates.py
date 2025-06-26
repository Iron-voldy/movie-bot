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


class MediaAreaCoordinates(TLObject):  # type: ignore
    """Coordinates and size of a clicable rectangular area on top of a story.

    Constructor of :obj:`~hydrogram.raw.base.MediaAreaCoordinates`.

    Details:
        - Layer: ``181``
        - ID: ``3D1EA4E``

    Parameters:
        x (``float`` ``64-bit``):
            The abscissa of the rectangle's center, as a percentage of the media width (0-100).

        y (``float`` ``64-bit``):
            The ordinate of the rectangle's center, as a percentage of the media height (0-100).

        w (``float`` ``64-bit``):
            The width of the rectangle, as a percentage of the media width (0-100).

        h (``float`` ``64-bit``):
            The height of the rectangle, as a percentage of the media height (0-100).

        rotation (``float`` ``64-bit``):
            Clockwise rotation angle of the rectangle, in degrees (0-360).

    """

    __slots__: List[str] = ["x", "y", "w", "h", "rotation"]

    ID = 0x3d1ea4e
    QUALNAME = "types.MediaAreaCoordinates"

    def __init__(self, *, x: float, y: float, w: float, h: float, rotation: float) -> None:
        self.x = x  # double
        self.y = y  # double
        self.w = w  # double
        self.h = h  # double
        self.rotation = rotation  # double

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaCoordinates":
        # No flags
        
        x = Double.read(b)
        
        y = Double.read(b)
        
        w = Double.read(b)
        
        h = Double.read(b)
        
        rotation = Double.read(b)
        
        return MediaAreaCoordinates(x=x, y=y, w=w, h=h, rotation=rotation)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Double(self.x))
        
        b.write(Double(self.y))
        
        b.write(Double(self.w))
        
        b.write(Double(self.h))
        
        b.write(Double(self.rotation))
        
        return b.getvalue()
