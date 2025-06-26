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


class MessageActionGroupCall(TLObject):  # type: ignore
    """The group call has ended

    Constructor of :obj:`~hydrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``7A0D7F42``

    Parameters:
        call (:obj:`InputGroupCall <hydrogram.raw.base.InputGroupCall>`):
            Group call

        duration (``int`` ``32-bit``, *optional*):
            Group call duration

    """

    __slots__: List[str] = ["call", "duration"]

    ID = 0x7a0d7f42
    QUALNAME = "types.MessageActionGroupCall"

    def __init__(self, *, call: "raw.base.InputGroupCall", duration: Optional[int] = None) -> None:
        self.call = call  # InputGroupCall
        self.duration = duration  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGroupCall":
        
        flags = Int.read(b)
        
        call = TLObject.read(b)
        
        duration = Int.read(b) if flags & (1 << 0) else None
        return MessageActionGroupCall(call=call, duration=duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.duration is not None else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        if self.duration is not None:
            b.write(Int(self.duration))
        
        return b.getvalue()
