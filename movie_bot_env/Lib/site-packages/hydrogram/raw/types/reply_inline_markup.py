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


class ReplyInlineMarkup(TLObject):  # type: ignore
    """Bot or inline keyboard

    Constructor of :obj:`~hydrogram.raw.base.ReplyMarkup`.

    Details:
        - Layer: ``181``
        - ID: ``48A30254``

    Parameters:
        rows (List of :obj:`KeyboardButtonRow <hydrogram.raw.base.KeyboardButtonRow>`):
            Bot or inline keyboard rows

    """

    __slots__: List[str] = ["rows"]

    ID = 0x48a30254
    QUALNAME = "types.ReplyInlineMarkup"

    def __init__(self, *, rows: List["raw.base.KeyboardButtonRow"]) -> None:
        self.rows = rows  # Vector<KeyboardButtonRow>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReplyInlineMarkup":
        # No flags
        
        rows = TLObject.read(b)
        
        return ReplyInlineMarkup(rows=rows)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.rows))
        
        return b.getvalue()
