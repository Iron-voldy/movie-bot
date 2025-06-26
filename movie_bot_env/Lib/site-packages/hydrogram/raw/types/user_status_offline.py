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


class UserStatusOffline(TLObject):  # type: ignore
    """The user's offline status.

    Constructor of :obj:`~hydrogram.raw.base.UserStatus`.

    Details:
        - Layer: ``181``
        - ID: ``8C703F``

    Parameters:
        was_online (``int`` ``32-bit``):
            Time the user was last seen online

    """

    __slots__: List[str] = ["was_online"]

    ID = 0x8c703f
    QUALNAME = "types.UserStatusOffline"

    def __init__(self, *, was_online: int) -> None:
        self.was_online = was_online  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UserStatusOffline":
        # No flags
        
        was_online = Int.read(b)
        
        return UserStatusOffline(was_online=was_online)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.was_online))
        
        return b.getvalue()
