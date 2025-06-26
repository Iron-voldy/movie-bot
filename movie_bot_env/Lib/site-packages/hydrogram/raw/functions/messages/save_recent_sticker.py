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


class SaveRecentSticker(TLObject):  # type: ignore
    """Add/remove sticker from recent stickers list


    Details:
        - Layer: ``181``
        - ID: ``392718F8``

    Parameters:
        id (:obj:`InputDocument <hydrogram.raw.base.InputDocument>`):
            Sticker

        unsave (``bool``):
            Whether to save or unsave the sticker

        attached (``bool``, *optional*):
            Whether to add/remove stickers recently attached to photo or video files

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "unsave", "attached"]

    ID = 0x392718f8
    QUALNAME = "functions.messages.SaveRecentSticker"

    def __init__(self, *, id: "raw.base.InputDocument", unsave: bool, attached: Optional[bool] = None) -> None:
        self.id = id  # InputDocument
        self.unsave = unsave  # Bool
        self.attached = attached  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveRecentSticker":
        
        flags = Int.read(b)
        
        attached = True if flags & (1 << 0) else False
        id = TLObject.read(b)
        
        unsave = Bool.read(b)
        
        return SaveRecentSticker(id=id, unsave=unsave, attached=attached)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.attached else 0
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        b.write(Bool(self.unsave))
        
        return b.getvalue()
