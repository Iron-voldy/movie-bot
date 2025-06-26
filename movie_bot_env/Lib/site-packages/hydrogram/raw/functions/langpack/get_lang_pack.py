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


class GetLangPack(TLObject):  # type: ignore
    """Get localization pack strings


    Details:
        - Layer: ``181``
        - ID: ``F2F2330A``

    Parameters:
        lang_pack (``str``):
            Language pack name, usually obtained from a language pack link

        lang_code (``str``):
            Language code

    Returns:
        :obj:`LangPackDifference <hydrogram.raw.base.LangPackDifference>`
    """

    __slots__: List[str] = ["lang_pack", "lang_code"]

    ID = 0xf2f2330a
    QUALNAME = "functions.langpack.GetLangPack"

    def __init__(self, *, lang_pack: str, lang_code: str) -> None:
        self.lang_pack = lang_pack  # string
        self.lang_code = lang_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetLangPack":
        # No flags
        
        lang_pack = String.read(b)
        
        lang_code = String.read(b)
        
        return GetLangPack(lang_pack=lang_pack, lang_code=lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.lang_pack))
        
        b.write(String(self.lang_code))
        
        return b.getvalue()
