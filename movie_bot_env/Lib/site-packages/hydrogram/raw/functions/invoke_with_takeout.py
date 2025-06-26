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


class InvokeWithTakeout(TLObject):  # type: ignore
    """Invoke a method within a takeout session, see here » for more info.


    Details:
        - Layer: ``181``
        - ID: ``ACA9FD2E``

    Parameters:
        takeout_id (``int`` ``64-bit``):
            Takeout session ID »

        query (Any function from :obj:`~hydrogram.raw.functions`):
            Query

    Returns:
        Any object from :obj:`~hydrogram.raw.types`
    """

    __slots__: List[str] = ["takeout_id", "query"]

    ID = 0xaca9fd2e
    QUALNAME = "functions.InvokeWithTakeout"

    def __init__(self, *, takeout_id: int, query: TLObject) -> None:
        self.takeout_id = takeout_id  # long
        self.query = query  # !X

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWithTakeout":
        # No flags
        
        takeout_id = Long.read(b)
        
        query = TLObject.read(b)
        
        return InvokeWithTakeout(takeout_id=takeout_id, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.takeout_id))
        
        b.write(self.query.write())
        
        return b.getvalue()
