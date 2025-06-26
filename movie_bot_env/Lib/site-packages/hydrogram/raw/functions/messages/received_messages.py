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


class ReceivedMessages(TLObject):  # type: ignore
    """Confirms receipt of messages by a client, cancels PUSH-notification sending.


    Details:
        - Layer: ``181``
        - ID: ``5A954C0``

    Parameters:
        max_id (``int`` ``32-bit``):
            Maximum message ID available in a client.

    Returns:
        List of :obj:`ReceivedNotifyMessage <hydrogram.raw.base.ReceivedNotifyMessage>`
    """

    __slots__: List[str] = ["max_id"]

    ID = 0x5a954c0
    QUALNAME = "functions.messages.ReceivedMessages"

    def __init__(self, *, max_id: int) -> None:
        self.max_id = max_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReceivedMessages":
        # No flags
        
        max_id = Int.read(b)
        
        return ReceivedMessages(max_id=max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.max_id))
        
        return b.getvalue()
