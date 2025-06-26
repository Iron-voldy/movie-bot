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


class UploadMedia(TLObject):  # type: ignore
    """Upload a file and associate it to a chat (without actually sending it to the chat)


    Details:
        - Layer: ``181``
        - ID: ``14967978``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            The chat, can be inputPeerEmpty for bots and inputPeerSelf for users.

        media (:obj:`InputMedia <hydrogram.raw.base.InputMedia>`):
            File uploaded in chunks as described in files »

        business_connection_id (``str``, *optional*):
            

    Returns:
        :obj:`MessageMedia <hydrogram.raw.base.MessageMedia>`
    """

    __slots__: List[str] = ["peer", "media", "business_connection_id"]

    ID = 0x14967978
    QUALNAME = "functions.messages.UploadMedia"

    def __init__(self, *, peer: "raw.base.InputPeer", media: "raw.base.InputMedia", business_connection_id: Optional[str] = None) -> None:
        self.peer = peer  # InputPeer
        self.media = media  # InputMedia
        self.business_connection_id = business_connection_id  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadMedia":
        
        flags = Int.read(b)
        
        business_connection_id = String.read(b) if flags & (1 << 0) else None
        peer = TLObject.read(b)
        
        media = TLObject.read(b)
        
        return UploadMedia(peer=peer, media=media, business_connection_id=business_connection_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.business_connection_id is not None else 0
        b.write(Int(flags))
        
        if self.business_connection_id is not None:
            b.write(String(self.business_connection_id))
        
        b.write(self.peer.write())
        
        b.write(self.media.write())
        
        return b.getvalue()
