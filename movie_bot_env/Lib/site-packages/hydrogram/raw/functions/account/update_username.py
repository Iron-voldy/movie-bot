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


class UpdateUsername(TLObject):  # type: ignore
    """Changes username for the current user.


    Details:
        - Layer: ``181``
        - ID: ``3E0BDD7C``

    Parameters:
        username (``str``):
            username or empty string if username is to be removedAccepted characters: a-z (case-insensitive), 0-9 and underscores.Length: 5-32 characters.

    Returns:
        :obj:`User <hydrogram.raw.base.User>`
    """

    __slots__: List[str] = ["username"]

    ID = 0x3e0bdd7c
    QUALNAME = "functions.account.UpdateUsername"

    def __init__(self, *, username: str) -> None:
        self.username = username  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateUsername":
        # No flags
        
        username = String.read(b)
        
        return UpdateUsername(username=username)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.username))
        
        return b.getvalue()
