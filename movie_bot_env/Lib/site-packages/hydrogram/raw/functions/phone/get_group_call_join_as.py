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


class GetGroupCallJoinAs(TLObject):  # type: ignore
    """Get a list of peers that can be used to join a group call, presenting yourself as a specific user/channel.


    Details:
        - Layer: ``181``
        - ID: ``EF7C213A``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            The dialog whose group call or livestream we're trying to join

    Returns:
        :obj:`phone.JoinAsPeers <hydrogram.raw.base.phone.JoinAsPeers>`
    """

    __slots__: List[str] = ["peer"]

    ID = 0xef7c213a
    QUALNAME = "functions.phone.GetGroupCallJoinAs"

    def __init__(self, *, peer: "raw.base.InputPeer") -> None:
        self.peer = peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGroupCallJoinAs":
        # No flags
        
        peer = TLObject.read(b)
        
        return GetGroupCallJoinAs(peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        return b.getvalue()
