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


class SendStory(TLObject):  # type: ignore
    """Uploads a Telegram Story.


    Details:
        - Layer: ``181``
        - ID: ``E4E6694B``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            The peer to send the story as.

        media (:obj:`InputMedia <hydrogram.raw.base.InputMedia>`):
            The story media.

        privacy_rules (List of :obj:`InputPrivacyRule <hydrogram.raw.base.InputPrivacyRule>`):
            Privacy rules for the story, indicating who can or can't view the story.

        random_id (``int`` ``64-bit``):
            Unique client message ID required to prevent message resending.

        pinned (``bool``, *optional*):
            Whether to add the story to the profile automatically upon expiration. If not set, the story will only be added to the archive, see here » for more info.

        noforwards (``bool``, *optional*):
            If set, disables forwards, screenshots, and downloads.

        fwd_modified (``bool``, *optional*):
            Set this flag when reposting stories with fwd_from_id+fwd_from_id, if the media was modified before reposting.

        media_areas (List of :obj:`MediaArea <hydrogram.raw.base.MediaArea>`, *optional*):
            Media areas associated to the story, see here » for more info.

        caption (``str``, *optional*):
            Story caption.

        entities (List of :obj:`MessageEntity <hydrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text, if allowed by the stories_entities client configuration parameter ».

        period (``int`` ``32-bit``, *optional*):
            Period after which the story is moved to archive (and to the profile if pinned is set), in seconds; must be one of 6 * 3600, 12 * 3600, 86400, or 2 * 86400 for Telegram Premium users, and 86400 otherwise.

        fwd_from_id (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`, *optional*):
            If set, indicates that this story is a repost of story with ID fwd_from_story posted by the peer in fwd_from_id.

        fwd_from_story (``int`` ``32-bit``, *optional*):
            If set, indicates that this story is a repost of story with ID fwd_from_story posted by the peer in fwd_from_id.

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "media", "privacy_rules", "random_id", "pinned", "noforwards", "fwd_modified", "media_areas", "caption", "entities", "period", "fwd_from_id", "fwd_from_story"]

    ID = 0xe4e6694b
    QUALNAME = "functions.stories.SendStory"

    def __init__(self, *, peer: "raw.base.InputPeer", media: "raw.base.InputMedia", privacy_rules: List["raw.base.InputPrivacyRule"], random_id: int, pinned: Optional[bool] = None, noforwards: Optional[bool] = None, fwd_modified: Optional[bool] = None, media_areas: Optional[List["raw.base.MediaArea"]] = None, caption: Optional[str] = None, entities: Optional[List["raw.base.MessageEntity"]] = None, period: Optional[int] = None, fwd_from_id: "raw.base.InputPeer" = None, fwd_from_story: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.media = media  # InputMedia
        self.privacy_rules = privacy_rules  # Vector<InputPrivacyRule>
        self.random_id = random_id  # long
        self.pinned = pinned  # flags.2?true
        self.noforwards = noforwards  # flags.4?true
        self.fwd_modified = fwd_modified  # flags.7?true
        self.media_areas = media_areas  # flags.5?Vector<MediaArea>
        self.caption = caption  # flags.0?string
        self.entities = entities  # flags.1?Vector<MessageEntity>
        self.period = period  # flags.3?int
        self.fwd_from_id = fwd_from_id  # flags.6?InputPeer
        self.fwd_from_story = fwd_from_story  # flags.6?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendStory":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 2) else False
        noforwards = True if flags & (1 << 4) else False
        fwd_modified = True if flags & (1 << 7) else False
        peer = TLObject.read(b)
        
        media = TLObject.read(b)
        
        media_areas = TLObject.read(b) if flags & (1 << 5) else []
        
        caption = String.read(b) if flags & (1 << 0) else None
        entities = TLObject.read(b) if flags & (1 << 1) else []
        
        privacy_rules = TLObject.read(b)
        
        random_id = Long.read(b)
        
        period = Int.read(b) if flags & (1 << 3) else None
        fwd_from_id = TLObject.read(b) if flags & (1 << 6) else None
        
        fwd_from_story = Int.read(b) if flags & (1 << 6) else None
        return SendStory(peer=peer, media=media, privacy_rules=privacy_rules, random_id=random_id, pinned=pinned, noforwards=noforwards, fwd_modified=fwd_modified, media_areas=media_areas, caption=caption, entities=entities, period=period, fwd_from_id=fwd_from_id, fwd_from_story=fwd_from_story)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.pinned else 0
        flags |= (1 << 4) if self.noforwards else 0
        flags |= (1 << 7) if self.fwd_modified else 0
        flags |= (1 << 5) if self.media_areas else 0
        flags |= (1 << 0) if self.caption is not None else 0
        flags |= (1 << 1) if self.entities else 0
        flags |= (1 << 3) if self.period is not None else 0
        flags |= (1 << 6) if self.fwd_from_id is not None else 0
        flags |= (1 << 6) if self.fwd_from_story is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(self.media.write())
        
        if self.media_areas is not None:
            b.write(Vector(self.media_areas))
        
        if self.caption is not None:
            b.write(String(self.caption))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        b.write(Vector(self.privacy_rules))
        
        b.write(Long(self.random_id))
        
        if self.period is not None:
            b.write(Int(self.period))
        
        if self.fwd_from_id is not None:
            b.write(self.fwd_from_id.write())
        
        if self.fwd_from_story is not None:
            b.write(Int(self.fwd_from_story))
        
        return b.getvalue()
