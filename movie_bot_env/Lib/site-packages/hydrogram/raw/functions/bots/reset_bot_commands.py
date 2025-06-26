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


class ResetBotCommands(TLObject):  # type: ignore
    """Clear bot commands for the specified bot scope and language code


    Details:
        - Layer: ``181``
        - ID: ``3D8DE0F9``

    Parameters:
        scope (:obj:`BotCommandScope <hydrogram.raw.base.BotCommandScope>`):
            Command scope

        lang_code (``str``):
            Language code

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["scope", "lang_code"]

    ID = 0x3d8de0f9
    QUALNAME = "functions.bots.ResetBotCommands"

    def __init__(self, *, scope: "raw.base.BotCommandScope", lang_code: str) -> None:
        self.scope = scope  # BotCommandScope
        self.lang_code = lang_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetBotCommands":
        # No flags
        
        scope = TLObject.read(b)
        
        lang_code = String.read(b)
        
        return ResetBotCommands(scope=scope, lang_code=lang_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.scope.write())
        
        b.write(String(self.lang_code))
        
        return b.getvalue()
