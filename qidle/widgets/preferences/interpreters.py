import logging
import os
from pyqode.qt import QtCore, QtGui, QtWidgets

from pyqode.core.api.client import BackendProcess
from pyqode.core.backend import NotRunning
from pyqode.core.managers import BackendManager
from pyqode.python.backend import server

from qidle import icons
from qidle.dialogs.virtualenv import DlgCreateVirtualEnv
from qidle.forms import settings_page_interpreters_ui
from qidle.python import get_installed_packages, is_system_interpreter, \
    upgrade_package, uninstall_package, install_package
from qidle.preferences import Preferences
from qidle.system import get_library_zip_path, WINDOWS, LINUX, DARWIN, \
    get_authentication_program
from qidle.widgets.preferences.base import Page
from qidle.widgets.utils import load_interpreters


def _logger():
    return logging.getLogger(__name__)


class PageInterpreters(Page):
    """
    Page for interpreter settings, the user can choose the default interpreter
    that will be used when running new scripts/projects. The user can also
    add local interpreters or create a virtual environments.

    This page also offer a view of the installed package and let the user
    install, uninstall and update any package.

    The list of packages for a specific interpreter is collected by a
    background process which uses pip.get_installed_distributions. So for this
    to work, pip must be installed on the target interpreter sites-package.
    """
    def __init__(self, parent=None):
        self.ui = settings_page_interpreters_ui.Ui_Form()
        self.movie = QtGui.QMovie(':/icons/loader.gif')
        self.backend = BackendManager(self)
        super(PageInterpreters, self).__init__(self.ui, parent)
        self._create_virtualenv_thread = None
        self.ui.table_packages.itemSelectionChanged.connect(
            self._on_selected_package_changed)
        self.ui.lblMovie.setMovie(self.movie)
        self.ui.combo_interpreters.currentIndexChanged.connect(
            self._refresh_packages)
        self.menu_cfg = QtWidgets.QMenu(self.ui.bt_cfg)
        self.action_add_local = self.menu_cfg.addAction('add local')
        self.action_create_virtualenv = self.menu_cfg.addAction(
            'create virtual env')
        self.action_remove_interpreter = self.menu_cfg.addAction('remove')
        self.ui.bt_cfg.setMenu(self.menu_cfg)

        self.ui.bt_install_package.setIcon(icons.list_add)
        self.ui.bt_uninstall_package.setIcon(icons.list_remove)
        self.ui.bt_upgrade_package.setIcon(icons.go_up)
        self.ui.bt_cfg.setIcon(icons.configure)
        self.action_add_local.setIcon(icons.list_add)
        self.action_remove_interpreter.setIcon(icons.list_remove)
        self.action_create_virtualenv.setIcon(icons.python_virtualenv)
        self._refresh_packages(0)

        self.action_add_local.triggered.connect(self._add_local)
        self.action_remove_interpreter.triggered.connect(
            self._remove_interpreter)
        self.action_create_virtualenv.triggered.connect(
            self._create_virtualenv)

        self.ui.bt_upgrade_package.clicked.connect(self._upgrade)
        self.ui.bt_uninstall_package.clicked.connect(self._uninstall)
        self.ui.bt_install_package.clicked.connect(self._install)

    def stop_backend(self):
        """
        Stops the backend process used to execute pip command on a foreign
        interpreter.
        """
        self.backend.stop()

    def _start_gif(self):
        """
        Starts the gif (waiting) animation, and show the info widget
        """
        self.movie.start()
        self.ui.lblMovie.show()
        self.ui.widgetInfos.show()

    def _clear_packages(self):
        """
        Clears the package table.
        """
        self.ui.table_packages.clear()
        self.ui.table_packages.setColumnCount(3)
        self.ui.table_packages.setRowCount(0)
        self.ui.table_packages.setHorizontalHeaderLabels(
            ['Name', 'Version', 'Path'])

    def _start_backend(self, interpreter):
        """
        Starts the backend process for the specified interpreter
        :param interpreter: The python interpreter used to run the backend.
        """
        self.backend.start(
            server.__file__, interpreter=interpreter,
            args=['-s',  get_library_zip_path()],
            error_callback=self._on_backend_error)

    def _on_backend_error(self, *args):
        self._enable_buttons(True)
        self._stop_gif()

    def _enable_buttons(self, enable):
        """
        Enable/Disable buttons.
        """
        self.ui.combo_interpreters.setEnabled(enable)
        self.ui.bt_cfg.setEnabled(enable)
        self.ui.bt_install_package.setEnabled(enable)
        self.ui.bt_uninstall_package.setEnabled(enable)
        self.ui.bt_upgrade_package.setEnabled(enable)

    @QtCore.pyqtSlot(int)
    def _refresh_packages(self, *args):
        """
        Refreshes the list of packages for the current interpreter.
        """
        _logger().info('refreshing packages')
        self.ui.lblInfos.setText('Refreshing packages list')
        interpreter = self.ui.combo_interpreters.currentText()
        self.action_remove_interpreter.setEnabled(
            not is_system_interpreter(interpreter))
        # stop previous backend, it will be run by a different interpreter
        self._start_gif()
        self._clear_packages()
        self._enable_buttons(False)
        self._start_backend(interpreter)
        # QtCore.QTimer.singleShot(1000, self._send_refesh_request)
        self._send_refesh_request()

    def _send_refesh_request(self):
        """
        Sends the refresh package request to the backend
        """
        try:
            print(self.backend.running)
            self.backend.send_request(
                get_installed_packages, 'refresh_packages',
                on_receive=self._on_refresh_finished)
        except NotRunning:
            if self.backend.exit_code:
                # backend stopped working, may happen if pip or another
                # package is missing for the target interpreter's
                # site-packages
                QtWidgets.QMessageBox.warning(
                    self, 'Refresh failed',
                    'Failed to refresh packages list for %s\n'
                    'Ensure pip and pyqode.python has been installed for the '
                    'target intepreter' %
                    self.ui.combo_interpreters.currentText())
                self._on_refresh_finished(None)
            else:
                # waiting for the backend to start, retry in a few milliseconds
                QtCore.QTimer.singleShot(100, self._send_refesh_request)

    def _stop_gif(self):
        """
        Stops the gif animation and hide the infos widget.
        """
        self.movie.stop()
        self.ui.widgetInfos.hide()
        self.ui.lblMovie.hide()

    def _on_refresh_finished(self, results):
        """
        Display the refreshed list of packages when the backend command
        finished.

        :param status: Command status
        :param results: Command results
        """
        try:
            status, output = results
        except ValueError:
            status = False
            output = []
        self._stop_gif()
        self.stop_backend()
        self._enable_buttons(True)
        self.ui.table_packages.setRowCount(len(output))
        for i, data in enumerate(sorted(output, key=lambda x: x[0])):
            for c, val in enumerate(data):
                item = QtWidgets.QTableWidgetItem(
                    val)
                self.ui.table_packages.setItem(i, c, item)

        self._on_selected_package_changed()
        _logger().info('packages refresh succeeded')

    def _on_selected_package_changed(self):
        """
        Enable buttons depending on whether a package has been selected
        or not.
        """
        enable = self.ui.table_packages.currentRow() != -1
        self.ui.bt_uninstall_package.setEnabled(enable)
        self.ui.bt_upgrade_package.setEnabled(enable)

    def reset(self, default=None):
        """
        Reset the page: reload the list of interpreters and refresh the default
        interpreter packages

        :param default: Default interpreter.
        """
        load_interpreters(self.ui.combo_interpreters, default=default)
        if hasattr(self, 'action_remove_interpreter'):
            self._refresh_packages(0)

    def restore_defaults(self):
        """
        Restor defaults. Removes all added interpreters (locals or virtual
        envs).
        """
        pass

    def apply(self):
        """
        Apply page settings to the application preferences (here we just set
        the default interpreter).
        """
        prefs = Preferences()
        prefs.interpreters.default = self.ui.combo_interpreters.currentText()
        _logger().info('default interpreter: %s' % prefs.interpreters.default)

    def _add_local(self):
        """
        Adds a local interpeter.        """
        path, filter = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Add local interpreter')
        if path:
            lst = Preferences().interpreters.locals
            lst.append(path)
            Preferences().interpreters.locals = lst
            self.reset()
            self.ui.combo_interpreters.setCurrentIndex(
                self.ui.combo_interpreters.count() - 1)
            _logger().info('local interpreter added: %s', path)

    def _remove_interpreter(self):
        """
        Removes the selected interpreter.
        """
        path = self.ui.combo_interpreters.currentText()
        lst = Preferences().interpreters.locals
        try:
            lst.remove(path)
        except ValueError:
            lst = Preferences().interpreters.virtual_envs
            try:
                lst.remove(path)
            except ValueError:
                pass
            else:
                Preferences().interpreters.virtual_envs = lst
        else:
            Preferences().interpreters.locals = lst
        self.ui.combo_interpreters.removeItem(
            self.ui.combo_interpreters.currentIndex())
        _logger().info('interpreter removed: %s', path)

    def _create_virtualenv(self):
        """
        Creates a new virtual environment.
        """
        data = DlgCreateVirtualEnv.get_virtualenv_creation_params(self)
        if data:
            path, interpreter, site_packages = data
            self._clear_packages()
            self._create_virtualenv_thread = CreateVirtualEnvThread()
            self._create_virtualenv_thread.path = path
            self._create_virtualenv_thread.interpreter = interpreter
            self._create_virtualenv_thread.system_site_packages = site_packages
            self._create_virtualenv_thread.created.connect(
                self._on_virtualenv_created)
            self.ui.lblInfos.setText('Creating virtual environment')
            self._start_gif()
            self._create_virtualenv_thread.start()
            _logger().info('creating virtual env')
            _logger().info('path: %s' % path)
            _logger().info('base interpreter: %s' % interpreter)

    def _on_virtualenv_created(self, path):
        """
        Display the new virtual env in the interpreter list and refresh
        its packages.

        :param path: path to the new interpreter
        """
        if path:
            envs = Preferences().interpreters.virtual_envs
            envs.append(path)
            Preferences().interpreters.virtual_envs = envs
            self.reset(default=path)
            self._stop_gif()
            self.ui.widgetInfos.show()
            self.ui.lblInfos.setText('Virtual env sucessfully created at %s' %
                                     path)
            _logger().info('virtualenv created successfully')
        else:
            self._stop_gif()
            self.ui.widgetInfos.show()
            _logger().info('failed to create virtualenv')
            self.ui.lblInfos.setText('Failed to create virtual env')

    def _upgrade(self):
        """
        Upgrade the selected package for the current interpreter.
        """
        package = self.ui.table_packages.item(
            self.ui.table_packages.currentRow(), 0).text()
        _logger().info('upgrading package: %s', package)
        self.run_pip_command(self.ui.combo_interpreters.currentText(),
                             upgrade_package, package,
                             'Upgrading package %s' % package)

    def _uninstall(self):
        """
        Uninstall the selected package for the current interpreter.
        """
        package = self.ui.table_packages.item(
            self.ui.table_packages.currentRow(), 0).text()
        _logger().info('uninstalling package: %s', package)
        self.run_pip_command(
            self.ui.combo_interpreters.currentText(), uninstall_package,
            package, 'Uninstalling package %s' % package)

    def _install(self):
        """
        Install one or more package.

        Asks the user the list of packages to install (each package is
        separated by a space.
        """
        package, status = QtWidgets.QInputDialog.getText(
            self, 'Install package', 'Package:')
        if not status:
            return
        _logger().info('installing packages: %r', package)
        self.run_pip_command(
            self.ui.combo_interpreters.currentText(), install_package,
            package, 'Installing package %s' % package)

    def run_pip_command(self, interpreter, worker_function, package,
                        operation):
        """
        Run a pip command. The command is run on the backend for the current
        interpreter.

        :param interpreter: Interpreter which is going to run the backend
        :param worker_function: The worker function to execute.
        :param package: The list of packages to install, as a string where each
            item is separated by a space.
        :param operation: Operation title (used for the info label)
        """
        self.stop_backend()
        self.ui.lblInfos.setText(operation)
        self._worker = worker_function
        self._package = package
        self.stop_backend()
        self.backend = BackendManager(self)
        process = BackendProcess(self.parent())
        process.finished.connect(self._on_process_finished)
        self.backend._process = process
        server_script = server.__file__.replace('.pyc', '.py')
        port = self.backend.pick_free_port()
        self.backend._port = port
        if LINUX and self._need_root_perms(interpreter):
            _logger().info('running pip command with root privileges')
            auth = get_authentication_program()
            if 'kdesu' in auth:
                # no quotes around command when using kdesu
                cmd = '%s %s %s %s --syspath %s'
            else:
                # gksu requires quotes around command
                cmd = '%s "%s %s %s --syspath %s"'
            cmd = cmd % (auth, interpreter, server_script,
                     str(port), get_library_zip_path())
            process.start(cmd)
        elif DARWIN and self._need_root_perms(interpreter):
            cmd = 'sudo %s %s %s --syspath %s' % (interpreter, server_script,
                 str(port), get_library_zip_path())
            auth_process = QtCore.QProcess()
            auth_process.start('pseudo')
            auth_process.waitForFinished()
            process.start(cmd)
        else:
            self.backend.start(
                server.__file__, interpreter=interpreter,
                args=['-s'] + [get_library_zip_path()])
        QtCore.QTimer.singleShot(100, self._run_command)

    def _on_process_finished(self):
        self._stop_gif()
        self._enable_buttons(True)

    def _need_root_perms(self, interpreter):
        """
        Checks if we need root perms for running the pip command.

        We need persm for any interpreter no installed under home on linux.

        TODO: fix this for mac osx

        :param interpreter: path of the interpreter.
        """
        if LINUX and not interpreter.startswith('/home'):
            return True
        elif DARWIN and not interpreter.startswith(('/usr/local', '/Users/')):
            return True
        return False

    def _run_command(self):
        """
        Run the pip command as soon as the connection has been established.
        """
        try:
            self.backend.send_request(self._worker, self._package,
                                      on_receive=self._on_command_finished)
        except NotRunning:
            QtCore.QTimer.singleShot(100, self._run_command)
        else:
            self._start_gif()

    def _on_command_finished(self, results):
        """
        Displays command results if the command failed or refreshes the list
        of packages.

        :param status: Command status. False if the command failed.
        :param output: Command output.
        """
        status, output = results
        _logger().info('pip command finished: %d - %s', status, output)
        self._stop_gif()
        self.ui.widgetInfos.setVisible(True)
        self.backend._process.kill()
        self.backend = None
        if status:
            self._refresh_packages()
        else:
            QtWidgets.QMessageBox.warning(self, 'Pip command failed', output)


class CreateVirtualEnvThread(QtCore.QThread):
    """
    Thread used to run the process that creates a new virtual env.
    """
    #: Signal emitted when the virtual env has been created
    created = QtCore.pyqtSignal(str)
    #: Path of the environment to create
    path = ''
    #: Base interpreter, must be a system interpreter
    interpreter = ''
    #: True to enable system site-packages. Not recommended.
    system_site_packages = False

    def run(self):
        """
        Creates the virtual env
        """
        command = ['virtualenv', '-p', self.interpreter, self.path]
        if self.system_site_packages:
            command.insert(1, '--system-site-packages')
        command = ' '.join(command)
        if os.system(command) == 0:
            ext = '.exe' if WINDOWS else ''
            path = os.path.join(self.path, 'bin', 'python' + ext)
        else:
            path = None
        self.created.emit(path)
