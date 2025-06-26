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


class SetDefaultReaction(TLObject):  # type: ignore
    """Change default emoji reaction to use in the quick reaction menu: the value is synced across devices and can be fetched using help.getConfig, reactions_default field.


    Details:
        - Layer: ``181``
        - ID: ``4F47A016``

    Parameters:
        reaction (:obj:`Reaction <hydrogram.raw.base.Reaction>`):
            New emoji reaction

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["reaction"]

    ID = 0x4f47a016
    QUALNAME = "functions.messages.SetDefaultReaction"

    def __init__(self, *, reaction: "raw.base.Reaction") -> None:
        self.reaction = reaction  # Reaction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetDefaultReaction":
        # No flags
        
        reaction = TLObject.read(b)
        
        return SetDefaultReaction(reaction=reaction)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.reaction.write())
        
        return b.getvalue()
