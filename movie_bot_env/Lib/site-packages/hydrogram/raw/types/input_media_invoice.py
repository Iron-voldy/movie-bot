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


class InputMediaInvoice(TLObject):  # type: ignore
    """Generated invoice of a bot payment

    Constructor of :obj:`~hydrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``181``
        - ID: ``405FEF0D``

    Parameters:
        title (``str``):
            Product name, 1-32 characters

        description (``str``):
            Product description, 1-255 characters

        invoice (:obj:`Invoice <hydrogram.raw.base.Invoice>`):
            The actual invoice

        payload (``bytes``):
            Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.

        provider_data (:obj:`DataJSON <hydrogram.raw.base.DataJSON>`):
            JSON-encoded data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.

        photo (:obj:`InputWebDocument <hydrogram.raw.base.InputWebDocument>`, *optional*):
            URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.

        provider (``str``, *optional*):
            Payments provider token, obtained via Botfather

        start_param (``str``, *optional*):
            Unique bot deep links start parameter. If present, forwarded copies of the sent message will have a URL button with a deep link to the bot (instead of a Pay button), with the value used as the start parameter. If absent, forwarded copies of the sent message will have a Pay button, allowing multiple users to pay directly from the forwarded message, using the same invoice.

        extended_media (:obj:`InputMedia <hydrogram.raw.base.InputMedia>`, *optional*):
            Extended media

    """

    __slots__: List[str] = ["title", "description", "invoice", "payload", "provider_data", "photo", "provider", "start_param", "extended_media"]

    ID = 0x405fef0d
    QUALNAME = "types.InputMediaInvoice"

    def __init__(self, *, title: str, description: str, invoice: "raw.base.Invoice", payload: bytes, provider_data: "raw.base.DataJSON", photo: "raw.base.InputWebDocument" = None, provider: Optional[str] = None, start_param: Optional[str] = None, extended_media: "raw.base.InputMedia" = None) -> None:
        self.title = title  # string
        self.description = description  # string
        self.invoice = invoice  # Invoice
        self.payload = payload  # bytes
        self.provider_data = provider_data  # DataJSON
        self.photo = photo  # flags.0?InputWebDocument
        self.provider = provider  # flags.3?string
        self.start_param = start_param  # flags.1?string
        self.extended_media = extended_media  # flags.2?InputMedia

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaInvoice":
        
        flags = Int.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 0) else None
        
        invoice = TLObject.read(b)
        
        payload = Bytes.read(b)
        
        provider = String.read(b) if flags & (1 << 3) else None
        provider_data = TLObject.read(b)
        
        start_param = String.read(b) if flags & (1 << 1) else None
        extended_media = TLObject.read(b) if flags & (1 << 2) else None
        
        return InputMediaInvoice(title=title, description=description, invoice=invoice, payload=payload, provider_data=provider_data, photo=photo, provider=provider, start_param=start_param, extended_media=extended_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 3) if self.provider is not None else 0
        flags |= (1 << 1) if self.start_param is not None else 0
        flags |= (1 << 2) if self.extended_media is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        b.write(self.invoice.write())
        
        b.write(Bytes(self.payload))
        
        if self.provider is not None:
            b.write(String(self.provider))
        
        b.write(self.provider_data.write())
        
        if self.start_param is not None:
            b.write(String(self.start_param))
        
        if self.extended_media is not None:
            b.write(self.extended_media.write())
        
        return b.getvalue()
