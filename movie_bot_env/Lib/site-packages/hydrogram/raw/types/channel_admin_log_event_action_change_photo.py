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


class ChannelAdminLogEventActionChangePhoto(TLObject):  # type: ignore
    """The channel/supergroup's picture was changed

    Constructor of :obj:`~hydrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``181``
        - ID: ``434BD2AF``

    Parameters:
        prev_photo (:obj:`Photo <hydrogram.raw.base.Photo>`):
            Previous picture

        new_photo (:obj:`Photo <hydrogram.raw.base.Photo>`):
            New picture

    """

    __slots__: List[str] = ["prev_photo", "new_photo"]

    ID = 0x434bd2af
    QUALNAME = "types.ChannelAdminLogEventActionChangePhoto"

    def __init__(self, *, prev_photo: "raw.base.Photo", new_photo: "raw.base.Photo") -> None:
        self.prev_photo = prev_photo  # Photo
        self.new_photo = new_photo  # Photo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangePhoto":
        # No flags
        
        prev_photo = TLObject.read(b)
        
        new_photo = TLObject.read(b)
        
        return ChannelAdminLogEventActionChangePhoto(prev_photo=prev_photo, new_photo=new_photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.prev_photo.write())
        
        b.write(self.new_photo.write())
        
        return b.getvalue()
