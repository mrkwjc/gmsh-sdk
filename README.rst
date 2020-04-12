========
gmsh-sdk
========
The aim of this package is to download and install the `Gmsh SDK <http://gmsh.info>`_
in a pythonic way, i.e. via ``pip`` command. **No gmsh files are maintained here**.
Installation should work under Linux, Windows and MacOSX for both Python 2 and 3.

The package ensures that *latest stable* Gmsh SDK is installed.

Before installation make sure that possibly conflicting packages are uninstalled::

    $ pip uninstall gmsh-sdk gmsh-sdk-git

then install (or upgrade) ``gmsh-sdk-stable``::

    $ pip install --upgrade --force-reinstall gmsh-sdk-stable

and use::

    $ gmsh --help
    $ python -c "import gmsh; gmsh.initialize(['', '--help'])"
