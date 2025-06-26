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

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from hydrogram import raw
from hydrogram.raw.core import TLObject

SendMessageAction = Union["raw.types.SendMessageCancelAction", "raw.types.SendMessageChooseContactAction", "raw.types.SendMessageChooseStickerAction", "raw.types.SendMessageEmojiInteraction", "raw.types.SendMessageEmojiInteractionSeen", "raw.types.SendMessageGamePlayAction", "raw.types.SendMessageGeoLocationAction", "raw.types.SendMessageHistoryImportAction", "raw.types.SendMessageRecordAudioAction", "raw.types.SendMessageRecordRoundAction", "raw.types.SendMessageRecordVideoAction", "raw.types.SendMessageTypingAction", "raw.types.SendMessageUploadAudioAction", "raw.types.SendMessageUploadDocumentAction", "raw.types.SendMessageUploadPhotoAction", "raw.types.SendMessageUploadRoundAction", "raw.types.SendMessageUploadVideoAction", "raw.types.SpeakingInGroupCallAction"]


class SendMessageAction:  # type: ignore
    """User actions. Use this to provide users with detailed info about their chat partner's actions: typing or sending attachments of all kinds.

    Constructors:
        This base type has 18 constructors available.

        .. currentmodule:: hydrogram.raw.types

        .. autosummary::
            :nosignatures:

            SendMessageCancelAction
            SendMessageChooseContactAction
            SendMessageChooseStickerAction
            SendMessageEmojiInteraction
            SendMessageEmojiInteractionSeen
            SendMessageGamePlayAction
            SendMessageGeoLocationAction
            SendMessageHistoryImportAction
            SendMessageRecordAudioAction
            SendMessageRecordRoundAction
            SendMessageRecordVideoAction
            SendMessageTypingAction
            SendMessageUploadAudioAction
            SendMessageUploadDocumentAction
            SendMessageUploadPhotoAction
            SendMessageUploadRoundAction
            SendMessageUploadVideoAction
            SpeakingInGroupCallAction
    """

    QUALNAME = "hydrogram.raw.base.SendMessageAction"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.hydrogram.org/en/latest/telegram/base/send-message-action.html")
