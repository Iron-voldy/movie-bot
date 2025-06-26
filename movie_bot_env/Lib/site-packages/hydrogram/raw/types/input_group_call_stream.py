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


class InputGroupCallStream(TLObject):  # type: ignore
    """Chunk of a livestream

    Constructor of :obj:`~hydrogram.raw.base.InputFileLocation`.

    Details:
        - Layer: ``181``
        - ID: ``598A92A``

    Parameters:
        call (:obj:`InputGroupCall <hydrogram.raw.base.InputGroupCall>`):
            Livestream info

        time_ms (``int`` ``64-bit``):
            Timestamp in milliseconds

        scale (``int`` ``32-bit``):
            Specifies the duration of the video segment to fetch in milliseconds, by bitshifting 1000 to the right scale times: duration_ms := 1000 >> scale

        video_channel (``int`` ``32-bit``, *optional*):
            Selected video channel

        video_quality (``int`` ``32-bit``, *optional*):
            Selected video quality (0 = lowest, 1 = medium, 2 = best)

    """

    __slots__: List[str] = ["call", "time_ms", "scale", "video_channel", "video_quality"]

    ID = 0x598a92a
    QUALNAME = "types.InputGroupCallStream"

    def __init__(self, *, call: "raw.base.InputGroupCall", time_ms: int, scale: int, video_channel: Optional[int] = None, video_quality: Optional[int] = None) -> None:
        self.call = call  # InputGroupCall
        self.time_ms = time_ms  # long
        self.scale = scale  # int
        self.video_channel = video_channel  # flags.0?int
        self.video_quality = video_quality  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputGroupCallStream":
        
        flags = Int.read(b)
        
        call = TLObject.read(b)
        
        time_ms = Long.read(b)
        
        scale = Int.read(b)
        
        video_channel = Int.read(b) if flags & (1 << 0) else None
        video_quality = Int.read(b) if flags & (1 << 0) else None
        return InputGroupCallStream(call=call, time_ms=time_ms, scale=scale, video_channel=video_channel, video_quality=video_quality)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.video_channel is not None else 0
        flags |= (1 << 0) if self.video_quality is not None else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        b.write(Long(self.time_ms))
        
        b.write(Int(self.scale))
        
        if self.video_channel is not None:
            b.write(Int(self.video_channel))
        
        if self.video_quality is not None:
            b.write(Int(self.video_quality))
        
        return b.getvalue()
