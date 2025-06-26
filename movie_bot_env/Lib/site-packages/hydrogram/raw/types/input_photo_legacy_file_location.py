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


class InputPhotoLegacyFileLocation(TLObject):  # type: ignore
    """DEPRECATED legacy photo file location

    Constructor of :obj:`~hydrogram.raw.base.InputFileLocation`.

    Details:
        - Layer: ``181``
        - ID: ``D83466F3``

    Parameters:
        id (``int`` ``64-bit``):
            Photo ID

        access_hash (``int`` ``64-bit``):
            Access hash

        file_reference (``bytes``):
            File reference

        volume_id (``int`` ``64-bit``):
            Volume ID

        local_id (``int`` ``32-bit``):
            Local ID

        secret (``int`` ``64-bit``):
            Secret

    """

    __slots__: List[str] = ["id", "access_hash", "file_reference", "volume_id", "local_id", "secret"]

    ID = 0xd83466f3
    QUALNAME = "types.InputPhotoLegacyFileLocation"

    def __init__(self, *, id: int, access_hash: int, file_reference: bytes, volume_id: int, local_id: int, secret: int) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.file_reference = file_reference  # bytes
        self.volume_id = volume_id  # long
        self.local_id = local_id  # int
        self.secret = secret  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPhotoLegacyFileLocation":
        # No flags
        
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        file_reference = Bytes.read(b)
        
        volume_id = Long.read(b)
        
        local_id = Int.read(b)
        
        secret = Long.read(b)
        
        return InputPhotoLegacyFileLocation(id=id, access_hash=access_hash, file_reference=file_reference, volume_id=volume_id, local_id=local_id, secret=secret)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Bytes(self.file_reference))
        
        b.write(Long(self.volume_id))
        
        b.write(Int(self.local_id))
        
        b.write(Long(self.secret))
        
        return b.getvalue()
