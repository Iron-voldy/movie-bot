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


class UpdateLangPack(TLObject):  # type: ignore
    """Language pack updated

    Constructor of :obj:`~hydrogram.raw.base.Update`.

    Details:
        - Layer: ``181``
        - ID: ``56022F4D``

    Parameters:
        difference (:obj:`LangPackDifference <hydrogram.raw.base.LangPackDifference>`):
            Changed strings

    """

    __slots__: List[str] = ["difference"]

    ID = 0x56022f4d
    QUALNAME = "types.UpdateLangPack"

    def __init__(self, *, difference: "raw.base.LangPackDifference") -> None:
        self.difference = difference  # LangPackDifference

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateLangPack":
        # No flags
        
        difference = TLObject.read(b)
        
        return UpdateLangPack(difference=difference)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.difference.write())
        
        return b.getvalue()
