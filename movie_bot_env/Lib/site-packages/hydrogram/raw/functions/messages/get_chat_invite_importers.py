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


class GetChatInviteImporters(TLObject):  # type: ignore
    """Get info about the users that joined the chat using a specific chat invite


    Details:
        - Layer: ``181``
        - ID: ``DF04DD4E``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Chat

        offset_date (``int`` ``32-bit``):
            Offsets for pagination, for more info click here

        offset_user (:obj:`InputUser <hydrogram.raw.base.InputUser>`):
            User ID for pagination: if set, offset_date must also be set.

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

        requested (``bool``, *optional*):
            If set, only returns info about users with pending join requests »

        link (``str``, *optional*):
            Invite link

        q (``str``, *optional*):
            Search for a user in the pending join requests » list: only available when the requested flag is set, cannot be used together with a specific link.

    Returns:
        :obj:`messages.ChatInviteImporters <hydrogram.raw.base.messages.ChatInviteImporters>`
    """

    __slots__: List[str] = ["peer", "offset_date", "offset_user", "limit", "requested", "link", "q"]

    ID = 0xdf04dd4e
    QUALNAME = "functions.messages.GetChatInviteImporters"

    def __init__(self, *, peer: "raw.base.InputPeer", offset_date: int, offset_user: "raw.base.InputUser", limit: int, requested: Optional[bool] = None, link: Optional[str] = None, q: Optional[str] = None) -> None:
        self.peer = peer  # InputPeer
        self.offset_date = offset_date  # int
        self.offset_user = offset_user  # InputUser
        self.limit = limit  # int
        self.requested = requested  # flags.0?true
        self.link = link  # flags.1?string
        self.q = q  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChatInviteImporters":
        
        flags = Int.read(b)
        
        requested = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        link = String.read(b) if flags & (1 << 1) else None
        q = String.read(b) if flags & (1 << 2) else None
        offset_date = Int.read(b)
        
        offset_user = TLObject.read(b)
        
        limit = Int.read(b)
        
        return GetChatInviteImporters(peer=peer, offset_date=offset_date, offset_user=offset_user, limit=limit, requested=requested, link=link, q=q)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.requested else 0
        flags |= (1 << 1) if self.link is not None else 0
        flags |= (1 << 2) if self.q is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.link is not None:
            b.write(String(self.link))
        
        if self.q is not None:
            b.write(String(self.q))
        
        b.write(Int(self.offset_date))
        
        b.write(self.offset_user.write())
        
        b.write(Int(self.limit))
        
        return b.getvalue()
