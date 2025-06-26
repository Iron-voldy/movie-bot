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


class InputStorePaymentStars(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.InputStorePaymentPurpose`.

    Details:
        - Layer: ``181``
        - ID: ``4F0EE8DF``

    Parameters:
        stars (``int`` ``64-bit``):
            

        currency (``str``):
            

        amount (``int`` ``64-bit``):
            

    """

    __slots__: List[str] = ["stars", "currency", "amount"]

    ID = 0x4f0ee8df
    QUALNAME = "types.InputStorePaymentStars"

    def __init__(self, *, stars: int, currency: str, amount: int) -> None:
        self.stars = stars  # long
        self.currency = currency  # string
        self.amount = amount  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStorePaymentStars":
        
        flags = Int.read(b)
        
        stars = Long.read(b)
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        return InputStorePaymentStars(stars=stars, currency=currency, amount=amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        
        b.write(Int(flags))
        
        b.write(Long(self.stars))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        return b.getvalue()
