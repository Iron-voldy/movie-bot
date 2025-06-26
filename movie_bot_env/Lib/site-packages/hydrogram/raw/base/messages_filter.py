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

MessagesFilter = Union["raw.types.InputMessagesFilterChatPhotos", "raw.types.InputMessagesFilterContacts", "raw.types.InputMessagesFilterDocument", "raw.types.InputMessagesFilterEmpty", "raw.types.InputMessagesFilterGeo", "raw.types.InputMessagesFilterGif", "raw.types.InputMessagesFilterMusic", "raw.types.InputMessagesFilterMyMentions", "raw.types.InputMessagesFilterPhoneCalls", "raw.types.InputMessagesFilterPhotoVideo", "raw.types.InputMessagesFilterPhotos", "raw.types.InputMessagesFilterPinned", "raw.types.InputMessagesFilterRoundVideo", "raw.types.InputMessagesFilterRoundVoice", "raw.types.InputMessagesFilterUrl", "raw.types.InputMessagesFilterVideo", "raw.types.InputMessagesFilterVoice"]


class MessagesFilter:  # type: ignore
    """Object describes message filter.

    Constructors:
        This base type has 17 constructors available.

        .. currentmodule:: hydrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputMessagesFilterChatPhotos
            InputMessagesFilterContacts
            InputMessagesFilterDocument
            InputMessagesFilterEmpty
            InputMessagesFilterGeo
            InputMessagesFilterGif
            InputMessagesFilterMusic
            InputMessagesFilterMyMentions
            InputMessagesFilterPhoneCalls
            InputMessagesFilterPhotoVideo
            InputMessagesFilterPhotos
            InputMessagesFilterPinned
            InputMessagesFilterRoundVideo
            InputMessagesFilterRoundVoice
            InputMessagesFilterUrl
            InputMessagesFilterVideo
            InputMessagesFilterVoice
    """

    QUALNAME = "hydrogram.raw.base.MessagesFilter"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.hydrogram.org/en/latest/telegram/base/messages-filter.html")
