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


class SaveAutoSaveSettings(TLObject):  # type: ignore
    """Modify autosave settings


    Details:
        - Layer: ``181``
        - ID: ``D69B8361``

    Parameters:
        settings (:obj:`AutoSaveSettings <hydrogram.raw.base.AutoSaveSettings>`):
            The new autosave settings

        users (``bool``, *optional*):
            Whether the new settings should affect all private chats

        chats (``bool``, *optional*):
            Whether the new settings should affect all groups

        broadcasts (``bool``, *optional*):
            Whether the new settings should affect all channels

        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`, *optional*):
            Whether the new settings should affect a specific peer

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["settings", "users", "chats", "broadcasts", "peer"]

    ID = 0xd69b8361
    QUALNAME = "functions.account.SaveAutoSaveSettings"

    def __init__(self, *, settings: "raw.base.AutoSaveSettings", users: Optional[bool] = None, chats: Optional[bool] = None, broadcasts: Optional[bool] = None, peer: "raw.base.InputPeer" = None) -> None:
        self.settings = settings  # AutoSaveSettings
        self.users = users  # flags.0?true
        self.chats = chats  # flags.1?true
        self.broadcasts = broadcasts  # flags.2?true
        self.peer = peer  # flags.3?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveAutoSaveSettings":
        
        flags = Int.read(b)
        
        users = True if flags & (1 << 0) else False
        chats = True if flags & (1 << 1) else False
        broadcasts = True if flags & (1 << 2) else False
        peer = TLObject.read(b) if flags & (1 << 3) else None
        
        settings = TLObject.read(b)
        
        return SaveAutoSaveSettings(settings=settings, users=users, chats=chats, broadcasts=broadcasts, peer=peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.users else 0
        flags |= (1 << 1) if self.chats else 0
        flags |= (1 << 2) if self.broadcasts else 0
        flags |= (1 << 3) if self.peer is not None else 0
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        b.write(self.settings.write())
        
        return b.getvalue()
