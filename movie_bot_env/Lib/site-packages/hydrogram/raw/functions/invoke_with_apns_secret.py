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


class InvokeWithApnsSecret(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``181``
        - ID: ``0DAE54F8``

    Parameters:
        nonce (``str``):
            

        secret (``str``):
            

        query (Any function from :obj:`~hydrogram.raw.functions`):
            

    Returns:
        Any object from :obj:`~hydrogram.raw.types`
    """

    __slots__: List[str] = ["nonce", "secret", "query"]

    ID = 0x0dae54f8
    QUALNAME = "functions.InvokeWithApnsSecret"

    def __init__(self, *, nonce: str, secret: str, query: TLObject) -> None:
        self.nonce = nonce  # string
        self.secret = secret  # string
        self.query = query  # !X

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InvokeWithApnsSecret":
        # No flags
        
        nonce = String.read(b)
        
        secret = String.read(b)
        
        query = TLObject.read(b)
        
        return InvokeWithApnsSecret(nonce=nonce, secret=secret, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.nonce))
        
        b.write(String(self.secret))
        
        b.write(self.query.write())
        
        return b.getvalue()
