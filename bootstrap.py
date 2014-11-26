#!/usr/bin/env python3
"""
The bootstrap script let you run the editor from source checkout:

1) patch sys.path so that ``qidle`` appears on sys.path
2) parse command line options: let you choose the qt api: 4 or 5
4) check if required dependencies have been installed and warn you about
   missing packages.

.. note:: to run the app with a specific qt api, use the --qt arguments::

        python bootstrap.py --qt 4

"""
import logging
logger = logging.getLogger('boostrap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)
import os
import time
time_start = time.time()
import os.path as osp
import sys

#--- bootstrapping QIdle
logger.info("Executing QIdle from source checkout")

#--- patching sys.path
DEVPATH = osp.dirname(osp.abspath(__file__))
sys.path.insert(0, DEVPATH)
logger.info("01. Patched sys.path with %s", DEVPATH)

#--- configure argument parser
from qidle.argparser import parse_args
args = parse_args()
logger.info('02. Parsed command line arguments: %r', args)


#--- check qt api
if args.qt == 5:
    os.environ['QT_API'] = 'pyqt5'
else:
    os.environ['QT_API'] = 'pyqt4'
try:
    # try with the api selected by the user
    import pyqode.qt
except ImportError:
    # failure: try the other API
    if os.environ['QT_API'] == 'pyqt5':
        os.environ['QT_API'] = 'pyqt4'
    else:
        os.environ['QT_API'] = 'pyqt5'
    try:
        import pyqode.qt
    except ImportError:
        # Total failure, pyqt not found
        logger.exception('03. Failed to import Qt. Please install PyQt4 or '
                          'PyQt5')
        sys.exit(1)
api = os.environ['QT_API'].replace('p', 'P').replace('q', 'Q')
logger.info('03. Imported %s' % api)
if os.environ['QT_API'] == 'pyqt4':
    from PyQt4.Qt import PYQT_VERSION_STR
    from PyQt4.QtCore import QT_VERSION_STR
else:
    from PyQt5.QtCore import PYQT_VERSION_STR
    from PyQt5.QtCore import QT_VERSION_STR
logger.info('    [Qt %s, %s %s]' % (QT_VERSION_STR, api, PYQT_VERSION_STR))

#--- check pyqode root package
try:
    import pyqode
    from pyqode.qt import __version__ as qt_version
    from pyqode.core import __version__ as core_version
    from pyqode.python import __version__ as python_version
except ImportError:
    logger.exception('04. Cannot import pyQode: please install the following packages:'
                     'pyqode.qt, pyqode.core, pyqode.python')
    sys.exit(1)
else:
    logger.info('04. Imported pyQode')
    logger.info('    [pyqode.qt %s, pyqode.core %s, pyqode.python %s]' %
                (qt_version, core_version, python_version))
    if core_version.replace('.dev', '') < '2.4':
        logger.warning('Wrong pyQode version, you need pyqode >= 2.4')
        sys.exit(1)

#--- check IPython
try:
    from IPython import __version__ as IPython_version
except ImportError:
    # warn about missing IPython (optional dependency)
    logger.exception('05. Failed to import IPython. Please install IPython '
                     'otherwise the python console might not work.')
else:
    try:
        from zmq import __version__
    except ImportError:
        logger.exception('05. Failed to import pyzmq. Please install pyzmq '
                         'otherwise the python console might not work')
    else:
        logger.info("05. Imported IPython")
        logger.info('    [IPython %s, pyzmq %s]' % (
            IPython_version, __version__))

#--- check virtualenv
try:
    from virtualenv import __version__
except ImportError:
    logger.exception('06. Failed to import virtualenv. Please install '
                     'virtualenv otherwise virtualenv creation will fail.')
else:
    logger.info('06. Imported virtualenv %s' % __version__)

#--- check setupools
try:
    from setuptools import __version__
except ImportError:
    logger.exception('07. Failed to import setuptools. Please install '
                     'setuptools otherwise the package manager might not work '
                     'as expected.')
else:
    logger.info('07. Imported setuptools %s' % __version__)


#--- check pip
try:
    from pip import __version__
except ImportError:
    logger.exception('08. Failed to import pip. Please install pip otherwise '
                     'the package manager might not work as expected.')
else:
    logger.info('08. Imported pip %s' % __version__)

from qidle import versions
from qidle.main import main
all_versions = versions.get_versions()
logger.info("09. Imported QIdle %s (%s)" % (
    all_versions['qidle'], versions.get_vcs_revision()))
logger.info("    [Python %s %dbits, on %s]" % (
    all_versions['python'], all_versions['bitness'], all_versions['system']))
main()
