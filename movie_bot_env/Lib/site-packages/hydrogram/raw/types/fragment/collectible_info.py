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


class CollectibleInfo(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.fragment.CollectibleInfo`.

    Details:
        - Layer: ``181``
        - ID: ``6EBDFF91``

    Parameters:
        purchase_date (``int`` ``32-bit``):
            

        currency (``str``):
            

        amount (``int`` ``64-bit``):
            

        crypto_currency (``str``):
            

        crypto_amount (``int`` ``64-bit``):
            

        url (``str``):
            

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            fragment.GetCollectibleInfo
    """

    __slots__: List[str] = ["purchase_date", "currency", "amount", "crypto_currency", "crypto_amount", "url"]

    ID = 0x6ebdff91
    QUALNAME = "types.fragment.CollectibleInfo"

    def __init__(self, *, purchase_date: int, currency: str, amount: int, crypto_currency: str, crypto_amount: int, url: str) -> None:
        self.purchase_date = purchase_date  # int
        self.currency = currency  # string
        self.amount = amount  # long
        self.crypto_currency = crypto_currency  # string
        self.crypto_amount = crypto_amount  # long
        self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CollectibleInfo":
        # No flags
        
        purchase_date = Int.read(b)
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        crypto_currency = String.read(b)
        
        crypto_amount = Long.read(b)
        
        url = String.read(b)
        
        return CollectibleInfo(purchase_date=purchase_date, currency=currency, amount=amount, crypto_currency=crypto_currency, crypto_amount=crypto_amount, url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.purchase_date))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        b.write(String(self.crypto_currency))
        
        b.write(Long(self.crypto_amount))
        
        b.write(String(self.url))
        
        return b.getvalue()
