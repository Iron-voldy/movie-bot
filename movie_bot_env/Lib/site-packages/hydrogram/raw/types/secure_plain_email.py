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


class SecurePlainEmail(TLObject):  # type: ignore
    """Email address to use in telegram passport: it must be verified, first ».

    Constructor of :obj:`~hydrogram.raw.base.SecurePlainData`.

    Details:
        - Layer: ``181``
        - ID: ``21EC5A5F``

    Parameters:
        email (``str``):
            Email address

    """

    __slots__: List[str] = ["email"]

    ID = 0x21ec5a5f
    QUALNAME = "types.SecurePlainEmail"

    def __init__(self, *, email: str) -> None:
        self.email = email  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecurePlainEmail":
        # No flags
        
        email = String.read(b)
        
        return SecurePlainEmail(email=email)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.email))
        
        return b.getvalue()
