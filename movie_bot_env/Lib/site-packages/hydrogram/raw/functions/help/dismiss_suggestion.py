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


class DismissSuggestion(TLObject):  # type: ignore
    """Dismiss a suggestion, see here for more info ».


    Details:
        - Layer: ``181``
        - ID: ``F50DBAA1``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            In the case of pending suggestions in channels, the channel ID.

        suggestion (``str``):
            Suggestion, see here for more info ».

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "suggestion"]

    ID = 0xf50dbaa1
    QUALNAME = "functions.help.DismissSuggestion"

    def __init__(self, *, peer: "raw.base.InputPeer", suggestion: str) -> None:
        self.peer = peer  # InputPeer
        self.suggestion = suggestion  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DismissSuggestion":
        # No flags
        
        peer = TLObject.read(b)
        
        suggestion = String.read(b)
        
        return DismissSuggestion(peer=peer, suggestion=suggestion)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(String(self.suggestion))
        
        return b.getvalue()
