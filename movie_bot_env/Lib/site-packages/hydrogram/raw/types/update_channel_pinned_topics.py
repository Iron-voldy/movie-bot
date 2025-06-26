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


class UpdateChannelPinnedTopics(TLObject):  # type: ignore
    """The pinned topics of a forum have changed.

    Constructor of :obj:`~hydrogram.raw.base.Update`.

    Details:
        - Layer: ``181``
        - ID: ``FE198602``

    Parameters:
        channel_id (``int`` ``64-bit``):
            Forum ID.

        order (List of ``int`` ``32-bit``, *optional*):
            Ordered list containing the IDs of all pinned topics.

    """

    __slots__: List[str] = ["channel_id", "order"]

    ID = 0xfe198602
    QUALNAME = "types.UpdateChannelPinnedTopics"

    def __init__(self, *, channel_id: int, order: Optional[List[int]] = None) -> None:
        self.channel_id = channel_id  # long
        self.order = order  # flags.0?Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelPinnedTopics":
        
        flags = Int.read(b)
        
        channel_id = Long.read(b)
        
        order = TLObject.read(b, Int) if flags & (1 << 0) else []
        
        return UpdateChannelPinnedTopics(channel_id=channel_id, order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.order else 0
        b.write(Int(flags))
        
        b.write(Long(self.channel_id))
        
        if self.order is not None:
            b.write(Vector(self.order, Int))
        
        return b.getvalue()
