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


class SponsoredMessageReportResultChooseOption(TLObject):  # type: ignore
    """{schema}

    Constructor of :obj:`~hydrogram.raw.base.channels.SponsoredMessageReportResult`.

    Details:
        - Layer: ``181``
        - ID: ``846F9E42``

    Parameters:
        title (``str``):
            

        options (List of :obj:`SponsoredMessageReportOption <hydrogram.raw.base.SponsoredMessageReportOption>`):
            

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            channels.ReportSponsoredMessage
    """

    __slots__: List[str] = ["title", "options"]

    ID = 0x846f9e42
    QUALNAME = "types.channels.SponsoredMessageReportResultChooseOption"

    def __init__(self, *, title: str, options: List["raw.base.SponsoredMessageReportOption"]) -> None:
        self.title = title  # string
        self.options = options  # Vector<SponsoredMessageReportOption>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredMessageReportResultChooseOption":
        # No flags
        
        title = String.read(b)
        
        options = TLObject.read(b)
        
        return SponsoredMessageReportResultChooseOption(title=title, options=options)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.title))
        
        b.write(Vector(self.options))
        
        return b.getvalue()
