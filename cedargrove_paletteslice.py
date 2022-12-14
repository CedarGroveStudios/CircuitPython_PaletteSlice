# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
# SPDX-License-Identifier: MIT
"""
`cedargrove_paletteslice`
================================================================================
PaletteSlice is a CircuitPython wrapper class to add list slice capability to a
displayio.Palette object while preserving transparency values. Creates a sliced
displayio.Palette object.

* Author(s): JG

Implementation Notes
--------------------
**Hardware:**

**Software and Dependencies:**
* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

"""

import displayio

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/CedarGroveStudios/CircuitPython_PaletteSlice.git"


class PaletteSlice:
    """A CircuitPython wrapper class to add list slice capability to a displayio.Palette
    object while preserving transparency values."""

    def __init__(self, source_palette):
        """Instantiate the palette slice class. Creates a reference list and a
        displayio.Palette object with source palette color values. Transparency is preserved.
        param displayio.Palette source_palette: The source displayio palette object."""
        self._source_palette = source_palette

        # Create a clean new_palette
        self._new_palette = displayio.Palette(len(self._source_palette))

        # Create reference_list and new_palette copy using the source color and transparency
        self._reference_list = []

        for idx, color in enumerate(self._source_palette):
            # Create reference_list with color and transparency
            self._reference_list.append(
                (color, self._source_palette.is_transparent(idx))
            )
            # Add color to new_palette
            self._new_palette[idx] = color
            # Set new_palette color index transparency
            if self._source_palette.is_transparent(idx):
                self._new_palette.make_transparent(idx)

    def __getitem__(self, key):
        """Create a new_palette slice from reference_list.
        param slice key: The slice object specifying the new palette."""

        # Move reference_list slice into working_list
        working_list = self._reference_list[key]
        self._create_new_palette(working_list)
        return self._new_palette

    def __setitem__(self, key, new_color):
        """Replace or add new color palette to a sliced new_palette.
        param slice key: The target slice object for creating new_palette.
        param displayio.Palette new_color: The palette of new colors."""

        # Extract color and transparency from new_color palette and create working_list
        working_list = []
        for idx, color in enumerate(new_color):
            working_list.append((color, new_color.is_transparent(idx)))

        # Move working_list into the specified reference_list slice
        self._reference_list[key] = working_list
        self._create_new_palette(self._reference_list)
        return self._new_palette

    def __delitem__(self, key):
        """Delete a slice from the primary class displayio.Palette.
        param slice key: The target slice object to delete from the new color palette."""
        # pylint: disable = (unnecessary-pass)
        pass

    def __contains__(self, item):
        """Determine if the primary class displayio.Palette contains the item.
        param ? item: The item to find."""
        # pylint: disable = (unnecessary-pass)
        pass

    @property
    def palette(self):
        """The primary class palette (adjusted displayio.Palette object)."""
        return self._new_palette

    @property
    def reference_list(self):
        """A list of color, transparency tuples from the primary class palette."""
        return self._reference_list

    def append(self, entry):
        """Append a color, transparency tuple to the primary class palette.
        param tuple entry: The color, transparency tuple to be added to the end of
        the primary class palette."""
        # pylint: disable = (unnecessary-pass)
        pass

    """TO-DO: consider adding other list functions/attributes: clear, copy, count, extend,
    index, insert, pop, remove, reverse, sort"""

    def _create_new_palette(self, source_list):
        """Create new_palette from a source list composed of color, transparency tuples."""
        # Create a clean new_palette
        self._new_palette = displayio.Palette(len(source_list))
        # Add contents to new_palette using sliced source_list color and transparency
        for idx, (color, transparency) in enumerate(source_list):
            # Add color to new_palette
            self._new_palette[idx] = color
            if transparency:
                # Set new_palette color index transparency
                self._new_palette.make_transparent(idx)
