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


class UpdateNewEncryptedMessage(TLObject):  # type: ignore
    """New encrypted message.

    Constructor of :obj:`~hydrogram.raw.base.Update`.

    Details:
        - Layer: ``181``
        - ID: ``12BCBD9A``

    Parameters:
        message (:obj:`EncryptedMessage <hydrogram.raw.base.EncryptedMessage>`):
            Message

        qts (``int`` ``32-bit``):
            New qts value, see updates » for more info.

    """

    __slots__: List[str] = ["message", "qts"]

    ID = 0x12bcbd9a
    QUALNAME = "types.UpdateNewEncryptedMessage"

    def __init__(self, *, message: "raw.base.EncryptedMessage", qts: int) -> None:
        self.message = message  # EncryptedMessage
        self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateNewEncryptedMessage":
        # No flags
        
        message = TLObject.read(b)
        
        qts = Int.read(b)
        
        return UpdateNewEncryptedMessage(message=message, qts=qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.message.write())
        
        b.write(Int(self.qts))
        
        return b.getvalue()
