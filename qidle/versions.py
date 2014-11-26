"""
Provides some functions to retrieve various version informations.
"""
import os
import subprocess
from qidle import __version__


def get_vcs_revision():
    """
    Gets the vcs revision (git branch + commit).
    """
    def get_git_revision_hash():
        return subprocess.check_output(
            ['git', 'rev-parse', '--short', 'HEAD']).decode('utf-8').replace('\n', '')

    def get_git_branch_name():
        output = subprocess.check_output(['git', 'branch']).decode('utf-8')
        for l in output.splitlines():
            if l.startswith('*'):
                return l.replace('*', '').replace(' ', '')
        return 'master'

    return '%s@%s' % (get_git_revision_hash(), get_git_branch_name())


def get_versions():
    """ Get version information for components used by MellowPlayer """
    import sys
    import platform

    from pyqode.qt.QtCore import __version__ as QT_VERSION_STR
    if os.environ['QT_API'] == 'pyqt4':
        from PyQt4.Qt import PYQT_VERSION_STR
    else:
        from pyqode.qt.QtCore import PYQT_VERSION_STR
    from pyqode.qt import __version__ as qtv
    from pyqode.core import __version__ as corev
    from pyqode.python import __version__ as pythonv

    return {
        'qidle': __version__,
        'python': platform.python_version(),  # "2.7.3"
        'bitness': 64 if sys.maxsize > 2**32 else 32,
        'qt': QT_VERSION_STR,
        'qt_api': os.environ['QT_API'].replace('p', 'P').replace('q', 'Q'),
        'qt_api_ver': PYQT_VERSION_STR,
        'system': platform.system(),
        'pyqode.qt': qtv,
        'pyqode.core': corev,
        'pyqode.python': pythonv,
    }