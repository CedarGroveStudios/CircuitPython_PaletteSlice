# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
# SPDX-License-Identifier: MIT
"""
`paletteslice_simpletest`
================================================================================
A test of the PaletteSlice wrapper class.

* Author(s): JG
"""

import time
import random
import board
import terminalio
import displayio
import adafruit_imageload
from adafruit_display_text.label import Label
from cedargrove_paletteslice import PaletteSlice

BKG_IMAGE_FILE = "jp_hohimer.bmp"


def print_list(new_list):
    print("print_list object:", new_list)
    print("print_list object length:", len(new_list))
    for i, (color, transparency) in enumerate(new_list):
        print(f"index: {i:03.0f} color: {color:#08x} transparency: {transparency}")


# Define the display and primary display group
display = board.DISPLAY
display.brightness = 0.05
primary_group = displayio.Group()

# Display the test image and source color palette
test_bitmap, test_palette_source = adafruit_imageload.load(
    BKG_IMAGE_FILE, bitmap=displayio.Bitmap, palette=displayio.Palette
)
# Instantiate a sliceable copy of the reference palette
pal_sliceable = PaletteSlice(test_palette_source)

# Test of append()
print("\n" + ("=" * 15))
print("TEST append()")
test = 0xF0F0F0
print(f"  value to insert: {test:#08x}")

(last_color, last_transparency) = pal_sliceable.reference_list[-1]
length = len(pal_sliceable.palette)
print(
    f"length BEFORE append: {length} last item: {last_color:#08x} {last_transparency}"
)

pal_sliceable.append(test)

(last_color, last_transparency) = pal_sliceable.reference_list[-1]
length = len(pal_sliceable.palette)
print(
    f"length  AFTER append: {length} last item: {last_color:#08x} {last_transparency}"
)

# Test of __contains__
print("\n" + ("=" * 15))
print("TEST __contains__")
test = 0
print(f"  value to find: {test}")

if test in pal_sliceable:
    print(f"< {test} > in pal_sliceable (True)")
else:
    print(f"< {test} > NOT in pal_sliceable (False)")

# Place the test image into a tile and append to the primary display group
test_tile = displayio.TileGrid(test_bitmap, pixel_shader=test_palette_source)
primary_group.append(test_tile)

# Define on-screen label for slice object and palette length
slice_label = Label(
    terminalio.FONT, text="PALETTE SLICE TESTER: __getitem__", color=0xFFFFFF
)
slice_label.anchor_point = (0, 0.5)
slice_label.anchored_position = (10, 225)
primary_group.append(slice_label)

# Show the test image and label
display.show(primary_group)
time.sleep(2)

while True:
    # Create a random slice object; prohibit step == 0
    start = random.randrange(0, 255)
    stop = random.randrange(0, 255)
    step = random.randrange(-5, 6)
    if step == 0:
        step = 1

    # Slice the palette and use for bkg_tile
    test_tile.pixel_shader = pal_sliceable[start:stop:step]

    if len(pal_sliceable.palette) != 0:
        # Display slice object and pause to view
        slice_label.text = f"[{start}:{stop}:{step}]  \nLENGTH={len(pal_sliceable)}"
        time.sleep(0.75)

print("\nfin\n")
while True:
    time.sleep(0.1)
