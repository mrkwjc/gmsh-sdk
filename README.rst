========
gmsh-sdk
========
The aim of this package is to download and install the `Gmsh SDK <http://gmsh.info>`_
in a pythonic way, i.e. via ``pip`` command. **No gmsh files are maintained here**.
Installation should work under Linux, Windows and MacOSX for both Python 2 and 3. 
Note: on Linux you will need gfortran from gcc-6.x or lower (libgfortran.so.3),
otherwise gmsh will not work.

Just install::

    $ pip install --upgrade gmsh-sdk

and use::

    $ gmsh --help
    $ python -c "import gmsh; gmsh.initialize(['', '--help'])"

