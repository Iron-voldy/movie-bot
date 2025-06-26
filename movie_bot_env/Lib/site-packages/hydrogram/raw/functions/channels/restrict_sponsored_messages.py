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


class RestrictSponsoredMessages(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``181``
        - ID: ``9AE91519``

    Parameters:
        channel (:obj:`InputChannel <hydrogram.raw.base.InputChannel>`):
            

        restricted (``bool``):
            

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "restricted"]

    ID = 0x9ae91519
    QUALNAME = "functions.channels.RestrictSponsoredMessages"

    def __init__(self, *, channel: "raw.base.InputChannel", restricted: bool) -> None:
        self.channel = channel  # InputChannel
        self.restricted = restricted  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RestrictSponsoredMessages":
        # No flags
        
        channel = TLObject.read(b)
        
        restricted = Bool.read(b)
        
        return RestrictSponsoredMessages(channel=channel, restricted=restricted)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Bool(self.restricted))
        
        return b.getvalue()
