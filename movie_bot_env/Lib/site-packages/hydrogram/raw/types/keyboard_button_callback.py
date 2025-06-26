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


class KeyboardButtonCallback(TLObject):  # type: ignore
    """Callback button

    Constructor of :obj:`~hydrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``181``
        - ID: ``35BBDB6B``

    Parameters:
        text (``str``):
            Button text

        data (``bytes``):
            Callback data

        requires_password (``bool``, *optional*):
            Whether the user should verify his identity by entering his 2FA SRP parameters to the messages.getBotCallbackAnswer method. NOTE: telegram and the bot WILL NOT have access to the plaintext password, thanks to SRP. This button is mainly used by the official @botfather bot, for verifying the user's identity before transferring ownership of a bot to another user.

    """

    __slots__: List[str] = ["text", "data", "requires_password"]

    ID = 0x35bbdb6b
    QUALNAME = "types.KeyboardButtonCallback"

    def __init__(self, *, text: str, data: bytes, requires_password: Optional[bool] = None) -> None:
        self.text = text  # string
        self.data = data  # bytes
        self.requires_password = requires_password  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonCallback":
        
        flags = Int.read(b)
        
        requires_password = True if flags & (1 << 0) else False
        text = String.read(b)
        
        data = Bytes.read(b)
        
        return KeyboardButtonCallback(text=text, data=data, requires_password=requires_password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.requires_password else 0
        b.write(Int(flags))
        
        b.write(String(self.text))
        
        b.write(Bytes(self.data))
        
        return b.getvalue()
