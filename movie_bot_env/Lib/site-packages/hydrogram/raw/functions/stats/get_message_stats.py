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


class GetMessageStats(TLObject):  # type: ignore
    """Get message statistics


    Details:
        - Layer: ``181``
        - ID: ``B6E0A3F5``

    Parameters:
        channel (:obj:`InputChannel <hydrogram.raw.base.InputChannel>`):
            Channel ID

        msg_id (``int`` ``32-bit``):
            Message ID

        dark (``bool``, *optional*):
            Whether to enable dark theme for graph colors

    Returns:
        :obj:`stats.MessageStats <hydrogram.raw.base.stats.MessageStats>`
    """

    __slots__: List[str] = ["channel", "msg_id", "dark"]

    ID = 0xb6e0a3f5
    QUALNAME = "functions.stats.GetMessageStats"

    def __init__(self, *, channel: "raw.base.InputChannel", msg_id: int, dark: Optional[bool] = None) -> None:
        self.channel = channel  # InputChannel
        self.msg_id = msg_id  # int
        self.dark = dark  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessageStats":
        
        flags = Int.read(b)
        
        dark = True if flags & (1 << 0) else False
        channel = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        return GetMessageStats(channel=channel, msg_id=msg_id, dark=dark)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.dark else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()
