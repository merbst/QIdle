import functools
import os
import platform
from zipfile import ZipFile

from qidle import version

WINDOWS = platform.system() == 'Windows'
LINUX = platform.system() == 'Linux'
DARWIN = platform.system() == 'Darwin'


def ensure_cache_exists(func):
    @functools.wraps(func)
    def wrapper(*args, **kwds):
        ret = func(*args, **kwds)
        try:
            os.makedirs(ret)
        except OSError:
            pass
        return ret
    return wrapper


@ensure_cache_exists
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
    return os.path.join(get_cache_directory(), 'libraries-%s.zip' % str(version))


def embed_package_into_zip(packages, zip_path=get_library_zip_path()):
    print('-- creating zip file with external libraries: %s' % zip_path)
    with ZipFile(zip_path, 'w') as myzip:
        for package in packages:
            pfile = package.__file__
            path = pfile if not '__init__.py' in pfile else os.path.dirname(
                pfile)
            print('--- adding %s ' % package.__name__)
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
                            # print('   - %s' % arcname)
                            myzip.write(fn, arcname=arcname)
            else:
                arcname = os.path.split(path)[1]
                myzip.write(path, arcname=arcname)


if __name__ == '__main__':
    import jedi, pep8, pyqode, pyqode.core, pyqode.python, pyqode.qt, qidle, frosted, pies
    import time
    s = time.time()
    embed_package_into_zip([jedi, pep8, pyqode.core, pyqode.python,
                            pyqode.qt, qidle])
    print(time.time() - s)