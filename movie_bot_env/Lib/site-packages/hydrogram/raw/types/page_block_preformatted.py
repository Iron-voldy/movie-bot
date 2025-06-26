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


class PageBlockPreformatted(TLObject):  # type: ignore
    """Preformatted (<pre> text)

    Constructor of :obj:`~hydrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``181``
        - ID: ``C070D93E``

    Parameters:
        text (:obj:`RichText <hydrogram.raw.base.RichText>`):
            Text

        language (``str``):
            Programming language of preformatted text

    """

    __slots__: List[str] = ["text", "language"]

    ID = 0xc070d93e
    QUALNAME = "types.PageBlockPreformatted"

    def __init__(self, *, text: "raw.base.RichText", language: str) -> None:
        self.text = text  # RichText
        self.language = language  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockPreformatted":
        # No flags
        
        text = TLObject.read(b)
        
        language = String.read(b)
        
        return PageBlockPreformatted(text=text, language=language)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.text.write())
        
        b.write(String(self.language))
        
        return b.getvalue()
