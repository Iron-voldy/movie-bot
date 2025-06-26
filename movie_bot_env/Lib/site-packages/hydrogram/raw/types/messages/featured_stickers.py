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


class FeaturedStickers(TLObject):  # type: ignore
    """Featured stickersets

    Constructor of :obj:`~hydrogram.raw.base.messages.FeaturedStickers`.

    Details:
        - Layer: ``181``
        - ID: ``BE382906``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

        count (``int`` ``32-bit``):
            Total number of featured stickers

        sets (List of :obj:`StickerSetCovered <hydrogram.raw.base.StickerSetCovered>`):
            Featured stickersets

        unread (List of ``int`` ``64-bit``):
            IDs of new featured stickersets

        premium (``bool``, *optional*):
            Whether this is a premium stickerset

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetFeaturedStickers
            messages.GetOldFeaturedStickers
            messages.GetFeaturedEmojiStickers
    """

    __slots__: List[str] = ["hash", "count", "sets", "unread", "premium"]

    ID = 0xbe382906
    QUALNAME = "types.messages.FeaturedStickers"

    def __init__(self, *, hash: int, count: int, sets: List["raw.base.StickerSetCovered"], unread: List[int], premium: Optional[bool] = None) -> None:
        self.hash = hash  # long
        self.count = count  # int
        self.sets = sets  # Vector<StickerSetCovered>
        self.unread = unread  # Vector<long>
        self.premium = premium  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FeaturedStickers":
        
        flags = Int.read(b)
        
        premium = True if flags & (1 << 0) else False
        hash = Long.read(b)
        
        count = Int.read(b)
        
        sets = TLObject.read(b)
        
        unread = TLObject.read(b, Long)
        
        return FeaturedStickers(hash=hash, count=count, sets=sets, unread=unread, premium=premium)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.premium else 0
        b.write(Int(flags))
        
        b.write(Long(self.hash))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.sets))
        
        b.write(Vector(self.unread, Long))
        
        return b.getvalue()
