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


class ExportMessageLink(TLObject):  # type: ignore
    """Get link and embed info of a message in a channel/supergroup


    Details:
        - Layer: ``181``
        - ID: ``E63FADEB``

    Parameters:
        channel (:obj:`InputChannel <hydrogram.raw.base.InputChannel>`):
            Channel

        id (``int`` ``32-bit``):
            Message ID

        grouped (``bool``, *optional*):
            Whether to include other grouped media (for albums)

        thread (``bool``, *optional*):
            Whether to also include a thread ID, if available, inside of the link

    Returns:
        :obj:`ExportedMessageLink <hydrogram.raw.base.ExportedMessageLink>`
    """

    __slots__: List[str] = ["channel", "id", "grouped", "thread"]

    ID = 0xe63fadeb
    QUALNAME = "functions.channels.ExportMessageLink"

    def __init__(self, *, channel: "raw.base.InputChannel", id: int, grouped: Optional[bool] = None, thread: Optional[bool] = None) -> None:
        self.channel = channel  # InputChannel
        self.id = id  # int
        self.grouped = grouped  # flags.0?true
        self.thread = thread  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportMessageLink":
        
        flags = Int.read(b)
        
        grouped = True if flags & (1 << 0) else False
        thread = True if flags & (1 << 1) else False
        channel = TLObject.read(b)
        
        id = Int.read(b)
        
        return ExportMessageLink(channel=channel, id=id, grouped=grouped, thread=thread)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.grouped else 0
        flags |= (1 << 1) if self.thread else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(Int(self.id))
        
        return b.getvalue()
