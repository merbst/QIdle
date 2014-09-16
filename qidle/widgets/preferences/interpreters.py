import os
import platform
from PyQt4 import QtCore, QtGui
from pyqode.core.backend import NotConnected
from pyqode.core.managers import BackendManager
from pyqode.python.backend import server
from qidle import icons
from qidle.dialogs.pip import DlgPipCommand
from qidle.dialogs.virtualenv import DlgCreateVirtualEnv
from qidle.forms import settings_page_interpreters_ui
from qidle.python import get_installed_packages, is_system_interpreter, \
    upgrade_package
from qidle.preferences import Preferences
from qidle.system import get_library_zip_path, WINDOWS
from qidle.widgets.preferences.base import Page
from qidle.widgets.utils import load_interpreters


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
        self.backend = None
        super(PageInterpreters, self).__init__(self.ui, parent)
        self._create_virtualenv_thread = None
        self.ui.table_packages.itemSelectionChanged.connect(
            self._on_selected_package_changed)
        self.ui.lblMovie.setMovie(self.movie)
        self.ui.combo_interpreters.currentIndexChanged.connect(
            self._refresh_packages)
        self.menu_cfg = QtGui.QMenu(self.ui.bt_cfg)
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

    def __del__(self):
        self._stop_backend()

    def _stop_backend(self):
        if self.backend is not None:
            self.backend.stop()
            self.backend = None

    def _start_movie(self):
        self.movie.start()
        self.ui.widgetInfos.show()

    def _get_sys_paths(self):
        # adapt sys path so that the backend can find pyqode and qidle
        # package if ran by a different process than sys.executable
        paths = [
            get_library_zip_path()
        ]
        return paths

    def _clear_packages(self):
        self.ui.table_packages.clear()
        self.ui.table_packages.setColumnCount(3)
        self.ui.table_packages.setRowCount(0)
        self.ui.table_packages.setHorizontalHeaderLabels(
            ['Name', 'Version', 'Path'])

    def _start_backend(self, interpreter):
        self._stop_backend()
        self.backend = BackendManager(self)
        print('start backend', interpreter, self._get_sys_paths())
        self.backend.start(
            server.__file__, interpreter=interpreter,
            args=['-s'] + self._get_sys_paths())

    def _enable_buttons(self, enable):
        self.ui.combo_interpreters.setEnabled(enable)
        self.ui.bt_cfg.setEnabled(enable)
        self.ui.bt_install_package.setEnabled(enable)
        self.ui.bt_uninstall_package.setEnabled(enable)
        self.ui.bt_upgrade_package.setEnabled(enable)

    @QtCore.pyqtSlot(int)
    def _refresh_packages(self, index):
        interpreter = self.ui.combo_interpreters.currentText()
        self.action_remove_interpreter.setEnabled(
            not is_system_interpreter(interpreter))
        # stop previous backend, it will be run by a different interpreter
        self._start_movie()
        self._clear_packages()
        self._start_backend(interpreter)
        self._send_request()
        self._enable_buttons(False)

    def _send_request(self):
        try:
            self.backend.send_request(
                get_installed_packages, 'refresh_packages',
                on_receive=self._on_refresh_finished)
        except NotConnected:
            if self.backend.exit_code:
                # backend stopped working, may happen if pip or another
                # package is missing for the target interpreter's
                # site-packages
                QtGui.QMessageBox.warning(
                    self, 'Refresh failed',
                    'Failed to refresh packages list. \n'
                    'Make sure you installed pip for the target interpreter: '
                    '%s' % self.ui.combo_interpreters.currentText())
                self._on_refresh_finished(False, None)
            else:
                # waiting for the backend to start, retry in a few milliseconds
                QtCore.QTimer.singleShot(100, self._send_request)

    def _stop_movie(self):
        self.movie.stop()
        self.ui.widgetInfos.hide()

    def _on_refresh_finished(self, status, results):
        self._stop_movie()
        self._stop_backend()
        self._enable_buttons(True)
        if status is False:
            return
        self.ui.table_packages.setRowCount(len(results))
        for i, data in enumerate(sorted(results, key=lambda x: x[0])):
            for c, val in enumerate(data):
                item = QtGui.QTableWidgetItem(
                    val)
                self.ui.table_packages.setItem(i, c, item)

        self._on_selected_package_changed()

    def _on_selected_package_changed(self):
        enable = self.ui.table_packages.currentRow() != -1
        self.ui.bt_uninstall_package.setEnabled(enable)
        self.ui.bt_upgrade_package.setEnabled(enable)

    def reset(self):
        load_interpreters(self.ui.combo_interpreters)
        if hasattr(self, 'action_remove_interpreter'):
            self._refresh_packages(0)

    def restore_defaults(self):
        pass

    def apply(self):
        prefs = Preferences()
        prefs.interpreters.default = self.ui.combo_interpreters.currentText()

    def _add_local(self):
        path = QtGui.QFileDialog.getOpenFileName(self, 'Add local interpreter')
        if path:
            lst = Preferences().interpreters.locals
            lst.append(path)
            Preferences().interpreters.locals = lst
            self.reset()
            self.ui.combo_interpreters.setCurrentIndex(
                self.ui.combo_interpreters.count() - 1)

    def _remove_interpreter(self):
        path = self.ui.combo_interpreters.currentText()
        lst = Preferences().interpreters.locals
        lst.remove(path)
        Preferences().interpreters.locals = lst
        self.ui.combo_interpreters.removeItem(
            self.ui.combo_interpreters.currentIndex())

    def _create_virtualenv(self):
        data = DlgCreateVirtualEnv.get_virtualenv_creation_params(self)
        if data:
            path, interpreter, site_packages = data
            self._create_virtualenv_thread = CreateVirtualEnvThread()
            self._create_virtualenv_thread.path = path
            self._create_virtualenv_thread.interpreter = interpreter
            self._create_virtualenv_thread.system_site_packages = site_packages
            self._create_virtualenv_thread.created.connect(
                self._on_virtualenv_created)
            self.ui.lblInfos.setText('Creating virtual environment')
            self._start_movie()
            self._create_virtualenv_thread.start()

    def _on_virtualenv_created(self, path):
        envs = Preferences().interpreters.virtual_envs
        envs.append(path)
        Preferences().interpreters.virtual_envs = envs
        self.reset()
        self.ui.combo_interpreters.setCurrentIndex(
            self.ui.combo_interpreters.count() - 1)
        self._stop_movie()
        self.ui.lblInfos.setText('Refreshing packages list')

    def _upgrade(self):
        package = self.ui.table_packages.item(
            self.ui.table_packages.currentRow(), 0).text()
        DlgPipCommand.run_command(
            self, self.ui.combo_interpreters.currentText(), upgrade_package,
            package, 'Upgrading package %s' % package)


class CreateVirtualEnvThread(QtCore.QThread):
    created = QtCore.pyqtSignal(str)
    path = ''
    interpreter = ''
    system_site_packages = False

    def run(self):
        command = ['virtualenv', '-p', self.interpreter, self.path]
        if self.system_site_packages:
            command.insert(1, '--system-site-packages')
        command = ' '.join(command)
        print(os.system(command))
        ext = '.exe' if WINDOWS else ''
        path = os.path.join(self.path, 'bin', 'python' + ext)
        self.created.emit(path)
