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


class ReadEncryptedHistory(TLObject):  # type: ignore
    """Marks message history within a secret chat as read.


    Details:
        - Layer: ``181``
        - ID: ``7F4B690A``

    Parameters:
        peer (:obj:`InputEncryptedChat <hydrogram.raw.base.InputEncryptedChat>`):
            Secret chat ID

        max_date (``int`` ``32-bit``):
            Maximum date value for received messages in history

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "max_date"]

    ID = 0x7f4b690a
    QUALNAME = "functions.messages.ReadEncryptedHistory"

    def __init__(self, *, peer: "raw.base.InputEncryptedChat", max_date: int) -> None:
        self.peer = peer  # InputEncryptedChat
        self.max_date = max_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReadEncryptedHistory":
        # No flags
        
        peer = TLObject.read(b)
        
        max_date = Int.read(b)
        
        return ReadEncryptedHistory(peer=peer, max_date=max_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.max_date))
        
        return b.getvalue()
