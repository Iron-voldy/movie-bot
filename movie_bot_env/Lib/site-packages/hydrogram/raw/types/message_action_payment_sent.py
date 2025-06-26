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


class MessageActionPaymentSent(TLObject):  # type: ignore
    """A payment was sent

    Constructor of :obj:`~hydrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``96163F56``

    Parameters:
        currency (``str``):
            Three-letter ISO 4217 currency code

        total_amount (``int`` ``64-bit``):
            Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

        recurring_init (``bool``, *optional*):
            Whether this is the first payment of a recurring payment we just subscribed to

        recurring_used (``bool``, *optional*):
            Whether this payment is part of a recurring payment

        invoice_slug (``str``, *optional*):
            An invoice slug taken from an invoice deep link or from the premium_invoice_slug app config parameter »

    """

    __slots__: List[str] = ["currency", "total_amount", "recurring_init", "recurring_used", "invoice_slug"]

    ID = 0x96163f56
    QUALNAME = "types.MessageActionPaymentSent"

    def __init__(self, *, currency: str, total_amount: int, recurring_init: Optional[bool] = None, recurring_used: Optional[bool] = None, invoice_slug: Optional[str] = None) -> None:
        self.currency = currency  # string
        self.total_amount = total_amount  # long
        self.recurring_init = recurring_init  # flags.2?true
        self.recurring_used = recurring_used  # flags.3?true
        self.invoice_slug = invoice_slug  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionPaymentSent":
        
        flags = Int.read(b)
        
        recurring_init = True if flags & (1 << 2) else False
        recurring_used = True if flags & (1 << 3) else False
        currency = String.read(b)
        
        total_amount = Long.read(b)
        
        invoice_slug = String.read(b) if flags & (1 << 0) else None
        return MessageActionPaymentSent(currency=currency, total_amount=total_amount, recurring_init=recurring_init, recurring_used=recurring_used, invoice_slug=invoice_slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.recurring_init else 0
        flags |= (1 << 3) if self.recurring_used else 0
        flags |= (1 << 0) if self.invoice_slug is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.currency))
        
        b.write(Long(self.total_amount))
        
        if self.invoice_slug is not None:
            b.write(String(self.invoice_slug))
        
        return b.getvalue()
