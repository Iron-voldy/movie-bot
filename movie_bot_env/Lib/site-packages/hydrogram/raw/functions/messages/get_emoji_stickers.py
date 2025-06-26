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


class GetEmojiStickers(TLObject):  # type: ignore
    """Gets the list of currently installed custom emoji stickersets.


    Details:
        - Layer: ``181``
        - ID: ``FBFCA18F``

    Parameters:
        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here.Note: the usual hash generation algorithm cannot be used in this case, please re-use the messages.allStickers.hash field returned by a previous call to the method, or pass 0 if this is the first call.

    Returns:
        :obj:`messages.AllStickers <hydrogram.raw.base.messages.AllStickers>`
    """

    __slots__: List[str] = ["hash"]

    ID = 0xfbfca18f
    QUALNAME = "functions.messages.GetEmojiStickers"

    def __init__(self, *, hash: int) -> None:
        self.hash = hash  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetEmojiStickers":
        # No flags
        
        hash = Long.read(b)
        
        return GetEmojiStickers(hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        return b.getvalue()
