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


class ReceivedQueue(TLObject):  # type: ignore
    """Confirms receipt of messages in a secret chat by client, cancels push notifications.
The method returns a list of random_ids of messages for which push notifications were cancelled.


    Details:
        - Layer: ``181``
        - ID: ``55A5BB66``

    Parameters:
        max_qts (``int`` ``32-bit``):
            Maximum qts value available at the client

    Returns:
        List of ``int`` ``64-bit``
    """

    __slots__: List[str] = ["max_qts"]

    ID = 0x55a5bb66
    QUALNAME = "functions.messages.ReceivedQueue"

    def __init__(self, *, max_qts: int) -> None:
        self.max_qts = max_qts  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReceivedQueue":
        # No flags
        
        max_qts = Int.read(b)
        
        return ReceivedQueue(max_qts=max_qts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.max_qts))
        
        return b.getvalue()
