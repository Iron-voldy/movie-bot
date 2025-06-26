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


class InvokeWebViewCustomMethod(TLObject):  # type: ignore
    """Send a custom request from a mini bot app, triggered by a web_app_invoke_custom_method event ».


    Details:
        - Layer: ``181``
        - ID: ``87FC5E7``

    Parameters:
        bot (:obj:`InputUser <hydrogram.raw.base.InputUser>`):
            Identifier of the bot associated to the mini bot app

        custom_method (``str``):
            Identifier of the custom method to invoke

        params (:obj:`DataJSON <hydrogram.raw.base.DataJSON>`):
            Method parameters

    Returns:
        :obj:`DataJSON <hydrogram.raw.base.DataJSON>`
    """

    __slots__: List[str] = ["bot", "custom_method", "params"]

    ID = 0x87fc5e7
    QUALNAME = "functions.bots.InvokeWebViewCustomMethod"

    def __init__(self, *, bot: "raw.base.InputUser", custom_method: str, params: "raw.base.DataJSON") -> None:
        self.bot = bot  # InputUser
        self.custom_method = custom_method  # string
        self.params = params  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWebViewCustomMethod":
        # No flags
        
        bot = TLObject.read(b)
        
        custom_method = String.read(b)
        
        params = TLObject.read(b)
        
        return InvokeWebViewCustomMethod(bot=bot, custom_method=custom_method, params=params)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(String(self.custom_method))
        
        b.write(self.params.write())
        
        return b.getvalue()
