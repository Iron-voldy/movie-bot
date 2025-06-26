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


class GroupCall(TLObject):  # type: ignore
    """Info about a group call or livestream

    Constructor of :obj:`~hydrogram.raw.base.GroupCall`.

    Details:
        - Layer: ``181``
        - ID: ``D597650C``

    Parameters:
        id (``int`` ``64-bit``):
            Group call ID

        access_hash (``int`` ``64-bit``):
            Group call access hash

        participants_count (``int`` ``32-bit``):
            Participant count

        unmuted_video_limit (``int`` ``32-bit``):
            Maximum number of people allowed to stream video into the call

        version (``int`` ``32-bit``):
            Version

        join_muted (``bool``, *optional*):
            Whether the user should be muted upon joining the call

        can_change_join_muted (``bool``, *optional*):
            Whether the current user can change the value of the join_muted flag using phone.toggleGroupCallSettings

        join_date_asc (``bool``, *optional*):
            Specifies the ordering to use when locally sorting by date and displaying in the UI group call participants.

        schedule_start_subscribed (``bool``, *optional*):
            Whether we subscribed to the scheduled call

        can_start_video (``bool``, *optional*):
            Whether you can start streaming video into the call

        record_video_active (``bool``, *optional*):
            Whether the group call is currently being recorded

        rtmp_stream (``bool``, *optional*):
            Whether RTMP streams are allowed

        listeners_hidden (``bool``, *optional*):
            Whether the listeners list is hidden and cannot be fetched using phone.getGroupParticipants. The phone.groupParticipants.count and groupCall.participants_count counters will still include listeners.

        title (``str``, *optional*):
            Group call title

        stream_dc_id (``int`` ``32-bit``, *optional*):
            DC ID to be used for livestream chunks

        record_start_date (``int`` ``32-bit``, *optional*):
            When was the recording started

        schedule_date (``int`` ``32-bit``, *optional*):
            When is the call scheduled to start

        unmuted_video_count (``int`` ``32-bit``, *optional*):
            Number of people currently streaming video into the call

    """

    __slots__: List[str] = ["id", "access_hash", "participants_count", "unmuted_video_limit", "version", "join_muted", "can_change_join_muted", "join_date_asc", "schedule_start_subscribed", "can_start_video", "record_video_active", "rtmp_stream", "listeners_hidden", "title", "stream_dc_id", "record_start_date", "schedule_date", "unmuted_video_count"]

    ID = 0xd597650c
    QUALNAME = "types.GroupCall"

    def __init__(self, *, id: int, access_hash: int, participants_count: int, unmuted_video_limit: int, version: int, join_muted: Optional[bool] = None, can_change_join_muted: Optional[bool] = None, join_date_asc: Optional[bool] = None, schedule_start_subscribed: Optional[bool] = None, can_start_video: Optional[bool] = None, record_video_active: Optional[bool] = None, rtmp_stream: Optional[bool] = None, listeners_hidden: Optional[bool] = None, title: Optional[str] = None, stream_dc_id: Optional[int] = None, record_start_date: Optional[int] = None, schedule_date: Optional[int] = None, unmuted_video_count: Optional[int] = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.participants_count = participants_count  # int
        self.unmuted_video_limit = unmuted_video_limit  # int
        self.version = version  # int
        self.join_muted = join_muted  # flags.1?true
        self.can_change_join_muted = can_change_join_muted  # flags.2?true
        self.join_date_asc = join_date_asc  # flags.6?true
        self.schedule_start_subscribed = schedule_start_subscribed  # flags.8?true
        self.can_start_video = can_start_video  # flags.9?true
        self.record_video_active = record_video_active  # flags.11?true
        self.rtmp_stream = rtmp_stream  # flags.12?true
        self.listeners_hidden = listeners_hidden  # flags.13?true
        self.title = title  # flags.3?string
        self.stream_dc_id = stream_dc_id  # flags.4?int
        self.record_start_date = record_start_date  # flags.5?int
        self.schedule_date = schedule_date  # flags.7?int
        self.unmuted_video_count = unmuted_video_count  # flags.10?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCall":
        
        flags = Int.read(b)
        
        join_muted = True if flags & (1 << 1) else False
        can_change_join_muted = True if flags & (1 << 2) else False
        join_date_asc = True if flags & (1 << 6) else False
        schedule_start_subscribed = True if flags & (1 << 8) else False
        can_start_video = True if flags & (1 << 9) else False
        record_video_active = True if flags & (1 << 11) else False
        rtmp_stream = True if flags & (1 << 12) else False
        listeners_hidden = True if flags & (1 << 13) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        participants_count = Int.read(b)
        
        title = String.read(b) if flags & (1 << 3) else None
        stream_dc_id = Int.read(b) if flags & (1 << 4) else None
        record_start_date = Int.read(b) if flags & (1 << 5) else None
        schedule_date = Int.read(b) if flags & (1 << 7) else None
        unmuted_video_count = Int.read(b) if flags & (1 << 10) else None
        unmuted_video_limit = Int.read(b)
        
        version = Int.read(b)
        
        return GroupCall(id=id, access_hash=access_hash, participants_count=participants_count, unmuted_video_limit=unmuted_video_limit, version=version, join_muted=join_muted, can_change_join_muted=can_change_join_muted, join_date_asc=join_date_asc, schedule_start_subscribed=schedule_start_subscribed, can_start_video=can_start_video, record_video_active=record_video_active, rtmp_stream=rtmp_stream, listeners_hidden=listeners_hidden, title=title, stream_dc_id=stream_dc_id, record_start_date=record_start_date, schedule_date=schedule_date, unmuted_video_count=unmuted_video_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.join_muted else 0
        flags |= (1 << 2) if self.can_change_join_muted else 0
        flags |= (1 << 6) if self.join_date_asc else 0
        flags |= (1 << 8) if self.schedule_start_subscribed else 0
        flags |= (1 << 9) if self.can_start_video else 0
        flags |= (1 << 11) if self.record_video_active else 0
        flags |= (1 << 12) if self.rtmp_stream else 0
        flags |= (1 << 13) if self.listeners_hidden else 0
        flags |= (1 << 3) if self.title is not None else 0
        flags |= (1 << 4) if self.stream_dc_id is not None else 0
        flags |= (1 << 5) if self.record_start_date is not None else 0
        flags |= (1 << 7) if self.schedule_date is not None else 0
        flags |= (1 << 10) if self.unmuted_video_count is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.participants_count))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.stream_dc_id is not None:
            b.write(Int(self.stream_dc_id))
        
        if self.record_start_date is not None:
            b.write(Int(self.record_start_date))
        
        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))
        
        if self.unmuted_video_count is not None:
            b.write(Int(self.unmuted_video_count))
        
        b.write(Int(self.unmuted_video_limit))
        
        b.write(Int(self.version))
        
        return b.getvalue()
