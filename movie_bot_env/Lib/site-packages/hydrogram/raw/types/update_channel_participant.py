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


class UpdateChannelParticipant(TLObject):  # type: ignore
    """A participant has left, joined, was banned or admined in a channel or supergroup.

    Constructor of :obj:`~hydrogram.raw.base.Update`.

    Details:
        - Layer: ``181``
        - ID: ``985D3ABB``

    Parameters:
        channel_id (``int`` ``64-bit``):
            Channel ID

        date (``int`` ``32-bit``):
            Date of the event

        actor_id (``int`` ``64-bit``):
            User that triggered the change (inviter, admin that kicked the user, or the even the user_id itself)

        user_id (``int`` ``64-bit``):
            User that was affected by the change

        qts (``int`` ``32-bit``):
            New qts value, see updates » for more info.

        via_chatlist (``bool``, *optional*):
            Whether the participant joined using a chat folder deep link ».

        prev_participant (:obj:`ChannelParticipant <hydrogram.raw.base.ChannelParticipant>`, *optional*):
            Previous participant status

        new_participant (:obj:`ChannelParticipant <hydrogram.raw.base.ChannelParticipant>`, *optional*):
            New participant status

        invite (:obj:`ExportedChatInvite <hydrogram.raw.base.ExportedChatInvite>`, *optional*):
            Chat invite used to join the channel/supergroup

    """

    __slots__: List[str] = ["channel_id", "date", "actor_id", "user_id", "qts", "via_chatlist", "prev_participant", "new_participant", "invite"]

    ID = 0x985d3abb
    QUALNAME = "types.UpdateChannelParticipant"

    def __init__(self, *, channel_id: int, date: int, actor_id: int, user_id: int, qts: int, via_chatlist: Optional[bool] = None, prev_participant: "raw.base.ChannelParticipant" = None, new_participant: "raw.base.ChannelParticipant" = None, invite: "raw.base.ExportedChatInvite" = None) -> None:
        self.channel_id = channel_id  # long
        self.date = date  # int
        self.actor_id = actor_id  # long
        self.user_id = user_id  # long
        self.qts = qts  # int
        self.via_chatlist = via_chatlist  # flags.3?true
        self.prev_participant = prev_participant  # flags.0?ChannelParticipant
        self.new_participant = new_participant  # flags.1?ChannelParticipant
        self.invite = invite  # flags.2?ExportedChatInvite

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelParticipant":
        
        flags = Int.read(b)
        
        via_chatlist = True if flags & (1 << 3) else False
        channel_id = Long.read(b)
        
        date = Int.read(b)
        
        actor_id = Long.read(b)
        
        user_id = Long.read(b)
        
        prev_participant = TLObject.read(b) if flags & (1 << 0) else None
        
        new_participant = TLObject.read(b) if flags & (1 << 1) else None
        
        invite = TLObject.read(b) if flags & (1 << 2) else None
        
        qts = Int.read(b)
        
        return UpdateChannelParticipant(channel_id=channel_id, date=date, actor_id=actor_id, user_id=user_id, qts=qts, via_chatlist=via_chatlist, prev_participant=prev_participant, new_participant=new_participant, invite=invite)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.via_chatlist else 0
        flags |= (1 << 0) if self.prev_participant is not None else 0
        flags |= (1 << 1) if self.new_participant is not None else 0
        flags |= (1 << 2) if self.invite is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.date))
        
        b.write(Long(self.actor_id))
        
        b.write(Long(self.user_id))
        
        if self.prev_participant is not None:
            b.write(self.prev_participant.write())
        
        if self.new_participant is not None:
            b.write(self.new_participant.write())
        
        if self.invite is not None:
            b.write(self.invite.write())
        
        b.write(Int(self.qts))
        
        return b.getvalue()
