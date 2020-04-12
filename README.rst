========
gmsh-sdk
========
The aim of this package is to download and install the `Gmsh SDK <http://gmsh.info>`_
in a pythonic way, i.e. via ``pip`` command. **No gmsh files are maintained here**.
Installation should work under Linux, Windows and MacOSX for both Python 2 and 3.

The package installs *latest stable* Gmsh SDK.

Just install (or upgrade) ``gmsh-sdk-stable``::

    $ pip install --upgrade --force-reinstall gmsh-sdk-stable

and use it::

    $ gmsh --help
    $ python -c "import gmsh; gmsh.initialize(['', '--help'])"
