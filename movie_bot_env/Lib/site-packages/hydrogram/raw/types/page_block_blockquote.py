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


class PageBlockBlockquote(TLObject):  # type: ignore
    """Quote (equivalent to the HTML <blockquote>)

    Constructor of :obj:`~hydrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``181``
        - ID: ``263D7C26``

    Parameters:
        text (:obj:`RichText <hydrogram.raw.base.RichText>`):
            Quote contents

        caption (:obj:`RichText <hydrogram.raw.base.RichText>`):
            Caption

    """

    __slots__: List[str] = ["text", "caption"]

    ID = 0x263d7c26
    QUALNAME = "types.PageBlockBlockquote"

    def __init__(self, *, text: "raw.base.RichText", caption: "raw.base.RichText") -> None:
        self.text = text  # RichText
        self.caption = caption  # RichText

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockBlockquote":
        # No flags
        
        text = TLObject.read(b)
        
        caption = TLObject.read(b)
        
        return PageBlockBlockquote(text=text, caption=caption)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.text.write())
        
        b.write(self.caption.write())
        
        return b.getvalue()
