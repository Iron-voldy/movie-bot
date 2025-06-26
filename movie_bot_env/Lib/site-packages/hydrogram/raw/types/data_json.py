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


class DataJSON(TLObject):  # type: ignore
    """Represents a json-encoded object

    Constructor of :obj:`~hydrogram.raw.base.DataJSON`.

    Details:
        - Layer: ``181``
        - ID: ``7D748D04``

    Parameters:
        data (``str``):
            JSON-encoded object

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.SendCustomRequest
            bots.InvokeWebViewCustomMethod
            phone.GetCallConfig
    """

    __slots__: List[str] = ["data"]

    ID = 0x7d748d04
    QUALNAME = "types.DataJSON"

    def __init__(self, *, data: str) -> None:
        self.data = data  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DataJSON":
        # No flags
        
        data = String.read(b)
        
        return DataJSON(data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.data))
        
        return b.getvalue()
