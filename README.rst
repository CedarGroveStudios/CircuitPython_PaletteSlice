Introduction
============

CedarGroveStudios/CircuitPython_PaletteSlice
--------------------------------------------


.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/CedarGroveStudios/CircuitPython_PaletteSlice/workflows/Build%20CI/badge.svg
    :target: https://github.com/CedarGroveStudios/CircuitPython_PaletteSlice/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

*A CircuitPython wrapper class to add list slice and extended slice capability to a ``displayio.Palette`` object while preserving transparency.*

The default functionality of a ``displayio.Palette`` object is similar to a Python list object, but very limited. For example, the integer value of color elements of the palette can be modified but only one element can be changed at a time. The PaletteSlice wrapper class provides the ability to use a slice object to specify a subset of a palette to change or to create a new palette from a source palette. Both slice and extended slice objects are supported.

In addition to a palette property (``.palette``), PaletteSlice contains a list representation (``.reference_list``) of the source palette with color and transparency values stored as a tuple.

The ability to create and manipulate palettes using slicing allows for the use of a standardized palette to be used to provide a color scheme for multiple objects within a project framework, regardless of an object's color depth. For example, a standard color palette of 1024 individual colors could be used for a 64-color bitmap object by slicing the standard palette using an extended slice object:

``bitmap_image.pixel_shader = source_palette[::16]``

======

Note that a PaletteSlice object behaves correctly only when a slice object is included in the syntax. For example,

``bitmap_image.pixel_shader = source_palette``

will cause a type error:

``TypeError: pixel_shader must be displayio.Palette or displayio.ColorConverter``

At a minimum, the PaletteSlice object must include the "all" slice object in order to return a displayio.Palette object:

``bitmap_image.pixel_shader = source_palette[:]``

======


Two Versions -- Minimal and Acme
--------------------------------

Two versions of PaletteSlice are available. ``cedargrove_paletteslice.paletteslice`` is a minimal version that only supports palette slicing and the traditional palette functions:

* ``.is_transparent(index)``
* ``.make_transparent(index)``
* ``.make_opaque(index)``
* ``len(palette)``

The second version, ``cedargrove_paletteslice.paletteslice_acme`` currently extends the functionality of the minimal version with the additional functions:

* ``__contains__(color)``  (usage: ``color in PaletteSlice.palette`` )
* ``.append(color)``
* ``.count(color)``
* ``.index(color)``
* ``.pop(key)``

Under consideration for a future "acme" version are:

* ``.entend(new_palette)``
* ``.insert(key)``
* ``.remove(color)``
* ``.reverse()``
* ``.sort(key, reverse)``

and perhaps the extended functions of:

* ``min(palette)``
* ``max(palette)``

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install cedargrove_paletteslice

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: python

    from cedargrove_paletteslice.paletteslice import PaletteSlice
    sliceable_palette = PaletteSlice(source_palette)

    # Create a new palette from the sliceable palette
    new_sliced_palette = sliceable_palette[0:124:2]

``paletteslice_simpletest.py``, ``paletteslice_acme_simpletest.py``, and ``paletteslice_ulab_test.py`` are contained in the ``examples`` folder.

Using slice with narray Pseudocolor Palettes:

.. image:: https://github.com/CedarGroveStudios/CircuitPython_PaletteSlice/blob/main/media/display_capture_composite.png
    :alt: Using slice with narray Pseudocolor Palettes
    :width: 600pt

Documentation
=============
`PaletteSlice API Documentation <https://github.com/CedarGroveStudios/CircuitPython_PaletteSlice/blob/main/media/pseudo_rtd_cedargrove_paletteslice.pdf>`_

.. image:: https://github.com/CedarGroveStudios/CircuitPython_PaletteSlice/blob/main/media/PaletteSlice_class_desc_minimal.png
    :alt: Brainstorm Diagram
    :width: 600pt

.. image:: https://github.com/CedarGroveStudios/CircuitPython_PaletteSlice/blob/main/media/PaletteSlice_class_desc_acme.png
    :alt: Brainstorm Diagram
    :width: 600pt

.. image:: https://github.com/CedarGroveStudios/CircuitPython_PaletteSlice/blob/main/media/PaletteSlice_class_internals.png
    :alt: Brainstorm Diagram
    :width: 600pt

PaletteSlice Design Considerations
----------------------------------

CircuitPython classes such as PaletteSlice cannot inherit ``displayio.Palette`` or ``list`` attributes because of their specific core implementation. Therefore, PaletteSlice uses composition to appear to be a ``displayio.Palette`` object.

The PaletteSlice project began as a learning experience for the author but is also became a proof-of-concept for testing the usefulness of list slicing for ``displayio.Palette`` objects. It is hoped that this project will encourage list slice and extended slice capabilities be added to ``displayio.Palette`` in the CircuitPython core.

.. image:: https://github.com/CedarGroveStudios/CircuitPython_PaletteSlice/blob/main/media/PaletteSlice_design_brainstorm.png
    :alt: Brainstorm Diagram
    :width: 600pt

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/CedarGroveStudios/Cedargrove_CircuitPython_PaletteSlice/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
