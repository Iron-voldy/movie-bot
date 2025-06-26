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


class LeaveChatlist(TLObject):  # type: ignore
    """Delete a folder imported using a chat folder deep link »


    Details:
        - Layer: ``181``
        - ID: ``74FAE13A``

    Parameters:
        chatlist (:obj:`InputChatlist <hydrogram.raw.base.InputChatlist>`):
            Folder ID

        peers (List of :obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Also leave the specified channels and groups

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["chatlist", "peers"]

    ID = 0x74fae13a
    QUALNAME = "functions.chatlists.LeaveChatlist"

    def __init__(self, *, chatlist: "raw.base.InputChatlist", peers: List["raw.base.InputPeer"]) -> None:
        self.chatlist = chatlist  # InputChatlist
        self.peers = peers  # Vector<InputPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LeaveChatlist":
        # No flags
        
        chatlist = TLObject.read(b)
        
        peers = TLObject.read(b)
        
        return LeaveChatlist(chatlist=chatlist, peers=peers)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.chatlist.write())
        
        b.write(Vector(self.peers))
        
        return b.getvalue()
