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


class UpdateBotWebhookJSONQuery(TLObject):  # type: ignore
    """A new incoming query; for bots only

    Constructor of :obj:`~hydrogram.raw.base.Update`.

    Details:
        - Layer: ``181``
        - ID: ``9B9240A6``

    Parameters:
        query_id (``int`` ``64-bit``):
            Query identifier

        data (:obj:`DataJSON <hydrogram.raw.base.DataJSON>`):
            Query data

        timeout (``int`` ``32-bit``):
            Query timeout

    """

    __slots__: List[str] = ["query_id", "data", "timeout"]

    ID = 0x9b9240a6
    QUALNAME = "types.UpdateBotWebhookJSONQuery"

    def __init__(self, *, query_id: int, data: "raw.base.DataJSON", timeout: int) -> None:
        self.query_id = query_id  # long
        self.data = data  # DataJSON
        self.timeout = timeout  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotWebhookJSONQuery":
        # No flags
        
        query_id = Long.read(b)
        
        data = TLObject.read(b)
        
        timeout = Int.read(b)
        
        return UpdateBotWebhookJSONQuery(query_id=query_id, data=data, timeout=timeout)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.query_id))
        
        b.write(self.data.write())
        
        b.write(Int(self.timeout))
        
        return b.getvalue()
