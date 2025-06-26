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


class InputPhotoFileLocation(TLObject):  # type: ignore
    """Use this object to download a photo with upload.getFile method

    Constructor of :obj:`~hydrogram.raw.base.InputFileLocation`.

    Details:
        - Layer: ``181``
        - ID: ``40181FFE``

    Parameters:
        id (``int`` ``64-bit``):
            Photo ID, obtained from the photo object

        access_hash (``int`` ``64-bit``):
            Photo's access hash, obtained from the photo object

        file_reference (``bytes``):
            File reference

        thumb_size (``str``):
            The PhotoSize to download: must be set to the type field of the desired PhotoSize object of the photo

    """

    __slots__: List[str] = ["id", "access_hash", "file_reference", "thumb_size"]

    ID = 0x40181ffe
    QUALNAME = "types.InputPhotoFileLocation"

    def __init__(self, *, id: int, access_hash: int, file_reference: bytes, thumb_size: str) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.file_reference = file_reference  # bytes
        self.thumb_size = thumb_size  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPhotoFileLocation":
        # No flags
        
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        file_reference = Bytes.read(b)
        
        thumb_size = String.read(b)
        
        return InputPhotoFileLocation(id=id, access_hash=access_hash, file_reference=file_reference, thumb_size=thumb_size)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Bytes(self.file_reference))
        
        b.write(String(self.thumb_size))
        
        return b.getvalue()
