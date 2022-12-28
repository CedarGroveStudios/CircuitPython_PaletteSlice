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
from ulab import numpy as np
import adafruit_imageload
from adafruit_display_text.label import Label
from cedargrove_paletteslice.cedargrove_paletteslice import PaletteSlice

BKG_IMAGE_FILE = "orchid.bmp"


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

# Test of append()
print("\n" + ("=" * 15))
print("TEST append()")
test = 0xF0F0F0
print(f"  value to insert: {test:#08x}")

(last_color, last_transparency) = pal_sliceable.reference_list[-1]
length = len(pal_sliceable)
print(
    f"length BEFORE append: {length} last item: {last_color:#08x} {last_transparency}"
)

pal_sliceable.append(test)

(last_color, last_transparency) = pal_sliceable.reference_list[-1]
length = len(pal_sliceable)
print(
    f"length  AFTER append: {length} last item: {last_color:#08x} {last_transparency}"
)

# Test of is_transparent(), make_transparent(), make_opaque()
print("\n" + ("=" * 15))
test = -1  # Index to test
print("TEST is_transparent(), make_transparent(), make_opaque()")
print(f"  index value for test: {test}")
print(f"  is_transparent: {pal_sliceable.is_transparent(test)}")
pal_sliceable.make_transparent(test)
print(f"AFTER make_transparent -> is_transparent: {pal_sliceable.is_transparent(test)}")
pal_sliceable.make_opaque(test)
print(f"AFTER make_opaque      -> is_transparent: {pal_sliceable.is_transparent(test)}")

# Test of count()
print("\n" + ("=" * 15))
print("TEST count()")
test = 0xFFFFFF  # Color value for search
print(f"  color value for search: {test:#08x}")

print(f"number of occurrences: {pal_sliceable.count(test)}")

# Test of index()
print("\n" + ("=" * 15))
print("TEST index()")
test = 0xFFFFF0  # Color value for search
print(f"  color value for search: {test:#08x}")

print(f"first index found: {pal_sliceable.index(test)}")

# Test of pop()
print("\n" + ("=" * 15))
print("TEST pop()")
test = -1  # Remove last item
print(f"  index to pop: {test}")

print(f"  length BEFORE pop: {len(pal_sliceable)}")
print(f"value removed: {pal_sliceable.pop(test):#08x}")
print(f"  length  AFTER pop: {len(pal_sliceable)}")

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
    terminalio.FONT, text="PALETTE SLICE: __getitem__ TEST", color=0xFFFFFF
)
slice_label.anchor_point = (0, 0.5)
slice_label.anchored_position = (10, 225)
primary_group.append(slice_label)

# Show the test image and label
display.show(primary_group)
print("TEST of default image")
time.sleep(2)
slice_label.text = "PALETTE SLICE: source image and palette"
time.sleep(3)

print("TEST of ulab narray -generated palette")
slice_label.text = "PALETTE SLICE: ulab narray false colors TEST"
# Prepare a test narray for the ulab narray test
# Create a ulab test array
NUMBER_OF_COLORS = 255
ulab_narray = np.zeros(NUMBER_OF_COLORS)
for idx in range(NUMBER_OF_COLORS):
    # Create a range of pseudorandom color values
    ulab_narray[idx] = int(idx * 255 * 255)

# Instantiate a sliceable palette object from test_palette
test_palette = displayio.Palette(NUMBER_OF_COLORS)
ulab_test_palette = PaletteSlice(test_palette)

# "Broadside" copy the ulab narray object into the sliceable palette
ulab_test_palette[:] = ulab_narray[:]
test_tile.pixel_shader = ulab_test_palette[:]
time.sleep(3)


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
