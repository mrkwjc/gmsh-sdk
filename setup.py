# -*- coding: utf-8 -*-
########################################################################
# Copyright (C) 2018 by Marek Wojciechowski
# <mwojc@p.lodz.pl>
#
# Distributed under the terms of GPL-2.0 license
# https://opensource.org/licenses/GPL-2.0
########################################################################

from __future__ import print_function
import sys
import os
import platform
from future.moves.urllib.request import urlopen
import tarfile
import zipfile
from distutils import sysconfig
from distutils.core import setup

if __name__ == "__main__":
    server = 'http://gmsh.info/bin'
    version = '4.0.4'

    system = platform.system().lower()
    machine = platform.machine().lower()
    plat = None
    plat = 'Linux64' if 'linux' in system and '64' in machine else plat
    plat = 'Linux32' if 'linux' in system and '64' not in machine else plat
    plat = 'Windows64' if 'windows' in system and '64' in machine else plat
    plat = 'Windows32' if 'windows' in system and '64' not in machine else plat
    plat = 'MacOSX' if 'darwin' in system else plat
    if plat is None:
        raise TypeError(
                "Platform '{}' is not supported.".format(system+'-'+machine))
    name = "gmsh-{}-{}-sdk".format(version, plat)
    ext = '.zip' if plat.startswith('Windows') else '.tgz'
    fname = name + ext
    if plat.startswith('Linux'):
        url = server + "/Linux/" + fname
    elif plat.startswith('Windows'):
        url = server + "/Windows/" + fname
    else:
        url = server + "/MacOSX/" + fname
    print('Downloading {}, please wait...'.format(url))
    with open(fname, "wb") as f:
        f.write(urlopen(url).read())
    # urllib.urlretrieve(url, fname)
    print('Unpacking {}, please wait...'.format(fname))
    tar = tarfile.open(fname) if ext == '.tgz' else zipfile.ZipFile(fname, 'r')
    tar.extractall()
    pth = open('gmsh.pth', 'w')
    pth.write(name+'/lib\n')
    pth.write(name+'/bin')
    pth.close()
    site_dirpath = sysconfig.get_python_lib(prefix='')
    dirs = [site_dirpath]
    files = [['gmsh.pth']]
    for (dirpath, dirnames, filenames) in os.walk(name):
        dirs += [os.path.join(site_dirpath, dirpath)]
        files += [[os.path.join(dirpath, file) for file in filenames]]
    data_files = list(zip(dirs, files))

    setup(name              = 'gmsh-sdk',
        version           = version,
        description       = 'A three-dimensional finite element mesh generator',
        keywords          = ['mesh', 'finite element method'],
        url               = 'http://gmsh.info/',
        license           = 'GPL-2',
        platforms         = 'Posix, Windows',
        classifiers       = ['Development Status :: 5 - Production/Stable',
                            'Intended Audience :: Education',
                            'Intended Audience :: Science/Research',
                            'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
                            'Operating System :: POSIX :: Linux',
                            'Operating System :: Microsoft :: Windows',
                            'Operating System :: MacOS :: MacOS X',
                            'Programming Language :: C',
                            'Programming Language :: C++',
                            'Programming Language :: Python :: Implementation :: CPython',
                            'Topic :: Scientific/Engineering'],
        data_files=data_files,
        scripts=['gmsh']
        )
