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


class AutoSaveException(TLObject):  # type: ignore
    """Peer-specific media autosave settings

    Constructor of :obj:`~hydrogram.raw.base.AutoSaveException`.

    Details:
        - Layer: ``181``
        - ID: ``81602D47``

    Parameters:
        peer (:obj:`Peer <hydrogram.raw.base.Peer>`):
            The peer

        settings (:obj:`AutoSaveSettings <hydrogram.raw.base.AutoSaveSettings>`):
            Media autosave settings

    """

    __slots__: List[str] = ["peer", "settings"]

    ID = 0x81602d47
    QUALNAME = "types.AutoSaveException"

    def __init__(self, *, peer: "raw.base.Peer", settings: "raw.base.AutoSaveSettings") -> None:
        self.peer = peer  # Peer
        self.settings = settings  # AutoSaveSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AutoSaveException":
        # No flags
        
        peer = TLObject.read(b)
        
        settings = TLObject.read(b)
        
        return AutoSaveException(peer=peer, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.settings.write())
        
        return b.getvalue()
