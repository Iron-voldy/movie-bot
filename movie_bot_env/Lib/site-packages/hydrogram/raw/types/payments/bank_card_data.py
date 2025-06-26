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


class BankCardData(TLObject):  # type: ignore
    """Credit card info, provided by the card's bank(s)

    Constructor of :obj:`~hydrogram.raw.base.payments.BankCardData`.

    Details:
        - Layer: ``181``
        - ID: ``3E24E573``

    Parameters:
        title (``str``):
            Credit card title

        open_urls (List of :obj:`BankCardOpenUrl <hydrogram.raw.base.BankCardOpenUrl>`):
            Info URL(s) provided by the card's bank(s)

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetBankCardData
    """

    __slots__: List[str] = ["title", "open_urls"]

    ID = 0x3e24e573
    QUALNAME = "types.payments.BankCardData"

    def __init__(self, *, title: str, open_urls: List["raw.base.BankCardOpenUrl"]) -> None:
        self.title = title  # string
        self.open_urls = open_urls  # Vector<BankCardOpenUrl>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BankCardData":
        # No flags
        
        title = String.read(b)
        
        open_urls = TLObject.read(b)
        
        return BankCardData(title=title, open_urls=open_urls)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.title))
        
        b.write(Vector(self.open_urls))
        
        return b.getvalue()
