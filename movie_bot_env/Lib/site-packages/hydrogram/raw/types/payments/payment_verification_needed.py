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


class PaymentVerificationNeeded(TLObject):  # type: ignore
    """Payment was not successful, additional verification is needed

    Constructor of :obj:`~hydrogram.raw.base.payments.PaymentResult`.

    Details:
        - Layer: ``181``
        - ID: ``D8411139``

    Parameters:
        url (``str``):
            URL for additional payment credentials verification

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.SendPaymentForm
            payments.SendStarsForm
    """

    __slots__: List[str] = ["url"]

    ID = 0xd8411139
    QUALNAME = "types.payments.PaymentVerificationNeeded"

    def __init__(self, *, url: str) -> None:
        self.url = url  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentVerificationNeeded":
        # No flags
        
        url = String.read(b)
        
        return PaymentVerificationNeeded(url=url)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        return b.getvalue()
