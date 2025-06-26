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


class AcceptAuthorization(TLObject):  # type: ignore
    """Sends a Telegram Passport authorization form, effectively sharing data with the service


    Details:
        - Layer: ``181``
        - ID: ``F3ED4C73``

    Parameters:
        bot_id (``int`` ``64-bit``):
            Bot ID

        scope (``str``):
            Telegram Passport element types requested by the service

        public_key (``str``):
            Service's public key

        value_hashes (List of :obj:`SecureValueHash <hydrogram.raw.base.SecureValueHash>`):
            Types of values sent and their hashes

        credentials (:obj:`SecureCredentialsEncrypted <hydrogram.raw.base.SecureCredentialsEncrypted>`):
            Encrypted values

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["bot_id", "scope", "public_key", "value_hashes", "credentials"]

    ID = 0xf3ed4c73
    QUALNAME = "functions.account.AcceptAuthorization"

    def __init__(self, *, bot_id: int, scope: str, public_key: str, value_hashes: List["raw.base.SecureValueHash"], credentials: "raw.base.SecureCredentialsEncrypted") -> None:
        self.bot_id = bot_id  # long
        self.scope = scope  # string
        self.public_key = public_key  # string
        self.value_hashes = value_hashes  # Vector<SecureValueHash>
        self.credentials = credentials  # SecureCredentialsEncrypted

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AcceptAuthorization":
        # No flags
        
        bot_id = Long.read(b)
        
        scope = String.read(b)
        
        public_key = String.read(b)
        
        value_hashes = TLObject.read(b)
        
        credentials = TLObject.read(b)
        
        return AcceptAuthorization(bot_id=bot_id, scope=scope, public_key=public_key, value_hashes=value_hashes, credentials=credentials)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.bot_id))
        
        b.write(String(self.scope))
        
        b.write(String(self.public_key))
        
        b.write(Vector(self.value_hashes))
        
        b.write(self.credentials.write())
        
        return b.getvalue()
