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


class ReuploadCdnFile(TLObject):  # type: ignore
    """Request a reupload of a certain file to a CDN DC.


    Details:
        - Layer: ``181``
        - ID: ``9B2754A8``

    Parameters:
        file_token (``bytes``):
            File token

        request_token (``bytes``):
            Request token

    Returns:
        List of :obj:`FileHash <hydrogram.raw.base.FileHash>`
    """

    __slots__: List[str] = ["file_token", "request_token"]

    ID = 0x9b2754a8
    QUALNAME = "functions.upload.ReuploadCdnFile"

    def __init__(self, *, file_token: bytes, request_token: bytes) -> None:
        self.file_token = file_token  # bytes
        self.request_token = request_token  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReuploadCdnFile":
        # No flags
        
        file_token = Bytes.read(b)
        
        request_token = Bytes.read(b)
        
        return ReuploadCdnFile(file_token=file_token, request_token=request_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.file_token))
        
        b.write(Bytes(self.request_token))
        
        return b.getvalue()
