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


class UpdateBotCommands(TLObject):  # type: ignore
    """The command set of a certain bot in a certain chat has changed.

    Constructor of :obj:`~hydrogram.raw.base.Update`.

    Details:
        - Layer: ``181``
        - ID: ``4D712F2E``

    Parameters:
        peer (:obj:`Peer <hydrogram.raw.base.Peer>`):
            The affected chat

        bot_id (``int`` ``64-bit``):
            ID of the bot that changed its command set

        commands (List of :obj:`BotCommand <hydrogram.raw.base.BotCommand>`):
            New bot commands

    """

    __slots__: List[str] = ["peer", "bot_id", "commands"]

    ID = 0x4d712f2e
    QUALNAME = "types.UpdateBotCommands"

    def __init__(self, *, peer: "raw.base.Peer", bot_id: int, commands: List["raw.base.BotCommand"]) -> None:
        self.peer = peer  # Peer
        self.bot_id = bot_id  # long
        self.commands = commands  # Vector<BotCommand>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotCommands":
        # No flags
        
        peer = TLObject.read(b)
        
        bot_id = Long.read(b)
        
        commands = TLObject.read(b)
        
        return UpdateBotCommands(peer=peer, bot_id=bot_id, commands=commands)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Long(self.bot_id))
        
        b.write(Vector(self.commands))
        
        return b.getvalue()
