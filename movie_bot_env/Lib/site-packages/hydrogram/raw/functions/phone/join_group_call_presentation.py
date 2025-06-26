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


class JoinGroupCallPresentation(TLObject):  # type: ignore
    """Start screen sharing in a call


    Details:
        - Layer: ``181``
        - ID: ``CBEA6BC4``

    Parameters:
        call (:obj:`InputGroupCall <hydrogram.raw.base.InputGroupCall>`):
            The group call

        params (:obj:`DataJSON <hydrogram.raw.base.DataJSON>`):
            WebRTC parameters

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "params"]

    ID = 0xcbea6bc4
    QUALNAME = "functions.phone.JoinGroupCallPresentation"

    def __init__(self, *, call: "raw.base.InputGroupCall", params: "raw.base.DataJSON") -> None:
        self.call = call  # InputGroupCall
        self.params = params  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JoinGroupCallPresentation":
        # No flags
        
        call = TLObject.read(b)
        
        params = TLObject.read(b)
        
        return JoinGroupCallPresentation(call=call, params=params)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(self.params.write())
        
        return b.getvalue()
