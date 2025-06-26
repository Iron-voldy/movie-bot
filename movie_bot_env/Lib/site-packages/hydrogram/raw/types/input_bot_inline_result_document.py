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


class InputBotInlineResultDocument(TLObject):  # type: ignore
    """Document (media of any type except for photos)

    Constructor of :obj:`~hydrogram.raw.base.InputBotInlineResult`.

    Details:
        - Layer: ``181``
        - ID: ``FFF8FDC4``

    Parameters:
        id (``str``):
            Result ID

        type (``str``):
            Result type (see bot API docs)

        document (:obj:`InputDocument <hydrogram.raw.base.InputDocument>`):
            Document to send

        send_message (:obj:`InputBotInlineMessage <hydrogram.raw.base.InputBotInlineMessage>`):
            Message to send when the result is selected

        title (``str``, *optional*):
            Result title

        description (``str``, *optional*):
            Result description

    """

    __slots__: List[str] = ["id", "type", "document", "send_message", "title", "description"]

    ID = 0xfff8fdc4
    QUALNAME = "types.InputBotInlineResultDocument"

    def __init__(self, *, id: str, type: str, document: "raw.base.InputDocument", send_message: "raw.base.InputBotInlineMessage", title: Optional[str] = None, description: Optional[str] = None) -> None:
        self.id = id  # string
        self.type = type  # string
        self.document = document  # InputDocument
        self.send_message = send_message  # InputBotInlineMessage
        self.title = title  # flags.1?string
        self.description = description  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputBotInlineResultDocument":
        
        flags = Int.read(b)
        
        id = String.read(b)
        
        type = String.read(b)
        
        title = String.read(b) if flags & (1 << 1) else None
        description = String.read(b) if flags & (1 << 2) else None
        document = TLObject.read(b)
        
        send_message = TLObject.read(b)
        
        return InputBotInlineResultDocument(id=id, type=type, document=document, send_message=send_message, title=title, description=description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.title is not None else 0
        flags |= (1 << 2) if self.description is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.id))
        
        b.write(String(self.type))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.description is not None:
            b.write(String(self.description))
        
        b.write(self.document.write())
        
        b.write(self.send_message.write())
        
        return b.getvalue()
