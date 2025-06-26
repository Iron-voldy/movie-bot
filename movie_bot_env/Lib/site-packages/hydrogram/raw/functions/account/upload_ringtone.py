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


class UploadRingtone(TLObject):  # type: ignore
    """Upload notification sound, use account.saveRingtone to convert it and add it to the list of saved notification sounds.


    Details:
        - Layer: ``181``
        - ID: ``831A83A2``

    Parameters:
        file (:obj:`InputFile <hydrogram.raw.base.InputFile>`):
            Notification sound

        file_name (``str``):
            File name

        mime_type (``str``):
            MIME type of file

    Returns:
        :obj:`Document <hydrogram.raw.base.Document>`
    """

    __slots__: List[str] = ["file", "file_name", "mime_type"]

    ID = 0x831a83a2
    QUALNAME = "functions.account.UploadRingtone"

    def __init__(self, *, file: "raw.base.InputFile", file_name: str, mime_type: str) -> None:
        self.file = file  # InputFile
        self.file_name = file_name  # string
        self.mime_type = mime_type  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadRingtone":
        # No flags
        
        file = TLObject.read(b)
        
        file_name = String.read(b)
        
        mime_type = String.read(b)
        
        return UploadRingtone(file=file, file_name=file_name, mime_type=mime_type)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.file.write())
        
        b.write(String(self.file_name))
        
        b.write(String(self.mime_type))
        
        return b.getvalue()
