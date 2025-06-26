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


class SendEncryptedService(TLObject):  # type: ignore
    """Sends a service message to a secret chat.


    Details:
        - Layer: ``181``
        - ID: ``32D439A4``

    Parameters:
        peer (:obj:`InputEncryptedChat <hydrogram.raw.base.InputEncryptedChat>`):
            Secret chat ID

        random_id (``int`` ``64-bit``):
            Unique client message ID required to prevent message resending

        data (``bytes``):
            TL-serialization of  DecryptedMessage type, encrypted with a key generated during chat initialization

    Returns:
        :obj:`messages.SentEncryptedMessage <hydrogram.raw.base.messages.SentEncryptedMessage>`
    """

    __slots__: List[str] = ["peer", "random_id", "data"]

    ID = 0x32d439a4
    QUALNAME = "functions.messages.SendEncryptedService"

    def __init__(self, *, peer: "raw.base.InputEncryptedChat", random_id: int, data: bytes) -> None:
        self.peer = peer  # InputEncryptedChat
        self.random_id = random_id  # long
        self.data = data  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendEncryptedService":
        # No flags
        
        peer = TLObject.read(b)
        
        random_id = Long.read(b)
        
        data = Bytes.read(b)
        
        return SendEncryptedService(peer=peer, random_id=random_id, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Long(self.random_id))
        
        b.write(Bytes(self.data))
        
        return b.getvalue()
