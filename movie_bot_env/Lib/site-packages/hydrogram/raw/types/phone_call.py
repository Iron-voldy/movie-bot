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


class PhoneCall(TLObject):  # type: ignore
    """Phone call

    Constructor of :obj:`~hydrogram.raw.base.PhoneCall`.

    Details:
        - Layer: ``181``
        - ID: ``30535AF5``

    Parameters:
        id (``int`` ``64-bit``):
            Call ID

        access_hash (``int`` ``64-bit``):
            Access hash

        date (``int`` ``32-bit``):
            Date of creation of the call

        admin_id (``int`` ``64-bit``):
            User ID of the creator of the call

        participant_id (``int`` ``64-bit``):
            User ID of the other participant in the call

        g_a_or_b (``bytes``):
            Parameter for key exchange

        key_fingerprint (``int`` ``64-bit``):
            Key fingerprint

        protocol (:obj:`PhoneCallProtocol <hydrogram.raw.base.PhoneCallProtocol>`):
            Call protocol info to be passed to libtgvoip

        connections (List of :obj:`PhoneConnection <hydrogram.raw.base.PhoneConnection>`):
            List of endpoints the user can connect to to exchange call data

        start_date (``int`` ``32-bit``):
            When was the call actually started

        p2p_allowed (``bool``, *optional*):
            Whether P2P connection to the other peer is allowed

        video (``bool``, *optional*):
            Whether this is a video call

        custom_parameters (:obj:`DataJSON <hydrogram.raw.base.DataJSON>`, *optional*):
            

    """

    __slots__: List[str] = ["id", "access_hash", "date", "admin_id", "participant_id", "g_a_or_b", "key_fingerprint", "protocol", "connections", "start_date", "p2p_allowed", "video", "custom_parameters"]

    ID = 0x30535af5
    QUALNAME = "types.PhoneCall"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int, g_a_or_b: bytes, key_fingerprint: int, protocol: "raw.base.PhoneCallProtocol", connections: List["raw.base.PhoneConnection"], start_date: int, p2p_allowed: Optional[bool] = None, video: Optional[bool] = None, custom_parameters: "raw.base.DataJSON" = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.date = date  # int
        self.admin_id = admin_id  # long
        self.participant_id = participant_id  # long
        self.g_a_or_b = g_a_or_b  # bytes
        self.key_fingerprint = key_fingerprint  # long
        self.protocol = protocol  # PhoneCallProtocol
        self.connections = connections  # Vector<PhoneConnection>
        self.start_date = start_date  # int
        self.p2p_allowed = p2p_allowed  # flags.5?true
        self.video = video  # flags.6?true
        self.custom_parameters = custom_parameters  # flags.7?DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCall":
        
        flags = Int.read(b)
        
        p2p_allowed = True if flags & (1 << 5) else False
        video = True if flags & (1 << 6) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        date = Int.read(b)
        
        admin_id = Long.read(b)
        
        participant_id = Long.read(b)
        
        g_a_or_b = Bytes.read(b)
        
        key_fingerprint = Long.read(b)
        
        protocol = TLObject.read(b)
        
        connections = TLObject.read(b)
        
        start_date = Int.read(b)
        
        custom_parameters = TLObject.read(b) if flags & (1 << 7) else None
        
        return PhoneCall(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, g_a_or_b=g_a_or_b, key_fingerprint=key_fingerprint, protocol=protocol, connections=connections, start_date=start_date, p2p_allowed=p2p_allowed, video=video, custom_parameters=custom_parameters)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.p2p_allowed else 0
        flags |= (1 << 6) if self.video else 0
        flags |= (1 << 7) if self.custom_parameters is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.date))
        
        b.write(Long(self.admin_id))
        
        b.write(Long(self.participant_id))
        
        b.write(Bytes(self.g_a_or_b))
        
        b.write(Long(self.key_fingerprint))
        
        b.write(self.protocol.write())
        
        b.write(Vector(self.connections))
        
        b.write(Int(self.start_date))
        
        if self.custom_parameters is not None:
            b.write(self.custom_parameters.write())
        
        return b.getvalue()
