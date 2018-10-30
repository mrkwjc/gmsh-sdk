# gmsh-sdk
This project downloads and installs Gmsh SDK in a pythonic way, just for your convenience.
Installation should work under Linux, Windows and MacOSX for both Python 2 and 3.

Install with:
```
pip install --upgrade gmsh-sdk
```
and then write your scripts:
```python
# simple.py example form Gmsh repo...
import gmsh
import sys

gmsh.initialize(sys.argv)
gmsh.model.add("square")
gmsh.model.geo.addPoint(0, 0, 0, 0.1, 1)
gmsh.model.geo.addPoint(1, 0, 0, 0.1, 2)
gmsh.model.geo.addPoint(1, 1, 0, 0.1, 3)
gmsh.model.geo.addPoint(0, 1, 0, 0.1, 4)
gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(2, 3, 2)
gmsh.model.geo.addLine(3, 4, 3)
# try automatic assignement of tag
line4 = gmsh.model.geo.addLine(4, 1)
gmsh.model.geo.addCurveLoop([1, 2, 3, line4], 1)
gmsh.model.geo.addPlaneSurface([1], 6)
gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(2)
gmsh.write("square.msh")
```
A wrapper for `gmsh` executable is also available so the following should work as well:
```python
import subprocess
subprocess.call(['gmsh', '--help'])
```
