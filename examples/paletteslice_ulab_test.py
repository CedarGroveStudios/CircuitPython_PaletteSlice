# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
# SPDX-License-Identifier: MIT
"""
`paletteslice_ulab_test`
================================================================================
A test of the PaletteSlice wrapper class with a sliced ulab narray list.

* Author(s): JG
"""

import time
import board
import terminalio
import displayio
from ulab import numpy as np
import adafruit_imageload
from adafruit_display_text.label import Label
from cedargrove_paletteslice.paletteslice import PaletteSlice
from cedargrove_rgb_spectrumtools import visible

BKG_IMAGE_FILE = "orchid.bmp"
NUMBER_OF_COLORS = 255  # narray size
FRAME_DURATION = 2  # seconds per frame

# Define the display and primary display group
display = board.DISPLAY
display.brightness = 0.1
primary_group = displayio.Group()

# Display the test image and source color palette
test_bitmap, test_palette_source = adafruit_imageload.load(
    BKG_IMAGE_FILE, bitmap=displayio.Bitmap, palette=displayio.Palette
)

# Instantiate a sliceable copy of the reference palette
pal_sliceable = PaletteSlice(test_palette_source)

# Place the test image into a tile and append to the primary display group
test_tile = displayio.TileGrid(test_bitmap, pixel_shader=test_palette_source)
primary_group.append(test_tile)

# Prepare a test narray for the ulab narray test
#   Create a ulab test array
ulab_narray = np.zeros(NUMBER_OF_COLORS)
for idx in range(NUMBER_OF_COLORS):
    #   Create a range of spectral color values
    ulab_narray[idx] = int(visible.index_to_rgb(idx / NUMBER_OF_COLORS))

#   Instantiate a sliceable palette object from test_palette
test_palette = displayio.Palette(NUMBER_OF_COLORS)
ulab_test_palette = PaletteSlice(test_palette)

#   Copy the ulab narray object into the sliceable palette
ulab_test_palette[:] = ulab_narray[:]

#   Define on-screen label for slice object and palette length
slice_label = Label(terminalio.FONT, text="", color=0xFFFFFF)
slice_label.anchor_point = (0, 0.5)
slice_label.anchored_position = (10, 225)
primary_group.append(slice_label)

# Display the primary group
display.show(primary_group)

while True:

    # Show the source image and label
    # print("TEST of source image and palette")
    test_tile.pixel_shader = pal_sliceable[:]
    slice_label.text = "PALETTE SLICE: source image and palette"
    time.sleep(FRAME_DURATION)

    # Show the ulab image and label
    # print("TEST of ulab narray pseudocolor palette")
    test_tile.pixel_shader = ulab_test_palette[:]
    slice_label.text = "PALETTE SLICE: ulab narray pseudocolor TEST"
    time.sleep(FRAME_DURATION)
