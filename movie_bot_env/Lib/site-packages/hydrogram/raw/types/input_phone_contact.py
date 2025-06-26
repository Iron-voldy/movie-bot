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


class InputPhoneContact(TLObject):  # type: ignore
    """Phone contact.

    Constructor of :obj:`~hydrogram.raw.base.InputContact`.

    Details:
        - Layer: ``181``
        - ID: ``F392B7F4``

    Parameters:
        client_id (``int`` ``64-bit``):
            An arbitrary 64-bit integer: it should be set, for example, to an incremental number when using contacts.importContacts, in order to retry importing only the contacts that weren't imported successfully, according to the client_ids returned in contacts.importedContacts.retry_contacts.

        phone (``str``):
            Phone number

        first_name (``str``):
            Contact's first name

        last_name (``str``):
            Contact's last name

    """

    __slots__: List[str] = ["client_id", "phone", "first_name", "last_name"]

    ID = 0xf392b7f4
    QUALNAME = "types.InputPhoneContact"

    def __init__(self, *, client_id: int, phone: str, first_name: str, last_name: str) -> None:
        self.client_id = client_id  # long
        self.phone = phone  # string
        self.first_name = first_name  # string
        self.last_name = last_name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPhoneContact":
        # No flags
        
        client_id = Long.read(b)
        
        phone = String.read(b)
        
        first_name = String.read(b)
        
        last_name = String.read(b)
        
        return InputPhoneContact(client_id=client_id, phone=phone, first_name=first_name, last_name=last_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.client_id))
        
        b.write(String(self.phone))
        
        b.write(String(self.first_name))
        
        b.write(String(self.last_name))
        
        return b.getvalue()
