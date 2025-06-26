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


class JoinAsPeers(TLObject):  # type: ignore
    """A list of peers that can be used to join a group call, presenting yourself as a specific user/channel.

    Constructor of :obj:`~hydrogram.raw.base.phone.JoinAsPeers`.

    Details:
        - Layer: ``181``
        - ID: ``AFE5623F``

    Parameters:
        peers (List of :obj:`Peer <hydrogram.raw.base.Peer>`):
            Peers

        chats (List of :obj:`Chat <hydrogram.raw.base.Chat>`):
            Chats mentioned in the peers vector

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            Users mentioned in the peers vector

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.GetGroupCallJoinAs
    """

    __slots__: List[str] = ["peers", "chats", "users"]

    ID = 0xafe5623f
    QUALNAME = "types.phone.JoinAsPeers"

    def __init__(self, *, peers: List["raw.base.Peer"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.peers = peers  # Vector<Peer>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JoinAsPeers":
        # No flags
        
        peers = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return JoinAsPeers(peers=peers, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.peers))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
