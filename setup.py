#!/usr/bin/env python3
"""
Setup script for QIdle
"""
import sys
from setuptools import setup, find_packages
from qidle import version

try:
    from pyqt_distutils.build_ui import build_ui
    cmdclass = {'build_ui': build_ui}
except ImportError:
    build_ui = None
    cmdclass = {}


# get long description
with open('README.rst', 'r') as readme:
    long_desc = readme.read()


# install requirements
requirements = ['pygments', 'pyqode.python']


data_files = []
if sys.platform == 'linux':
    data_files.append(('/usr/share/applications',
                       ['share/QIdle.desktop']))
    data_files.append(('/usr/share/pixmaps', ['share/QIdle.png']))


setup(
    name='QIdle',
    version=version,
    packages=[p for p in find_packages() if 'test' not in p],
    keywords=['Python; IDLE; IDE'],
    data_files=data_files,
    url='https://github.com/OpenCobolIDE/QIdle',
    license='MIT',
    author='Colin Duquesnoy',
    author_email='colin.duquesnoy@gmail.com',
    description='A clone of IDLE made with PyQt and pyQode',
    long_description=long_desc,
    install_requires=requirements,
    entry_points={'gui_scripts': ['QIdle = qidle.main:main']},
    cmdclass=cmdclass
)
