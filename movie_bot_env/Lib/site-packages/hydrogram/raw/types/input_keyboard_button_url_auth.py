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


class InputKeyboardButtonUrlAuth(TLObject):  # type: ignore
    """Button to request a user to authorize via URL using Seamless Telegram Login.

    Constructor of :obj:`~hydrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``181``
        - ID: ``D02E7FD4``

    Parameters:
        text (``str``):
            Button text

        url (``str``):
            An HTTP URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data.NOTE: You must always check the hash of the received data to verify the authentication and the integrity of the data as described in Checking authorization.

        bot (:obj:`InputUser <hydrogram.raw.base.InputUser>`):
            Username of a bot, which will be used for user authorization. See Setting up a bot for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.

        request_write_access (``bool``, *optional*):
            Set this flag to request the permission for your bot to send messages to the user.

        fwd_text (``str``, *optional*):
            New text of the button in forwarded messages.

    """

    __slots__: List[str] = ["text", "url", "bot", "request_write_access", "fwd_text"]

    ID = 0xd02e7fd4
    QUALNAME = "types.InputKeyboardButtonUrlAuth"

    def __init__(self, *, text: str, url: str, bot: "raw.base.InputUser", request_write_access: Optional[bool] = None, fwd_text: Optional[str] = None) -> None:
        self.text = text  # string
        self.url = url  # string
        self.bot = bot  # InputUser
        self.request_write_access = request_write_access  # flags.0?true
        self.fwd_text = fwd_text  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputKeyboardButtonUrlAuth":
        
        flags = Int.read(b)
        
        request_write_access = True if flags & (1 << 0) else False
        text = String.read(b)
        
        fwd_text = String.read(b) if flags & (1 << 1) else None
        url = String.read(b)
        
        bot = TLObject.read(b)
        
        return InputKeyboardButtonUrlAuth(text=text, url=url, bot=bot, request_write_access=request_write_access, fwd_text=fwd_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.request_write_access else 0
        flags |= (1 << 1) if self.fwd_text is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.text))
        
        if self.fwd_text is not None:
            b.write(String(self.fwd_text))
        
        b.write(String(self.url))
        
        b.write(self.bot.write())
        
        return b.getvalue()
