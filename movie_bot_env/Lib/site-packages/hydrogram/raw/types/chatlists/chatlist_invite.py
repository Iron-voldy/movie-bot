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


class ChatlistInvite(TLObject):  # type: ignore
    """Info about a chat folder deep link ».

    Constructor of :obj:`~hydrogram.raw.base.chatlists.ChatlistInvite`.

    Details:
        - Layer: ``181``
        - ID: ``1DCD839D``

    Parameters:
        title (``str``):
            Name of the link

        peers (List of :obj:`Peer <hydrogram.raw.base.Peer>`):
            Supergroups and channels to join

        chats (List of :obj:`Chat <hydrogram.raw.base.Chat>`):
            Related chat information

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            Related user information

        emoticon (``str``, *optional*):
            Emoji to use as icon for the folder.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            chatlists.CheckChatlistInvite
    """

    __slots__: List[str] = ["title", "peers", "chats", "users", "emoticon"]

    ID = 0x1dcd839d
    QUALNAME = "types.chatlists.ChatlistInvite"

    def __init__(self, *, title: str, peers: List["raw.base.Peer"], chats: List["raw.base.Chat"], users: List["raw.base.User"], emoticon: Optional[str] = None) -> None:
        self.title = title  # string
        self.peers = peers  # Vector<Peer>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.emoticon = emoticon  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatlistInvite":
        
        flags = Int.read(b)
        
        title = String.read(b)
        
        emoticon = String.read(b) if flags & (1 << 0) else None
        peers = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ChatlistInvite(title=title, peers=peers, chats=chats, users=users, emoticon=emoticon)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.emoticon is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        if self.emoticon is not None:
            b.write(String(self.emoticon))
        
        b.write(Vector(self.peers))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
