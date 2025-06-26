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


class ToggleViewForumAsMessages(TLObject):  # type: ignore
    """Users may also choose to display messages from all topics of a forum as if they were sent to a normal group, using a "View as messages" setting in the local client: this setting only affects the current account, and is synced to other logged in sessions using this method.


    Details:
        - Layer: ``181``
        - ID: ``9738BB15``

    Parameters:
        channel (:obj:`InputChannel <hydrogram.raw.base.InputChannel>`):
            The forum

        enabled (``bool``):
            The new value of the view_forum_as_messages flag.

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "enabled"]

    ID = 0x9738bb15
    QUALNAME = "functions.channels.ToggleViewForumAsMessages"

    def __init__(self, *, channel: "raw.base.InputChannel", enabled: bool) -> None:
        self.channel = channel  # InputChannel
        self.enabled = enabled  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleViewForumAsMessages":
        # No flags
        
        channel = TLObject.read(b)
        
        enabled = Bool.read(b)
        
        return ToggleViewForumAsMessages(channel=channel, enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Bool(self.enabled))
        
        return b.getvalue()
