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


class GetInlineBotResults(TLObject):  # type: ignore
    """Query an inline bot


    Details:
        - Layer: ``181``
        - ID: ``514E999D``

    Parameters:
        bot (:obj:`InputUser <hydrogram.raw.base.InputUser>`):
            The bot to query

        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            The currently opened chat

        query (``str``):
            The query

        offset (``str``):
            The offset within the results, will be passed directly as-is to the bot.

        geo_point (:obj:`InputGeoPoint <hydrogram.raw.base.InputGeoPoint>`, *optional*):
            The geolocation, if requested

    Returns:
        :obj:`messages.BotResults <hydrogram.raw.base.messages.BotResults>`
    """

    __slots__: List[str] = ["bot", "peer", "query", "offset", "geo_point"]

    ID = 0x514e999d
    QUALNAME = "functions.messages.GetInlineBotResults"

    def __init__(self, *, bot: "raw.base.InputUser", peer: "raw.base.InputPeer", query: str, offset: str, geo_point: "raw.base.InputGeoPoint" = None) -> None:
        self.bot = bot  # InputUser
        self.peer = peer  # InputPeer
        self.query = query  # string
        self.offset = offset  # string
        self.geo_point = geo_point  # flags.0?InputGeoPoint

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetInlineBotResults":
        
        flags = Int.read(b)
        
        bot = TLObject.read(b)
        
        peer = TLObject.read(b)
        
        geo_point = TLObject.read(b) if flags & (1 << 0) else None
        
        query = String.read(b)
        
        offset = String.read(b)
        
        return GetInlineBotResults(bot=bot, peer=peer, query=query, offset=offset, geo_point=geo_point)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.geo_point is not None else 0
        b.write(Int(flags))
        
        b.write(self.bot.write())
        
        b.write(self.peer.write())
        
        if self.geo_point is not None:
            b.write(self.geo_point.write())
        
        b.write(String(self.query))
        
        b.write(String(self.offset))
        
        return b.getvalue()
