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


class InputChannelFromMessage(TLObject):  # type: ignore
    """Defines a min channel that was seen in a certain message of a certain chat.

    Constructor of :obj:`~hydrogram.raw.base.InputChannel`.

    Details:
        - Layer: ``181``
        - ID: ``5B934F9D``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            The chat where the channel was seen

        msg_id (``int`` ``32-bit``):
            The message ID in the chat where the channel was seen

        channel_id (``int`` ``64-bit``):
            The channel ID

    """

    __slots__: List[str] = ["peer", "msg_id", "channel_id"]

    ID = 0x5b934f9d
    QUALNAME = "types.InputChannelFromMessage"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, channel_id: int) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.channel_id = channel_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputChannelFromMessage":
        # No flags
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        channel_id = Long.read(b)
        
        return InputChannelFromMessage(peer=peer, msg_id=msg_id, channel_id=channel_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Long(self.channel_id))
        
        return b.getvalue()
