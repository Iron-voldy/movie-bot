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


class InstallTheme(TLObject):  # type: ignore
    """Install a theme


    Details:
        - Layer: ``181``
        - ID: ``C727BB3B``

    Parameters:
        dark (``bool``, *optional*):
            Whether to install the dark version

        theme (:obj:`InputTheme <hydrogram.raw.base.InputTheme>`, *optional*):
            Theme to install

        format (``str``, *optional*):
            Theme format, a string that identifies the theming engines supported by the client

        base_theme (:obj:`BaseTheme <hydrogram.raw.base.BaseTheme>`, *optional*):
            Indicates a basic theme provided by all clients

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["dark", "theme", "format", "base_theme"]

    ID = 0xc727bb3b
    QUALNAME = "functions.account.InstallTheme"

    def __init__(self, *, dark: Optional[bool] = None, theme: "raw.base.InputTheme" = None, format: Optional[str] = None, base_theme: "raw.base.BaseTheme" = None) -> None:
        self.dark = dark  # flags.0?true
        self.theme = theme  # flags.1?InputTheme
        self.format = format  # flags.2?string
        self.base_theme = base_theme  # flags.3?BaseTheme

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InstallTheme":
        
        flags = Int.read(b)
        
        dark = True if flags & (1 << 0) else False
        theme = TLObject.read(b) if flags & (1 << 1) else None
        
        format = String.read(b) if flags & (1 << 2) else None
        base_theme = TLObject.read(b) if flags & (1 << 3) else None
        
        return InstallTheme(dark=dark, theme=theme, format=format, base_theme=base_theme)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.dark else 0
        flags |= (1 << 1) if self.theme is not None else 0
        flags |= (1 << 2) if self.format is not None else 0
        flags |= (1 << 3) if self.base_theme is not None else 0
        b.write(Int(flags))
        
        if self.theme is not None:
            b.write(self.theme.write())
        
        if self.format is not None:
            b.write(String(self.format))
        
        if self.base_theme is not None:
            b.write(self.base_theme.write())
        
        return b.getvalue()
