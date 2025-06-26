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


class JoinGroupCall(TLObject):  # type: ignore
    """Join a group call


    Details:
        - Layer: ``181``
        - ID: ``B132FF7B``

    Parameters:
        call (:obj:`InputGroupCall <hydrogram.raw.base.InputGroupCall>`):
            The group call

        join_as (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Join the group call, presenting yourself as the specified user/channel

        params (:obj:`DataJSON <hydrogram.raw.base.DataJSON>`):
            WebRTC parameters

        muted (``bool``, *optional*):
            If set, the user will be muted by default upon joining.

        video_stopped (``bool``, *optional*):
            If set, the user's video will be disabled by default upon joining.

        invite_hash (``str``, *optional*):
            The invitation hash from the invite link », if provided allows speaking in a livestream or muted group chat.

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "join_as", "params", "muted", "video_stopped", "invite_hash"]

    ID = 0xb132ff7b
    QUALNAME = "functions.phone.JoinGroupCall"

    def __init__(self, *, call: "raw.base.InputGroupCall", join_as: "raw.base.InputPeer", params: "raw.base.DataJSON", muted: Optional[bool] = None, video_stopped: Optional[bool] = None, invite_hash: Optional[str] = None) -> None:
        self.call = call  # InputGroupCall
        self.join_as = join_as  # InputPeer
        self.params = params  # DataJSON
        self.muted = muted  # flags.0?true
        self.video_stopped = video_stopped  # flags.2?true
        self.invite_hash = invite_hash  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "JoinGroupCall":
        
        flags = Int.read(b)
        
        muted = True if flags & (1 << 0) else False
        video_stopped = True if flags & (1 << 2) else False
        call = TLObject.read(b)
        
        join_as = TLObject.read(b)
        
        invite_hash = String.read(b) if flags & (1 << 1) else None
        params = TLObject.read(b)
        
        return JoinGroupCall(call=call, join_as=join_as, params=params, muted=muted, video_stopped=video_stopped, invite_hash=invite_hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.muted else 0
        flags |= (1 << 2) if self.video_stopped else 0
        flags |= (1 << 1) if self.invite_hash is not None else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        b.write(self.join_as.write())
        
        if self.invite_hash is not None:
            b.write(String(self.invite_hash))
        
        b.write(self.params.write())
        
        return b.getvalue()
