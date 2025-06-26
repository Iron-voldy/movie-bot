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

MessageMedia = Union["raw.types.MessageMediaContact", "raw.types.MessageMediaDice", "raw.types.MessageMediaDocument", "raw.types.MessageMediaEmpty", "raw.types.MessageMediaGame", "raw.types.MessageMediaGeo", "raw.types.MessageMediaGeoLive", "raw.types.MessageMediaGiveaway", "raw.types.MessageMediaGiveawayResults", "raw.types.MessageMediaInvoice", "raw.types.MessageMediaPhoto", "raw.types.MessageMediaPoll", "raw.types.MessageMediaStory", "raw.types.MessageMediaUnsupported", "raw.types.MessageMediaVenue", "raw.types.MessageMediaWebPage"]


class MessageMedia:  # type: ignore
    """Media

    Constructors:
        This base type has 16 constructors available.

        .. currentmodule:: hydrogram.raw.types

        .. autosummary::
            :nosignatures:

            MessageMediaContact
            MessageMediaDice
            MessageMediaDocument
            MessageMediaEmpty
            MessageMediaGame
            MessageMediaGeo
            MessageMediaGeoLive
            MessageMediaGiveaway
            MessageMediaGiveawayResults
            MessageMediaInvoice
            MessageMediaPhoto
            MessageMediaPoll
            MessageMediaStory
            MessageMediaUnsupported
            MessageMediaVenue
            MessageMediaWebPage

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetWebPagePreview
            messages.UploadMedia
            messages.UploadImportedMedia
    """

    QUALNAME = "hydrogram.raw.base.MessageMedia"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.hydrogram.org/en/latest/telegram/base/message-media.html")
