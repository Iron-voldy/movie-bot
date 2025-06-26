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


class MessageActionBotAllowed(TLObject):  # type: ignore
    """We have given the bot permission to send us direct messages.

    Constructor of :obj:`~hydrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``C516D679``

    Parameters:
        attach_menu (``bool``, *optional*):
            We have authorized the bot to send us messages by installing the bot's attachment menu.

        from_request (``bool``, *optional*):
            We have allowed the bot to send us messages using bots.allowSendMessage ».

        domain (``str``, *optional*):
            We have authorized the bot to send us messages by logging into a website via Telegram Login »; this field contains the domain name of the website on which the user has logged in.

        app (:obj:`BotApp <hydrogram.raw.base.BotApp>`, *optional*):
            We have authorized the bot to send us messages by opening the specified bot mini app.

    """

    __slots__: List[str] = ["attach_menu", "from_request", "domain", "app"]

    ID = 0xc516d679
    QUALNAME = "types.MessageActionBotAllowed"

    def __init__(self, *, attach_menu: Optional[bool] = None, from_request: Optional[bool] = None, domain: Optional[str] = None, app: "raw.base.BotApp" = None) -> None:
        self.attach_menu = attach_menu  # flags.1?true
        self.from_request = from_request  # flags.3?true
        self.domain = domain  # flags.0?string
        self.app = app  # flags.2?BotApp

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionBotAllowed":
        
        flags = Int.read(b)
        
        attach_menu = True if flags & (1 << 1) else False
        from_request = True if flags & (1 << 3) else False
        domain = String.read(b) if flags & (1 << 0) else None
        app = TLObject.read(b) if flags & (1 << 2) else None
        
        return MessageActionBotAllowed(attach_menu=attach_menu, from_request=from_request, domain=domain, app=app)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.attach_menu else 0
        flags |= (1 << 3) if self.from_request else 0
        flags |= (1 << 0) if self.domain is not None else 0
        flags |= (1 << 2) if self.app is not None else 0
        b.write(Int(flags))
        
        if self.domain is not None:
            b.write(String(self.domain))
        
        if self.app is not None:
            b.write(self.app.write())
        
        return b.getvalue()
