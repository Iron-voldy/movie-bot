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


class AttachMenuBotIcon(TLObject):  # type: ignore
    """Represents an attachment menu icon for bot mini apps »

    Constructor of :obj:`~hydrogram.raw.base.AttachMenuBotIcon`.

    Details:
        - Layer: ``181``
        - ID: ``B2A7386B``

    Parameters:
        name (``str``):
            One of the following values: note that animated icons must be played when the user clicks on the button, activating the bot mini app. default_static - Default attachment menu icon in SVG format placeholder_static - Default placeholder for opened Web Apps in SVG format ios_static - Attachment menu icon in SVG format for the official iOS app ios_animated - Animated attachment menu icon in TGS format for the official iOS app android_animated - Animated attachment menu icon in TGS format for the official Android app macos_animated - Animated attachment menu icon in TGS format for the official native Mac OS app ios_side_menu_static - Side menu icon in PNG format for the official iOS app android_side_menu_static - Side menu icon in SVG format for the official android app macos_side_menu_static - Side menu icon in PNG format for the official native Mac OS app

        icon (:obj:`Document <hydrogram.raw.base.Document>`):
            The actual icon file.

        colors (List of :obj:`AttachMenuBotIconColor <hydrogram.raw.base.AttachMenuBotIconColor>`, *optional*):
            Attachment menu icon colors.

    """

    __slots__: List[str] = ["name", "icon", "colors"]

    ID = 0xb2a7386b
    QUALNAME = "types.AttachMenuBotIcon"

    def __init__(self, *, name: str, icon: "raw.base.Document", colors: Optional[List["raw.base.AttachMenuBotIconColor"]] = None) -> None:
        self.name = name  # string
        self.icon = icon  # Document
        self.colors = colors  # flags.0?Vector<AttachMenuBotIconColor>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuBotIcon":
        
        flags = Int.read(b)
        
        name = String.read(b)
        
        icon = TLObject.read(b)
        
        colors = TLObject.read(b) if flags & (1 << 0) else []
        
        return AttachMenuBotIcon(name=name, icon=icon, colors=colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.colors else 0
        b.write(Int(flags))
        
        b.write(String(self.name))
        
        b.write(self.icon.write())
        
        if self.colors is not None:
            b.write(Vector(self.colors))
        
        return b.getvalue()
