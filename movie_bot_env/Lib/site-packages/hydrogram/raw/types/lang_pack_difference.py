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


class LangPackDifference(TLObject):  # type: ignore
    """Changes to the app's localization pack

    Constructor of :obj:`~hydrogram.raw.base.LangPackDifference`.

    Details:
        - Layer: ``181``
        - ID: ``F385C1F6``

    Parameters:
        lang_code (``str``):
            Language code

        from_version (``int`` ``32-bit``):
            Previous version number

        version (``int`` ``32-bit``):
            New version number

        strings (List of :obj:`LangPackString <hydrogram.raw.base.LangPackString>`):
            Localized strings

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            langpack.GetLangPack
            langpack.GetDifference
    """

    __slots__: List[str] = ["lang_code", "from_version", "version", "strings"]

    ID = 0xf385c1f6
    QUALNAME = "types.LangPackDifference"

    def __init__(self, *, lang_code: str, from_version: int, version: int, strings: List["raw.base.LangPackString"]) -> None:
        self.lang_code = lang_code  # string
        self.from_version = from_version  # int
        self.version = version  # int
        self.strings = strings  # Vector<LangPackString>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LangPackDifference":
        # No flags
        
        lang_code = String.read(b)
        
        from_version = Int.read(b)
        
        version = Int.read(b)
        
        strings = TLObject.read(b)
        
        return LangPackDifference(lang_code=lang_code, from_version=from_version, version=version, strings=strings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.lang_code))
        
        b.write(Int(self.from_version))
        
        b.write(Int(self.version))
        
        b.write(Vector(self.strings))
        
        return b.getvalue()
