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


class StatsGraphAsync(TLObject):  # type: ignore
    """This channel statistics graph must be generated asynchronously using stats.loadAsyncGraph to reduce server load

    Constructor of :obj:`~hydrogram.raw.base.StatsGraph`.

    Details:
        - Layer: ``181``
        - ID: ``4A27EB2D``

    Parameters:
        token (``str``):
            Token to use for fetching the async graph

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.LoadAsyncGraph
    """

    __slots__: List[str] = ["token"]

    ID = 0x4a27eb2d
    QUALNAME = "types.StatsGraphAsync"

    def __init__(self, *, token: str) -> None:
        self.token = token  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StatsGraphAsync":
        # No flags
        
        token = String.read(b)
        
        return StatsGraphAsync(token=token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.token))
        
        return b.getvalue()
