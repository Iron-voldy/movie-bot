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


class SentCodeTypeSetUpEmailRequired(TLObject):  # type: ignore
    """The user should add and verify an email address in order to login as described here ».

    Constructor of :obj:`~hydrogram.raw.base.auth.SentCodeType`.

    Details:
        - Layer: ``181``
        - ID: ``A5491DEA``

    Parameters:
        apple_signin_allowed (``bool``, *optional*):
            Whether authorization through Apple ID is allowed

        google_signin_allowed (``bool``, *optional*):
            Whether authorization through Google ID is allowed

    """

    __slots__: List[str] = ["apple_signin_allowed", "google_signin_allowed"]

    ID = 0xa5491dea
    QUALNAME = "types.auth.SentCodeTypeSetUpEmailRequired"

    def __init__(self, *, apple_signin_allowed: Optional[bool] = None, google_signin_allowed: Optional[bool] = None) -> None:
        self.apple_signin_allowed = apple_signin_allowed  # flags.0?true
        self.google_signin_allowed = google_signin_allowed  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeSetUpEmailRequired":
        
        flags = Int.read(b)
        
        apple_signin_allowed = True if flags & (1 << 0) else False
        google_signin_allowed = True if flags & (1 << 1) else False
        return SentCodeTypeSetUpEmailRequired(apple_signin_allowed=apple_signin_allowed, google_signin_allowed=google_signin_allowed)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.apple_signin_allowed else 0
        flags |= (1 << 1) if self.google_signin_allowed else 0
        b.write(Int(flags))
        
        return b.getvalue()
