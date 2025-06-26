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

PrivacyRule = Union["raw.types.PrivacyValueAllowAll", "raw.types.PrivacyValueAllowChatParticipants", "raw.types.PrivacyValueAllowCloseFriends", "raw.types.PrivacyValueAllowContacts", "raw.types.PrivacyValueAllowPremium", "raw.types.PrivacyValueAllowUsers", "raw.types.PrivacyValueDisallowAll", "raw.types.PrivacyValueDisallowChatParticipants", "raw.types.PrivacyValueDisallowContacts", "raw.types.PrivacyValueDisallowUsers"]


class PrivacyRule:  # type: ignore
    """Privacy rules together with privacy keys indicate what can or can't someone do and are specified by a PrivacyRule constructor, and its input counterpart InputPrivacyRule.

    Constructors:
        This base type has 10 constructors available.

        .. currentmodule:: hydrogram.raw.types

        .. autosummary::
            :nosignatures:

            PrivacyValueAllowAll
            PrivacyValueAllowChatParticipants
            PrivacyValueAllowCloseFriends
            PrivacyValueAllowContacts
            PrivacyValueAllowPremium
            PrivacyValueAllowUsers
            PrivacyValueDisallowAll
            PrivacyValueDisallowChatParticipants
            PrivacyValueDisallowContacts
            PrivacyValueDisallowUsers
    """

    QUALNAME = "hydrogram.raw.base.PrivacyRule"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.hydrogram.org/en/latest/telegram/base/privacy-rule.html")
