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


class InputCheckPasswordSRP(TLObject):  # type: ignore
    """Constructor for checking the validity of a 2FA SRP password (see SRP)

    Constructor of :obj:`~hydrogram.raw.base.InputCheckPasswordSRP`.

    Details:
        - Layer: ``181``
        - ID: ``D27FF082``

    Parameters:
        srp_id (``int`` ``64-bit``):
            SRP ID

        A (``bytes``):
            A parameter (see SRP)

        M1 (``bytes``):
            M1 parameter (see SRP)

    """

    __slots__: List[str] = ["srp_id", "A", "M1"]

    ID = 0xd27ff082
    QUALNAME = "types.InputCheckPasswordSRP"

    def __init__(self, *, srp_id: int, A: bytes, M1: bytes) -> None:
        self.srp_id = srp_id  # long
        self.A = A  # bytes
        self.M1 = M1  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputCheckPasswordSRP":
        # No flags
        
        srp_id = Long.read(b)
        
        A = Bytes.read(b)
        
        M1 = Bytes.read(b)
        
        return InputCheckPasswordSRP(srp_id=srp_id, A=A, M1=M1)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.srp_id))
        
        b.write(Bytes(self.A))
        
        b.write(Bytes(self.M1))
        
        return b.getvalue()
