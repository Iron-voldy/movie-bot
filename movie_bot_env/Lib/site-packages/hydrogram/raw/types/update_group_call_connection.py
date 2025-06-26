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


class UpdateGroupCallConnection(TLObject):  # type: ignore
    """New WebRTC parameters

    Constructor of :obj:`~hydrogram.raw.base.Update`.

    Details:
        - Layer: ``181``
        - ID: ``B783982``

    Parameters:
        params (:obj:`DataJSON <hydrogram.raw.base.DataJSON>`):
            WebRTC parameters

        presentation (``bool``, *optional*):
            Are these parameters related to the screen capture session currently in progress?

    """

    __slots__: List[str] = ["params", "presentation"]

    ID = 0xb783982
    QUALNAME = "types.UpdateGroupCallConnection"

    def __init__(self, *, params: "raw.base.DataJSON", presentation: Optional[bool] = None) -> None:
        self.params = params  # DataJSON
        self.presentation = presentation  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateGroupCallConnection":
        
        flags = Int.read(b)
        
        presentation = True if flags & (1 << 0) else False
        params = TLObject.read(b)
        
        return UpdateGroupCallConnection(params=params, presentation=presentation)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.presentation else 0
        b.write(Int(flags))
        
        b.write(self.params.write())
        
        return b.getvalue()
