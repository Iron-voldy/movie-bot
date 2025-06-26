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


class InputStorePaymentPremiumSubscription(TLObject):  # type: ignore
    """Info about a Telegram Premium purchase

    Constructor of :obj:`~hydrogram.raw.base.InputStorePaymentPurpose`.

    Details:
        - Layer: ``181``
        - ID: ``A6751E66``

    Parameters:
        restore (``bool``, *optional*):
            Pass true if this is a restore of a Telegram Premium purchase; only for the App Store

        upgrade (``bool``, *optional*):
            Pass true if this is an upgrade from a monthly subscription to a yearly subscription; only for App Store

    """

    __slots__: List[str] = ["restore", "upgrade"]

    ID = 0xa6751e66
    QUALNAME = "types.InputStorePaymentPremiumSubscription"

    def __init__(self, *, restore: Optional[bool] = None, upgrade: Optional[bool] = None) -> None:
        self.restore = restore  # flags.0?true
        self.upgrade = upgrade  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStorePaymentPremiumSubscription":
        
        flags = Int.read(b)
        
        restore = True if flags & (1 << 0) else False
        upgrade = True if flags & (1 << 1) else False
        return InputStorePaymentPremiumSubscription(restore=restore, upgrade=upgrade)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.restore else 0
        flags |= (1 << 1) if self.upgrade else 0
        b.write(Int(flags))
        
        return b.getvalue()
