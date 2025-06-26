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


class MediaAreaChannelPost(TLObject):  # type: ignore
    """Represents a channel post.

    Constructor of :obj:`~hydrogram.raw.base.MediaArea`.

    Details:
        - Layer: ``181``
        - ID: ``770416AF``

    Parameters:
        coordinates (:obj:`MediaAreaCoordinates <hydrogram.raw.base.MediaAreaCoordinates>`):
            The size and location of the media area corresponding to the location sticker on top of the story media.

        channel_id (``int`` ``64-bit``):
            The channel that posted the message

        msg_id (``int`` ``32-bit``):
            ID of the channel message

    """

    __slots__: List[str] = ["coordinates", "channel_id", "msg_id"]

    ID = 0x770416af
    QUALNAME = "types.MediaAreaChannelPost"

    def __init__(self, *, coordinates: "raw.base.MediaAreaCoordinates", channel_id: int, msg_id: int) -> None:
        self.coordinates = coordinates  # MediaAreaCoordinates
        self.channel_id = channel_id  # long
        self.msg_id = msg_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MediaAreaChannelPost":
        # No flags
        
        coordinates = TLObject.read(b)
        
        channel_id = Long.read(b)
        
        msg_id = Int.read(b)
        
        return MediaAreaChannelPost(coordinates=coordinates, channel_id=channel_id, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.coordinates.write())
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()
