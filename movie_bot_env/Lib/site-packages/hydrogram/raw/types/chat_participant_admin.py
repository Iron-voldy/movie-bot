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


class ChatParticipantAdmin(TLObject):  # type: ignore
    """Chat admin

    Constructor of :obj:`~hydrogram.raw.base.ChatParticipant`.

    Details:
        - Layer: ``181``
        - ID: ``A0933F5B``

    Parameters:
        user_id (``int`` ``64-bit``):
            ID of a group member that is admin

        inviter_id (``int`` ``64-bit``):
            ID of the user that added the member to the group

        date (``int`` ``32-bit``):
            Date when the user was added

    """

    __slots__: List[str] = ["user_id", "inviter_id", "date"]

    ID = 0xa0933f5b
    QUALNAME = "types.ChatParticipantAdmin"

    def __init__(self, *, user_id: int, inviter_id: int, date: int) -> None:
        self.user_id = user_id  # long
        self.inviter_id = inviter_id  # long
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatParticipantAdmin":
        # No flags
        
        user_id = Long.read(b)
        
        inviter_id = Long.read(b)
        
        date = Int.read(b)
        
        return ChatParticipantAdmin(user_id=user_id, inviter_id=inviter_id, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(Long(self.inviter_id))
        
        b.write(Int(self.date))
        
        return b.getvalue()
