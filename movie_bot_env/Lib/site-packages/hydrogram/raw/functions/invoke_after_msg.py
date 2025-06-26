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


class InvokeAfterMsg(TLObject):  # type: ignore
    """Invokes a query after successful completion of one of the previous queries.


    Details:
        - Layer: ``181``
        - ID: ``CB9F372D``

    Parameters:
        msg_id (``int`` ``64-bit``):
            Message identifier on which a current query depends

        query (Any function from :obj:`~hydrogram.raw.functions`):
            The query itself

    Returns:
        Any object from :obj:`~hydrogram.raw.types`
    """

    __slots__: List[str] = ["msg_id", "query"]

    ID = 0xcb9f372d
    QUALNAME = "functions.InvokeAfterMsg"

    def __init__(self, *, msg_id: int, query: TLObject) -> None:
        self.msg_id = msg_id  # long
        self.query = query  # !X

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeAfterMsg":
        # No flags
        
        msg_id = Long.read(b)
        
        query = TLObject.read(b)
        
        return InvokeAfterMsg(msg_id=msg_id, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.msg_id))
        
        b.write(self.query.write())
        
        return b.getvalue()
