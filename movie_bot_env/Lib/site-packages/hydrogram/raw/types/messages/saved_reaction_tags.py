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


class SavedReactionTags(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.messages.SavedReactionTags`.

    Details:
        - Layer: ``181``
        - ID: ``3259950A``

    Parameters:
        tags (List of :obj:`SavedReactionTag <hydrogram.raw.base.SavedReactionTag>`):
            

        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSavedReactionTags
    """

    __slots__: List[str] = ["tags", "hash"]

    ID = 0x3259950a
    QUALNAME = "types.messages.SavedReactionTags"

    def __init__(self, *, tags: List["raw.base.SavedReactionTag"], hash: int) -> None:
        self.tags = tags  # Vector<SavedReactionTag>
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedReactionTags":
        # No flags
        
        tags = TLObject.read(b)
        
        hash = Long.read(b)
        
        return SavedReactionTags(tags=tags, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.tags))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
