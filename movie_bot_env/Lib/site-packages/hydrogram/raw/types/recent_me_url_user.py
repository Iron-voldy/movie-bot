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


class RecentMeUrlUser(TLObject):  # type: ignore
    """Recent t.me link to a user

    Constructor of :obj:`~hydrogram.raw.base.RecentMeUrl`.

    Details:
        - Layer: ``181``
        - ID: ``B92C09E2``

    Parameters:
        url (``str``):
            URL

        user_id (``int`` ``64-bit``):
            User ID

    """

    __slots__: List[str] = ["url", "user_id"]

    ID = 0xb92c09e2
    QUALNAME = "types.RecentMeUrlUser"

    def __init__(self, *, url: str, user_id: int) -> None:
        self.url = url  # string
        self.user_id = user_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RecentMeUrlUser":
        # No flags
        
        url = String.read(b)
        
        user_id = Long.read(b)
        
        return RecentMeUrlUser(url=url, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(Long(self.user_id))
        
        return b.getvalue()
