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


class ReportMissingCode(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``181``
        - ID: ``CB9DEFF6``

    Parameters:
        phone_number (``str``):
            

        phone_code_hash (``str``):
            

        mnc (``str``):
            

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash", "mnc"]

    ID = 0xcb9deff6
    QUALNAME = "functions.auth.ReportMissingCode"

    def __init__(self, *, phone_number: str, phone_code_hash: str, mnc: str) -> None:
        self.phone_number = phone_number  # string
        self.phone_code_hash = phone_code_hash  # string
        self.mnc = mnc  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReportMissingCode":
        # No flags
        
        phone_number = String.read(b)
        
        phone_code_hash = String.read(b)
        
        mnc = String.read(b)
        
        return ReportMissingCode(phone_number=phone_number, phone_code_hash=phone_code_hash, mnc=mnc)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.phone_number))
        
        b.write(String(self.phone_code_hash))
        
        b.write(String(self.mnc))
        
        return b.getvalue()
