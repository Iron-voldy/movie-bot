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


class GetBotCallbackAnswer(TLObject):  # type: ignore
    """Press an inline callback button and get a callback answer from the bot


    Details:
        - Layer: ``181``
        - ID: ``9342CA07``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Where was the inline keyboard sent

        msg_id (``int`` ``32-bit``):
            ID of the Message with the inline keyboard

        game (``bool``, *optional*):
            Whether this is a "play game" button

        data (``bytes``, *optional*):
            Callback data

        password (:obj:`InputCheckPasswordSRP <hydrogram.raw.base.InputCheckPasswordSRP>`, *optional*):
            For buttons requiring you to verify your identity with your 2FA password, the SRP payload generated using SRP.

    Returns:
        :obj:`messages.BotCallbackAnswer <hydrogram.raw.base.messages.BotCallbackAnswer>`
    """

    __slots__: List[str] = ["peer", "msg_id", "game", "data", "password"]

    ID = 0x9342ca07
    QUALNAME = "functions.messages.GetBotCallbackAnswer"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, game: Optional[bool] = None, data: Optional[bytes] = None, password: "raw.base.InputCheckPasswordSRP" = None) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.game = game  # flags.1?true
        self.data = data  # flags.0?bytes
        self.password = password  # flags.2?InputCheckPasswordSRP

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetBotCallbackAnswer":
        
        flags = Int.read(b)
        
        game = True if flags & (1 << 1) else False
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        data = Bytes.read(b) if flags & (1 << 0) else None
        password = TLObject.read(b) if flags & (1 << 2) else None
        
        return GetBotCallbackAnswer(peer=peer, msg_id=msg_id, game=game, data=data, password=password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.game else 0
        flags |= (1 << 0) if self.data is not None else 0
        flags |= (1 << 2) if self.password is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        if self.data is not None:
            b.write(Bytes(self.data))
        
        if self.password is not None:
            b.write(self.password.write())
        
        return b.getvalue()
