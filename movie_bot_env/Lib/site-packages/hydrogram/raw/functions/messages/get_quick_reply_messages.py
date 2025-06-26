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


class GetQuickReplyMessages(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``181``
        - ID: ``94A495C3``

    Parameters:
        shortcut_id (``int`` ``32-bit``):
            

        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

        id (List of ``int`` ``32-bit``, *optional*):
            

    Returns:
        :obj:`messages.Messages <hydrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["shortcut_id", "hash", "id"]

    ID = 0x94a495c3
    QUALNAME = "functions.messages.GetQuickReplyMessages"

    def __init__(self, *, shortcut_id: int, hash: int, id: Optional[List[int]] = None) -> None:
        self.shortcut_id = shortcut_id  # int
        self.hash = hash  # long
        self.id = id  # flags.0?Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetQuickReplyMessages":
        
        flags = Int.read(b)
        
        shortcut_id = Int.read(b)
        
        id = TLObject.read(b, Int) if flags & (1 << 0) else []
        
        hash = Long.read(b)
        
        return GetQuickReplyMessages(shortcut_id=shortcut_id, hash=hash, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.id else 0
        b.write(Int(flags))
        
        b.write(Int(self.shortcut_id))
        
        if self.id is not None:
            b.write(Vector(self.id, Int))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
