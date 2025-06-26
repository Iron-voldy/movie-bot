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

from io import BytesIO

from hydrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from hydrogram.raw.core import TLObject
from hydrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class Contacts(TLObject):  # type: ignore
    """The current user's contact list and info on users.

    Constructor of :obj:`~hydrogram.raw.base.contacts.Contacts`.

    Details:
        - Layer: ``181``
        - ID: ``EAE87E42``

    Parameters:
        contacts (List of :obj:`Contact <hydrogram.raw.base.Contact>`):
            Contact list

        saved_count (``int`` ``32-bit``):
            Number of contacts that were saved successfully

        users (List of :obj:`User <hydrogram.raw.base.User>`):
            User list

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            contacts.GetContacts
    """

    __slots__: List[str] = ["contacts", "saved_count", "users"]

    ID = 0xeae87e42
    QUALNAME = "types.contacts.Contacts"

    def __init__(self, *, contacts: List["raw.base.Contact"], saved_count: int, users: List["raw.base.User"]) -> None:
        self.contacts = contacts  # Vector<Contact>
        self.saved_count = saved_count  # int
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Contacts":
        # No flags
        
        contacts = TLObject.read(b)
        
        saved_count = Int.read(b)
        
        users = TLObject.read(b)
        
        return Contacts(contacts=contacts, saved_count=saved_count, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.contacts))
        
        b.write(Int(self.saved_count))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
