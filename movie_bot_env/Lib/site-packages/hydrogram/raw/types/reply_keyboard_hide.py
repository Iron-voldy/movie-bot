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


class ReplyKeyboardHide(TLObject):  # type: ignore
    """Hide sent bot keyboard

    Constructor of :obj:`~hydrogram.raw.base.ReplyMarkup`.

    Details:
        - Layer: ``181``
        - ID: ``A03E5B85``

    Parameters:
        selective (``bool``, *optional*):
            Use this flag if you want to remove the keyboard for specific users only. Targets: 1) users that are @mentioned in the text of the Message object; 2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet

    """

    __slots__: List[str] = ["selective"]

    ID = 0xa03e5b85
    QUALNAME = "types.ReplyKeyboardHide"

    def __init__(self, *, selective: Optional[bool] = None) -> None:
        self.selective = selective  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReplyKeyboardHide":
        
        flags = Int.read(b)
        
        selective = True if flags & (1 << 2) else False
        return ReplyKeyboardHide(selective=selective)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.selective else 0
        b.write(Int(flags))
        
        return b.getvalue()
