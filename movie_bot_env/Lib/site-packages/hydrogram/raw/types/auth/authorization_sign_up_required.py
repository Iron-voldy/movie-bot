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


class AuthorizationSignUpRequired(TLObject):  # type: ignore
    """An account with this phone number doesn't exist on telegram: the user has to enter basic information and sign up

    Constructor of :obj:`~hydrogram.raw.base.auth.Authorization`.

    Details:
        - Layer: ``181``
        - ID: ``44747E9A``

    Parameters:
        terms_of_service (:obj:`help.TermsOfService <hydrogram.raw.base.help.TermsOfService>`, *optional*):
            Telegram's terms of service: the user must read and accept the terms of service before signing up to telegram

    Functions:
        This object can be returned by 7 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.SignUp
            auth.SignIn
            auth.ImportAuthorization
            auth.ImportBotAuthorization
            auth.CheckPassword
            auth.RecoverPassword
            auth.ImportWebTokenAuthorization
    """

    __slots__: List[str] = ["terms_of_service"]

    ID = 0x44747e9a
    QUALNAME = "types.auth.AuthorizationSignUpRequired"

    def __init__(self, *, terms_of_service: "raw.base.help.TermsOfService" = None) -> None:
        self.terms_of_service = terms_of_service  # flags.0?help.TermsOfService

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AuthorizationSignUpRequired":
        
        flags = Int.read(b)
        
        terms_of_service = TLObject.read(b) if flags & (1 << 0) else None
        
        return AuthorizationSignUpRequired(terms_of_service=terms_of_service)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.terms_of_service is not None else 0
        b.write(Int(flags))
        
        if self.terms_of_service is not None:
            b.write(self.terms_of_service.write())
        
        return b.getvalue()
