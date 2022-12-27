# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
# SPDX-License-Identifier: MIT
"""
`paletteslice_simpletest_lite`
================================================================================
A test of the PaletteSlice (lite) wrapper class.

* Author(s): JG
"""

import time
import random
import board
import terminalio
import displayio
from ulab import numpy as np
import adafruit_imageload
from adafruit_display_text.label import Label
from cedargrove_paletteslice.cedargrove_paletteslice_lite import PaletteSlice

BKG_IMAGE_FILE = "jp_hohimer.bmp"


def print_list(new_list):
    print("print_list object:", new_list)
    print("print_list object length:", len(new_list))
    for i, (color, transparency) in enumerate(new_list):
        print(f"index: {i:03.0f} color: {color:#08x} transparency: {transparency}")


def print_palette(new_palette):
    print("print_palette object:", new_palette)
    print("print_palette object length:", len(new_palette))
    for i, color in enumerate(new_palette):
        print(
            f"index: {i:03.0f} color: {color:#08x} transparency: {new_palette.is_transparent(i)}"
        )


# Prepare a test narray for the ulab narray test
# Create a ulab test array of 32 colors
ulab_narray = np.zeros(32)
for idx in range(32):
    ulab_narray[idx] = int(idx * 255 * 255) + 0x808080

# Instantiate a sliceable palette object from test_palette
test_palette = displayio.Palette(32)
ulab_test_palette = PaletteSlice(test_palette)

# "Broadside" copy the ulab narray object into the sliceable palette
ulab_test_palette[:] = ulab_narray[:]

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

# Test of __get__
print("\n" + ("=" * 15))
print("TEST __get__()")
start = 0  # Slice start
stop = 5  # Slice stop
step = 1  # Slice step
print(f"  slice object: [{start}:{stop}:{step}]")
get_palette = pal_sliceable[start:stop:step]
print_palette(get_palette)

# Test of __set__
print("\n" + ("=" * 15))
print("TEST __set__()")
start = 1  # Slice start
stop = 6  # Slice stop
step = 1  # Slice step
print(f"  slice object: [{start}:{stop}:{step}]")
pal_sliceable[start:stop:step] = get_palette
print_palette(pal_sliceable[0:8])

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
print("TEST of default image")
time.sleep(2)

print("TEST of ulab narray -generated palette")
test_tile.pixel_shader = ulab_test_palette[:]
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
