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


class Difference(TLObject):  # type: ignore
    """Full list of occurred events.

    Constructor of :obj:`~hydrogram.raw.base.updates.Difference`.

    Details:
        - Layer: ``181``
        - ID: ``F49CA0``

    Parameters:
        new_messages (List of :obj:`Message <hydrogram.raw.base.Message>`):
            List of new messages

        new_encrypted_messages (List of :obj:`EncryptedMessage <hydrogram.raw.base.EncryptedMessage>`):
            List of new encrypted secret chat messages

        other_updates (List of :obj:`Update <hydrogram.raw.base.Update>`):
            List of updates

        chats (List of :obj:`Chat <hydrogram.raw.base.Chat>`):
            List of chats mentioned in events

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            List of users mentioned in events

        state (:obj:`updates.State <hydrogram.raw.base.updates.State>`):
            Current state

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            updates.GetDifference
    """

    __slots__: List[str] = ["new_messages", "new_encrypted_messages", "other_updates", "chats", "users", "state"]

    ID = 0xf49ca0
    QUALNAME = "types.updates.Difference"

    def __init__(self, *, new_messages: List["raw.base.Message"], new_encrypted_messages: List["raw.base.EncryptedMessage"], other_updates: List["raw.base.Update"], chats: List["raw.base.Chat"], users: List["raw.base.User"], state: "raw.base.updates.State") -> None:
        self.new_messages = new_messages  # Vector<Message>
        self.new_encrypted_messages = new_encrypted_messages  # Vector<EncryptedMessage>
        self.other_updates = other_updates  # Vector<Update>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.state = state  # updates.State

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Difference":
        # No flags
        
        new_messages = TLObject.read(b)
        
        new_encrypted_messages = TLObject.read(b)
        
        other_updates = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        state = TLObject.read(b)
        
        return Difference(new_messages=new_messages, new_encrypted_messages=new_encrypted_messages, other_updates=other_updates, chats=chats, users=users, state=state)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.new_messages))
        
        b.write(Vector(self.new_encrypted_messages))
        
        b.write(Vector(self.other_updates))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        b.write(self.state.write())
        
        return b.getvalue()
