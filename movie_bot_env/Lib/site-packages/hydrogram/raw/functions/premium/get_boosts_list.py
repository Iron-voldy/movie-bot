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


class GetBoostsList(TLObject):  # type: ignore
    """Obtains info about the boosts that were applied to a certain channel (admins only)


    Details:
        - Layer: ``181``
        - ID: ``60F67660``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            The channel

        offset (``str``):
            Offset for pagination, obtained from premium.boostsList.next_offset

        limit (``int`` ``32-bit``):
            Maximum number of results to return, see pagination

        gifts (``bool``, *optional*):
            Whether to return only info about boosts received from gift codes and giveaways created by the channel »

    Returns:
        :obj:`premium.BoostsList <hydrogram.raw.base.premium.BoostsList>`
    """

    __slots__: List[str] = ["peer", "offset", "limit", "gifts"]

    ID = 0x60f67660
    QUALNAME = "functions.premium.GetBoostsList"

    def __init__(self, *, peer: "raw.base.InputPeer", offset: str, limit: int, gifts: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.offset = offset  # string
        self.limit = limit  # int
        self.gifts = gifts  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBoostsList":
        
        flags = Int.read(b)
        
        gifts = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        offset = String.read(b)
        
        limit = Int.read(b)
        
        return GetBoostsList(peer=peer, offset=offset, limit=limit, gifts=gifts)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.gifts else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(String(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
