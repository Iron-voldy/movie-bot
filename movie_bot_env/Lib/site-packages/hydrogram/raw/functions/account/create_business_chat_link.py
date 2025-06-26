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


class CreateBusinessChatLink(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``181``
        - ID: ``8851E68E``

    Parameters:
        link (:obj:`InputBusinessChatLink <hydrogram.raw.base.InputBusinessChatLink>`):
            

    Returns:
        :obj:`BusinessChatLink <hydrogram.raw.base.BusinessChatLink>`
    """

    __slots__: List[str] = ["link"]

    ID = 0x8851e68e
    QUALNAME = "functions.account.CreateBusinessChatLink"

    def __init__(self, *, link: "raw.base.InputBusinessChatLink") -> None:
        self.link = link  # InputBusinessChatLink

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateBusinessChatLink":
        # No flags
        
        link = TLObject.read(b)
        
        return CreateBusinessChatLink(link=link)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.link.write())
        
        return b.getvalue()
