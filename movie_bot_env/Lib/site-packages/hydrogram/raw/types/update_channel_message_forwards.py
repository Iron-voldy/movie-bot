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


class UpdateChannelMessageForwards(TLObject):  # type: ignore
    """The forward counter of a message in a channel has changed

    Constructor of :obj:`~hydrogram.raw.base.Update`.

    Details:
        - Layer: ``181``
        - ID: ``D29A27F4``

    Parameters:
        channel_id (``int`` ``64-bit``):
            Channel ID

        id (``int`` ``32-bit``):
            ID of the message

        forwards (``int`` ``32-bit``):
            New forward counter

    """

    __slots__: List[str] = ["channel_id", "id", "forwards"]

    ID = 0xd29a27f4
    QUALNAME = "types.UpdateChannelMessageForwards"

    def __init__(self, *, channel_id: int, id: int, forwards: int) -> None:
        self.channel_id = channel_id  # long
        self.id = id  # int
        self.forwards = forwards  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelMessageForwards":
        # No flags
        
        channel_id = Long.read(b)
        
        id = Int.read(b)
        
        forwards = Int.read(b)
        
        return UpdateChannelMessageForwards(channel_id=channel_id, id=id, forwards=forwards)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.id))
        
        b.write(Int(self.forwards))
        
        return b.getvalue()
