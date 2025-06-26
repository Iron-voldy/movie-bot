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


class UserEmpty(TLObject):  # type: ignore
    """Empty constructor, non-existent user.

    Constructor of :obj:`~hydrogram.raw.base.User`.

    Details:
        - Layer: ``181``
        - ID: ``D3BC4B7A``

    Parameters:
        id (``int`` ``64-bit``):
            User identifier or 0

    Functions:
        This object can be returned by 5 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.UpdateProfile
            account.UpdateUsername
            account.ChangePhone
            users.GetUsers
            contacts.ImportContactToken
    """

    __slots__: List[str] = ["id"]

    ID = 0xd3bc4b7a
    QUALNAME = "types.UserEmpty"

    def __init__(self, *, id: int) -> None:
        self.id = id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserEmpty":
        # No flags
        
        id = Long.read(b)
        
        return UserEmpty(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        return b.getvalue()
