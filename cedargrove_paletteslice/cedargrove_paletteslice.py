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
        """Returns a new_palette slice from reference_list.

        param slice key: The slice object specifying the new palette."""

        # Move reference_list slice into working_list
        working_list = self._reference_list[key]
        self._create_new_palette(working_list)
        return self._new_palette

    def __setitem__(self, key, value):
        """Replace or add new color palette, list, or narray to a sliced new_palette.

        param slice key: The target slice object for creating new_palette.
        param Union(displayio.Palette, list, narray) value: The palette of new colors."""

        # Extract color and transparency from new_color palette and create working_list
        working_list = []
        list_flag = isinstance(value[0], (float, int))
        for idx, color in enumerate(value):
            if list_flag:
                # value is an array or list
                working_list.append((int(color), False))
            else:
                # value is likely a palette
                working_list.append((color, value.is_transparent(idx)))

        # Move working_list into the specified reference_list slice
        self._reference_list[key] = working_list
        self._create_new_palette(self._reference_list)

    def __delitem__(self, key):
        """UNTESTED:
        Delete a slice from the primary class displayio.Palette. Permanently removes
        the slice from reference_list and creates a new_palette.
        Usage is del PaletteSlice[key]. ONLY WORKS IN REPL

        param slice key: The target slice object to delete from the new color palette."""
        """self._reference_list = del self._reference_list[key]
        self._create_new_palette(self._reference_list)"""
        # pylint: disable = (unnecessary-pass)
        pass

    def __contains__(self, color):
        """Determine if reference_list contains the singleton color
        (not a tuple). Returns True or False.
        Usage is color in PaletteSlice.palette.

        param int color: The color to find."""
        for _, element in enumerate(self._reference_list):
            if element[0] == color:
                return True
        return False

    def __len__(self):
        return len(self._new_palette)

    @property
    def palette(self):
        """The primary class palette (adjusted displayio.Palette object)."""
        return self._new_palette

    @property
    def reference_list(self):
        """A list of color, transparency tuples from the primary class palette."""
        return self._reference_list

    def append(self, color):
        """Append a color value to the primary class palette.
        Permanently changes reference_list and creates a new_palette.
        Usage is PaletteSlice.append(color).

        param tuple color: The color value tuple to be added to the end of
        the primary class palette."""
        self._reference_list.append((color, False))
        self._create_new_palette(self._reference_list)

    def count(self, color):
        """Counts the occurrences of the color value in the reference_list.
        Usage is PaletteSlice.count(color).

        param int color: The color value to count."""
        counter = 0
        for _, (element, _) in enumerate(self._reference_list):
            if element == color:
                counter += 1
        return counter

    def extend(self, add_list):
        """UNTESTED:
        Append a list of color, transparency tuples to the primary class
        palette. Permanently changes reference_list and creates a new_palette.
        Usage is PaletteSlice.extend(add_list).

        param list add_list: The list of color, transparency tuples to be added to the
        end of the primary class palette."""
        self._reference_list.extend(add_list)
        self._create_new_palette(self._reference_list)

    def insert(self, key, color):
        """UNTESTED:
        Insert an opaque color value into the primary class palette at
        slice object key. Permanently changes reference_list and creates a new_palette.
        Usage is PaletteSlice.insert(key, color).

        param slice key: The target slice object to insert into the new color palette.
        param tuple element: The color, transparency tuple to be inserted into
        the primary class palette."""
        self._reference_list.insert(key, (color, False))
        self._create_new_palette(self._reference_list)

    def pop(self, key):
        """Remove a color, transparency tuple from the primary class palette at
        slice object key. Permanently changes reference_list and creates a new_palette.
        Returns the removed color value from the reference_list tuple.
        Usage is PaletteSlice.pop(key).

        param slice key: The target slice object to insert into the new color palette."""
        color, _ = self._reference_list[key]
        self._reference_list.pop(key)
        self._create_new_palette(self._reference_list)
        return color

    def index(self, color, start=None, stop=None):
        """Returns the smallest index where the color matches the element value or
        None if not found. start and stop optionally specify the starting and
        ending index for the search.
        Usage is PaletteSlice.index(color).

        param integer color: The color value for the search.
        param integer start: The starting index value. Defaults to None, the start of the list.
        param integer end: The ending index value. Defaults to None, the end of the list."""

        if not start:
            start = 0
        if not stop:
            stop = len(self._reference_list) - 1

        for index, (element, _) in enumerate(self._reference_list):
            if element == color:
                return index
        return None

    """TO-DO: consider adding other list functions/attributes:
    remove(), reverse(), sort(), min(), max(), all(), any()"""

    def is_transparent(self, index):
        """Returns True if the palette index is transparent. Returns False if opaque.
        Usage: PaletteSlice.is_transparend(index)

        param int index: The palette color index to test."""
        return self._reference_list[index][1]

    def make_transparent(self, index):
        """Set a palette index to transparency. Permanently modifies reference_list
        and new_palette.
        Usage: PaletteSlice.make_opaque(index)

        param int index: The palette color index to be made transparent."""
        self._reference_list[index] = (self._reference_list[index][0], True)
        self._create_new_palette(self._reference_list)

    def make_opaque(self, index):
        """Set a palette index to opaque. Permanently modifies reference_list
        and new_palette.
        Usage: PaletteSlice.make_opaque(index)

        param int index: The palette color index to be made opaque."""
        self._reference_list[index] = (self._reference_list[index][0], False)
        self._create_new_palette(self._reference_list)

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
