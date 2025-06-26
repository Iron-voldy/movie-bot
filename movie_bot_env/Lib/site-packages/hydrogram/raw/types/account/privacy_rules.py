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


class PrivacyRules(TLObject):  # type: ignore
    """Privacy rules

    Constructor of :obj:`~hydrogram.raw.base.account.PrivacyRules`.

    Details:
        - Layer: ``181``
        - ID: ``50A04E45``

    Parameters:
        rules (List of :obj:`PrivacyRule <hydrogram.raw.base.PrivacyRule>`):
            Privacy rules

        chats (List of :obj:`Chat <hydrogram.raw.base.Chat>`):
            Chats to which the rules apply

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            Users to which the rules apply

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetPrivacy
            account.SetPrivacy
    """

    __slots__: List[str] = ["rules", "chats", "users"]

    ID = 0x50a04e45
    QUALNAME = "types.account.PrivacyRules"

    def __init__(self, *, rules: List["raw.base.PrivacyRule"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.rules = rules  # Vector<PrivacyRule>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PrivacyRules":
        # No flags
        
        rules = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return PrivacyRules(rules=rules, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.rules))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
