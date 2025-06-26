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


class EditChatAdmin(TLObject):  # type: ignore
    """Make a user admin in a basic group.


    Details:
        - Layer: ``181``
        - ID: ``A85BD1C2``

    Parameters:
        chat_id (``int`` ``64-bit``):
            The ID of the group

        user_id (:obj:`InputUser <hydrogram.raw.base.InputUser>`):
            The user to make admin

        is_admin (``bool``):
            Whether to make them admin

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["chat_id", "user_id", "is_admin"]

    ID = 0xa85bd1c2
    QUALNAME = "functions.messages.EditChatAdmin"

    def __init__(self, *, chat_id: int, user_id: "raw.base.InputUser", is_admin: bool) -> None:
        self.chat_id = chat_id  # long
        self.user_id = user_id  # InputUser
        self.is_admin = is_admin  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditChatAdmin":
        # No flags
        
        chat_id = Long.read(b)
        
        user_id = TLObject.read(b)
        
        is_admin = Bool.read(b)
        
        return EditChatAdmin(chat_id=chat_id, user_id=user_id, is_admin=is_admin)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.chat_id))
        
        b.write(self.user_id.write())
        
        b.write(Bool(self.is_admin))
        
        return b.getvalue()
