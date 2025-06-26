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


class TermsOfServiceUpdateEmpty(TLObject):  # type: ignore
    """No changes were made to telegram's terms of service

    Constructor of :obj:`~hydrogram.raw.base.help.TermsOfServiceUpdate`.

    Details:
        - Layer: ``181``
        - ID: ``E3309F7F``

    Parameters:
        expires (``int`` ``32-bit``):
            New TOS updates will have to be queried using help.getTermsOfServiceUpdate in expires seconds

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetTermsOfServiceUpdate
    """

    __slots__: List[str] = ["expires"]

    ID = 0xe3309f7f
    QUALNAME = "types.help.TermsOfServiceUpdateEmpty"

    def __init__(self, *, expires: int) -> None:
        self.expires = expires  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TermsOfServiceUpdateEmpty":
        # No flags
        
        expires = Int.read(b)
        
        return TermsOfServiceUpdateEmpty(expires=expires)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.expires))
        
        return b.getvalue()
