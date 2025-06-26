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


class PrepaidGiveaway(TLObject):  # type: ignore
    """Contains info about a prepaid giveaway ».

    Constructor of :obj:`~hydrogram.raw.base.PrepaidGiveaway`.

    Details:
        - Layer: ``181``
        - ID: ``B2539D54``

    Parameters:
        id (``int`` ``64-bit``):
            Prepaid giveaway ID.

        months (``int`` ``32-bit``):
            Duration in months of each gifted Telegram Premium subscription.

        quantity (``int`` ``32-bit``):
            Number of given away Telegram Premium subscriptions.

        date (``int`` ``32-bit``):
            Payment date.

    """

    __slots__: List[str] = ["id", "months", "quantity", "date"]

    ID = 0xb2539d54
    QUALNAME = "types.PrepaidGiveaway"

    def __init__(self, *, id: int, months: int, quantity: int, date: int) -> None:
        self.id = id  # long
        self.months = months  # int
        self.quantity = quantity  # int
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PrepaidGiveaway":
        # No flags
        
        id = Long.read(b)
        
        months = Int.read(b)
        
        quantity = Int.read(b)
        
        date = Int.read(b)
        
        return PrepaidGiveaway(id=id, months=months, quantity=quantity, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(Int(self.months))
        
        b.write(Int(self.quantity))
        
        b.write(Int(self.date))
        
        return b.getvalue()
