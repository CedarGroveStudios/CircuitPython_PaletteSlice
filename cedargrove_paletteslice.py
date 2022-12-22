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
        #return self._new_palette

    def __setitem__(self, key, value):
        """Replace or add new color palette to a sliced new_palette.
        param slice key: The target slice object for creating new_palette.
        param displayio.Palette value: The palette of new colors."""

        # Extract color and transparency from new_color palette and create working_list
        working_list = []
        for idx, color in enumerate(value):
            working_list.append((color, value.is_transparent(idx)))

        # Move working_list into the specified reference_list slice
        self._reference_list[key] = working_list
        self._create_new_palette(self._reference_list)
        #return self._new_palette

    def __delitem__(self, key):
        """Delete a slice from the primary class displayio.Palette. Permanently removes
        the slice from reference_list and creates a new_palette. Usage is
        del PaletteSlice[key]. UNTESTED -- ONLY WORKS IN REPL
        param slice key: The target slice object to delete from the new color palette."""
        """self._reference_list = del self._reference_list[key]
        self._create_new_palette(self._reference_list)
        return self._new_palette"""
        # pylint: disable = (unnecessary-pass)
        pass

    def __contains__(self, obj):
        """Determine if the primary class displayio.Palette contains the object.
        Useage is obj in PaletteSlice. Returns True or False.
        param ? obj: The object to find."""
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

    def append(self, element):
        """Append a color, transparency tuple to the primary class palette. Permanently
        changes reference_list and creates a new_palette. Usage is
        PaletteSlice.append(element). UNTESTED
        param tuple element: The color, transparency tuple to be added to the end of
        the primary class palette."""
        self._reference_list.append(element)
        self._create_new_palette(self._reference_list)
        #return self._new_palette

    def count(self, element):
        """Counts the occurrences of the color, transparency tuple in the reference_list.
        Usage is PaletteSlice.count(element). UNTESTED
        param tuple element: The color, transparency tuple to be added to the end of
        the primary class palette."""
        return self._reference_list.count(element)

    def extend(self, add_list):
        """Append a list of color, transparency tuples to the primary class palette.
        Permanently changes reference_list and creates a new_palette. Usage is
        PaletteSlice.extend(add_list). UNTESTED
        param list add_list: The list of color, transparency tuples to be added to the end of
        the primary class palette."""
        self._reference_list.extend(add_list)
        self._create_new_palette(self._reference_list)
        #return self._new_palette

    def insert(self, key, element):
        """Insert a color, transparency tuple to the primary class palette at slice
        object key. Permanently changes reference_list and creates a new_palette.
        Usage is PaletteSlice.insert(key, element). UNTESTED
        param slice key: The target slice object to insert into the new color palette.
        param tuple element: The color, transparency tuple to be inserted into
        the primary class palette."""
        self._reference_list.insert(key, element)
        self._create_new_palette(self._reference_list)
        #return self._new_palette

    """TO-DO: consider adding other list functions/attributes:
    index(), pop(), remove(), reverse(), sort(), min(), max(), all(), any()"""

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
