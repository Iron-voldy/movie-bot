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


class FinishJob(TLObject):  # type: ignore
    """{schema}


    Details:
        - Layer: ``181``
        - ID: ``4F1EBF24``

    Parameters:
        job_id (``str``):
            

        error (``str``, *optional*):
            

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["job_id", "error"]

    ID = 0x4f1ebf24
    QUALNAME = "functions.smsjobs.FinishJob"

    def __init__(self, *, job_id: str, error: Optional[str] = None) -> None:
        self.job_id = job_id  # string
        self.error = error  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FinishJob":
        
        flags = Int.read(b)
        
        job_id = String.read(b)
        
        error = String.read(b) if flags & (1 << 0) else None
        return FinishJob(job_id=job_id, error=error)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.error is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.job_id))
        
        if self.error is not None:
            b.write(String(self.error))
        
        return b.getvalue()
