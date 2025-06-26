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


class LaunchPrepaidGiveaway(TLObject):  # type: ignore
    """Launch a prepaid giveaway ».


    Details:
        - Layer: ``181``
        - ID: ``5FF58F20``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            The peer where to launch the giveaway.

        giveaway_id (``int`` ``64-bit``):
            The prepaid giveaway ID.

        purpose (:obj:`InputStorePaymentPurpose <hydrogram.raw.base.InputStorePaymentPurpose>`):
            Giveway parameters

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "giveaway_id", "purpose"]

    ID = 0x5ff58f20
    QUALNAME = "functions.payments.LaunchPrepaidGiveaway"

    def __init__(self, *, peer: "raw.base.InputPeer", giveaway_id: int, purpose: "raw.base.InputStorePaymentPurpose") -> None:
        self.peer = peer  # InputPeer
        self.giveaway_id = giveaway_id  # long
        self.purpose = purpose  # InputStorePaymentPurpose

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LaunchPrepaidGiveaway":
        # No flags
        
        peer = TLObject.read(b)
        
        giveaway_id = Long.read(b)
        
        purpose = TLObject.read(b)
        
        return LaunchPrepaidGiveaway(peer=peer, giveaway_id=giveaway_id, purpose=purpose)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Long(self.giveaway_id))
        
        b.write(self.purpose.write())
        
        return b.getvalue()
