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


class ExportAuthorization(TLObject):  # type: ignore
    """Returns data for copying authorization to another data-center.


    Details:
        - Layer: ``181``
        - ID: ``E5BFFFCD``

    Parameters:
        dc_id (``int`` ``32-bit``):
            Number of a target data-center

    Returns:
        :obj:`auth.ExportedAuthorization <hydrogram.raw.base.auth.ExportedAuthorization>`
    """

    __slots__: List[str] = ["dc_id"]

    ID = 0xe5bfffcd
    QUALNAME = "functions.auth.ExportAuthorization"

    def __init__(self, *, dc_id: int) -> None:
        self.dc_id = dc_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportAuthorization":
        # No flags
        
        dc_id = Int.read(b)
        
        return ExportAuthorization(dc_id=dc_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.dc_id))
        
        return b.getvalue()
