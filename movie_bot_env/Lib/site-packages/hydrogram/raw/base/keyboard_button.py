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

KeyboardButton = Union["raw.types.InputKeyboardButtonRequestPeer", "raw.types.InputKeyboardButtonUrlAuth", "raw.types.InputKeyboardButtonUserProfile", "raw.types.KeyboardButton", "raw.types.KeyboardButtonBuy", "raw.types.KeyboardButtonCallback", "raw.types.KeyboardButtonGame", "raw.types.KeyboardButtonRequestGeoLocation", "raw.types.KeyboardButtonRequestPeer", "raw.types.KeyboardButtonRequestPhone", "raw.types.KeyboardButtonRequestPoll", "raw.types.KeyboardButtonSimpleWebView", "raw.types.KeyboardButtonSwitchInline", "raw.types.KeyboardButtonUrl", "raw.types.KeyboardButtonUrlAuth", "raw.types.KeyboardButtonUserProfile", "raw.types.KeyboardButtonWebView"]


class KeyboardButton:  # type: ignore
    """Bot or inline keyboard buttons

    Constructors:
        This base type has 17 constructors available.

        .. currentmodule:: hydrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputKeyboardButtonRequestPeer
            InputKeyboardButtonUrlAuth
            InputKeyboardButtonUserProfile
            KeyboardButton
            KeyboardButtonBuy
            KeyboardButtonCallback
            KeyboardButtonGame
            KeyboardButtonRequestGeoLocation
            KeyboardButtonRequestPeer
            KeyboardButtonRequestPhone
            KeyboardButtonRequestPoll
            KeyboardButtonSimpleWebView
            KeyboardButtonSwitchInline
            KeyboardButtonUrl
            KeyboardButtonUrlAuth
            KeyboardButtonUserProfile
            KeyboardButtonWebView
    """

    QUALNAME = "hydrogram.raw.base.KeyboardButton"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.hydrogram.org/en/latest/telegram/base/keyboard-button.html")
