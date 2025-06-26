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


class GetArchivedStickers(TLObject):  # type: ignore
    """Get all archived stickers


    Details:
        - Layer: ``181``
        - ID: ``57F17692``

    Parameters:
        offset_id (``int`` ``64-bit``):
            Offsets for pagination, for more info click here

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

        masks (``bool``, *optional*):
            Get mask stickers

        emojis (``bool``, *optional*):
            Get custom emoji stickers

    Returns:
        :obj:`messages.ArchivedStickers <hydrogram.raw.base.messages.ArchivedStickers>`
    """

    __slots__: List[str] = ["offset_id", "limit", "masks", "emojis"]

    ID = 0x57f17692
    QUALNAME = "functions.messages.GetArchivedStickers"

    def __init__(self, *, offset_id: int, limit: int, masks: Optional[bool] = None, emojis: Optional[bool] = None) -> None:
        self.offset_id = offset_id  # long
        self.limit = limit  # int
        self.masks = masks  # flags.0?true
        self.emojis = emojis  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetArchivedStickers":
        
        flags = Int.read(b)
        
        masks = True if flags & (1 << 0) else False
        emojis = True if flags & (1 << 1) else False
        offset_id = Long.read(b)
        
        limit = Int.read(b)
        
        return GetArchivedStickers(offset_id=offset_id, limit=limit, masks=masks, emojis=emojis)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.masks else 0
        flags |= (1 << 1) if self.emojis else 0
        b.write(Int(flags))
        
        b.write(Long(self.offset_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
