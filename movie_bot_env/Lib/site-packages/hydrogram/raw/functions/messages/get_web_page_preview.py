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


class GetWebPagePreview(TLObject):  # type: ignore
    """Get preview of webpage


    Details:
        - Layer: ``181``
        - ID: ``8B68B0CC``

    Parameters:
        message (``str``):
            Message from which to extract the preview

        entities (List of :obj:`MessageEntity <hydrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text

    Returns:
        :obj:`MessageMedia <hydrogram.raw.base.MessageMedia>`
    """

    __slots__: List[str] = ["message", "entities"]

    ID = 0x8b68b0cc
    QUALNAME = "functions.messages.GetWebPagePreview"

    def __init__(self, *, message: str, entities: Optional[List["raw.base.MessageEntity"]] = None) -> None:
        self.message = message  # string
        self.entities = entities  # flags.3?Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetWebPagePreview":
        
        flags = Int.read(b)
        
        message = String.read(b)
        
        entities = TLObject.read(b) if flags & (1 << 3) else []
        
        return GetWebPagePreview(message=message, entities=entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.entities else 0
        b.write(Int(flags))
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        return b.getvalue()
