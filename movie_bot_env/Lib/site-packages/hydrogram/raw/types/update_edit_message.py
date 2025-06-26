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


class UpdateEditMessage(TLObject):  # type: ignore
    """A message was edited

    Constructor of :obj:`~hydrogram.raw.base.Update`.

    Details:
        - Layer: ``181``
        - ID: ``E40370A3``

    Parameters:
        message (:obj:`Message <hydrogram.raw.base.Message>`):
            The new edited message

        pts (``int`` ``32-bit``):
            PTS

        pts_count (``int`` ``32-bit``):
            PTS count

    """

    __slots__: List[str] = ["message", "pts", "pts_count"]

    ID = 0xe40370a3
    QUALNAME = "types.UpdateEditMessage"

    def __init__(self, *, message: "raw.base.Message", pts: int, pts_count: int) -> None:
        self.message = message  # Message
        self.pts = pts  # int
        self.pts_count = pts_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateEditMessage":
        # No flags
        
        message = TLObject.read(b)
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        return UpdateEditMessage(message=message, pts=pts, pts_count=pts_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.message.write())
        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        return b.getvalue()
