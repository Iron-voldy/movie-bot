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


class SentCodeTypeFragmentSms(TLObject):  # type: ignore
    """The code was delivered via fragment.com.

    Constructor of :obj:`~hydrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``181``
        - ID: ``D9565C39``

    Parameters:
        url (``str``):
            Open the specified URL to log into fragment.com with the wallet that owns the specified phone number and view the code.

        length (``int`` ``32-bit``):
            Length of the delivered code.

    """

    __slots__: List[str] = ["url", "length"]

    ID = 0xd9565c39
    QUALNAME = "types.auth.SentCodeTypeFragmentSms"

    def __init__(self, *, url: str, length: int) -> None:
        self.url = url  # string
        self.length = length  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeFragmentSms":
        # No flags
        
        url = String.read(b)
        
        length = Int.read(b)
        
        return SentCodeTypeFragmentSms(url=url, length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(Int(self.length))
        
        return b.getvalue()
