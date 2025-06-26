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


class SecureSecretSettings(TLObject):  # type: ignore
    """Secure settings

    Constructor of :obj:`~hydrogram.raw.base.SecureSecretSettings`.

    Details:
        - Layer: ``181``
        - ID: ``1527BCAC``

    Parameters:
        secure_algo (:obj:`SecurePasswordKdfAlgo <hydrogram.raw.base.SecurePasswordKdfAlgo>`):
            Secure KDF algo

        secure_secret (``bytes``):
            Secure secret

        secure_secret_id (``int`` ``64-bit``):
            Secret ID

    """

    __slots__: List[str] = ["secure_algo", "secure_secret", "secure_secret_id"]

    ID = 0x1527bcac
    QUALNAME = "types.SecureSecretSettings"

    def __init__(self, *, secure_algo: "raw.base.SecurePasswordKdfAlgo", secure_secret: bytes, secure_secret_id: int) -> None:
        self.secure_algo = secure_algo  # SecurePasswordKdfAlgo
        self.secure_secret = secure_secret  # bytes
        self.secure_secret_id = secure_secret_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureSecretSettings":
        # No flags
        
        secure_algo = TLObject.read(b)
        
        secure_secret = Bytes.read(b)
        
        secure_secret_id = Long.read(b)
        
        return SecureSecretSettings(secure_algo=secure_algo, secure_secret=secure_secret, secure_secret_id=secure_secret_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.secure_algo.write())
        
        b.write(Bytes(self.secure_secret))
        
        b.write(Long(self.secure_secret_id))
        
        return b.getvalue()
