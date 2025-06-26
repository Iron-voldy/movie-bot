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


class BroadcastRevenueBalances(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.BroadcastRevenueBalances`.

    Details:
        - Layer: ``181``
        - ID: ``8438F1C6``

    Parameters:
        current_balance (``int`` ``64-bit``):
            

        available_balance (``int`` ``64-bit``):
            

        overall_revenue (``int`` ``64-bit``):
            

    """

    __slots__: List[str] = ["current_balance", "available_balance", "overall_revenue"]

    ID = 0x8438f1c6
    QUALNAME = "types.BroadcastRevenueBalances"

    def __init__(self, *, current_balance: int, available_balance: int, overall_revenue: int) -> None:
        self.current_balance = current_balance  # long
        self.available_balance = available_balance  # long
        self.overall_revenue = overall_revenue  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BroadcastRevenueBalances":
        # No flags
        
        current_balance = Long.read(b)
        
        available_balance = Long.read(b)
        
        overall_revenue = Long.read(b)
        
        return BroadcastRevenueBalances(current_balance=current_balance, available_balance=available_balance, overall_revenue=overall_revenue)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.current_balance))
        
        b.write(Long(self.available_balance))
        
        b.write(Long(self.overall_revenue))
        
        return b.getvalue()
