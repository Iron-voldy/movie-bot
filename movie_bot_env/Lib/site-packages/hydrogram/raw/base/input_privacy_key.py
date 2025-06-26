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

InputPrivacyKey = Union["raw.types.InputPrivacyKeyAbout", "raw.types.InputPrivacyKeyAddedByPhone", "raw.types.InputPrivacyKeyBirthday", "raw.types.InputPrivacyKeyChatInvite", "raw.types.InputPrivacyKeyForwards", "raw.types.InputPrivacyKeyPhoneCall", "raw.types.InputPrivacyKeyPhoneNumber", "raw.types.InputPrivacyKeyPhoneP2P", "raw.types.InputPrivacyKeyProfilePhoto", "raw.types.InputPrivacyKeyStatusTimestamp", "raw.types.InputPrivacyKeyVoiceMessages"]


class InputPrivacyKey:  # type: ignore
    """Privacy keys together with privacy rules » indicate what can or can't someone do and are specified by a PrivacyKey constructor, and its input counterpart InputPrivacyKey.

    Constructors:
        This base type has 11 constructors available.

        .. currentmodule:: hydrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputPrivacyKeyAbout
            InputPrivacyKeyAddedByPhone
            InputPrivacyKeyBirthday
            InputPrivacyKeyChatInvite
            InputPrivacyKeyForwards
            InputPrivacyKeyPhoneCall
            InputPrivacyKeyPhoneNumber
            InputPrivacyKeyPhoneP2P
            InputPrivacyKeyProfilePhoto
            InputPrivacyKeyStatusTimestamp
            InputPrivacyKeyVoiceMessages
    """

    QUALNAME = "hydrogram.raw.base.InputPrivacyKey"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.hydrogram.org/en/latest/telegram/base/input-privacy-key.html")
