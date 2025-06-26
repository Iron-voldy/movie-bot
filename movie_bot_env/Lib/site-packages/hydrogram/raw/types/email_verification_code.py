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


class EmailVerificationCode(TLObject):  # type: ignore
    """Email verification code

    Constructor of :obj:`~hydrogram.raw.base.EmailVerification`.

    Details:
        - Layer: ``181``
        - ID: ``922E55A9``

    Parameters:
        code (``str``):
            Received verification code

    """

    __slots__: List[str] = ["code"]

    ID = 0x922e55a9
    QUALNAME = "types.EmailVerificationCode"

    def __init__(self, *, code: str) -> None:
        self.code = code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmailVerificationCode":
        # No flags
        
        code = String.read(b)
        
        return EmailVerificationCode(code=code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.code))
        
        return b.getvalue()
