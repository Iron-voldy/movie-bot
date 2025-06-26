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


class GetAllStories(TLObject):  # type: ignore
    """Fetch the List of active (or active and hidden) stories, see here » for more info on watching stories.


    Details:
        - Layer: ``181``
        - ID: ``EEB0D625``

    Parameters:
        next (``bool``, *optional*):
            If next and state are both set, uses the passed state to paginate to the next results; if neither state nor next are set, fetches the initial page; if state is set and next is not set, check for changes in the active/hidden peerset, see here » for more info on the full flow.

        hidden (``bool``, *optional*):
            If set, fetches the hidden active story list, otherwise fetches the active story list, see here » for more info on the full flow.

        state (``str``, *optional*):
            If next and state are both set, uses the passed state to paginate to the next results; if neither state nor next are set, fetches the initial page; if state is set and next is not set, check for changes in the active/hidden peerset, see here » for more info on the full flow.

    Returns:
        :obj:`stories.AllStories <hydrogram.raw.base.stories.AllStories>`
    """

    __slots__: List[str] = ["next", "hidden", "state"]

    ID = 0xeeb0d625
    QUALNAME = "functions.stories.GetAllStories"

    def __init__(self, *, next: Optional[bool] = None, hidden: Optional[bool] = None, state: Optional[str] = None) -> None:
        self.next = next  # flags.1?true
        self.hidden = hidden  # flags.2?true
        self.state = state  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetAllStories":
        
        flags = Int.read(b)
        
        next = True if flags & (1 << 1) else False
        hidden = True if flags & (1 << 2) else False
        state = String.read(b) if flags & (1 << 0) else None
        return GetAllStories(next=next, hidden=hidden, state=state)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.next else 0
        flags |= (1 << 2) if self.hidden else 0
        flags |= (1 << 0) if self.state is not None else 0
        b.write(Int(flags))
        
        if self.state is not None:
            b.write(String(self.state))
        
        return b.getvalue()
