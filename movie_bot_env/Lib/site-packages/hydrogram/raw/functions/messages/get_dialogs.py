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


class GetDialogs(TLObject):  # type: ignore
    """Returns the current user dialog list.


    Details:
        - Layer: ``181``
        - ID: ``A0F4CB4F``

    Parameters:
        offset_date (``int`` ``32-bit``):
            Offsets for pagination, for more info click here

        offset_id (``int`` ``32-bit``):
            Offsets for pagination, for more info click here (top_message ID used for pagination)

        offset_peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Offset peer for pagination

        limit (``int`` ``32-bit``):
            Number of list elements to be returned

        hash (``int`` ``64-bit``):
            Hash for pagination, for more info click here

        exclude_pinned (``bool``, *optional*):
            Exclude pinned dialogs

        folder_id (``int`` ``32-bit``, *optional*):
            Peer folder ID, for more info click here

    Returns:
        :obj:`messages.Dialogs <hydrogram.raw.base.messages.Dialogs>`
    """

    __slots__: List[str] = ["offset_date", "offset_id", "offset_peer", "limit", "hash", "exclude_pinned", "folder_id"]

    ID = 0xa0f4cb4f
    QUALNAME = "functions.messages.GetDialogs"

    def __init__(self, *, offset_date: int, offset_id: int, offset_peer: "raw.base.InputPeer", limit: int, hash: int, exclude_pinned: Optional[bool] = None, folder_id: Optional[int] = None) -> None:
        self.offset_date = offset_date  # int
        self.offset_id = offset_id  # int
        self.offset_peer = offset_peer  # InputPeer
        self.limit = limit  # int
        self.hash = hash  # long
        self.exclude_pinned = exclude_pinned  # flags.0?true
        self.folder_id = folder_id  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDialogs":
        
        flags = Int.read(b)
        
        exclude_pinned = True if flags & (1 << 0) else False
        folder_id = Int.read(b) if flags & (1 << 1) else None
        offset_date = Int.read(b)
        
        offset_id = Int.read(b)
        
        offset_peer = TLObject.read(b)
        
        limit = Int.read(b)
        
        hash = Long.read(b)
        
        return GetDialogs(offset_date=offset_date, offset_id=offset_id, offset_peer=offset_peer, limit=limit, hash=hash, exclude_pinned=exclude_pinned, folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.exclude_pinned else 0
        flags |= (1 << 1) if self.folder_id is not None else 0
        b.write(Int(flags))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        b.write(Int(self.offset_date))
        
        b.write(Int(self.offset_id))
        
        b.write(self.offset_peer.write())
        
        b.write(Int(self.limit))
        
        b.write(Long(self.hash))
        
        return b.getvalue()
