Introduction
============




.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/CedarGroveStudios/CircuitPython_PaletteSlice/workflows/Build%20CI/badge.svg
    :target: https://github.com/CedarGroveStudios/CircuitPython_PaletteSlice/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

A CircuitPython wrapper class to add list slice capability to a ``displayio.Palette`` object while preserving transparency.

This initial version will be used as a learning experience for class composition versus inheritance since neither the ``displayio.Palette`` or ``list`` classes can be inherited. The objective is to first create all the dunder and methods for the class so that a ``displayio.Palette`` object can be manipulated as a list while preserving the ``displayio.Palette`` type/attribute. The final version will likely just implement the ``__getitem__`` and ``__setitem__`` processes to allow slicing, trimming out all the other list methods.

.. image:: https://github.com/CedarGroveStudios/CircuitPython_PaletteSlice/blob/main/media/PaletteSlice_design_brainstorm.png
    :alt: Brainstorm Diagram

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
