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


class GetMessageReadParticipants(TLObject):  # type: ignore
    """Get which users read a specific message: only available for groups and supergroups with less than chat_read_mark_size_threshold members, read receipts will be stored for chat_read_mark_expire_period seconds after the message was sent, see client configuration for more info ».


    Details:
        - Layer: ``181``
        - ID: ``31C1C44F``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Dialog

        msg_id (``int`` ``32-bit``):
            Message ID

    Returns:
        List of :obj:`ReadParticipantDate <hydrogram.raw.base.ReadParticipantDate>`
    """

    __slots__: List[str] = ["peer", "msg_id"]

    ID = 0x31c1c44f
    QUALNAME = "functions.messages.GetMessageReadParticipants"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessageReadParticipants":
        # No flags
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        return GetMessageReadParticipants(peer=peer, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()
