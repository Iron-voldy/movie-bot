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


class GetGiveawayInfo(TLObject):  # type: ignore
    """Obtain information about a Telegram Premium giveaway ».


    Details:
        - Layer: ``181``
        - ID: ``F4239425``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            The peer where the giveaway was posted.

        msg_id (``int`` ``32-bit``):
            Message ID of the messageActionGiveawayLaunch service message

    Returns:
        :obj:`payments.GiveawayInfo <hydrogram.raw.base.payments.GiveawayInfo>`
    """

    __slots__: List[str] = ["peer", "msg_id"]

    ID = 0xf4239425
    QUALNAME = "functions.payments.GetGiveawayInfo"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGiveawayInfo":
        # No flags
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        return GetGiveawayInfo(peer=peer, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()
