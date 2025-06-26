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


class UpdateConnectedBot(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``181``
        - ID: ``43D8521D``

    Parameters:
        bot (:obj:`InputUser <hydrogram.raw.base.InputUser>`):
            

        recipients (:obj:`InputBusinessBotRecipients <hydrogram.raw.base.InputBusinessBotRecipients>`):
            

        can_reply (``bool``, *optional*):
            

        deleted (``bool``, *optional*):
            

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["bot", "recipients", "can_reply", "deleted"]

    ID = 0x43d8521d
    QUALNAME = "functions.account.UpdateConnectedBot"

    def __init__(self, *, bot: "raw.base.InputUser", recipients: "raw.base.InputBusinessBotRecipients", can_reply: Optional[bool] = None, deleted: Optional[bool] = None) -> None:
        self.bot = bot  # InputUser
        self.recipients = recipients  # InputBusinessBotRecipients
        self.can_reply = can_reply  # flags.0?true
        self.deleted = deleted  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateConnectedBot":
        
        flags = Int.read(b)
        
        can_reply = True if flags & (1 << 0) else False
        deleted = True if flags & (1 << 1) else False
        bot = TLObject.read(b)
        
        recipients = TLObject.read(b)
        
        return UpdateConnectedBot(bot=bot, recipients=recipients, can_reply=can_reply, deleted=deleted)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.can_reply else 0
        flags |= (1 << 1) if self.deleted else 0
        b.write(Int(flags))
        
        b.write(self.bot.write())
        
        b.write(self.recipients.write())
        
        return b.getvalue()
