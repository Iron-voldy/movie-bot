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


class ExportLoginToken(TLObject):  # type: ignore
    """Generate a login token, for login via QR code.
The generated login token should be encoded using base64url, then shown as a tg://login?token=base64encodedtoken deep link » in the QR code.


    Details:
        - Layer: ``181``
        - ID: ``B7E085FE``

    Parameters:
        api_id (``int`` ``32-bit``):
            Application identifier (see. App configuration)

        api_hash (``str``):
            Application identifier hash (see. App configuration)

        except_ids (List of ``int`` ``64-bit``):
            List of already logged-in user IDs, to prevent logging in twice with the same user

    Returns:
        :obj:`auth.LoginToken <hydrogram.raw.base.auth.LoginToken>`
    """

    __slots__: List[str] = ["api_id", "api_hash", "except_ids"]

    ID = 0xb7e085fe
    QUALNAME = "functions.auth.ExportLoginToken"

    def __init__(self, *, api_id: int, api_hash: str, except_ids: List[int]) -> None:
        self.api_id = api_id  # int
        self.api_hash = api_hash  # string
        self.except_ids = except_ids  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportLoginToken":
        # No flags
        
        api_id = Int.read(b)
        
        api_hash = String.read(b)
        
        except_ids = TLObject.read(b, Long)
        
        return ExportLoginToken(api_id=api_id, api_hash=api_hash, except_ids=except_ids)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.api_id))
        
        b.write(String(self.api_hash))
        
        b.write(Vector(self.except_ids, Long))
        
        return b.getvalue()
