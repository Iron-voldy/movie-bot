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


class ChatInvite(TLObject):  # type: ignore
    """Chat invite info

    Constructor of :obj:`~hydrogram.raw.base.ChatInvite`.

    Details:
        - Layer: ``181``
        - ID: ``CDE0EC40``

    Parameters:
        title (``str``):
            Chat/supergroup/channel title

        photo (:obj:`Photo <hydrogram.raw.base.Photo>`):
            Chat/supergroup/channel photo

        participants_count (``int`` ``32-bit``):
            Participant count

        color (``int`` ``32-bit``):
            Profile color palette ID

        channel (``bool``, *optional*):
            Whether this is a channel/supergroup or a normal group

        broadcast (``bool``, *optional*):
            Whether this is a channel

        public (``bool``, *optional*):
            Whether this is a public channel/supergroup

        megagroup (``bool``, *optional*):
            Whether this is a supergroup

        request_needed (``bool``, *optional*):
            Whether the join request » must be first approved by an administrator

        verified (``bool``, *optional*):
            Is this chat or channel verified by Telegram?

        scam (``bool``, *optional*):
            This chat is probably a scam

        fake (``bool``, *optional*):
            If set, this chat was reported by many users as a fake or scam: be careful when interacting with it.

        about (``str``, *optional*):
            Description of the group of channel

        participants (List of :obj:`User <hydrogram.raw.base.User>`, *optional*):
            A few of the participants that are in the group

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.CheckChatInvite
    """

    __slots__: List[str] = ["title", "photo", "participants_count", "color", "channel", "broadcast", "public", "megagroup", "request_needed", "verified", "scam", "fake", "about", "participants"]

    ID = 0xcde0ec40
    QUALNAME = "types.ChatInvite"

    def __init__(self, *, title: str, photo: "raw.base.Photo", participants_count: int, color: int, channel: Optional[bool] = None, broadcast: Optional[bool] = None, public: Optional[bool] = None, megagroup: Optional[bool] = None, request_needed: Optional[bool] = None, verified: Optional[bool] = None, scam: Optional[bool] = None, fake: Optional[bool] = None, about: Optional[str] = None, participants: Optional[List["raw.base.User"]] = None) -> None:
        self.title = title  # string
        self.photo = photo  # Photo
        self.participants_count = participants_count  # int
        self.color = color  # int
        self.channel = channel  # flags.0?true
        self.broadcast = broadcast  # flags.1?true
        self.public = public  # flags.2?true
        self.megagroup = megagroup  # flags.3?true
        self.request_needed = request_needed  # flags.6?true
        self.verified = verified  # flags.7?true
        self.scam = scam  # flags.8?true
        self.fake = fake  # flags.9?true
        self.about = about  # flags.5?string
        self.participants = participants  # flags.4?Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatInvite":
        
        flags = Int.read(b)
        
        channel = True if flags & (1 << 0) else False
        broadcast = True if flags & (1 << 1) else False
        public = True if flags & (1 << 2) else False
        megagroup = True if flags & (1 << 3) else False
        request_needed = True if flags & (1 << 6) else False
        verified = True if flags & (1 << 7) else False
        scam = True if flags & (1 << 8) else False
        fake = True if flags & (1 << 9) else False
        title = String.read(b)
        
        about = String.read(b) if flags & (1 << 5) else None
        photo = TLObject.read(b)
        
        participants_count = Int.read(b)
        
        participants = TLObject.read(b) if flags & (1 << 4) else []
        
        color = Int.read(b)
        
        return ChatInvite(title=title, photo=photo, participants_count=participants_count, color=color, channel=channel, broadcast=broadcast, public=public, megagroup=megagroup, request_needed=request_needed, verified=verified, scam=scam, fake=fake, about=about, participants=participants)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.channel else 0
        flags |= (1 << 1) if self.broadcast else 0
        flags |= (1 << 2) if self.public else 0
        flags |= (1 << 3) if self.megagroup else 0
        flags |= (1 << 6) if self.request_needed else 0
        flags |= (1 << 7) if self.verified else 0
        flags |= (1 << 8) if self.scam else 0
        flags |= (1 << 9) if self.fake else 0
        flags |= (1 << 5) if self.about is not None else 0
        flags |= (1 << 4) if self.participants else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        if self.about is not None:
            b.write(String(self.about))
        
        b.write(self.photo.write())
        
        b.write(Int(self.participants_count))
        
        if self.participants is not None:
            b.write(Vector(self.participants))
        
        b.write(Int(self.color))
        
        return b.getvalue()
