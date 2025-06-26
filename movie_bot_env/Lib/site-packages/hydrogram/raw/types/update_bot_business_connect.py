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


class UpdateBotBusinessConnect(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.Update`.

    Details:
        - Layer: ``181``
        - ID: ``8AE5C97A``

    Parameters:
        connection (:obj:`BotBusinessConnection <hydrogram.raw.base.BotBusinessConnection>`):
            

        qts (``int`` ``32-bit``):
            

    """

    __slots__: List[str] = ["connection", "qts"]

    ID = 0x8ae5c97a
    QUALNAME = "types.UpdateBotBusinessConnect"

    def __init__(self, *, connection: "raw.base.BotBusinessConnection", qts: int) -> None:
        self.connection = connection  # BotBusinessConnection
        self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotBusinessConnect":
        # No flags
        
        connection = TLObject.read(b)
        
        qts = Int.read(b)
        
        return UpdateBotBusinessConnect(connection=connection, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.connection.write())
        
        b.write(Int(self.qts))
        
        return b.getvalue()
