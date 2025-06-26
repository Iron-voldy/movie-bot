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


class InputMediaAreaChannelPost(TLObject):  # type: ignore
    """Represents a channel post

    Constructor of :obj:`~hydrogram.raw.base.MediaArea`.

    Details:
        - Layer: ``181``
        - ID: ``2271F2BF``

    Parameters:
        coordinates (:obj:`MediaAreaCoordinates <hydrogram.raw.base.MediaAreaCoordinates>`):
            The size and location of the media area corresponding to the location sticker on top of the story media.

        channel (:obj:`InputChannel <hydrogram.raw.base.InputChannel>`):
            The channel that posted the message

        msg_id (``int`` ``32-bit``):
            ID of the channel message

    """

    __slots__: List[str] = ["coordinates", "channel", "msg_id"]

    ID = 0x2271f2bf
    QUALNAME = "types.InputMediaAreaChannelPost"

    def __init__(self, *, coordinates: "raw.base.MediaAreaCoordinates", channel: "raw.base.InputChannel", msg_id: int) -> None:
        self.coordinates = coordinates  # MediaAreaCoordinates
        self.channel = channel  # InputChannel
        self.msg_id = msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaAreaChannelPost":
        # No flags
        
        coordinates = TLObject.read(b)
        
        channel = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        return InputMediaAreaChannelPost(coordinates=coordinates, channel=channel, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.coordinates.write())
        
        b.write(self.channel.write())
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()
