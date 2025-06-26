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


class NearestDc(TLObject):  # type: ignore
    """Nearest data center, according to geo-ip.

    Constructor of :obj:`~hydrogram.raw.base.NearestDc`.

    Details:
        - Layer: ``181``
        - ID: ``8E1A1775``

    Parameters:
        country (``str``):
            Country code determined by geo-ip

        this_dc (``int`` ``32-bit``):
            Number of current data center

        nearest_dc (``int`` ``32-bit``):
            Number of nearest data center

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetNearestDc
    """

    __slots__: List[str] = ["country", "this_dc", "nearest_dc"]

    ID = 0x8e1a1775
    QUALNAME = "types.NearestDc"

    def __init__(self, *, country: str, this_dc: int, nearest_dc: int) -> None:
        self.country = country  # string
        self.this_dc = this_dc  # int
        self.nearest_dc = nearest_dc  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "NearestDc":
        # No flags
        
        country = String.read(b)
        
        this_dc = Int.read(b)
        
        nearest_dc = Int.read(b)
        
        return NearestDc(country=country, this_dc=this_dc, nearest_dc=nearest_dc)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.country))
        
        b.write(Int(self.this_dc))
        
        b.write(Int(self.nearest_dc))
        
        return b.getvalue()
