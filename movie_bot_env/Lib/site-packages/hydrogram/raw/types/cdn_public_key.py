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


class CdnPublicKey(TLObject):  # type: ignore
    """Public key to use only during handshakes to CDN DCs.

    Constructor of :obj:`~hydrogram.raw.base.CdnPublicKey`.

    Details:
        - Layer: ``181``
        - ID: ``C982EABA``

    Parameters:
        dc_id (``int`` ``32-bit``):
            CDN DC ID

        public_key (``str``):
            RSA public key

    """

    __slots__: List[str] = ["dc_id", "public_key"]

    ID = 0xc982eaba
    QUALNAME = "types.CdnPublicKey"

    def __init__(self, *, dc_id: int, public_key: str) -> None:
        self.dc_id = dc_id  # int
        self.public_key = public_key  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CdnPublicKey":
        # No flags
        
        dc_id = Int.read(b)
        
        public_key = String.read(b)
        
        return CdnPublicKey(dc_id=dc_id, public_key=public_key)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.dc_id))
        
        b.write(String(self.public_key))
        
        return b.getvalue()
