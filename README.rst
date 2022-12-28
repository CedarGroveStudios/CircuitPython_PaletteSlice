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

A CircuitPython wrapper class to add list slice and extended slice capability to a ``displayio.Palette`` object while preserving transparency.

Two versions are available for testing. ``cedargrove_paletteslice.paletteslice`` is a minimal version that only supports palette slicing and the traditional palette functions:

* ``len(palette)``
* ``.make_transparent(index)``
* ``.make_opaque(index)``
* ``.is_transparent(index)``

The second version, ``cedargrove_paletteslice.paletteslice_acme`` currently extends the functionality of the minimal version with the additional functions:

* ``__contains__(color)``
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

CircuitPython classes such as PaletteSlice cannot inherit ``displayio.Palette`` or ``list`` attributes because of their specific core implementation. Therefore, PaletteSlice uses composition to appear to be a ``displayio.Palette`` object. The PaletteSlice project began as a learning experience for the author but is also became a proof-of-concept for testing the usefulness of list slicing for ``displayio.Palette`` objects. Hopefully the project will encourage list slice and extended slice capabilities be added to ``displayio.Palette`` in the CircuitPython core.

.. image:: https://github.com/CedarGroveStudios/CircuitPython_PaletteSlice/blob/main/media/PaletteSlice_design_brainstorm.png
    :alt: Brainstorm Diagram
    :width: 600pt

PaletteSlide Design Considerations

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

``paletteslice_simpletest.py`` and ``paletteslice_simpletest_acme.py`` are contained in the ``examples`` folder.

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://circuitpython-paletteslice.readthedocs.io/>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/CedarGroveStudios/Cedargrove_CircuitPython_PaletteSlice/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
