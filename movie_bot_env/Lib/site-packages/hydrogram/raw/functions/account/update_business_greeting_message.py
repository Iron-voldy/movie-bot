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


class UpdateBusinessGreetingMessage(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``181``
        - ID: ``66CDAFC4``

    Parameters:
        message (:obj:`InputBusinessGreetingMessage <hydrogram.raw.base.InputBusinessGreetingMessage>`, *optional*):
            

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["message"]

    ID = 0x66cdafc4
    QUALNAME = "functions.account.UpdateBusinessGreetingMessage"

    def __init__(self, *, message: "raw.base.InputBusinessGreetingMessage" = None) -> None:
        self.message = message  # flags.0?InputBusinessGreetingMessage

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBusinessGreetingMessage":
        
        flags = Int.read(b)
        
        message = TLObject.read(b) if flags & (1 << 0) else None
        
        return UpdateBusinessGreetingMessage(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.message is not None else 0
        b.write(Int(flags))
        
        if self.message is not None:
            b.write(self.message.write())
        
        return b.getvalue()
