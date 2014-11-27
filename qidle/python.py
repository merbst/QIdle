"""
This module contains utility function related to python interpreters
"""
import glob
import logging
import os
import subprocess
import tempfile
import pip
import platform
import re
import sys


def _logger():
    return logging.getLogger(__name__)


def detect_system_interpreters():
    """
    Detects system python interpreters
    :return:
    """
    def check_version(path):
        if not os.path.isfile(path):
            return False
        try:
            tmp_dir = os.path.join(tempfile.gettempdir(), 'version')
            with open(tmp_dir, 'w') as stderr:
                output = subprocess.check_output([path, '--version'],
                                                 stderr=stderr).decode()
            if not output:
                # Python2 print version to stderr (at least on OSX)
                with open(tmp_dir, 'r') as stderr:
                    output = stderr.read()
            version = output.split(' ')[1]
        except (IndexError, OSError) as e:
            print('error with path: %s' % path, e)
            return False
        else:
            return version > '2.7.0'

    if platform.system().lower() != 'windows':
        executables = []
        for base in ['/usr/bin', '/usr/local/bin',
                     '/usr/opt', '/usr/local/opt']:
            for pth in glob.glob('%s/python*' % base):
                prog = re.compile(r'python[\d.]*$')
                if prog.match(os.path.split(pth)[1]) and check_version(pth):

                    executables.append(os.path.realpath(pth))
    else:
        executables = set()
        paths = os.environ['PATH'].split(';')
        for path in paths:
            if 'python' in path.lower():
                if 'scripts' in path.lower():
                     path = os.path.abspath(os.path.join(path, os.pardir))
                path = os.path.join(path, 'python.exe')
                if os.path.exists(path):
                    executables.add(path)
    ret_val = list(set(executables))
    _logger().debug('system interpreters: %r' % ret_val)
    return ret_val


def is_system_interpreter(path):
    return path in detect_system_interpreters()


def get_installed_packages(*args):
    packages = []
    for dist in pip.get_installed_distributions(skip=['python']):
        name = dist.key
        version = dist.version
        packages.append((name, version, dist.location))
    return True, packages


def run_pip_command(args):
    def setup_log_file():
        old_stdout = sys.stdout
        log_file = 'tmp'
        sys.stdout = open(log_file, 'w')
        return log_file, old_stdout

    def get_output(log_file):
        with open(log_file, 'r') as f:
            output = f.read()
        try:
            os.remove(log_file)
        except OSError:
            pass
        return output

    log_file, old_stdout = setup_log_file()
    print('pip %s' % ' '.join(args))
    retval = pip.main(args)
    sys.stdout = old_stdout
    return retval == 0, get_output(log_file)


def install_package(package):
    # ensure pyqode.python is also installed (pyqode.core will be installed
    # as a dependency of pyqode.python)
    if 'pyqode' in package and 'pyqode.python' not in package:
        package = 'pyqode.python ' + package
    args = ['install'] + package.split(' ')
    return run_pip_command(args)


def upgrade_package(package):
    args = ['install', package, '--upgrade']
    return run_pip_command(args)


def uninstall_package(package):
    args = ['uninstall', '-y', package]
    return run_pip_command(args)
