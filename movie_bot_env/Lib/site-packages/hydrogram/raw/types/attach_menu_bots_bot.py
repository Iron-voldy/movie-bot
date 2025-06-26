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


class AttachMenuBotsBot(TLObject):  # type: ignore
    """Represents a bot mini app that can be launched from the attachment menu »

    Constructor of :obj:`~hydrogram.raw.base.AttachMenuBotsBot`.

    Details:
        - Layer: ``181``
        - ID: ``93BF667F``

    Parameters:
        bot (:obj:`AttachMenuBot <hydrogram.raw.base.AttachMenuBot>`):
            Represents a bot mini app that can be launched from the attachment menu »

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            Info about related users and bots

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAttachMenuBot
    """

    __slots__: List[str] = ["bot", "users"]

    ID = 0x93bf667f
    QUALNAME = "types.AttachMenuBotsBot"

    def __init__(self, *, bot: "raw.base.AttachMenuBot", users: List["raw.base.User"]) -> None:
        self.bot = bot  # AttachMenuBot
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuBotsBot":
        # No flags
        
        bot = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return AttachMenuBotsBot(bot=bot, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()
