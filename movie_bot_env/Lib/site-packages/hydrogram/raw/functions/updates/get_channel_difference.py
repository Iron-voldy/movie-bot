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


class GetChannelDifference(TLObject):  # type: ignore
    """Returns the difference between the current state of updates of a certain channel and transmitted.


    Details:
        - Layer: ``181``
        - ID: ``3173D78``

    Parameters:
        channel (:obj:`InputChannel <hydrogram.raw.base.InputChannel>`):
            The channel

        filter (:obj:`ChannelMessagesFilter <hydrogram.raw.base.ChannelMessagesFilter>`):
            Messsage filter

        pts (``int`` ``32-bit``):
            Persistent timestamp (see updates)

        limit (``int`` ``32-bit``):
            How many updates to fetch, max 100000Ordinary (non-bot) users are supposed to pass 10-100

        force (``bool``, *optional*):
            Set to true to skip some possibly unneeded updates and reduce server-side load

    Returns:
        :obj:`updates.ChannelDifference <hydrogram.raw.base.updates.ChannelDifference>`
    """

    __slots__: List[str] = ["channel", "filter", "pts", "limit", "force"]

    ID = 0x3173d78
    QUALNAME = "functions.updates.GetChannelDifference"

    def __init__(self, *, channel: "raw.base.InputChannel", filter: "raw.base.ChannelMessagesFilter", pts: int, limit: int, force: Optional[bool] = None) -> None:
        self.channel = channel  # InputChannel
        self.filter = filter  # ChannelMessagesFilter
        self.pts = pts  # int
        self.limit = limit  # int
        self.force = force  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetChannelDifference":
        
        flags = Int.read(b)
        
        force = True if flags & (1 << 0) else False
        channel = TLObject.read(b)
        
        filter = TLObject.read(b)
        
        pts = Int.read(b)
        
        limit = Int.read(b)
        
        return GetChannelDifference(channel=channel, filter=filter, pts=pts, limit=limit, force=force)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.force else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(self.filter.write())
        
        b.write(Int(self.pts))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
