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


class DeepLinkInfo(TLObject):  # type: ignore
    """Deep link info, see the here for more details

    Constructor of :obj:`~hydrogram.raw.base.help.DeepLinkInfo`.

    Details:
        - Layer: ``181``
        - ID: ``6A4EE832``

    Parameters:
        message (``str``):
            Message to show to the user

        update_app (``bool``, *optional*):
            An update of the app is required to parse this link

        entities (List of :obj:`MessageEntity <hydrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetDeepLinkInfo
    """

    __slots__: List[str] = ["message", "update_app", "entities"]

    ID = 0x6a4ee832
    QUALNAME = "types.help.DeepLinkInfo"

    def __init__(self, *, message: str, update_app: Optional[bool] = None, entities: Optional[List["raw.base.MessageEntity"]] = None) -> None:
        self.message = message  # string
        self.update_app = update_app  # flags.0?true
        self.entities = entities  # flags.1?Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeepLinkInfo":
        
        flags = Int.read(b)
        
        update_app = True if flags & (1 << 0) else False
        message = String.read(b)
        
        entities = TLObject.read(b) if flags & (1 << 1) else []
        
        return DeepLinkInfo(message=message, update_app=update_app, entities=entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.update_app else 0
        flags |= (1 << 1) if self.entities else 0
        b.write(Int(flags))
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        return b.getvalue()
