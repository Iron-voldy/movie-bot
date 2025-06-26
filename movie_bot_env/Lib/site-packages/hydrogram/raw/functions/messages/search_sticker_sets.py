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


class SearchStickerSets(TLObject):  # type: ignore
    """Search for stickersets


    Details:
        - Layer: ``181``
        - ID: ``35705B8A``

    Parameters:
        q (``str``):
            Query string

        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here.Note: the usual hash generation algorithm cannot be used in this case, please re-use the messages.foundStickerSets.hash field returned by a previous call to the method, or pass 0 if this is the first call.

        exclude_featured (``bool``, *optional*):
            Exclude featured stickersets from results

    Returns:
        :obj:`messages.FoundStickerSets <hydrogram.raw.base.messages.FoundStickerSets>`
    """

    __slots__: List[str] = ["q", "hash", "exclude_featured"]

    ID = 0x35705b8a
    QUALNAME = "functions.messages.SearchStickerSets"

    def __init__(self, *, q: str, hash: int, exclude_featured: Optional[bool] = None) -> None:
        self.q = q  # string
        self.hash = hash  # long
        self.exclude_featured = exclude_featured  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchStickerSets":
        
        flags = Int.read(b)
        
        exclude_featured = True if flags & (1 << 0) else False
        q = String.read(b)
        
        hash = Long.read(b)
        
        return SearchStickerSets(q=q, hash=hash, exclude_featured=exclude_featured)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.exclude_featured else 0
        b.write(Int(flags))
        
        b.write(String(self.q))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
