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


class GetLeaveChatlistSuggestions(TLObject):  # type: ignore
    """Returns identifiers of pinned or always included chats from a chat folder imported using a chat folder deep link », which are suggested to be left when the chat folder is deleted.


    Details:
        - Layer: ``181``
        - ID: ``FDBCD714``

    Parameters:
        chatlist (:obj:`InputChatlist <hydrogram.raw.base.InputChatlist>`):
            Folder ID

    Returns:
        List of :obj:`Peer <hydrogram.raw.base.Peer>`
    """

    __slots__: List[str] = ["chatlist"]

    ID = 0xfdbcd714
    QUALNAME = "functions.chatlists.GetLeaveChatlistSuggestions"

    def __init__(self, *, chatlist: "raw.base.InputChatlist") -> None:
        self.chatlist = chatlist  # InputChatlist

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetLeaveChatlistSuggestions":
        # No flags
        
        chatlist = TLObject.read(b)
        
        return GetLeaveChatlistSuggestions(chatlist=chatlist)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.chatlist.write())
        
        return b.getvalue()
