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


class InputWebFileLocation(TLObject):  # type: ignore
    """Location of a remote HTTP(s) file

    Constructor of :obj:`~hydrogram.raw.base.InputWebFileLocation`.

    Details:
        - Layer: ``181``
        - ID: ``C239D686``

    Parameters:
        url (``str``):
            HTTP URL of file

        access_hash (``int`` ``64-bit``):
            Access hash

    """

    __slots__: List[str] = ["url", "access_hash"]

    ID = 0xc239d686
    QUALNAME = "types.InputWebFileLocation"

    def __init__(self, *, url: str, access_hash: int) -> None:
        self.url = url  # string
        self.access_hash = access_hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWebFileLocation":
        # No flags
        
        url = String.read(b)
        
        access_hash = Long.read(b)
        
        return InputWebFileLocation(url=url, access_hash=access_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(Long(self.access_hash))
        
        return b.getvalue()
