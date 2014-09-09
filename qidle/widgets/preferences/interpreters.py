import os
import platform
from PyQt4 import QtCore, QtGui
from pyqode.core.backend import NotConnected
from pyqode.core.managers import BackendManager
from pyqode.python.backend import server
from qidle.interpreter import get_installed_packages
from qidle.widgets.preferences.base import Page
from qidle.widgets.utils import load_interpreters
from qidle.forms.preferences import page_interpreters_ui


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
        self.ui = page_interpreters_ui.Ui_Form()
        self.movie = QtGui.QMovie(':/icons/loader.gif')
        self.backend = None
        super().__init__(self.ui, parent)
        self.ui.lblMovie.setMovie(self.movie)
        self.ui.combo_interpreters.currentIndexChanged.connect(
            self._refresh_packages)
        self.menu_cfg = QtGui.QMenu(self.ui.bt_cfg)
        self.action_add_local = self.menu_cfg.addAction('add local')
        self.action_create_virtualenv = self.menu_cfg.addAction(
            'create virtual env')
        self.action_remove_interpreter = self.menu_cfg.addAction('remove')
        self.ui.bt_cfg.setMenu(self.menu_cfg)

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
        zip_path = os.path.join(os.getcwd(), 'libraries.zip')
        if not os.path.exists(zip_path):
            if platform.system().lower() == 'linux':
                zip_path = '/usr/share/qidle/libraries.zip'
        paths = [
            os.getcwd(),
            zip_path
        ]
        return list(set(paths))

    def _clear_packages(self):
        self.ui.table_packages.clear()
        self.ui.table_packages.setColumnCount(3)
        self.ui.table_packages.setRowCount(0)
        self.ui.table_packages.setHorizontalHeaderLabels(
            ['Name', 'Version', 'Path'])

    def _start_backend(self, interpreter):
        self._stop_backend()
        self.backend = BackendManager(self)
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
        # stop previous backend, it will be run by a different interpreter
        self._start_movie()
        self._clear_packages()
        self._start_backend(self.ui.combo_interpreters.currentText())
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

    def reset(self):
        load_interpreters(self.ui.combo_interpreters)
        self._refresh_packages(0)

    def restore_defaults(self):
        pass

    def apply(self):
        pass
