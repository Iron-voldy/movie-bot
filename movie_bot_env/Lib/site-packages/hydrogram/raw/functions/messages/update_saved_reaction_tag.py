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


class UpdateSavedReactionTag(TLObject):  # type: ignore
    """Update the description of a saved message tag ».


    Details:
        - Layer: ``181``
        - ID: ``60297DEC``

    Parameters:
        reaction (:obj:`Reaction <hydrogram.raw.base.Reaction>`):
            Reaction associated to the tag

        title (``str``, *optional*):
            Tag description, max 12 UTF-8 characters; to remove the description call the method without setting this flag.

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["reaction", "title"]

    ID = 0x60297dec
    QUALNAME = "functions.messages.UpdateSavedReactionTag"

    def __init__(self, *, reaction: "raw.base.Reaction", title: Optional[str] = None) -> None:
        self.reaction = reaction  # Reaction
        self.title = title  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateSavedReactionTag":
        
        flags = Int.read(b)
        
        reaction = TLObject.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        return UpdateSavedReactionTag(reaction=reaction, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        b.write(Int(flags))
        
        b.write(self.reaction.write())
        
        if self.title is not None:
            b.write(String(self.title))
        
        return b.getvalue()
