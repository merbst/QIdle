"""
This module contains utility function related to python interpreters
"""
import glob
import os
import platform
import re


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
    return list(set(executables))


