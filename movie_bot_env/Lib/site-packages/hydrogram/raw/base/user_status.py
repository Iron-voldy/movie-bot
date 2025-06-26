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

UserStatus = Union["raw.types.UserStatusEmpty", "raw.types.UserStatusLastMonth", "raw.types.UserStatusLastWeek", "raw.types.UserStatusOffline", "raw.types.UserStatusOnline", "raw.types.UserStatusRecently"]


class UserStatus:  # type: ignore
    """User online status

    Constructors:
        This base type has 6 constructors available.

        .. currentmodule:: hydrogram.raw.types

        .. autosummary::
            :nosignatures:

            UserStatusEmpty
            UserStatusLastMonth
            UserStatusLastWeek
            UserStatusOffline
            UserStatusOnline
            UserStatusRecently
    """

    QUALNAME = "hydrogram.raw.base.UserStatus"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.hydrogram.org/en/latest/telegram/base/user-status.html")
