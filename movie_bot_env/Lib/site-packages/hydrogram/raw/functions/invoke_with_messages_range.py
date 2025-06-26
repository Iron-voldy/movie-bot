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


class InvokeWithMessagesRange(TLObject):  # type: ignore
    """Invoke with the given message range


    Details:
        - Layer: ``181``
        - ID: ``365275F2``

    Parameters:
        range (:obj:`MessageRange <hydrogram.raw.base.MessageRange>`):
            Message range

        query (Any function from :obj:`~hydrogram.raw.functions`):
            Query

    Returns:
        Any object from :obj:`~hydrogram.raw.types`
    """

    __slots__: List[str] = ["range", "query"]

    ID = 0x365275f2
    QUALNAME = "functions.InvokeWithMessagesRange"

    def __init__(self, *, range: "raw.base.MessageRange", query: TLObject) -> None:
        self.range = range  # MessageRange
        self.query = query  # !X

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWithMessagesRange":
        # No flags
        
        range = TLObject.read(b)
        
        query = TLObject.read(b)
        
        return InvokeWithMessagesRange(range=range, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.range.write())
        
        b.write(self.query.write())
        
        return b.getvalue()
