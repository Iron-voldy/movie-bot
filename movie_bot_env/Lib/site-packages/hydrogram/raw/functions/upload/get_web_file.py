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


class GetWebFile(TLObject):  # type: ignore
    """Returns content of a web file, by proxying the request through telegram, see the webfile docs for more info.


    Details:
        - Layer: ``181``
        - ID: ``24E6818D``

    Parameters:
        location (:obj:`InputWebFileLocation <hydrogram.raw.base.InputWebFileLocation>`):
            The file to download

        offset (``int`` ``32-bit``):
            Number of bytes to be skipped

        limit (``int`` ``32-bit``):
            Number of bytes to be returned

    Returns:
        :obj:`upload.WebFile <hydrogram.raw.base.upload.WebFile>`
    """

    __slots__: List[str] = ["location", "offset", "limit"]

    ID = 0x24e6818d
    QUALNAME = "functions.upload.GetWebFile"

    def __init__(self, *, location: "raw.base.InputWebFileLocation", offset: int, limit: int) -> None:
        self.location = location  # InputWebFileLocation
        self.offset = offset  # int
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetWebFile":
        # No flags
        
        location = TLObject.read(b)
        
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        return GetWebFile(location=location, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.location.write())
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
