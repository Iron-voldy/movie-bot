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


class StatsGraph(TLObject):  # type: ignore
    """Channel statistics graph

    Constructor of :obj:`~hydrogram.raw.base.StatsGraph`.

    Details:
        - Layer: ``181``
        - ID: ``8EA464B6``

    Parameters:
        json (:obj:`DataJSON <hydrogram.raw.base.DataJSON>`):
            Statistics data

        zoom_token (``str``, *optional*):
            Zoom token

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.LoadAsyncGraph
    """

    __slots__: List[str] = ["json", "zoom_token"]

    ID = 0x8ea464b6
    QUALNAME = "types.StatsGraph"

    def __init__(self, *, json: "raw.base.DataJSON", zoom_token: Optional[str] = None) -> None:
        self.json = json  # DataJSON
        self.zoom_token = zoom_token  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsGraph":
        
        flags = Int.read(b)
        
        json = TLObject.read(b)
        
        zoom_token = String.read(b) if flags & (1 << 0) else None
        return StatsGraph(json=json, zoom_token=zoom_token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.zoom_token is not None else 0
        b.write(Int(flags))
        
        b.write(self.json.write())
        
        if self.zoom_token is not None:
            b.write(String(self.zoom_token))
        
        return b.getvalue()
