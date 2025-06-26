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


class UpdatePinnedDialogs(TLObject):  # type: ignore
    """Pinned dialogs were updated

    Constructor of :obj:`~hydrogram.raw.base.Update`.

    Details:
        - Layer: ``181``
        - ID: ``FA0F3CA2``

    Parameters:
        folder_id (``int`` ``32-bit``, *optional*):
            Peer folder ID, for more info click here

        order (List of :obj:`DialogPeer <hydrogram.raw.base.DialogPeer>`, *optional*):
            New order of pinned dialogs

    """

    __slots__: List[str] = ["folder_id", "order"]

    ID = 0xfa0f3ca2
    QUALNAME = "types.UpdatePinnedDialogs"

    def __init__(self, *, folder_id: Optional[int] = None, order: Optional[List["raw.base.DialogPeer"]] = None) -> None:
        self.folder_id = folder_id  # flags.1?int
        self.order = order  # flags.0?Vector<DialogPeer>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePinnedDialogs":
        
        flags = Int.read(b)
        
        folder_id = Int.read(b) if flags & (1 << 1) else None
        order = TLObject.read(b) if flags & (1 << 0) else []
        
        return UpdatePinnedDialogs(folder_id=folder_id, order=order)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.folder_id is not None else 0
        flags |= (1 << 0) if self.order else 0
        b.write(Int(flags))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        if self.order is not None:
            b.write(Vector(self.order))
        
        return b.getvalue()
