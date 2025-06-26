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


class VideoSizeStickerMarkup(TLObject):  # type: ignore
    """An animated profile picture based on a sticker.

    Constructor of :obj:`~hydrogram.raw.base.VideoSize`.

    Details:
        - Layer: ``181``
        - ID: ``DA082FE``

    Parameters:
        stickerset (:obj:`InputStickerSet <hydrogram.raw.base.InputStickerSet>`):
            Stickerset

        sticker_id (``int`` ``64-bit``):
            Sticker ID

        background_colors (List of ``int`` ``32-bit``):
            1, 2, 3 or 4 RBG-24 colors used to generate a solid (1), gradient (2) or freeform gradient (3, 4) background, similar to how fill wallpapers are generated. The rotation angle for gradient backgrounds is 0.

    """

    __slots__: List[str] = ["stickerset", "sticker_id", "background_colors"]

    ID = 0xda082fe
    QUALNAME = "types.VideoSizeStickerMarkup"

    def __init__(self, *, stickerset: "raw.base.InputStickerSet", sticker_id: int, background_colors: List[int]) -> None:
        self.stickerset = stickerset  # InputStickerSet
        self.sticker_id = sticker_id  # long
        self.background_colors = background_colors  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "VideoSizeStickerMarkup":
        # No flags
        
        stickerset = TLObject.read(b)
        
        sticker_id = Long.read(b)
        
        background_colors = TLObject.read(b, Int)
        
        return VideoSizeStickerMarkup(stickerset=stickerset, sticker_id=sticker_id, background_colors=background_colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.stickerset.write())
        
        b.write(Long(self.sticker_id))
        
        b.write(Vector(self.background_colors, Int))
        
        return b.getvalue()
