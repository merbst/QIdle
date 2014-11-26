import functools
import logging
import os
import platform
from zipfile import ZipFile
from qidle import __version__

WINDOWS = platform.system() == 'Windows'
LINUX = platform.system() == 'Linux'
DARWIN = platform.system() == 'Darwin'


def ensure_directory_exists(func):
    @functools.wraps(func)
    def wrapper(*args, **kwds):
        ret = func(*args, **kwds)
        try:
            os.makedirs(ret)
        except OSError:
            pass
        return ret
    return wrapper


@ensure_directory_exists
def get_cache_directory():
    """
    Gets the platform specific cache directory (where we store the log file and
    the temporary files create by the linter).
    :return: platform specific cache directory.
    """
    if WINDOWS:
        return os.path.join(os.path.expanduser("~"), 'QIdle', 'cache')
    elif DARWIN:
        return os.path.join(os.path.expanduser("~"), 'Library',
                            'Caches', 'QIdle')
    else:
        return os.path.join(os.path.expanduser("~"), '.cache', 'QIdle')


def get_library_zip_path():
    lib = 'libraries-%s.zip' % __version__
    return os.path.join(get_cache_directory(), lib)


def _logger():
    return logging.getLogger(__name__)


def embed_package_into_zip(packages, zip_path=get_library_zip_path()):
    _logger().debug('creating zip file with external libraries: %s' % zip_path)
    with ZipFile(zip_path, 'w') as myzip:
        for package in packages:
            pfile = package.__file__
            pfile = pfile.replace('.pyc', '.py')
            path = pfile if not '__init__.py' in pfile else os.path.dirname(
                pfile)
            _logger().debug(' - adding %s ' % package.__name__)
            parent_path = os.path.abspath(os.path.join(path, '..'))
            if package.__name__ == 'pyqode':
                myzip.write(pfile, 'pyqode/__init__.py')
                continue
            elif 'pyqode' in package.__name__:
                parent_path = os.path.abspath(os.path.join(parent_path, '..'))
            if os.path.isdir(path):
                for dirpath, dirs, files in os.walk(path):
                    for f in files:
                        if '__pycache__' not in dirpath and \
                                os.path.splitext(f)[1] not in ['.pyc', '.zip']:
                            fn = os.path.join(dirpath, f)
                            arcname = os.path.relpath(fn, parent_path)
                            myzip.write(fn, arcname=arcname)
            else:
                arcname = os.path.split(path)[1]
                myzip.write(path, arcname=arcname)


def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def get_authentication_program():
    """
    Gets the authentication program used to run command as root (on linux only).

    The function try to use one of the following programs:
        - gksu
        - kdesu

    """
    if LINUX:
        for program in ['gksu', 'kdesu']:
            if which(program) is not None:
                return program
    elif DARWIN:
        return 'pseudo'  # https://github.com/sstephenson/pseudo
    return None


if __name__ == '__main__':
    import jedi, pep8, pyqode, pyqode.core, pyqode.python, pyqode.qt, qidle, frosted, pies
    import time
    s = time.time()
    embed_package_into_zip([jedi, pep8, pyqode.core, pyqode.python,
                            pyqode.qt, qidle])
    print(time.time() - s)
