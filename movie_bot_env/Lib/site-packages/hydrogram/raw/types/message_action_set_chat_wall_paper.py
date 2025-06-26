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


class MessageActionSetChatWallPaper(TLObject):  # type: ignore
    """The wallpaper » of the current chat was changed.

    Constructor of :obj:`~hydrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``5060A3F4``

    Parameters:
        wallpaper (:obj:`WallPaper <hydrogram.raw.base.WallPaper>`):
            New wallpaper

        same (``bool``, *optional*):
            If set, indicates the user applied a wallpaper » previously sent by the other user in a messageActionSetChatWallPaper message.

        for_both (``bool``, *optional*):
            If set, indicates the wallpaper was forcefully applied for both sides, without explicit confirmation from the other side. If the message is incoming, and we did not like the new wallpaper the other user has chosen for us, we can re-set our previous wallpaper just on our side, by invoking messages.setChatWallPaper, providing only the revert flag (and obviously the peer parameter).

    """

    __slots__: List[str] = ["wallpaper", "same", "for_both"]

    ID = 0x5060a3f4
    QUALNAME = "types.MessageActionSetChatWallPaper"

    def __init__(self, *, wallpaper: "raw.base.WallPaper", same: Optional[bool] = None, for_both: Optional[bool] = None) -> None:
        self.wallpaper = wallpaper  # WallPaper
        self.same = same  # flags.0?true
        self.for_both = for_both  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSetChatWallPaper":
        
        flags = Int.read(b)
        
        same = True if flags & (1 << 0) else False
        for_both = True if flags & (1 << 1) else False
        wallpaper = TLObject.read(b)
        
        return MessageActionSetChatWallPaper(wallpaper=wallpaper, same=same, for_both=for_both)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.same else 0
        flags |= (1 << 1) if self.for_both else 0
        b.write(Int(flags))
        
        b.write(self.wallpaper.write())
        
        return b.getvalue()
