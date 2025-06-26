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


class GetCdnFile(TLObject):  # type: ignore
    """Download a CDN file.


    Details:
        - Layer: ``181``
        - ID: ``395F69DA``

    Parameters:
        file_token (``bytes``):
            File token

        offset (``int`` ``64-bit``):
            Offset of chunk to download

        limit (``int`` ``32-bit``):
            Length of chunk to download

    Returns:
        :obj:`upload.CdnFile <hydrogram.raw.base.upload.CdnFile>`
    """

    __slots__: List[str] = ["file_token", "offset", "limit"]

    ID = 0x395f69da
    QUALNAME = "functions.upload.GetCdnFile"

    def __init__(self, *, file_token: bytes, offset: int, limit: int) -> None:
        self.file_token = file_token  # bytes
        self.offset = offset  # long
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCdnFile":
        # No flags
        
        file_token = Bytes.read(b)
        
        offset = Long.read(b)
        
        limit = Int.read(b)
        
        return GetCdnFile(file_token=file_token, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.file_token))
        
        b.write(Long(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
