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


class RecoverPassword(TLObject):  # type: ignore
    """Reset the 2FA password using the recovery code sent using auth.requestPasswordRecovery.


    Details:
        - Layer: ``181``
        - ID: ``37096C70``

    Parameters:
        code (``str``):
            Code received via email

        new_settings (:obj:`account.PasswordInputSettings <hydrogram.raw.base.account.PasswordInputSettings>`, *optional*):
            New password

    Returns:
        :obj:`auth.Authorization <hydrogram.raw.base.auth.Authorization>`
    """

    __slots__: List[str] = ["code", "new_settings"]

    ID = 0x37096c70
    QUALNAME = "functions.auth.RecoverPassword"

    def __init__(self, *, code: str, new_settings: "raw.base.account.PasswordInputSettings" = None) -> None:
        self.code = code  # string
        self.new_settings = new_settings  # flags.0?account.PasswordInputSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RecoverPassword":
        
        flags = Int.read(b)
        
        code = String.read(b)
        
        new_settings = TLObject.read(b) if flags & (1 << 0) else None
        
        return RecoverPassword(code=code, new_settings=new_settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.new_settings is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.code))
        
        if self.new_settings is not None:
            b.write(self.new_settings.write())
        
        return b.getvalue()
