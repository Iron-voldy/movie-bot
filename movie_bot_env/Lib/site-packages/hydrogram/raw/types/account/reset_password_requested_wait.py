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


class ResetPasswordRequestedWait(TLObject):  # type: ignore
    """You successfully requested a password reset, please wait until the specified date before finalizing the reset.

    Constructor of :obj:`~hydrogram.raw.base.account.ResetPasswordResult`.

    Details:
        - Layer: ``181``
        - ID: ``E9EFFC7D``

    Parameters:
        until_date (``int`` ``32-bit``):
            Wait until this date before finalizing the reset.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.ResetPassword
    """

    __slots__: List[str] = ["until_date"]

    ID = 0xe9effc7d
    QUALNAME = "types.account.ResetPasswordRequestedWait"

    def __init__(self, *, until_date: int) -> None:
        self.until_date = until_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResetPasswordRequestedWait":
        # No flags
        
        until_date = Int.read(b)
        
        return ResetPasswordRequestedWait(until_date=until_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.until_date))
        
        return b.getvalue()
