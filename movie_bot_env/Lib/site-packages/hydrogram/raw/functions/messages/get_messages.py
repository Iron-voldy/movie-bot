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


class GetMessages(TLObject):  # type: ignore
    """Returns the list of messages by their IDs.


    Details:
        - Layer: ``181``
        - ID: ``63C66506``

    Parameters:
        id (List of :obj:`InputMessage <hydrogram.raw.base.InputMessage>`):
            Message ID list

    Returns:
        :obj:`messages.Messages <hydrogram.raw.base.messages.Messages>`
    """

    __slots__: List[str] = ["id"]

    ID = 0x63c66506
    QUALNAME = "functions.messages.GetMessages"

    def __init__(self, *, id: List["raw.base.InputMessage"]) -> None:
        self.id = id  # Vector<InputMessage>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessages":
        # No flags
        
        id = TLObject.read(b)
        
        return GetMessages(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.id))
        
        return b.getvalue()
