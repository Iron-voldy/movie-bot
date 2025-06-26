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


class DocumentAttributeCustomEmoji(TLObject):  # type: ignore
    """Info about a custom emoji

    Constructor of :obj:`~hydrogram.raw.base.DocumentAttribute`.

    Details:
        - Layer: ``181``
        - ID: ``FD149899``

    Parameters:
        alt (``str``):
            The actual emoji

        stickerset (:obj:`InputStickerSet <hydrogram.raw.base.InputStickerSet>`):
            The emoji stickerset to which this emoji belongs.

        free (``bool``, *optional*):
            Whether this custom emoji can be sent by non-Premium users

        text_color (``bool``, *optional*):
            Whether the color of this TGS custom emoji should be changed to the text color when used in messages, the accent color if used as emoji status, white on chat photos, or another appropriate color based on context.

    """

    __slots__: List[str] = ["alt", "stickerset", "free", "text_color"]

    ID = 0xfd149899
    QUALNAME = "types.DocumentAttributeCustomEmoji"

    def __init__(self, *, alt: str, stickerset: "raw.base.InputStickerSet", free: Optional[bool] = None, text_color: Optional[bool] = None) -> None:
        self.alt = alt  # string
        self.stickerset = stickerset  # InputStickerSet
        self.free = free  # flags.0?true
        self.text_color = text_color  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeCustomEmoji":
        
        flags = Int.read(b)
        
        free = True if flags & (1 << 0) else False
        text_color = True if flags & (1 << 1) else False
        alt = String.read(b)
        
        stickerset = TLObject.read(b)
        
        return DocumentAttributeCustomEmoji(alt=alt, stickerset=stickerset, free=free, text_color=text_color)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.free else 0
        flags |= (1 << 1) if self.text_color else 0
        b.write(Int(flags))
        
        b.write(String(self.alt))
        
        b.write(self.stickerset.write())
        
        return b.getvalue()
