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


class SecureValueErrorFrontSide(TLObject):  # type: ignore
    """Represents an issue with the front side of a document. The error is considered resolved when the file with the front side of the document changes.

    Constructor of :obj:`~hydrogram.raw.base.SecureValueError`.

    Details:
        - Layer: ``181``
        - ID: ``BE3DFA``

    Parameters:
        type (:obj:`SecureValueType <hydrogram.raw.base.SecureValueType>`):
            One of secureValueTypePassport, secureValueTypeDriverLicense, secureValueTypeIdentityCard, secureValueTypeInternalPassport

        file_hash (``bytes``):
            File hash

        text (``str``):
            Error message

    """

    __slots__: List[str] = ["type", "file_hash", "text"]

    ID = 0xbe3dfa
    QUALNAME = "types.SecureValueErrorFrontSide"

    def __init__(self, *, type: "raw.base.SecureValueType", file_hash: bytes, text: str) -> None:
        self.type = type  # SecureValueType
        self.file_hash = file_hash  # bytes
        self.text = text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureValueErrorFrontSide":
        # No flags
        
        type = TLObject.read(b)
        
        file_hash = Bytes.read(b)
        
        text = String.read(b)
        
        return SecureValueErrorFrontSide(type=type, file_hash=file_hash, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.type.write())
        
        b.write(Bytes(self.file_hash))
        
        b.write(String(self.text))
        
        return b.getvalue()
