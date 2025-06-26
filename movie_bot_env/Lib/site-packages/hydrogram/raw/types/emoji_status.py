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


class EmojiStatus(TLObject):  # type: ignore
    """An emoji status

    Constructor of :obj:`~hydrogram.raw.base.EmojiStatus`.

    Details:
        - Layer: ``181``
        - ID: ``929B619D``

    Parameters:
        document_id (``int`` ``64-bit``):
            Custom emoji document ID

    """

    __slots__: List[str] = ["document_id"]

    ID = 0x929b619d
    QUALNAME = "types.EmojiStatus"

    def __init__(self, *, document_id: int) -> None:
        self.document_id = document_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmojiStatus":
        # No flags
        
        document_id = Long.read(b)
        
        return EmojiStatus(document_id=document_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.document_id))
        
        return b.getvalue()
