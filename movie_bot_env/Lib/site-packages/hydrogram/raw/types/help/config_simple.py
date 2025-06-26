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


class ConfigSimple(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~hydrogram.raw.base.help.ConfigSimple`.

    Details:
        - Layer: ``181``
        - ID: ``5A592A6C``

    Parameters:
        date (``int`` ``32-bit``):
            N/A

        expires (``int`` ``32-bit``):
            N/A

        rules (List of :obj:`AccessPointRule <hydrogram.raw.base.AccessPointRule>`):
            N/A

    """

    __slots__: List[str] = ["date", "expires", "rules"]

    ID = 0x5a592a6c
    QUALNAME = "types.help.ConfigSimple"

    def __init__(self, *, date: int, expires: int, rules: List["raw.base.AccessPointRule"]) -> None:
        self.date = date  # int
        self.expires = expires  # int
        self.rules = rules  # vector<AccessPointRule>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ConfigSimple":
        # No flags
        
        date = Int.read(b)
        
        expires = Int.read(b)
        
        rules = TLObject.read(b)
        
        return ConfigSimple(date=date, expires=expires, rules=rules)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.date))
        
        b.write(Int(self.expires))
        
        b.write(Vector(self.rules))
        
        return b.getvalue()
