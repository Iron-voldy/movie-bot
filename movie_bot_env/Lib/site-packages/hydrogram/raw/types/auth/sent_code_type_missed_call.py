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


class SentCodeTypeMissedCall(TLObject):  # type: ignore
    """The code will be sent via a flash phone call, that will be closed immediately. The last digits of the phone number that calls are the code that must be entered manually by the user.

    Constructor of :obj:`~hydrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``181``
        - ID: ``82006484``

    Parameters:
        prefix (``str``):
            Prefix of the phone number from which the call will be made

        length (``int`` ``32-bit``):
            Length of the verification code

    """

    __slots__: List[str] = ["prefix", "length"]

    ID = 0x82006484
    QUALNAME = "types.auth.SentCodeTypeMissedCall"

    def __init__(self, *, prefix: str, length: int) -> None:
        self.prefix = prefix  # string
        self.length = length  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeMissedCall":
        # No flags
        
        prefix = String.read(b)
        
        length = Int.read(b)
        
        return SentCodeTypeMissedCall(prefix=prefix, length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.prefix))
        
        b.write(Int(self.length))
        
        return b.getvalue()
