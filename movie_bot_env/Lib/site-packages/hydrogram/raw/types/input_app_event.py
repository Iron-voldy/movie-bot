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


class InputAppEvent(TLObject):  # type: ignore
    """Event that occurred in the application.

    Constructor of :obj:`~hydrogram.raw.base.InputAppEvent`.

    Details:
        - Layer: ``181``
        - ID: ``1D1B1245``

    Parameters:
        time (``float`` ``64-bit``):
            Client's exact timestamp for the event

        type (``str``):
            Type of event

        peer (``int`` ``64-bit``):
            Arbitrary numeric value for more convenient selection of certain event types, or events referring to a certain object

        data (:obj:`JSONValue <hydrogram.raw.base.JSONValue>`):
            Details of the event

    """

    __slots__: List[str] = ["time", "type", "peer", "data"]

    ID = 0x1d1b1245
    QUALNAME = "types.InputAppEvent"

    def __init__(self, *, time: float, type: str, peer: int, data: "raw.base.JSONValue") -> None:
        self.time = time  # double
        self.type = type  # string
        self.peer = peer  # long
        self.data = data  # JSONValue

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputAppEvent":
        # No flags
        
        time = Double.read(b)
        
        type = String.read(b)
        
        peer = Long.read(b)
        
        data = TLObject.read(b)
        
        return InputAppEvent(time=time, type=type, peer=peer, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Double(self.time))
        
        b.write(String(self.type))
        
        b.write(Long(self.peer))
        
        b.write(self.data.write())
        
        return b.getvalue()
