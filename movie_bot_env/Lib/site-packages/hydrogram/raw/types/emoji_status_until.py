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


class EmojiStatusUntil(TLObject):  # type: ignore
    """An emoji status valid until the specified date

    Constructor of :obj:`~hydrogram.raw.base.EmojiStatus`.

    Details:
        - Layer: ``181``
        - ID: ``FA30A8C7``

    Parameters:
        document_id (``int`` ``64-bit``):
            Custom emoji document ID

        until (``int`` ``32-bit``):
            This status is valid until this date

    """

    __slots__: List[str] = ["document_id", "until"]

    ID = 0xfa30a8c7
    QUALNAME = "types.EmojiStatusUntil"

    def __init__(self, *, document_id: int, until: int) -> None:
        self.document_id = document_id  # long
        self.until = until  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiStatusUntil":
        # No flags
        
        document_id = Long.read(b)
        
        until = Int.read(b)
        
        return EmojiStatusUntil(document_id=document_id, until=until)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.document_id))
        
        b.write(Int(self.until))
        
        return b.getvalue()
