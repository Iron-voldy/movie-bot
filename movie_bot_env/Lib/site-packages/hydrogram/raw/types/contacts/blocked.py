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


class Blocked(TLObject):  # type: ignore
    """Full list of blocked users.

    Constructor of :obj:`~hydrogram.raw.base.contacts.Blocked`.

    Details:
        - Layer: ``181``
        - ID: ``ADE1591``

    Parameters:
        blocked (List of :obj:`PeerBlocked <hydrogram.raw.base.PeerBlocked>`):
            List of blocked users

        chats (List of :obj:`Chat <hydrogram.raw.base.Chat>`):
            Blocked chats

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            List of users

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetBlocked
    """

    __slots__: List[str] = ["blocked", "chats", "users"]

    ID = 0xade1591
    QUALNAME = "types.contacts.Blocked"

    def __init__(self, *, blocked: List["raw.base.PeerBlocked"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.blocked = blocked  # Vector<PeerBlocked>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Blocked":
        # No flags
        
        blocked = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return Blocked(blocked=blocked, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.blocked))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
