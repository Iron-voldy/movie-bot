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


class FeaturedStickersNotModified(TLObject):  # type: ignore
    """Featured stickers haven't changed

    Constructor of :obj:`~hydrogram.raw.base.messages.FeaturedStickers`.

    Details:
        - Layer: ``181``
        - ID: ``C6DC0C66``

    Parameters:
        count (``int`` ``32-bit``):
            Total number of featured stickers

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetFeaturedStickers
            messages.GetOldFeaturedStickers
            messages.GetFeaturedEmojiStickers
    """

    __slots__: List[str] = ["count"]

    ID = 0xc6dc0c66
    QUALNAME = "types.messages.FeaturedStickersNotModified"

    def __init__(self, *, count: int) -> None:
        self.count = count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FeaturedStickersNotModified":
        # No flags
        
        count = Int.read(b)
        
        return FeaturedStickersNotModified(count=count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        return b.getvalue()
