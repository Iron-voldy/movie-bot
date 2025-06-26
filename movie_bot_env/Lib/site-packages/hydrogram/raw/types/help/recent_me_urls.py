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


class RecentMeUrls(TLObject):  # type: ignore
    """Recent t.me URLs

    Constructor of :obj:`~hydrogram.raw.base.help.RecentMeUrls`.

    Details:
        - Layer: ``181``
        - ID: ``E0310D7``

    Parameters:
        urls (List of :obj:`RecentMeUrl <hydrogram.raw.base.RecentMeUrl>`):
            URLs

        chats (List of :obj:`Chat <hydrogram.raw.base.Chat>`):
            Chats

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            Users

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetRecentMeUrls
    """

    __slots__: List[str] = ["urls", "chats", "users"]

    ID = 0xe0310d7
    QUALNAME = "types.help.RecentMeUrls"

    def __init__(self, *, urls: List["raw.base.RecentMeUrl"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.urls = urls  # Vector<RecentMeUrl>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RecentMeUrls":
        # No flags
        
        urls = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return RecentMeUrls(urls=urls, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.urls))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
