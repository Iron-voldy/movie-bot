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

MessageAction = Union["raw.types.MessageActionBoostApply", "raw.types.MessageActionBotAllowed", "raw.types.MessageActionChannelCreate", "raw.types.MessageActionChannelMigrateFrom", "raw.types.MessageActionChatAddUser", "raw.types.MessageActionChatCreate", "raw.types.MessageActionChatDeletePhoto", "raw.types.MessageActionChatDeleteUser", "raw.types.MessageActionChatEditPhoto", "raw.types.MessageActionChatEditTitle", "raw.types.MessageActionChatJoinedByLink", "raw.types.MessageActionChatJoinedByRequest", "raw.types.MessageActionChatMigrateTo", "raw.types.MessageActionContactSignUp", "raw.types.MessageActionCustomAction", "raw.types.MessageActionEmpty", "raw.types.MessageActionGameScore", "raw.types.MessageActionGeoProximityReached", "raw.types.MessageActionGiftCode", "raw.types.MessageActionGiftPremium", "raw.types.MessageActionGiveawayLaunch", "raw.types.MessageActionGiveawayResults", "raw.types.MessageActionGroupCall", "raw.types.MessageActionGroupCallScheduled", "raw.types.MessageActionHistoryClear", "raw.types.MessageActionInviteToGroupCall", "raw.types.MessageActionPaymentSent", "raw.types.MessageActionPaymentSentMe", "raw.types.MessageActionPhoneCall", "raw.types.MessageActionPinMessage", "raw.types.MessageActionRequestedPeer", "raw.types.MessageActionRequestedPeerSentMe", "raw.types.MessageActionScreenshotTaken", "raw.types.MessageActionSecureValuesSent", "raw.types.MessageActionSecureValuesSentMe", "raw.types.MessageActionSetChatTheme", "raw.types.MessageActionSetChatWallPaper", "raw.types.MessageActionSetMessagesTTL", "raw.types.MessageActionSuggestProfilePhoto", "raw.types.MessageActionTopicCreate", "raw.types.MessageActionTopicEdit", "raw.types.MessageActionWebViewDataSent", "raw.types.MessageActionWebViewDataSentMe"]


class MessageAction:  # type: ignore
    """Object describing actions connected to a service message.

    Constructors:
        This base type has 43 constructors available.

        .. currentmodule:: hydrogram.raw.types

        .. autosummary::
            :nosignatures:

            MessageActionBoostApply
            MessageActionBotAllowed
            MessageActionChannelCreate
            MessageActionChannelMigrateFrom
            MessageActionChatAddUser
            MessageActionChatCreate
            MessageActionChatDeletePhoto
            MessageActionChatDeleteUser
            MessageActionChatEditPhoto
            MessageActionChatEditTitle
            MessageActionChatJoinedByLink
            MessageActionChatJoinedByRequest
            MessageActionChatMigrateTo
            MessageActionContactSignUp
            MessageActionCustomAction
            MessageActionEmpty
            MessageActionGameScore
            MessageActionGeoProximityReached
            MessageActionGiftCode
            MessageActionGiftPremium
            MessageActionGiveawayLaunch
            MessageActionGiveawayResults
            MessageActionGroupCall
            MessageActionGroupCallScheduled
            MessageActionHistoryClear
            MessageActionInviteToGroupCall
            MessageActionPaymentSent
            MessageActionPaymentSentMe
            MessageActionPhoneCall
            MessageActionPinMessage
            MessageActionRequestedPeer
            MessageActionRequestedPeerSentMe
            MessageActionScreenshotTaken
            MessageActionSecureValuesSent
            MessageActionSecureValuesSentMe
            MessageActionSetChatTheme
            MessageActionSetChatWallPaper
            MessageActionSetMessagesTTL
            MessageActionSuggestProfilePhoto
            MessageActionTopicCreate
            MessageActionTopicEdit
            MessageActionWebViewDataSent
            MessageActionWebViewDataSentMe
    """

    QUALNAME = "hydrogram.raw.base.MessageAction"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.hydrogram.org/en/latest/telegram/base/message-action.html")
