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


class SentCodeTypeFlashCall(TLObject):  # type: ignore
    """The code will be sent via a flash phone call, that will be closed immediately. The phone code will then be the phone number itself, just make sure that the phone number matches the specified pattern.

    Constructor of :obj:`~hydrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``181``
        - ID: ``AB03C6D9``

    Parameters:
        pattern (``str``):
            pattern to match

    """

    __slots__: List[str] = ["pattern"]

    ID = 0xab03c6d9
    QUALNAME = "types.auth.SentCodeTypeFlashCall"

    def __init__(self, *, pattern: str) -> None:
        self.pattern = pattern  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeFlashCall":
        # No flags
        
        pattern = String.read(b)
        
        return SentCodeTypeFlashCall(pattern=pattern)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.pattern))
        
        return b.getvalue()
