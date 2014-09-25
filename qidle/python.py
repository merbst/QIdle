"""
This module contains utility function related to python interpreters
"""
import glob
import logging
import os
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
    if platform.system().lower() == 'linux':
        executables = []
        for base in ['/usr/bin', '/usr/local/bin']:
            for pth in glob.glob('%s/python*' % base):
                prog = re.compile(r'python[\d.]*$')
                if prog.match(os.path.split(pth)[1]):
                    executables.append(os.path.realpath(pth))
    else:
        executables = set()
        paths = os.environ['PATH'].split(';')
        for path in paths:
            if 'python' in path.lower():
                if 'scripts' in path.lower():
                     path = os.path.abspath(os.path.join(path, os.pardir))
                executables.add(os.path.join(path, 'python.exe'))
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
        os.remove(log_file)
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
