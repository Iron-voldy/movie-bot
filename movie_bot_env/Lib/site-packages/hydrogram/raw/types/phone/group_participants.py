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


class GroupParticipants(TLObject):  # type: ignore
    """Info about the participants of a group call or livestream

    Constructor of :obj:`~hydrogram.raw.base.phone.GroupParticipants`.

    Details:
        - Layer: ``181``
        - ID: ``F47751B6``

    Parameters:
        count (``int`` ``32-bit``):
            Number of participants

        participants (List of :obj:`GroupCallParticipant <hydrogram.raw.base.GroupCallParticipant>`):
            List of participants

        next_offset (``str``):
            If not empty, the specified list of participants is partial, and more participants can be fetched specifying this parameter as offset in phone.getGroupParticipants.

        chats (List of :obj:`Chat <hydrogram.raw.base.Chat>`):
            Mentioned chats

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            Mentioned users

        version (``int`` ``32-bit``):
            Version info

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.GetGroupParticipants
    """

    __slots__: List[str] = ["count", "participants", "next_offset", "chats", "users", "version"]

    ID = 0xf47751b6
    QUALNAME = "types.phone.GroupParticipants"

    def __init__(self, *, count: int, participants: List["raw.base.GroupCallParticipant"], next_offset: str, chats: List["raw.base.Chat"], users: List["raw.base.User"], version: int) -> None:
        self.count = count  # int
        self.participants = participants  # Vector<GroupCallParticipant>
        self.next_offset = next_offset  # string
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.version = version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupParticipants":
        # No flags
        
        count = Int.read(b)
        
        participants = TLObject.read(b)
        
        next_offset = String.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        version = Int.read(b)
        
        return GroupParticipants(count=count, participants=participants, next_offset=next_offset, chats=chats, users=users, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.participants))
        
        b.write(String(self.next_offset))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        b.write(Int(self.version))
        
        return b.getvalue()
