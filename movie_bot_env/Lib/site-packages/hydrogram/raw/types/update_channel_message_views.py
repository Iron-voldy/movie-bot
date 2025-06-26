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


class UpdateChannelMessageViews(TLObject):  # type: ignore
    """The view counter of a message in a channel has changed

    Constructor of :obj:`~hydrogram.raw.base.Update`.

    Details:
        - Layer: ``181``
        - ID: ``F226AC08``

    Parameters:
        channel_id (``int`` ``64-bit``):
            Channel ID

        id (``int`` ``32-bit``):
            ID of the message

        views (``int`` ``32-bit``):
            New view counter

    """

    __slots__: List[str] = ["channel_id", "id", "views"]

    ID = 0xf226ac08
    QUALNAME = "types.UpdateChannelMessageViews"

    def __init__(self, *, channel_id: int, id: int, views: int) -> None:
        self.channel_id = channel_id  # long
        self.id = id  # int
        self.views = views  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelMessageViews":
        # No flags
        
        channel_id = Long.read(b)
        
        id = Int.read(b)
        
        views = Int.read(b)
        
        return UpdateChannelMessageViews(channel_id=channel_id, id=id, views=views)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.id))
        
        b.write(Int(self.views))
        
        return b.getvalue()
