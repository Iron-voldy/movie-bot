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


class InputReplyToMessage(TLObject):  # type: ignore
    """Reply to a message.

    Constructor of :obj:`~hydrogram.raw.base.InputReplyTo`.

    Details:
        - Layer: ``181``
        - ID: ``22C0F6D5``

    Parameters:
        reply_to_msg_id (``int`` ``32-bit``):
            The message ID to reply to.

        top_msg_id (``int`` ``32-bit``, *optional*):
            This field must contain the topic ID only when replying to messages in forum topics different from the "General" topic (i.e. reply_to_msg_id is set and reply_to_msg_id != topicID and topicID != 1).  If the replied-to message is deleted before the method finishes execution, the value in this field will be used to send the message to the correct topic, instead of the "General" topic.

        reply_to_peer_id (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`, *optional*):
            Used to reply to messages sent to another chat (specified here), can only be used for non-protected chats and messages.

        quote_text (``str``, *optional*):
            Used to quote-reply to only a certain section (specified here) of the original message. The maximum UTF-8 length for quotes is specified in the quote_length_max config key.

        quote_entities (List of :obj:`MessageEntity <hydrogram.raw.base.MessageEntity>`, *optional*):
            Message entities for styled text from the quote_text field.

        quote_offset (``int`` ``32-bit``, *optional*):
            Offset of the message quote_text within the original message (in UTF-16 code units).

    """

    __slots__: List[str] = ["reply_to_msg_id", "top_msg_id", "reply_to_peer_id", "quote_text", "quote_entities", "quote_offset"]

    ID = 0x22c0f6d5
    QUALNAME = "types.InputReplyToMessage"

    def __init__(self, *, reply_to_msg_id: int, top_msg_id: Optional[int] = None, reply_to_peer_id: "raw.base.InputPeer" = None, quote_text: Optional[str] = None, quote_entities: Optional[List["raw.base.MessageEntity"]] = None, quote_offset: Optional[int] = None) -> None:
        self.reply_to_msg_id = reply_to_msg_id  # int
        self.top_msg_id = top_msg_id  # flags.0?int
        self.reply_to_peer_id = reply_to_peer_id  # flags.1?InputPeer
        self.quote_text = quote_text  # flags.2?string
        self.quote_entities = quote_entities  # flags.3?Vector<MessageEntity>
        self.quote_offset = quote_offset  # flags.4?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputReplyToMessage":
        
        flags = Int.read(b)
        
        reply_to_msg_id = Int.read(b)
        
        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        reply_to_peer_id = TLObject.read(b) if flags & (1 << 1) else None
        
        quote_text = String.read(b) if flags & (1 << 2) else None
        quote_entities = TLObject.read(b) if flags & (1 << 3) else []
        
        quote_offset = Int.read(b) if flags & (1 << 4) else None
        return InputReplyToMessage(reply_to_msg_id=reply_to_msg_id, top_msg_id=top_msg_id, reply_to_peer_id=reply_to_peer_id, quote_text=quote_text, quote_entities=quote_entities, quote_offset=quote_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        flags |= (1 << 1) if self.reply_to_peer_id is not None else 0
        flags |= (1 << 2) if self.quote_text is not None else 0
        flags |= (1 << 3) if self.quote_entities else 0
        flags |= (1 << 4) if self.quote_offset is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.reply_to_msg_id))
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        if self.reply_to_peer_id is not None:
            b.write(self.reply_to_peer_id.write())
        
        if self.quote_text is not None:
            b.write(String(self.quote_text))
        
        if self.quote_entities is not None:
            b.write(Vector(self.quote_entities))
        
        if self.quote_offset is not None:
            b.write(Int(self.quote_offset))
        
        return b.getvalue()
