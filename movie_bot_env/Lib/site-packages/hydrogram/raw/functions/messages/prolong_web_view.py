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


class ProlongWebView(TLObject):  # type: ignore
    """Indicate to the server (from the user side) that the user is still using a web app.


    Details:
        - Layer: ``181``
        - ID: ``B0D81A83``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Dialog where the web app was opened.

        bot (:obj:`InputUser <hydrogram.raw.base.InputUser>`):
            Bot that owns the web app

        query_id (``int`` ``64-bit``):
            Web app interaction ID obtained from messages.requestWebView

        silent (``bool``, *optional*):
            Whether the inline message that will be sent by the bot on behalf of the user once the web app interaction is terminated should be sent silently (no notifications for the receivers).

        reply_to (:obj:`InputReplyTo <hydrogram.raw.base.InputReplyTo>`, *optional*):
            If set, indicates that the inline message that will be sent by the bot on behalf of the user once the web app interaction is terminated should be sent in reply to the specified message or story.

        send_as (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`, *optional*):
            Open the web app as the specified peer

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "bot", "query_id", "silent", "reply_to", "send_as"]

    ID = 0xb0d81a83
    QUALNAME = "functions.messages.ProlongWebView"

    def __init__(self, *, peer: "raw.base.InputPeer", bot: "raw.base.InputUser", query_id: int, silent: Optional[bool] = None, reply_to: "raw.base.InputReplyTo" = None, send_as: "raw.base.InputPeer" = None) -> None:
        self.peer = peer  # InputPeer
        self.bot = bot  # InputUser
        self.query_id = query_id  # long
        self.silent = silent  # flags.5?true
        self.reply_to = reply_to  # flags.0?InputReplyTo
        self.send_as = send_as  # flags.13?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ProlongWebView":
        
        flags = Int.read(b)
        
        silent = True if flags & (1 << 5) else False
        peer = TLObject.read(b)
        
        bot = TLObject.read(b)
        
        query_id = Long.read(b)
        
        reply_to = TLObject.read(b) if flags & (1 << 0) else None
        
        send_as = TLObject.read(b) if flags & (1 << 13) else None
        
        return ProlongWebView(peer=peer, bot=bot, query_id=query_id, silent=silent, reply_to=reply_to, send_as=send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.silent else 0
        flags |= (1 << 0) if self.reply_to is not None else 0
        flags |= (1 << 13) if self.send_as is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(self.bot.write())
        
        b.write(Long(self.query_id))
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        if self.send_as is not None:
            b.write(self.send_as.write())
        
        return b.getvalue()
