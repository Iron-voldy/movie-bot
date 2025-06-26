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


class AddContact(TLObject):  # type: ignore
    """Add an existing telegram user as contact.


    Details:
        - Layer: ``181``
        - ID: ``E8F463D0``

    Parameters:
        id (:obj:`InputUser <hydrogram.raw.base.InputUser>`):
            Telegram ID of the other user

        first_name (``str``):
            First name

        last_name (``str``):
            Last name

        phone (``str``):
            User's phone number, may be omitted to simply add the user to the contact list, without a phone number.

        add_phone_privacy_exception (``bool``, *optional*):
            Allow the other user to see our phone number?

    Returns:
        :obj:`Updates <hydrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["id", "first_name", "last_name", "phone", "add_phone_privacy_exception"]

    ID = 0xe8f463d0
    QUALNAME = "functions.contacts.AddContact"

    def __init__(self, *, id: "raw.base.InputUser", first_name: str, last_name: str, phone: str, add_phone_privacy_exception: Optional[bool] = None) -> None:
        self.id = id  # InputUser
        self.first_name = first_name  # string
        self.last_name = last_name  # string
        self.phone = phone  # string
        self.add_phone_privacy_exception = add_phone_privacy_exception  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AddContact":
        
        flags = Int.read(b)
        
        add_phone_privacy_exception = True if flags & (1 << 0) else False
        id = TLObject.read(b)
        
        first_name = String.read(b)
        
        last_name = String.read(b)
        
        phone = String.read(b)
        
        return AddContact(id=id, first_name=first_name, last_name=last_name, phone=phone, add_phone_privacy_exception=add_phone_privacy_exception)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.add_phone_privacy_exception else 0
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        b.write(String(self.first_name))
        
        b.write(String(self.last_name))
        
        b.write(String(self.phone))
        
        return b.getvalue()
