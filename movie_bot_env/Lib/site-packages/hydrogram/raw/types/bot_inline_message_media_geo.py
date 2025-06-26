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


class BotInlineMessageMediaGeo(TLObject):  # type: ignore
    """Send a geolocation

    Constructor of :obj:`~hydrogram.raw.base.BotInlineMessage`.

    Details:
        - Layer: ``181``
        - ID: ``51846FD``

    Parameters:
        geo (:obj:`GeoPoint <hydrogram.raw.base.GeoPoint>`):
            Geolocation

        heading (``int`` ``32-bit``, *optional*):
            For live locations, a direction in which the location moves, in degrees; 1-360.

        period (``int`` ``32-bit``, *optional*):
            Validity period

        proximity_notification_radius (``int`` ``32-bit``, *optional*):
            For live locations, a maximum distance to another chat member for proximity alerts, in meters (0-100000).

        reply_markup (:obj:`ReplyMarkup <hydrogram.raw.base.ReplyMarkup>`, *optional*):
            Inline keyboard

    """

    __slots__: List[str] = ["geo", "heading", "period", "proximity_notification_radius", "reply_markup"]

    ID = 0x51846fd
    QUALNAME = "types.BotInlineMessageMediaGeo"

    def __init__(self, *, geo: "raw.base.GeoPoint", heading: Optional[int] = None, period: Optional[int] = None, proximity_notification_radius: Optional[int] = None, reply_markup: "raw.base.ReplyMarkup" = None) -> None:
        self.geo = geo  # GeoPoint
        self.heading = heading  # flags.0?int
        self.period = period  # flags.1?int
        self.proximity_notification_radius = proximity_notification_radius  # flags.3?int
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInlineMessageMediaGeo":
        
        flags = Int.read(b)
        
        geo = TLObject.read(b)
        
        heading = Int.read(b) if flags & (1 << 0) else None
        period = Int.read(b) if flags & (1 << 1) else None
        proximity_notification_radius = Int.read(b) if flags & (1 << 3) else None
        reply_markup = TLObject.read(b) if flags & (1 << 2) else None
        
        return BotInlineMessageMediaGeo(geo=geo, heading=heading, period=period, proximity_notification_radius=proximity_notification_radius, reply_markup=reply_markup)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.heading is not None else 0
        flags |= (1 << 1) if self.period is not None else 0
        flags |= (1 << 3) if self.proximity_notification_radius is not None else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        b.write(Int(flags))
        
        b.write(self.geo.write())
        
        if self.heading is not None:
            b.write(Int(self.heading))
        
        if self.period is not None:
            b.write(Int(self.period))
        
        if self.proximity_notification_radius is not None:
            b.write(Int(self.proximity_notification_radius))
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        return b.getvalue()
