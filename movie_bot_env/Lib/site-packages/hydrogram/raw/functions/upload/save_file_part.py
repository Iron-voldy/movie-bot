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


class SaveFilePart(TLObject):  # type: ignore
    """Saves a part of file for further sending to one of the methods.


    Details:
        - Layer: ``181``
        - ID: ``B304A621``

    Parameters:
        file_id (``int`` ``64-bit``):
            Random file identifier created by the client

        file_part (``int`` ``32-bit``):
            Numerical order of a part

        bytes (``bytes``):
            Binary data, content of a part

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["file_id", "file_part", "bytes"]

    ID = 0xb304a621
    QUALNAME = "functions.upload.SaveFilePart"

    def __init__(self, *, file_id: int, file_part: int, bytes: bytes) -> None:
        self.file_id = file_id  # long
        self.file_part = file_part  # int
        self.bytes = bytes  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveFilePart":
        # No flags
        
        file_id = Long.read(b)
        
        file_part = Int.read(b)
        
        bytes = Bytes.read(b)
        
        return SaveFilePart(file_id=file_id, file_part=file_part, bytes=bytes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.file_id))
        
        b.write(Int(self.file_part))
        
        b.write(Bytes(self.bytes))
        
        return b.getvalue()
