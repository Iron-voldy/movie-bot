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

InputStickerSet = Union["raw.types.InputStickerSetAnimatedEmoji", "raw.types.InputStickerSetAnimatedEmojiAnimations", "raw.types.InputStickerSetDice", "raw.types.InputStickerSetEmojiChannelDefaultStatuses", "raw.types.InputStickerSetEmojiDefaultStatuses", "raw.types.InputStickerSetEmojiDefaultTopicIcons", "raw.types.InputStickerSetEmojiGenericAnimations", "raw.types.InputStickerSetEmpty", "raw.types.InputStickerSetID", "raw.types.InputStickerSetPremiumGifts", "raw.types.InputStickerSetShortName"]


class InputStickerSet:  # type: ignore
    """Represents a stickerset

    Constructors:
        This base type has 11 constructors available.

        .. currentmodule:: hydrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputStickerSetAnimatedEmoji
            InputStickerSetAnimatedEmojiAnimations
            InputStickerSetDice
            InputStickerSetEmojiChannelDefaultStatuses
            InputStickerSetEmojiDefaultStatuses
            InputStickerSetEmojiDefaultTopicIcons
            InputStickerSetEmojiGenericAnimations
            InputStickerSetEmpty
            InputStickerSetID
            InputStickerSetPremiumGifts
            InputStickerSetShortName
    """

    QUALNAME = "hydrogram.raw.base.InputStickerSet"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.hydrogram.org/en/latest/telegram/base/input-sticker-set.html")
