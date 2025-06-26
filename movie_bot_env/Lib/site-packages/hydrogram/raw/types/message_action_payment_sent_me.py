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


class MessageActionPaymentSentMe(TLObject):  # type: ignore
    """A user just sent a payment to me (a bot)

    Constructor of :obj:`~hydrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``8F31B327``

    Parameters:
        currency (``str``):
            Three-letter ISO 4217 currency code

        total_amount (``int`` ``64-bit``):
            Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

        payload (``bytes``):
            Bot specified invoice payload

        charge (:obj:`PaymentCharge <hydrogram.raw.base.PaymentCharge>`):
            Provider payment identifier

        recurring_init (``bool``, *optional*):
            Whether this is the first payment of a recurring payment we just subscribed to

        recurring_used (``bool``, *optional*):
            Whether this payment is part of a recurring payment

        info (:obj:`PaymentRequestedInfo <hydrogram.raw.base.PaymentRequestedInfo>`, *optional*):
            Order info provided by the user

        shipping_option_id (``str``, *optional*):
            Identifier of the shipping option chosen by the user

    """

    __slots__: List[str] = ["currency", "total_amount", "payload", "charge", "recurring_init", "recurring_used", "info", "shipping_option_id"]

    ID = 0x8f31b327
    QUALNAME = "types.MessageActionPaymentSentMe"

    def __init__(self, *, currency: str, total_amount: int, payload: bytes, charge: "raw.base.PaymentCharge", recurring_init: Optional[bool] = None, recurring_used: Optional[bool] = None, info: "raw.base.PaymentRequestedInfo" = None, shipping_option_id: Optional[str] = None) -> None:
        self.currency = currency  # string
        self.total_amount = total_amount  # long
        self.payload = payload  # bytes
        self.charge = charge  # PaymentCharge
        self.recurring_init = recurring_init  # flags.2?true
        self.recurring_used = recurring_used  # flags.3?true
        self.info = info  # flags.0?PaymentRequestedInfo
        self.shipping_option_id = shipping_option_id  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionPaymentSentMe":
        
        flags = Int.read(b)
        
        recurring_init = True if flags & (1 << 2) else False
        recurring_used = True if flags & (1 << 3) else False
        currency = String.read(b)
        
        total_amount = Long.read(b)
        
        payload = Bytes.read(b)
        
        info = TLObject.read(b) if flags & (1 << 0) else None
        
        shipping_option_id = String.read(b) if flags & (1 << 1) else None
        charge = TLObject.read(b)
        
        return MessageActionPaymentSentMe(currency=currency, total_amount=total_amount, payload=payload, charge=charge, recurring_init=recurring_init, recurring_used=recurring_used, info=info, shipping_option_id=shipping_option_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.recurring_init else 0
        flags |= (1 << 3) if self.recurring_used else 0
        flags |= (1 << 0) if self.info is not None else 0
        flags |= (1 << 1) if self.shipping_option_id is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.currency))
        
        b.write(Long(self.total_amount))
        
        b.write(Bytes(self.payload))
        
        if self.info is not None:
            b.write(self.info.write())
        
        if self.shipping_option_id is not None:
            b.write(String(self.shipping_option_id))
        
        b.write(self.charge.write())
        
        return b.getvalue()
