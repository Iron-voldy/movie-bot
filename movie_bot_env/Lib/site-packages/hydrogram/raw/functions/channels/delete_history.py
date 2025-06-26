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


class DeleteHistory(TLObject):  # type: ignore
    """Delete the history of a supergroup


    Details:
        - Layer: ``181``
        - ID: ``9BAA9647``

    Parameters:
        channel (:obj:`InputChannel <hydrogram.raw.base.InputChannel>`):
            Supergroup whose history must be deleted

        max_id (``int`` ``32-bit``):
            ID of message up to which the history must be deleted

        for_everyone (``bool``, *optional*):
            Whether the history should be deleted for everyone

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "max_id", "for_everyone"]

    ID = 0x9baa9647
    QUALNAME = "functions.channels.DeleteHistory"

    def __init__(self, *, channel: "raw.base.InputChannel", max_id: int, for_everyone: Optional[bool] = None) -> None:
        self.channel = channel  # InputChannel
        self.max_id = max_id  # int
        self.for_everyone = for_everyone  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteHistory":
        
        flags = Int.read(b)
        
        for_everyone = True if flags & (1 << 0) else False
        channel = TLObject.read(b)
        
        max_id = Int.read(b)
        
        return DeleteHistory(channel=channel, max_id=max_id, for_everyone=for_everyone)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.for_everyone else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(Int(self.max_id))
        
        return b.getvalue()
