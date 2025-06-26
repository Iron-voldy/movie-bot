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


class AcceptTermsOfService(TLObject):  # type: ignore
    """Accept the new terms of service


    Details:
        - Layer: ``181``
        - ID: ``EE72F79A``

    Parameters:
        id (:obj:`DataJSON <hydrogram.raw.base.DataJSON>`):
            ID of terms of service

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id"]

    ID = 0xee72f79a
    QUALNAME = "functions.help.AcceptTermsOfService"

    def __init__(self, *, id: "raw.base.DataJSON") -> None:
        self.id = id  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AcceptTermsOfService":
        # No flags
        
        id = TLObject.read(b)
        
        return AcceptTermsOfService(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.id.write())
        
        return b.getvalue()
