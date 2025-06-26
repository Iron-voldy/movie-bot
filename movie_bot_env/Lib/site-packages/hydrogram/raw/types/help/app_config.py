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


class AppConfig(TLObject):  # type: ignore
    """Contains various client configuration parameters

    Constructor of :obj:`~hydrogram.raw.base.help.AppConfig`.

    Details:
        - Layer: ``181``
        - ID: ``DD18782E``

    Parameters:
        hash (``int`` ``32-bit``):
            Hash for pagination, for more info click here

        config (:obj:`JSONValue <hydrogram.raw.base.JSONValue>`):
            Client configuration parameters

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetAppConfig
    """

    __slots__: List[str] = ["hash", "config"]

    ID = 0xdd18782e
    QUALNAME = "types.help.AppConfig"

    def __init__(self, *, hash: int, config: "raw.base.JSONValue") -> None:
        self.hash = hash  # int
        self.config = config  # JSONValue

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AppConfig":
        # No flags
        
        hash = Int.read(b)
        
        config = TLObject.read(b)
        
        return AppConfig(hash=hash, config=config)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        b.write(self.config.write())
        
        return b.getvalue()
