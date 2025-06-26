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


class PublicForwards(TLObject):  # type: ignore
    """Contains info about the forwards of a story as a message to public chats and reposts by public channels.

    Constructor of :obj:`~hydrogram.raw.base.stats.PublicForwards`.

    Details:
        - Layer: ``181``
        - ID: ``93037E20``

    Parameters:
        count (``int`` ``32-bit``):
            Total number of results

        forwards (List of :obj:`PublicForward <hydrogram.raw.base.PublicForward>`):
            Info about the forwards of a story.

        chats (List of :obj:`Chat <hydrogram.raw.base.Chat>`):
            Mentioned chats

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            Mentioned users

        next_offset (``str``, *optional*):
            Offset used for pagination.

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.GetMessagePublicForwards
            stats.GetStoryPublicForwards
    """

    __slots__: List[str] = ["count", "forwards", "chats", "users", "next_offset"]

    ID = 0x93037e20
    QUALNAME = "types.stats.PublicForwards"

    def __init__(self, *, count: int, forwards: List["raw.base.PublicForward"], chats: List["raw.base.Chat"], users: List["raw.base.User"], next_offset: Optional[str] = None) -> None:
        self.count = count  # int
        self.forwards = forwards  # Vector<PublicForward>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PublicForwards":
        
        flags = Int.read(b)
        
        count = Int.read(b)
        
        forwards = TLObject.read(b)
        
        next_offset = String.read(b) if flags & (1 << 0) else None
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return PublicForwards(count=count, forwards=forwards, chats=chats, users=users, next_offset=next_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.forwards))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
