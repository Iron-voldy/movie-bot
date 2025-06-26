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


class PhoneCallRequested(TLObject):  # type: ignore
    """Requested phone call

    Constructor of :obj:`~hydrogram.raw.base.PhoneCall`.

    Details:
        - Layer: ``181``
        - ID: ``14B0ED0C``

    Parameters:
        id (``int`` ``64-bit``):
            Phone call ID

        access_hash (``int`` ``64-bit``):
            Access hash

        date (``int`` ``32-bit``):
            When was the phone call created

        admin_id (``int`` ``64-bit``):
            ID of the creator of the phone call

        participant_id (``int`` ``64-bit``):
            ID of the other participant of the phone call

        g_a_hash (``bytes``):
            Parameter for key exchange

        protocol (:obj:`PhoneCallProtocol <hydrogram.raw.base.PhoneCallProtocol>`):
            Call protocol info to be passed to libtgvoip

        video (``bool``, *optional*):
            Whether this is a video call

    """

    __slots__: List[str] = ["id", "access_hash", "date", "admin_id", "participant_id", "g_a_hash", "protocol", "video"]

    ID = 0x14b0ed0c
    QUALNAME = "types.PhoneCallRequested"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int, g_a_hash: bytes, protocol: "raw.base.PhoneCallProtocol", video: Optional[bool] = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.date = date  # int
        self.admin_id = admin_id  # long
        self.participant_id = participant_id  # long
        self.g_a_hash = g_a_hash  # bytes
        self.protocol = protocol  # PhoneCallProtocol
        self.video = video  # flags.6?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCallRequested":
        
        flags = Int.read(b)
        
        video = True if flags & (1 << 6) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        date = Int.read(b)
        
        admin_id = Long.read(b)
        
        participant_id = Long.read(b)
        
        g_a_hash = Bytes.read(b)
        
        protocol = TLObject.read(b)
        
        return PhoneCallRequested(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, g_a_hash=g_a_hash, protocol=protocol, video=video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 6) if self.video else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.date))
        
        b.write(Long(self.admin_id))
        
        b.write(Long(self.participant_id))
        
        b.write(Bytes(self.g_a_hash))
        
        b.write(self.protocol.write())
        
        return b.getvalue()
