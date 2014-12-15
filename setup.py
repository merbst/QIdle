#!/usr/bin/env python3
"""
Setup script for QIdle
"""
import qidle
from setuptools import setup, find_packages


# add build_ui command. This command is only used by developer to easily
# update the ui scripts.
# To use this command, you need to install the pyqt-distutils packages (using
# pip).
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
requirements = [
    'pyqode.python', 'ipython', 'pyzmq', 'virtualenv', 'pip>=1.5.6',
    'setuptools>=7.0'
]


# install desktop entry and pixmap on linux
data_files = []
# if sys.platform == 'linux':
#     data_files.append(('/usr/share/applications',
#                        ['share/QIdle.desktop']))
#     data_files.append(('/usr/share/pixmaps', ['share/QIdle.png']))


# run setup
setup(
    name='QIdle',
    version=qidle.__version__,
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
