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


class MissingInvitee(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.MissingInvitee`.

    Details:
        - Layer: ``181``
        - ID: ``628C9224``

    Parameters:
        user_id (``int`` ``64-bit``):
            

        premium_would_allow_invite (``bool``, *optional*):
            

        premium_required_for_pm (``bool``, *optional*):
            

    """

    __slots__: List[str] = ["user_id", "premium_would_allow_invite", "premium_required_for_pm"]

    ID = 0x628c9224
    QUALNAME = "types.MissingInvitee"

    def __init__(self, *, user_id: int, premium_would_allow_invite: Optional[bool] = None, premium_required_for_pm: Optional[bool] = None) -> None:
        self.user_id = user_id  # long
        self.premium_would_allow_invite = premium_would_allow_invite  # flags.0?true
        self.premium_required_for_pm = premium_required_for_pm  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MissingInvitee":
        
        flags = Int.read(b)
        
        premium_would_allow_invite = True if flags & (1 << 0) else False
        premium_required_for_pm = True if flags & (1 << 1) else False
        user_id = Long.read(b)
        
        return MissingInvitee(user_id=user_id, premium_would_allow_invite=premium_would_allow_invite, premium_required_for_pm=premium_required_for_pm)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.premium_would_allow_invite else 0
        flags |= (1 << 1) if self.premium_required_for_pm else 0
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        return b.getvalue()
