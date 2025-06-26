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


class PremiumGiftCodeOption(TLObject):  # type: ignore
    """Contains info about a giveaway/gift option.

    Constructor of :obj:`~hydrogram.raw.base.PremiumGiftCodeOption`.

    Details:
        - Layer: ``181``
        - ID: ``257E962B``

    Parameters:
        users (``int`` ``32-bit``):
            Number of users which will be able to activate the gift codes.

        months (``int`` ``32-bit``):
            Duration in months of each gifted Telegram Premium subscription.

        currency (``str``):
            Three-letter ISO 4217 currency code

        amount (``int`` ``64-bit``):
            Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

        store_product (``str``, *optional*):
            Identifier of the store product associated with the option, official apps only.

        store_quantity (``int`` ``32-bit``, *optional*):
            Number of times the store product must be paid

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetPremiumGiftCodeOptions
    """

    __slots__: List[str] = ["users", "months", "currency", "amount", "store_product", "store_quantity"]

    ID = 0x257e962b
    QUALNAME = "types.PremiumGiftCodeOption"

    def __init__(self, *, users: int, months: int, currency: str, amount: int, store_product: Optional[str] = None, store_quantity: Optional[int] = None) -> None:
        self.users = users  # int
        self.months = months  # int
        self.currency = currency  # string
        self.amount = amount  # long
        self.store_product = store_product  # flags.0?string
        self.store_quantity = store_quantity  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PremiumGiftCodeOption":
        
        flags = Int.read(b)
        
        users = Int.read(b)
        
        months = Int.read(b)
        
        store_product = String.read(b) if flags & (1 << 0) else None
        store_quantity = Int.read(b) if flags & (1 << 1) else None
        currency = String.read(b)
        
        amount = Long.read(b)
        
        return PremiumGiftCodeOption(users=users, months=months, currency=currency, amount=amount, store_product=store_product, store_quantity=store_quantity)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.store_product is not None else 0
        flags |= (1 << 1) if self.store_quantity is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.users))
        
        b.write(Int(self.months))
        
        if self.store_product is not None:
            b.write(String(self.store_product))
        
        if self.store_quantity is not None:
            b.write(Int(self.store_quantity))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        return b.getvalue()
