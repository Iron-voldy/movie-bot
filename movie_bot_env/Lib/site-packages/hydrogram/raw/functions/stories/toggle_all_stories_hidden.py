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


class ToggleAllStoriesHidden(TLObject):  # type: ignore
    """Hide the active stories of a specific peer, preventing them from being displayed on the action bar on the homescreen.


    Details:
        - Layer: ``181``
        - ID: ``7C2557C4``

    Parameters:
        hidden (``bool``):
            Whether to hide or unhide all active stories of the peer

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["hidden"]

    ID = 0x7c2557c4
    QUALNAME = "functions.stories.ToggleAllStoriesHidden"

    def __init__(self, *, hidden: bool) -> None:
        self.hidden = hidden  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleAllStoriesHidden":
        # No flags
        
        hidden = Bool.read(b)
        
        return ToggleAllStoriesHidden(hidden=hidden)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bool(self.hidden))
        
        return b.getvalue()
