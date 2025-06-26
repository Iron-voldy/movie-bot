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


class Folder(TLObject):  # type: ignore
    """Folder

    Constructor of :obj:`~hydrogram.raw.base.Folder`.

    Details:
        - Layer: ``181``
        - ID: ``FF544E65``

    Parameters:
        id (``int`` ``32-bit``):
            Folder ID

        title (``str``):
            Folder title

        autofill_new_broadcasts (``bool``, *optional*):
            Automatically add new channels to this folder

        autofill_public_groups (``bool``, *optional*):
            Automatically add joined new public supergroups to this folder

        autofill_new_correspondents (``bool``, *optional*):
            Automatically add new private chats to this folder

        photo (:obj:`ChatPhoto <hydrogram.raw.base.ChatPhoto>`, *optional*):
            Folder picture

    """

    __slots__: List[str] = ["id", "title", "autofill_new_broadcasts", "autofill_public_groups", "autofill_new_correspondents", "photo"]

    ID = 0xff544e65
    QUALNAME = "types.Folder"

    def __init__(self, *, id: int, title: str, autofill_new_broadcasts: Optional[bool] = None, autofill_public_groups: Optional[bool] = None, autofill_new_correspondents: Optional[bool] = None, photo: "raw.base.ChatPhoto" = None) -> None:
        self.id = id  # int
        self.title = title  # string
        self.autofill_new_broadcasts = autofill_new_broadcasts  # flags.0?true
        self.autofill_public_groups = autofill_public_groups  # flags.1?true
        self.autofill_new_correspondents = autofill_new_correspondents  # flags.2?true
        self.photo = photo  # flags.3?ChatPhoto

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Folder":
        
        flags = Int.read(b)
        
        autofill_new_broadcasts = True if flags & (1 << 0) else False
        autofill_public_groups = True if flags & (1 << 1) else False
        autofill_new_correspondents = True if flags & (1 << 2) else False
        id = Int.read(b)
        
        title = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 3) else None
        
        return Folder(id=id, title=title, autofill_new_broadcasts=autofill_new_broadcasts, autofill_public_groups=autofill_public_groups, autofill_new_correspondents=autofill_new_correspondents, photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.autofill_new_broadcasts else 0
        flags |= (1 << 1) if self.autofill_public_groups else 0
        flags |= (1 << 2) if self.autofill_new_correspondents else 0
        flags |= (1 << 3) if self.photo is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.title))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        return b.getvalue()
