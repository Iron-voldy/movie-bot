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


class GetMessagePublicForwards(TLObject):  # type: ignore
    """Obtains a list of messages, indicating to which other public channels was a channel message forwarded.
Will return a list of messages with peer_id equal to the public channel to which this message was forwarded.


    Details:
        - Layer: ``181``
        - ID: ``5F150144``

    Parameters:
        channel (:obj:`InputChannel <hydrogram.raw.base.InputChannel>`):
            Source channel

        msg_id (``int`` ``32-bit``):
            Source message ID

        offset (``str``):
            Offset for pagination, empty string on first call, then use the next_offset field of the returned constructor (if present, otherwise no more results are available).

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

    Returns:
        :obj:`stats.PublicForwards <hydrogram.raw.base.stats.PublicForwards>`
    """

    __slots__: List[str] = ["channel", "msg_id", "offset", "limit"]

    ID = 0x5f150144
    QUALNAME = "functions.stats.GetMessagePublicForwards"

    def __init__(self, *, channel: "raw.base.InputChannel", msg_id: int, offset: str, limit: int) -> None:
        self.channel = channel  # InputChannel
        self.msg_id = msg_id  # int
        self.offset = offset  # string
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessagePublicForwards":
        # No flags
        
        channel = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        offset = String.read(b)
        
        limit = Int.read(b)
        
        return GetMessagePublicForwards(channel=channel, msg_id=msg_id, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Int(self.msg_id))
        
        b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
