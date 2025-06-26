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


class DestroySessionNone(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~hydrogram.raw.base.DestroySessionRes`.

    Details:
        - Layer: ``181``
        - ID: ``62D350C9``

    Parameters:
        session_id (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            DestroySession
    """

    __slots__: List[str] = ["session_id"]

    ID = 0x62d350c9
    QUALNAME = "types.DestroySessionNone"

    def __init__(self, *, session_id: int) -> None:
        self.session_id = session_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DestroySessionNone":
        # No flags
        
        session_id = Long.read(b)
        
        return DestroySessionNone(session_id=session_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.session_id))
        
        return b.getvalue()
