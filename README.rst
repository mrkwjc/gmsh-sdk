============
gmsh-sdk-git
============
The aim of this package is to download and install the `Gmsh SDK <http://gmsh.info>`_
in a pythonic way, i.e. via ``pip`` command. **No gmsh files are maintained here**.
Installation should work under Linux, Windows and MacOSX for both Python 2 and 3.

This package installs *latest git snapshot* of Gmsh SDK.

Before installation make sure that possibly conflicting ``gmsh-sdk`` is uninstalled::

    $ pip uninstall gmsh-sdk

then install (or upgrade) ``gmsh-sdk-git``::

    $ pip install --upgrade --force-reinstall gmsh-sdk-git

and use::

    $ gmsh --help
    $ python -c "import gmsh; gmsh.initialize(['', '--help'])"
