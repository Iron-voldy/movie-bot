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


class SaveWallPaper(TLObject):  # type: ignore
    """Install/uninstall wallpaper


    Details:
        - Layer: ``181``
        - ID: ``6C5A5B37``

    Parameters:
        wallpaper (:obj:`InputWallPaper <hydrogram.raw.base.InputWallPaper>`):
            Wallpaper to install or uninstall

        unsave (``bool``):
            Uninstall wallpaper?

        settings (:obj:`WallPaperSettings <hydrogram.raw.base.WallPaperSettings>`):
            Wallpaper settings

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["wallpaper", "unsave", "settings"]

    ID = 0x6c5a5b37
    QUALNAME = "functions.account.SaveWallPaper"

    def __init__(self, *, wallpaper: "raw.base.InputWallPaper", unsave: bool, settings: "raw.base.WallPaperSettings") -> None:
        self.wallpaper = wallpaper  # InputWallPaper
        self.unsave = unsave  # Bool
        self.settings = settings  # WallPaperSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveWallPaper":
        # No flags
        
        wallpaper = TLObject.read(b)
        
        unsave = Bool.read(b)
        
        settings = TLObject.read(b)
        
        return SaveWallPaper(wallpaper=wallpaper, unsave=unsave, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.wallpaper.write())
        
        b.write(Bool(self.unsave))
        
        b.write(self.settings.write())
        
        return b.getvalue()
