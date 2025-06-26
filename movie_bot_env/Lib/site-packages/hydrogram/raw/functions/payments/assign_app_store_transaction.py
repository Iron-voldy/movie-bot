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


class AssignAppStoreTransaction(TLObject):  # type: ignore
    """Informs server about a purchase made through the App Store: for official applications only.


    Details:
        - Layer: ``181``
        - ID: ``80ED747D``

    Parameters:
        receipt (``bytes``):
            Receipt

        purpose (:obj:`InputStorePaymentPurpose <hydrogram.raw.base.InputStorePaymentPurpose>`):
            Payment purpose

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["receipt", "purpose"]

    ID = 0x80ed747d
    QUALNAME = "functions.payments.AssignAppStoreTransaction"

    def __init__(self, *, receipt: bytes, purpose: "raw.base.InputStorePaymentPurpose") -> None:
        self.receipt = receipt  # bytes
        self.purpose = purpose  # InputStorePaymentPurpose

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AssignAppStoreTransaction":
        # No flags
        
        receipt = Bytes.read(b)
        
        purpose = TLObject.read(b)
        
        return AssignAppStoreTransaction(receipt=receipt, purpose=purpose)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.receipt))
        
        b.write(self.purpose.write())
        
        return b.getvalue()
