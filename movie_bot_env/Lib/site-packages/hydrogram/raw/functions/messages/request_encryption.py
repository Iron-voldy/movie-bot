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


class RequestEncryption(TLObject):  # type: ignore
    """Sends a request to start a secret chat to the user.


    Details:
        - Layer: ``181``
        - ID: ``F64DAF43``

    Parameters:
        user_id (:obj:`InputUser <hydrogram.raw.base.InputUser>`):
            User ID

        random_id (``int`` ``32-bit``):
            Unique client request ID required to prevent resending. This also doubles as the chat ID.

        g_a (``bytes``):
            A = g ^ a mod p, see Wikipedia

    Returns:
        :obj:`EncryptedChat <hydrogram.raw.base.EncryptedChat>`
    """

    __slots__: List[str] = ["user_id", "random_id", "g_a"]

    ID = 0xf64daf43
    QUALNAME = "functions.messages.RequestEncryption"

    def __init__(self, *, user_id: "raw.base.InputUser", random_id: int, g_a: bytes) -> None:
        self.user_id = user_id  # InputUser
        self.random_id = random_id  # int
        self.g_a = g_a  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestEncryption":
        # No flags
        
        user_id = TLObject.read(b)
        
        random_id = Int.read(b)
        
        g_a = Bytes.read(b)
        
        return RequestEncryption(user_id=user_id, random_id=random_id, g_a=g_a)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.user_id.write())
        
        b.write(Int(self.random_id))
        
        b.write(Bytes(self.g_a))
        
        return b.getvalue()
