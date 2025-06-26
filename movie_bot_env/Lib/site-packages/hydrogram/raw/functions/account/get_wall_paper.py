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


class GetWallPaper(TLObject):  # type: ignore
    """Get info about a certain wallpaper


    Details:
        - Layer: ``181``
        - ID: ``FC8DDBEA``

    Parameters:
        wallpaper (:obj:`InputWallPaper <hydrogram.raw.base.InputWallPaper>`):
            The wallpaper to get info about

    Returns:
        :obj:`WallPaper <hydrogram.raw.base.WallPaper>`
    """

    __slots__: List[str] = ["wallpaper"]

    ID = 0xfc8ddbea
    QUALNAME = "functions.account.GetWallPaper"

    def __init__(self, *, wallpaper: "raw.base.InputWallPaper") -> None:
        self.wallpaper = wallpaper  # InputWallPaper

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetWallPaper":
        # No flags
        
        wallpaper = TLObject.read(b)
        
        return GetWallPaper(wallpaper=wallpaper)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.wallpaper.write())
        
        return b.getvalue()
