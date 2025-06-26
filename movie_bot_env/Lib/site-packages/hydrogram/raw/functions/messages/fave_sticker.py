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


class FaveSticker(TLObject):  # type: ignore
    """Mark or unmark a sticker as favorite


    Details:
        - Layer: ``181``
        - ID: ``B9FFC55B``

    Parameters:
        id (:obj:`InputDocument <hydrogram.raw.base.InputDocument>`):
            Sticker in question

        unfave (``bool``):
            Whether to add or remove a sticker from favorites

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id", "unfave"]

    ID = 0xb9ffc55b
    QUALNAME = "functions.messages.FaveSticker"

    def __init__(self, *, id: "raw.base.InputDocument", unfave: bool) -> None:
        self.id = id  # InputDocument
        self.unfave = unfave  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FaveSticker":
        # No flags
        
        id = TLObject.read(b)
        
        unfave = Bool.read(b)
        
        return FaveSticker(id=id, unfave=unfave)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.id.write())
        
        b.write(Bool(self.unfave))
        
        return b.getvalue()
