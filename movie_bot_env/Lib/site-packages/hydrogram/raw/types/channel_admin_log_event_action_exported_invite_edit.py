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


class ChannelAdminLogEventActionExportedInviteEdit(TLObject):  # type: ignore
    """A chat invite was edited

    Constructor of :obj:`~hydrogram.raw.base.ChannelAdminLogEventAction`.

    Details:
        - Layer: ``181``
        - ID: ``E90EBB59``

    Parameters:
        prev_invite (:obj:`ExportedChatInvite <hydrogram.raw.base.ExportedChatInvite>`):
            Previous chat invite information

        new_invite (:obj:`ExportedChatInvite <hydrogram.raw.base.ExportedChatInvite>`):
            New chat invite information

    """

    __slots__: List[str] = ["prev_invite", "new_invite"]

    ID = 0xe90ebb59
    QUALNAME = "types.ChannelAdminLogEventActionExportedInviteEdit"

    def __init__(self, *, prev_invite: "raw.base.ExportedChatInvite", new_invite: "raw.base.ExportedChatInvite") -> None:
        self.prev_invite = prev_invite  # ExportedChatInvite
        self.new_invite = new_invite  # ExportedChatInvite

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionExportedInviteEdit":
        # No flags
        
        prev_invite = TLObject.read(b)
        
        new_invite = TLObject.read(b)
        
        return ChannelAdminLogEventActionExportedInviteEdit(prev_invite=prev_invite, new_invite=new_invite)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.prev_invite.write())
        
        b.write(self.new_invite.write())
        
        return b.getvalue()
