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

# Display the background image and source color palette
bkg_bitmap, bkg_palette_source = adafruit_imageload.load(
    BKG_IMAGE_FILE, bitmap=displayio.Bitmap, palette=displayio.Palette
)
# make a sliceable copy of the reference palette
pal_sliceable = PaletteSlice(bkg_palette_source)

# test of append()
print("\n" + ("=" * 15))
print("test of append()")
test = 0xF0F0F0
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

# test of __contains__()
print("\n" + ("=" * 15))
print("test of __contains__")
test = 0
if test in pal_sliceable:
    print(f"< {test} > in pal_sliceable (True)")
else:
    print(f"< {test} > NOT in pal_sliceable (False)")

# place the background image into a tile and append to the primary display group
bkg_tile = displayio.TileGrid(bkg_bitmap, pixel_shader=bkg_palette_source)
primary_group.append(bkg_tile)

slice_label = Label(
    terminalio.FONT, text="PALETTE SLICE TESTER: __getitem__", color=0xFFFFFF
)
slice_label.anchor_point = (0, 0.5)
slice_label.anchored_position = (10, 225)
primary_group.append(slice_label)

display.show(primary_group)
time.sleep(2)

while True:
    start = random.randrange(0, 255)
    stop = random.randrange(0, 255)
    step = random.randrange(-5, 6)
    if step == 0:
        step = 1

    _ = pal_sliceable[start:stop:step]

    if len(pal_sliceable.palette) != 0:
        slice_label.text = (
            f"[{start}:{stop}:{step}]  \nLENGTH={len(pal_sliceable.palette)}"
        )

        bkg_tile.pixel_shader = pal_sliceable.palette
        time.sleep(0.75)

print("\nfin\n")
while True:
    time.sleep(0.1)
