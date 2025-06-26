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


class ToggleGroupCallRecord(TLObject):  # type: ignore
    """Start or stop recording a group call: the recorded audio and video streams will be automatically sent to Saved messages (the chat with ourselves).


    Details:
        - Layer: ``181``
        - ID: ``F128C708``

    Parameters:
        call (:obj:`InputGroupCall <hydrogram.raw.base.InputGroupCall>`):
            The group call or livestream

        start (``bool``, *optional*):
            Whether to start or stop recording

        video (``bool``, *optional*):
            Whether to also record video streams

        title (``str``, *optional*):
            Recording title

        video_portrait (``bool``, *optional*):
            If video stream recording is enabled, whether to record in portrait or landscape mode

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "start", "video", "title", "video_portrait"]

    ID = 0xf128c708
    QUALNAME = "functions.phone.ToggleGroupCallRecord"

    def __init__(self, *, call: "raw.base.InputGroupCall", start: Optional[bool] = None, video: Optional[bool] = None, title: Optional[str] = None, video_portrait: Optional[bool] = None) -> None:
        self.call = call  # InputGroupCall
        self.start = start  # flags.0?true
        self.video = video  # flags.2?true
        self.title = title  # flags.1?string
        self.video_portrait = video_portrait  # flags.2?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleGroupCallRecord":
        
        flags = Int.read(b)
        
        start = True if flags & (1 << 0) else False
        video = True if flags & (1 << 2) else False
        call = TLObject.read(b)
        
        title = String.read(b) if flags & (1 << 1) else None
        video_portrait = Bool.read(b) if flags & (1 << 2) else None
        return ToggleGroupCallRecord(call=call, start=start, video=video, title=title, video_portrait=video_portrait)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.start else 0
        flags |= (1 << 2) if self.video else 0
        flags |= (1 << 1) if self.title is not None else 0
        flags |= (1 << 2) if self.video_portrait is not None else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.video_portrait is not None:
            b.write(Bool(self.video_portrait))
        
        return b.getvalue()
