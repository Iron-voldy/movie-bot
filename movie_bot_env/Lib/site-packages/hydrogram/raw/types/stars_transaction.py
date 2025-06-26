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


class StarsTransaction(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.StarsTransaction`.

    Details:
        - Layer: ``181``
        - ID: ``CC7079B2``

    Parameters:
        id (``str``):
            

        stars (``int`` ``64-bit``):
            

        date (``int`` ``32-bit``):
            

        peer (:obj:`StarsTransactionPeer <hydrogram.raw.base.StarsTransactionPeer>`):
            

        refund (``bool``, *optional*):
            

        title (``str``, *optional*):
            

        description (``str``, *optional*):
            

        photo (:obj:`WebDocument <hydrogram.raw.base.WebDocument>`, *optional*):
            

    """

    __slots__: List[str] = ["id", "stars", "date", "peer", "refund", "title", "description", "photo"]

    ID = 0xcc7079b2
    QUALNAME = "types.StarsTransaction"

    def __init__(self, *, id: str, stars: int, date: int, peer: "raw.base.StarsTransactionPeer", refund: Optional[bool] = None, title: Optional[str] = None, description: Optional[str] = None, photo: "raw.base.WebDocument" = None) -> None:
        self.id = id  # string
        self.stars = stars  # long
        self.date = date  # int
        self.peer = peer  # StarsTransactionPeer
        self.refund = refund  # flags.3?true
        self.title = title  # flags.0?string
        self.description = description  # flags.1?string
        self.photo = photo  # flags.2?WebDocument

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarsTransaction":
        
        flags = Int.read(b)
        
        refund = True if flags & (1 << 3) else False
        id = String.read(b)
        
        stars = Long.read(b)
        
        date = Int.read(b)
        
        peer = TLObject.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        description = String.read(b) if flags & (1 << 1) else None
        photo = TLObject.read(b) if flags & (1 << 2) else None
        
        return StarsTransaction(id=id, stars=stars, date=date, peer=peer, refund=refund, title=title, description=description, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.refund else 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.description is not None else 0
        flags |= (1 << 2) if self.photo is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.id))
        
        b.write(Long(self.stars))
        
        b.write(Int(self.date))
        
        b.write(self.peer.write())
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.description is not None:
            b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        return b.getvalue()
