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


class SendWebViewResultMessage(TLObject):  # type: ignore
    """Terminate webview interaction started with messages.requestWebView, sending the specified message to the chat on behalf of the user.


    Details:
        - Layer: ``181``
        - ID: ``A4314F5``

    Parameters:
        bot_query_id (``str``):
            Webview interaction ID obtained from messages.requestWebView

        result (:obj:`InputBotInlineResult <hydrogram.raw.base.InputBotInlineResult>`):
            Message to send

    Returns:
        :obj:`WebViewMessageSent <hydrogram.raw.base.WebViewMessageSent>`
    """

    __slots__: List[str] = ["bot_query_id", "result"]

    ID = 0xa4314f5
    QUALNAME = "functions.messages.SendWebViewResultMessage"

    def __init__(self, *, bot_query_id: str, result: "raw.base.InputBotInlineResult") -> None:
        self.bot_query_id = bot_query_id  # string
        self.result = result  # InputBotInlineResult

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendWebViewResultMessage":
        # No flags
        
        bot_query_id = String.read(b)
        
        result = TLObject.read(b)
        
        return SendWebViewResultMessage(bot_query_id=bot_query_id, result=result)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.bot_query_id))
        
        b.write(self.result.write())
        
        return b.getvalue()
