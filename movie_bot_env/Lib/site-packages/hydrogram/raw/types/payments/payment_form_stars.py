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


class PaymentFormStars(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.payments.PaymentForm`.

    Details:
        - Layer: ``181``
        - ID: ``7BF6B15C``

    Parameters:
        form_id (``int`` ``64-bit``):
            

        bot_id (``int`` ``64-bit``):
            

        title (``str``):
            

        description (``str``):
            

        invoice (:obj:`Invoice <hydrogram.raw.base.Invoice>`):
            

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            

        photo (:obj:`WebDocument <hydrogram.raw.base.WebDocument>`, *optional*):
            

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetPaymentForm
    """

    __slots__: List[str] = ["form_id", "bot_id", "title", "description", "invoice", "users", "photo"]

    ID = 0x7bf6b15c
    QUALNAME = "types.payments.PaymentFormStars"

    def __init__(self, *, form_id: int, bot_id: int, title: str, description: str, invoice: "raw.base.Invoice", users: List["raw.base.User"], photo: "raw.base.WebDocument" = None) -> None:
        self.form_id = form_id  # long
        self.bot_id = bot_id  # long
        self.title = title  # string
        self.description = description  # string
        self.invoice = invoice  # Invoice
        self.users = users  # Vector<User>
        self.photo = photo  # flags.5?WebDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentFormStars":
        
        flags = Int.read(b)
        
        form_id = Long.read(b)
        
        bot_id = Long.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 5) else None
        
        invoice = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return PaymentFormStars(form_id=form_id, bot_id=bot_id, title=title, description=description, invoice=invoice, users=users, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.photo is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.form_id))
        
        b.write(Long(self.bot_id))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        b.write(self.invoice.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()
