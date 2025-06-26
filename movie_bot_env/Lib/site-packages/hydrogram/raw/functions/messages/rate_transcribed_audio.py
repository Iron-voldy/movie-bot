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


class RateTranscribedAudio(TLObject):  # type: ignore
    """Rate transcribed voice message


    Details:
        - Layer: ``181``
        - ID: ``7F1D072F``

    Parameters:
        peer (:obj:`InputPeer <hydrogram.raw.base.InputPeer>`):
            Peer where the voice message was sent

        msg_id (``int`` ``32-bit``):
            Message ID

        transcription_id (``int`` ``64-bit``):
            Transcription ID

        good (``bool``):
            Whether the transcription was correct

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "msg_id", "transcription_id", "good"]

    ID = 0x7f1d072f
    QUALNAME = "functions.messages.RateTranscribedAudio"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, transcription_id: int, good: bool) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.transcription_id = transcription_id  # long
        self.good = good  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RateTranscribedAudio":
        # No flags
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        transcription_id = Long.read(b)
        
        good = Bool.read(b)
        
        return RateTranscribedAudio(peer=peer, msg_id=msg_id, transcription_id=transcription_id, good=good)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Long(self.transcription_id))
        
        b.write(Bool(self.good))
        
        return b.getvalue()
