import os
import platform
from PyQt4 import QtCore, QtGui
from pyqode.core.backend import NotConnected
from pyqode.core.managers import BackendManager
from pyqode.python.backend import server
from qidle.interpreter import get_installed_packages
from qidle.preferences import Preferences
from qidle.widgets.preferences.base import Page
from qidle.forms.preferences import page_interpreters_ui


class PageInterpreters(Page):
    def __init__(self, parent=None):
        self.ui = page_interpreters_ui.Ui_Form()
        super().__init__(self.ui, parent)
        self.movie = QtGui.QMovie(':/icons/loader.gif')
        self.ui.lblMovie.setMovie(self.movie)
        self.backend = None
        self.normal_icon = QtGui.QIcon(':/icons/interpreter-sys.png')
        self.venv_icon = QtGui.QIcon(':/icons/interpreter-venv.png')
        self._load_interpreters()
        self._refresh_packages(0)
        self.ui.combo_interpreters.currentIndexChanged.connect(
            self._refresh_packages)

    def __del__(self):
        self._stop_backend()

    def _load_interpreters(self):
        default = Preferences().cache.default_interpreter()
        default_index = 0
        for interpreter, itype in sorted(
                Preferences().cache.get_interpreters()):
            index = self.ui.combo_interpreters.count()
            icon = self.normal_icon if 'virtualenv' else self.venv_icon
            self.ui.combo_interpreters.addItem(icon, interpreter)
            if interpreter == default:
                default_index = index
        self.ui.combo_interpreters.setCurrentIndex(default_index)

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
        self.ui.bt_configure.setEnabled(enable)
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
        pass

    def restore_defaults(self):
        pass

    def apply(self):
        pass
