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


class GetGroupCallStreamChannels(TLObject):  # type: ignore
    """Get info about RTMP streams in a group call or livestream.
This method should be invoked to the same group/channel-related DC used for downloading livestream chunks.
As usual, the media DC is preferred, if available.


    Details:
        - Layer: ``181``
        - ID: ``1AB21940``

    Parameters:
        call (:obj:`InputGroupCall <hydrogram.raw.base.InputGroupCall>`):
            Group call or livestream

    Returns:
        :obj:`phone.GroupCallStreamChannels <hydrogram.raw.base.phone.GroupCallStreamChannels>`
    """

    __slots__: List[str] = ["call"]

    ID = 0x1ab21940
    QUALNAME = "functions.phone.GetGroupCallStreamChannels"

    def __init__(self, *, call: "raw.base.InputGroupCall") -> None:
        self.call = call  # InputGroupCall

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGroupCallStreamChannels":
        # No flags
        
        call = TLObject.read(b)
        
        return GetGroupCallStreamChannels(call=call)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        return b.getvalue()
