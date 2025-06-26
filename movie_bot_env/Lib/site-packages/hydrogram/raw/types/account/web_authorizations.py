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


class WebAuthorizations(TLObject):  # type: ignore
    """Web authorizations

    Constructor of :obj:`~hydrogram.raw.base.account.WebAuthorizations`.

    Details:
        - Layer: ``181``
        - ID: ``ED56C9FC``

    Parameters:
        authorizations (List of :obj:`WebAuthorization <hydrogram.raw.base.WebAuthorization>`):
            Web authorization list

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            Users

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetWebAuthorizations
    """

    __slots__: List[str] = ["authorizations", "users"]

    ID = 0xed56c9fc
    QUALNAME = "types.account.WebAuthorizations"

    def __init__(self, *, authorizations: List["raw.base.WebAuthorization"], users: List["raw.base.User"]) -> None:
        self.authorizations = authorizations  # Vector<WebAuthorization>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebAuthorizations":
        # No flags
        
        authorizations = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return WebAuthorizations(authorizations=authorizations, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.authorizations))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
