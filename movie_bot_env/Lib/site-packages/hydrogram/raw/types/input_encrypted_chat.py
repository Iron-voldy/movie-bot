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


class InputEncryptedChat(TLObject):  # type: ignore
    """Creates an encrypted chat.

    Constructor of :obj:`~hydrogram.raw.base.InputEncryptedChat`.

    Details:
        - Layer: ``181``
        - ID: ``F141B5E1``

    Parameters:
        chat_id (``int`` ``32-bit``):
            Chat ID

        access_hash (``int`` ``64-bit``):
            Checking sum from constructor encryptedChat, encryptedChatWaiting or encryptedChatRequested

    """

    __slots__: List[str] = ["chat_id", "access_hash"]

    ID = 0xf141b5e1
    QUALNAME = "types.InputEncryptedChat"

    def __init__(self, *, chat_id: int, access_hash: int) -> None:
        self.chat_id = chat_id  # int
        self.access_hash = access_hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputEncryptedChat":
        # No flags
        
        chat_id = Int.read(b)
        
        access_hash = Long.read(b)
        
        return InputEncryptedChat(chat_id=chat_id, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.chat_id))
        
        b.write(Long(self.access_hash))
        
        return b.getvalue()
