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

MessageEntity = Union["raw.types.InputMessageEntityMentionName", "raw.types.MessageEntityBankCard", "raw.types.MessageEntityBlockquote", "raw.types.MessageEntityBold", "raw.types.MessageEntityBotCommand", "raw.types.MessageEntityCashtag", "raw.types.MessageEntityCode", "raw.types.MessageEntityCustomEmoji", "raw.types.MessageEntityEmail", "raw.types.MessageEntityHashtag", "raw.types.MessageEntityItalic", "raw.types.MessageEntityMention", "raw.types.MessageEntityMentionName", "raw.types.MessageEntityPhone", "raw.types.MessageEntityPre", "raw.types.MessageEntitySpoiler", "raw.types.MessageEntityStrike", "raw.types.MessageEntityTextUrl", "raw.types.MessageEntityUnderline", "raw.types.MessageEntityUnknown", "raw.types.MessageEntityUrl"]


class MessageEntity:  # type: ignore
    """Message entities, representing styled text in a message

    Constructors:
        This base type has 21 constructors available.

        .. currentmodule:: hydrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputMessageEntityMentionName
            MessageEntityBankCard
            MessageEntityBlockquote
            MessageEntityBold
            MessageEntityBotCommand
            MessageEntityCashtag
            MessageEntityCode
            MessageEntityCustomEmoji
            MessageEntityEmail
            MessageEntityHashtag
            MessageEntityItalic
            MessageEntityMention
            MessageEntityMentionName
            MessageEntityPhone
            MessageEntityPre
            MessageEntitySpoiler
            MessageEntityStrike
            MessageEntityTextUrl
            MessageEntityUnderline
            MessageEntityUnknown
            MessageEntityUrl
    """

    QUALNAME = "hydrogram.raw.base.MessageEntity"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.hydrogram.org/en/latest/telegram/base/message-entity.html")
