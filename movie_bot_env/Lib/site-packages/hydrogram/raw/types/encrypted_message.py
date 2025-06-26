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


class EncryptedMessage(TLObject):  # type: ignore
    """Encrypted message.

    Constructor of :obj:`~hydrogram.raw.base.EncryptedMessage`.

    Details:
        - Layer: ``181``
        - ID: ``ED18C118``

    Parameters:
        random_id (``int`` ``64-bit``):
            Random message ID, assigned by the author of message

        chat_id (``int`` ``32-bit``):
            ID of encrypted chat

        date (``int`` ``32-bit``):
            Date of sending

        bytes (``bytes``):
            TL-serialization of DecryptedMessage type, encrypted with the key created at chat initialization

        file (:obj:`EncryptedFile <hydrogram.raw.base.EncryptedFile>`):
            Attached encrypted file

    """

    __slots__: List[str] = ["random_id", "chat_id", "date", "bytes", "file"]

    ID = 0xed18c118
    QUALNAME = "types.EncryptedMessage"

    def __init__(self, *, random_id: int, chat_id: int, date: int, bytes: bytes, file: "raw.base.EncryptedFile") -> None:
        self.random_id = random_id  # long
        self.chat_id = chat_id  # int
        self.date = date  # int
        self.bytes = bytes  # bytes
        self.file = file  # EncryptedFile

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EncryptedMessage":
        # No flags
        
        random_id = Long.read(b)
        
        chat_id = Int.read(b)
        
        date = Int.read(b)
        
        bytes = Bytes.read(b)
        
        file = TLObject.read(b)
        
        return EncryptedMessage(random_id=random_id, chat_id=chat_id, date=date, bytes=bytes, file=file)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.random_id))
        
        b.write(Int(self.chat_id))
        
        b.write(Int(self.date))
        
        b.write(Bytes(self.bytes))
        
        b.write(self.file.write())
        
        return b.getvalue()
