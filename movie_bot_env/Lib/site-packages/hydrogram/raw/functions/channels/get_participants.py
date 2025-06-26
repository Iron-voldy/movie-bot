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


class GetParticipants(TLObject):  # type: ignore
    """Get the participants of a supergroup/channel


    Details:
        - Layer: ``181``
        - ID: ``77CED9D0``

    Parameters:
        channel (:obj:`InputChannel <hydrogram.raw.base.InputChannel>`):
            Channel

        filter (:obj:`ChannelParticipantsFilter <hydrogram.raw.base.ChannelParticipantsFilter>`):
            Which participant types to fetch

        offset (``int`` ``32-bit``):
            Offset

        limit (``int`` ``32-bit``):
            Limit

        hash (``int`` ``64-bit``):
            Hash

    Returns:
        :obj:`channels.ChannelParticipants <hydrogram.raw.base.channels.ChannelParticipants>`
    """

    __slots__: List[str] = ["channel", "filter", "offset", "limit", "hash"]

    ID = 0x77ced9d0
    QUALNAME = "functions.channels.GetParticipants"

    def __init__(self, *, channel: "raw.base.InputChannel", filter: "raw.base.ChannelParticipantsFilter", offset: int, limit: int, hash: int) -> None:
        self.channel = channel  # InputChannel
        self.filter = filter  # ChannelParticipantsFilter
        self.offset = offset  # int
        self.limit = limit  # int
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetParticipants":
        # No flags
        
        channel = TLObject.read(b)
        
        filter = TLObject.read(b)
        
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetParticipants(channel=channel, filter=filter, offset=offset, limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.filter.write())
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
