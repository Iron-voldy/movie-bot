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


class InputWallPaperNoFile(TLObject):  # type: ignore
    """Wallpaper with no file access hash, used for example when deleting (unsave=true) wallpapers using account.saveWallPaper, specifying just the wallpaper ID.

    Constructor of :obj:`~hydrogram.raw.base.InputWallPaper`.

    Details:
        - Layer: ``181``
        - ID: ``967A462E``

    Parameters:
        id (``int`` ``64-bit``):
            Wallpaper ID

    """

    __slots__: List[str] = ["id"]

    ID = 0x967a462e
    QUALNAME = "types.InputWallPaperNoFile"

    def __init__(self, *, id: int) -> None:
        self.id = id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWallPaperNoFile":
        # No flags
        
        id = Long.read(b)
        
        return InputWallPaperNoFile(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        return b.getvalue()
