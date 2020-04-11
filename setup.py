# -*- coding: utf-8 -*-
########################################################################
# Copyright (C) 2018 by Marek Wojciechowski
# <mwojc@p.lodz.pl>
#
# Distributed under the terms of GPL-2.0 license
# https://opensource.org/licenses/GPL-2.0
########################################################################

from __future__ import print_function
import os
import sys
import platform
import tarfile
import zipfile
from distutils import sysconfig
from setuptools import setup
from setuptools.command.install import install


# Server and gmsh version
server = 'http://gmsh.info/bin'
version = '4.5.6'
iversion = version+'-1'  # installer number

# Determine file name and and url to be downloaded and installed
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


# Create wrapper for install class
class DownloadAndInstall(install):
    def run(self):
        self._download()
        self._extract()
        self._include()
        install.run(self)
    
    def _download(self):
        import requests
        print('Downloading {}, please wait...'.format(url))
        sdk = requests.get(url, allow_redirects=True)
        with open(fname, "wb") as f:
            f.write(sdk.content)
    
    def _extract(self):
        print('Extracting {}, please wait...'.format(fname))
        tar = tarfile.open(fname) if ext == '.tgz' else zipfile.ZipFile(fname, 'r')
        tar.extractall()
    
    def _include(self):
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
        self.distribution.include(data_files=data_files)


# Run setup
if __name__ == "__main__":
    setup(name            = 'gmsh-sdk',
        version           = iversion,
        description       = 'Gmsh SDK installer. Gmsh is a three-dimensional finite element mesh generator.',
        long_description  = open('README.rst', 'r').read(),
        long_description_content_type='text/x-rst',
        maintainer        = 'Marek Wojciechowski',
        maintainer_email  = 'mrkwjc@gmail.com',
        keywords          = ['fem', 'mesh', 'finite element method'],
        url               = 'https://github.com/mrkwjc/gmsh-sdk',
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
        # data_files=data_files,
        scripts           = ['gmsh', 'gmsh.bat'] if plat.startswith('Windows') else ['gmsh'],
        cmdclass          = {'install': DownloadAndInstall},
        setup_requires    = ['requests']
        )
