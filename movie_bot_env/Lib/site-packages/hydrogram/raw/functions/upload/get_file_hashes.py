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


class GetFileHashes(TLObject):  # type: ignore
    """Get SHA256 hashes for verifying downloaded files


    Details:
        - Layer: ``181``
        - ID: ``9156982A``

    Parameters:
        location (:obj:`InputFileLocation <hydrogram.raw.base.InputFileLocation>`):
            File

        offset (``int`` ``64-bit``):
            Offset from which to get file hashes

    Returns:
        List of :obj:`FileHash <hydrogram.raw.base.FileHash>`
    """

    __slots__: List[str] = ["location", "offset"]

    ID = 0x9156982a
    QUALNAME = "functions.upload.GetFileHashes"

    def __init__(self, *, location: "raw.base.InputFileLocation", offset: int) -> None:
        self.location = location  # InputFileLocation
        self.offset = offset  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFileHashes":
        # No flags
        
        location = TLObject.read(b)
        
        offset = Long.read(b)
        
        return GetFileHashes(location=location, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.location.write())
        
        b.write(Long(self.offset))
        
        return b.getvalue()
