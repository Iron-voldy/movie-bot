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


class RequestPeerTypeUser(TLObject):  # type: ignore
    """Choose a user.

    Constructor of :obj:`~hydrogram.raw.base.RequestPeerType`.

    Details:
        - Layer: ``181``
        - ID: ``5F3B8A00``

    Parameters:
        bot (``bool``, *optional*):
            Whether to allow choosing only bots.

        premium (``bool``, *optional*):
            Whether to allow choosing only Premium users.

    """

    __slots__: List[str] = ["bot", "premium"]

    ID = 0x5f3b8a00
    QUALNAME = "types.RequestPeerTypeUser"

    def __init__(self, *, bot: Optional[bool] = None, premium: Optional[bool] = None) -> None:
        self.bot = bot  # flags.0?Bool
        self.premium = premium  # flags.1?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestPeerTypeUser":
        
        flags = Int.read(b)
        
        bot = Bool.read(b) if flags & (1 << 0) else None
        premium = Bool.read(b) if flags & (1 << 1) else None
        return RequestPeerTypeUser(bot=bot, premium=premium)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.bot is not None else 0
        flags |= (1 << 1) if self.premium is not None else 0
        b.write(Int(flags))
        
        if self.bot is not None:
            b.write(Bool(self.bot))
        
        if self.premium is not None:
            b.write(Bool(self.premium))
        
        return b.getvalue()
