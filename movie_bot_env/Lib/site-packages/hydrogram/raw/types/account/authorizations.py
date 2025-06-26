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


class Authorizations(TLObject):  # type: ignore
    """Logged-in sessions

    Constructor of :obj:`~hydrogram.raw.base.account.Authorizations`.

    Details:
        - Layer: ``181``
        - ID: ``4BFF8EA0``

    Parameters:
        authorization_ttl_days (``int`` ``32-bit``):
            Time-to-live of session

        authorizations (List of :obj:`Authorization <hydrogram.raw.base.Authorization>`):
            Logged-in sessions

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetAuthorizations
    """

    __slots__: List[str] = ["authorization_ttl_days", "authorizations"]

    ID = 0x4bff8ea0
    QUALNAME = "types.account.Authorizations"

    def __init__(self, *, authorization_ttl_days: int, authorizations: List["raw.base.Authorization"]) -> None:
        self.authorization_ttl_days = authorization_ttl_days  # int
        self.authorizations = authorizations  # Vector<Authorization>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Authorizations":
        # No flags
        
        authorization_ttl_days = Int.read(b)
        
        authorizations = TLObject.read(b)
        
        return Authorizations(authorization_ttl_days=authorization_ttl_days, authorizations=authorizations)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.authorization_ttl_days))
        
        b.write(Vector(self.authorizations))
        
        return b.getvalue()
