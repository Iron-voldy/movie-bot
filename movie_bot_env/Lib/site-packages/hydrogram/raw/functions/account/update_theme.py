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


class UpdateTheme(TLObject):  # type: ignore
    """Update theme


    Details:
        - Layer: ``181``
        - ID: ``2BF40CCC``

    Parameters:
        format (``str``):
            Theme format, a string that identifies the theming engines supported by the client

        theme (:obj:`InputTheme <hydrogram.raw.base.InputTheme>`):
            Theme to update

        slug (``str``, *optional*):
            Unique theme ID

        title (``str``, *optional*):
            Theme name

        document (:obj:`InputDocument <hydrogram.raw.base.InputDocument>`, *optional*):
            Theme file

        settings (List of :obj:`InputThemeSettings <hydrogram.raw.base.InputThemeSettings>`, *optional*):
            Theme settings

    Returns:
        :obj:`Theme <hydrogram.raw.base.Theme>`
    """

    __slots__: List[str] = ["format", "theme", "slug", "title", "document", "settings"]

    ID = 0x2bf40ccc
    QUALNAME = "functions.account.UpdateTheme"

    def __init__(self, *, format: str, theme: "raw.base.InputTheme", slug: Optional[str] = None, title: Optional[str] = None, document: "raw.base.InputDocument" = None, settings: Optional[List["raw.base.InputThemeSettings"]] = None) -> None:
        self.format = format  # string
        self.theme = theme  # InputTheme
        self.slug = slug  # flags.0?string
        self.title = title  # flags.1?string
        self.document = document  # flags.2?InputDocument
        self.settings = settings  # flags.3?Vector<InputThemeSettings>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateTheme":
        
        flags = Int.read(b)
        
        format = String.read(b)
        
        theme = TLObject.read(b)
        
        slug = String.read(b) if flags & (1 << 0) else None
        title = String.read(b) if flags & (1 << 1) else None
        document = TLObject.read(b) if flags & (1 << 2) else None
        
        settings = TLObject.read(b) if flags & (1 << 3) else []
        
        return UpdateTheme(format=format, theme=theme, slug=slug, title=title, document=document, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.slug is not None else 0
        flags |= (1 << 1) if self.title is not None else 0
        flags |= (1 << 2) if self.document is not None else 0
        flags |= (1 << 3) if self.settings else 0
        b.write(Int(flags))
        
        b.write(String(self.format))
        
        b.write(self.theme.write())
        
        if self.slug is not None:
            b.write(String(self.slug))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.settings is not None:
            b.write(Vector(self.settings))
        
        return b.getvalue()
