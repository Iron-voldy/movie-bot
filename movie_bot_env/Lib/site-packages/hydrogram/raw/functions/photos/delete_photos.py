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


class DeletePhotos(TLObject):  # type: ignore
    """Deletes profile photos. The method returns a list of successfully deleted photo IDs.


    Details:
        - Layer: ``181``
        - ID: ``87CF7F2F``

    Parameters:
        id (List of :obj:`InputPhoto <hydrogram.raw.base.InputPhoto>`):
            Input photos to delete

    Returns:
        List of ``int`` ``64-bit``
    """

    __slots__: List[str] = ["id"]

    ID = 0x87cf7f2f
    QUALNAME = "functions.photos.DeletePhotos"

    def __init__(self, *, id: List["raw.base.InputPhoto"]) -> None:
        self.id = id  # Vector<InputPhoto>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeletePhotos":
        # No flags
        
        id = TLObject.read(b)
        
        return DeletePhotos(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.id))
        
        return b.getvalue()
