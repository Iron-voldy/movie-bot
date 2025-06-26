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


class InputBotInlineMessageMediaInvoice(TLObject):  # type: ignore
    """An invoice

    Constructor of :obj:`~hydrogram.raw.base.InputBotInlineMessage`.

    Details:
        - Layer: ``181``
        - ID: ``D7E78225``

    Parameters:
        title (``str``):
            Product name, 1-32 characters

        description (``str``):
            Product description, 1-255 characters

        invoice (:obj:`Invoice <hydrogram.raw.base.Invoice>`):
            The invoice

        payload (``bytes``):
            Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.

        provider (``str``):
            Payments provider token, obtained via Botfather

        provider_data (:obj:`DataJSON <hydrogram.raw.base.DataJSON>`):
            A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider.

        photo (:obj:`InputWebDocument <hydrogram.raw.base.InputWebDocument>`, *optional*):
            Invoice photo

        reply_markup (:obj:`ReplyMarkup <hydrogram.raw.base.ReplyMarkup>`, *optional*):
            Inline keyboard

    """

    __slots__: List[str] = ["title", "description", "invoice", "payload", "provider", "provider_data", "photo", "reply_markup"]

    ID = 0xd7e78225
    QUALNAME = "types.InputBotInlineMessageMediaInvoice"

    def __init__(self, *, title: str, description: str, invoice: "raw.base.Invoice", payload: bytes, provider: str, provider_data: "raw.base.DataJSON", photo: "raw.base.InputWebDocument" = None, reply_markup: "raw.base.ReplyMarkup" = None) -> None:
        self.title = title  # string
        self.description = description  # string
        self.invoice = invoice  # Invoice
        self.payload = payload  # bytes
        self.provider = provider  # string
        self.provider_data = provider_data  # DataJSON
        self.photo = photo  # flags.0?InputWebDocument
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineMessageMediaInvoice":
        
        flags = Int.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 0) else None
        
        invoice = TLObject.read(b)
        
        payload = Bytes.read(b)
        
        provider = String.read(b)
        
        provider_data = TLObject.read(b)
        
        reply_markup = TLObject.read(b) if flags & (1 << 2) else None
        
        return InputBotInlineMessageMediaInvoice(title=title, description=description, invoice=invoice, payload=payload, provider=provider, provider_data=provider_data, photo=photo, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        b.write(self.invoice.write())
        
        b.write(Bytes(self.payload))
        
        b.write(String(self.provider))
        
        b.write(self.provider_data.write())
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        return b.getvalue()
