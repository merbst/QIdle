"""
This module contains utility function related to python interpreters
"""
import glob
import os
import pip
import platform
import re
import sys


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

    def get_root_perms():
        def get_authentification_program():
            """
            kdesu or gksu
            """
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
            for program in ['gksu', 'kdesu']:
                if which(program) is not None:
                    return program
            return None

        pgm = get_authentification_program()
        if pgm:
            pargs = [pgm, sys.executable] + sys.argv + [os.environ]
            # the next line replaces the currently-running process with the sudo
            os.execlpe(pgm, *pargs)

    def need_root_perms():
        return os.geteuid() != 0 and 'win32' not in sys.platform

    def get_output(log_file):
        with open(log_file, 'r') as f:
            output = f.read()
        os.remove(log_file)
        return output

    if need_root_perms():
        get_root_perms()
    log_file, old_stdout = setup_log_file()
    print('pip %s' % ' '.join(args))
    retval = pip.main(args)
    sys.stdout = old_stdout
    return retval, get_output(log_file)


def install_package(package):
    args = ['install', package]
    return run_pip_command(args)


def upgrade_package(package):
    args = ['install', package, '--upgrade']
    return run_pip_command(args)


def uninstall_package(package):
    args = ['uninstall', '-y', package]
    return run_pip_command(args)


# status, output = uninstall_package('pyflakes')
# print('STATUS: ', status)
# print('OUTPUT: ', output)

status, output = install_package('pyflakes')
print('STATUS: ', status)
print('OUTPUT: ', output)

# status, output = upgrade_package('pyflakes')
# print('STATUS: ', status)
# print('OUTPUT: ', output)

