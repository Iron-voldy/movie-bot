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


class ExportedStoryLink(TLObject):  # type: ignore
    """Represents a story deep link.

    Constructor of :obj:`~hydrogram.raw.base.ExportedStoryLink`.

    Details:
        - Layer: ``181``
        - ID: ``3FC9053B``

    Parameters:
        link (``str``):
            The story deep link.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stories.ExportStoryLink
    """

    __slots__: List[str] = ["link"]

    ID = 0x3fc9053b
    QUALNAME = "types.ExportedStoryLink"

    def __init__(self, *, link: str) -> None:
        self.link = link  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedStoryLink":
        # No flags
        
        link = String.read(b)
        
        return ExportedStoryLink(link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.link))
        
        return b.getvalue()
