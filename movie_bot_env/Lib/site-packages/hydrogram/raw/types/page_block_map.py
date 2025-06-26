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


class PageBlockMap(TLObject):  # type: ignore
    """A map

    Constructor of :obj:`~hydrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``181``
        - ID: ``A44F3EF6``

    Parameters:
        geo (:obj:`GeoPoint <hydrogram.raw.base.GeoPoint>`):
            Location of the map center

        zoom (``int`` ``32-bit``):
            Map zoom level; 13-20

        w (``int`` ``32-bit``):
            Map width in pixels before applying scale; 16-102

        h (``int`` ``32-bit``):
            Map height in pixels before applying scale; 16-1024

        caption (:obj:`PageCaption <hydrogram.raw.base.PageCaption>`):
            Caption

    """

    __slots__: List[str] = ["geo", "zoom", "w", "h", "caption"]

    ID = 0xa44f3ef6
    QUALNAME = "types.PageBlockMap"

    def __init__(self, *, geo: "raw.base.GeoPoint", zoom: int, w: int, h: int, caption: "raw.base.PageCaption") -> None:
        self.geo = geo  # GeoPoint
        self.zoom = zoom  # int
        self.w = w  # int
        self.h = h  # int
        self.caption = caption  # PageCaption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockMap":
        # No flags
        
        geo = TLObject.read(b)
        
        zoom = Int.read(b)
        
        w = Int.read(b)
        
        h = Int.read(b)
        
        caption = TLObject.read(b)
        
        return PageBlockMap(geo=geo, zoom=zoom, w=w, h=h, caption=caption)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.geo.write())
        
        b.write(Int(self.zoom))
        
        b.write(Int(self.w))
        
        b.write(Int(self.h))
        
        b.write(self.caption.write())
        
        return b.getvalue()
