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


class EmailVerifiedLogin(TLObject):  # type: ignore
    """The email was verified correctly, and a login code was just sent to it.

    Constructor of :obj:`~hydrogram.raw.base.account.EmailVerified`.

    Details:
        - Layer: ``181``
        - ID: ``E1BB0D61``

    Parameters:
        email (``str``):
            The verified email address.

        sent_code (:obj:`auth.SentCode <hydrogram.raw.base.auth.SentCode>`):
            Info about the sent login code

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.VerifyEmail
    """

    __slots__: List[str] = ["email", "sent_code"]

    ID = 0xe1bb0d61
    QUALNAME = "types.account.EmailVerifiedLogin"

    def __init__(self, *, email: str, sent_code: "raw.base.auth.SentCode") -> None:
        self.email = email  # string
        self.sent_code = sent_code  # auth.SentCode

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EmailVerifiedLogin":
        # No flags
        
        email = String.read(b)
        
        sent_code = TLObject.read(b)
        
        return EmailVerifiedLogin(email=email, sent_code=sent_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.email))
        
        b.write(self.sent_code.write())
        
        return b.getvalue()
