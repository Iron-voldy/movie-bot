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


class LangPackStringDeleted(TLObject):  # type: ignore
    """Deleted localization string

    Constructor of :obj:`~hydrogram.raw.base.LangPackString`.

    Details:
        - Layer: ``181``
        - ID: ``2979EEB2``

    Parameters:
        key (``str``):
            Localization key

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            langpack.GetStrings
    """

    __slots__: List[str] = ["key"]

    ID = 0x2979eeb2
    QUALNAME = "types.LangPackStringDeleted"

    def __init__(self, *, key: str) -> None:
        self.key = key  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LangPackStringDeleted":
        # No flags
        
        key = String.read(b)
        
        return LangPackStringDeleted(key=key)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.key))
        
        return b.getvalue()
