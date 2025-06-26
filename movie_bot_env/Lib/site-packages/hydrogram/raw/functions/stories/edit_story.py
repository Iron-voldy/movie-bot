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


class EditStory(TLObject):  # type: ignore
    """Edit an uploaded story


    Details:
        - Layer: ``181``
        - ID: ``B583BA46``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Peer where the story was posted.

        id (``int`` ``32-bit``):
            ID of story to edit.

        media (:obj:`InputMedia <hydrogram.raw.base.InputMedia>`, *optional*):
            If specified, replaces the story media.

        media_areas (List of :obj:`MediaArea <hydrogram.raw.base.MediaArea>`, *optional*):
            Media areas associated to the story, see here » for more info.

        caption (``str``, *optional*):
            If specified, replaces the story caption.

        entities (List of :obj:`MessageEntity <hydrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text in the caption, if allowed by the stories_entities client configuration parameter ».

        privacy_rules (List of :obj:`InputPrivacyRule <hydrogram.raw.base.InputPrivacyRule>`, *optional*):
            If specified, alters the privacy settings » of the story, changing who can or can't view the story.

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "id", "media", "media_areas", "caption", "entities", "privacy_rules"]

    ID = 0xb583ba46
    QUALNAME = "functions.stories.EditStory"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, media: "raw.base.InputMedia" = None, media_areas: Optional[List["raw.base.MediaArea"]] = None, caption: Optional[str] = None, entities: Optional[List["raw.base.MessageEntity"]] = None, privacy_rules: Optional[List["raw.base.InputPrivacyRule"]] = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.media = media  # flags.0?InputMedia
        self.media_areas = media_areas  # flags.3?Vector<MediaArea>
        self.caption = caption  # flags.1?string
        self.entities = entities  # flags.1?Vector<MessageEntity>
        self.privacy_rules = privacy_rules  # flags.2?Vector<InputPrivacyRule>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditStory":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        media = TLObject.read(b) if flags & (1 << 0) else None
        
        media_areas = TLObject.read(b) if flags & (1 << 3) else []
        
        caption = String.read(b) if flags & (1 << 1) else None
        entities = TLObject.read(b) if flags & (1 << 1) else []
        
        privacy_rules = TLObject.read(b) if flags & (1 << 2) else []
        
        return EditStory(peer=peer, id=id, media=media, media_areas=media_areas, caption=caption, entities=entities, privacy_rules=privacy_rules)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.media is not None else 0
        flags |= (1 << 3) if self.media_areas else 0
        flags |= (1 << 1) if self.caption is not None else 0
        flags |= (1 << 1) if self.entities else 0
        flags |= (1 << 2) if self.privacy_rules else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.media_areas is not None:
            b.write(Vector(self.media_areas))
        
        if self.caption is not None:
            b.write(String(self.caption))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.privacy_rules is not None:
            b.write(Vector(self.privacy_rules))
        
        return b.getvalue()
