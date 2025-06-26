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


class MessageActionSetMessagesTTL(TLObject):  # type: ignore
    """The Time-To-Live of messages in this chat was changed.

    Constructor of :obj:`~hydrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``181``
        - ID: ``3C134D7B``

    Parameters:
        period (``int`` ``32-bit``):
            New Time-To-Live of all messages sent in this chat; if 0, autodeletion was disabled.

        auto_setting_from (``int`` ``64-bit``, *optional*):
            If set, the chat TTL setting was set not due to a manual change by one of participants, but automatically because one of the participants has the default TTL settings enabled ». For example, when a user writes to us for the first time and we have set a default messages TTL of 1 week, this service message (with auto_setting_from=our_userid) will be emitted before our first message.

    """

    __slots__: List[str] = ["period", "auto_setting_from"]

    ID = 0x3c134d7b
    QUALNAME = "types.MessageActionSetMessagesTTL"

    def __init__(self, *, period: int, auto_setting_from: Optional[int] = None) -> None:
        self.period = period  # int
        self.auto_setting_from = auto_setting_from  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSetMessagesTTL":
        
        flags = Int.read(b)
        
        period = Int.read(b)
        
        auto_setting_from = Long.read(b) if flags & (1 << 0) else None
        return MessageActionSetMessagesTTL(period=period, auto_setting_from=auto_setting_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.auto_setting_from is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.period))
        
        if self.auto_setting_from is not None:
            b.write(Long(self.auto_setting_from))
        
        return b.getvalue()
