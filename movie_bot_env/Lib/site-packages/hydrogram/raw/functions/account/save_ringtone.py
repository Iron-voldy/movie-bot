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


class SaveRingtone(TLObject):  # type: ignore
    """Save or remove saved notification sound.


    Details:
        - Layer: ``181``
        - ID: ``3DEA5B03``

    Parameters:
        id (:obj:`InputDocument <hydrogram.raw.base.InputDocument>`):
            Notification sound uploaded using account.uploadRingtone

        unsave (``bool``):
            Whether to add or delete the notification sound

    Returns:
        :obj:`account.SavedRingtone <hydrogram.raw.base.account.SavedRingtone>`
    """

    __slots__: List[str] = ["id", "unsave"]

    ID = 0x3dea5b03
    QUALNAME = "functions.account.SaveRingtone"

    def __init__(self, *, id: "raw.base.InputDocument", unsave: bool) -> None:
        self.id = id  # InputDocument
        self.unsave = unsave  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveRingtone":
        # No flags
        
        id = TLObject.read(b)
        
        unsave = Bool.read(b)
        
        return SaveRingtone(id=id, unsave=unsave)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.id.write())
        
        b.write(Bool(self.unsave))
        
        return b.getvalue()
