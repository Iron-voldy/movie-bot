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


class ToggleSlowMode(TLObject):  # type: ignore
    """Toggle supergroup slow mode: if enabled, users will only be able to send one message every seconds seconds


    Details:
        - Layer: ``181``
        - ID: ``EDD49EF0``

    Parameters:
        channel (:obj:`InputChannel <hydrogram.raw.base.InputChannel>`):
            The supergroup

        seconds (``int`` ``32-bit``):
            Users will only be able to send one message every seconds seconds, 0 to disable the limitation

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "seconds"]

    ID = 0xedd49ef0
    QUALNAME = "functions.channels.ToggleSlowMode"

    def __init__(self, *, channel: "raw.base.InputChannel", seconds: int) -> None:
        self.channel = channel  # InputChannel
        self.seconds = seconds  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleSlowMode":
        # No flags
        
        channel = TLObject.read(b)
        
        seconds = Int.read(b)
        
        return ToggleSlowMode(channel=channel, seconds=seconds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Int(self.seconds))
        
        return b.getvalue()
