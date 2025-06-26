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


class AutoSaveSettings(TLObject):  # type: ignore
    """Media autosave settings

    Constructor of :obj:`~hydrogram.raw.base.AutoSaveSettings`.

    Details:
        - Layer: ``181``
        - ID: ``C84834CE``

    Parameters:
        photos (``bool``, *optional*):
            Whether photos should be autosaved to the gallery.

        videos (``bool``, *optional*):
            Whether videos should be autosaved to the gallery.

        video_max_size (``int`` ``64-bit``, *optional*):
            If set, specifies a size limit for autosavable videos

    """

    __slots__: List[str] = ["photos", "videos", "video_max_size"]

    ID = 0xc84834ce
    QUALNAME = "types.AutoSaveSettings"

    def __init__(self, *, photos: Optional[bool] = None, videos: Optional[bool] = None, video_max_size: Optional[int] = None) -> None:
        self.photos = photos  # flags.0?true
        self.videos = videos  # flags.1?true
        self.video_max_size = video_max_size  # flags.2?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AutoSaveSettings":
        
        flags = Int.read(b)
        
        photos = True if flags & (1 << 0) else False
        videos = True if flags & (1 << 1) else False
        video_max_size = Long.read(b) if flags & (1 << 2) else None
        return AutoSaveSettings(photos=photos, videos=videos, video_max_size=video_max_size)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.photos else 0
        flags |= (1 << 1) if self.videos else 0
        flags |= (1 << 2) if self.video_max_size is not None else 0
        b.write(Int(flags))
        
        if self.video_max_size is not None:
            b.write(Long(self.video_max_size))
        
        return b.getvalue()
