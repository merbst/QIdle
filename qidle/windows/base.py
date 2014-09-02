import weakref
from pyqode.core.widgets import MenuRecentFiles
from pyqode.qt import QtCore, QtWidgets, QtGui
from qidle.forms import win_script_ui
from qidle.settings import Settings


class WindowBase(QtWidgets.QMainWindow):
    closed = QtCore.Signal(QtWidgets.QMainWindow)

    @property
    def app(self):
        """
        :rtype: qidle.app.Application
        """
        return self._app()

    def _setup_mnu_file(self, app, ui):
        self.ui.menuFile.clear()
        self.ui.menuFile.addAction(self.ui.actionNew_file)
        self.ui.menuFile.addAction(self.ui.actionOpen_file)
        self.ui.menuFile.addSeparator()
        self.ui.menuFile.addAction(self.ui.actionNew_project)
        self.ui.menuFile.addAction(self.ui.actionOpen_directory)
        self.ui.menuFile.addSeparator()
        self.menu_recents = MenuRecentFiles(self,
                                            app.recent_files_manager,
                                            title='Recents')
        self.ui.menuFile.addMenu(self.menu_recents)
        self.ui.menuFile.addSeparator()
        self.ui.menuFile.addAction(self.ui.actionSave)
        self.ui.menuFile.addAction(self.ui.actionSave_as)
        self.ui.menuFile.addSeparator()
        self.ui.menuFile.addAction(self.ui.actionClose)
        self.ui.menuFile.addAction(self.ui.actionQuit)
        ui.actionNew_file.triggered.connect(self._on_new_file_triggered)
        ui.actionOpen_file.triggered.connect(self._on_open_file_triggered)
        self.ui.actionNew_project.setDisabled(True)
        self.ui.actionOpen_directory.setDisabled(True)
        ui.actionSave.triggered.connect(self.save)
        ui.actionSave_as.triggered.connect(self.save_as)
        self.ui.actionClose.triggered.connect(self._close)
        self.ui.actionQuit.triggered.connect(self._quit)

    def _setup_windows_menu(self, ui):
        ui.actionZoom_height.triggered.connect(self.zoom_height)
        ui.menuTools.addActions(self.createPopupMenu().actions())
        action_prev_window = QtWidgets.QAction(self)
        action_prev_window.setShortcut('Alt+Up')
        action_prev_window.triggered.connect(self._show_prev_window)
        self.addAction(action_prev_window)
        action_next_window = QtWidgets.QAction(self)
        action_next_window.setShortcut('Alt+Down')
        action_next_window.triggered.connect(self._show_next_window)
        self.addAction(action_next_window)

    def _setup_help_menu(self):
        self.ui.actionPython_docs.triggered.connect(self._show_python_docs)

    def __init__(self, ui, app):
        super().__init__()
        self._app = weakref.ref(app)
        self._height = None
        # path of the script, 'Untitled' if new file not saved to disk.
        self.path = None
        self.ui = ui
        self.ui.setupUi(self)
        self._setup_mnu_file(app, ui)
        self._setup_windows_menu(ui)
        self._setup_help_menu()

    def configure_shortcuts(self):
        self.addActions(self.ui.menuFile.actions())
        # menu edit already added
        self.addActions(self.ui.menuRun.actions())
        self.addActions(self.ui.menuOptions.actions())
        self.addActions(self.ui.menuWindows.actions())
        self.addActions(self.ui.menuHelp.actions())
        key_bindings = Settings().key_bindings
        for action in self.actions():
            try:
                key_sequence = key_bindings[action.objectName()]
            except KeyError:
                pass
            else:
                action.setShortcut(key_sequence)

    def save(self):
        raise NotImplementedError()

    def save_as(self):
        raise NotImplementedError()

    def restore_state(self):
        raise NotImplementedError()

    def save_state(self):
        raise NotImplementedError()

    def closeEvent(self, ev):
        if ev.isAccepted():
            super().closeEvent(ev)
            self.closed.emit(self)

    def _remember_height(self):
        self._height = self.height()

    def zoom_height(self):
        if self._height != self.height():
            print("zomm height", self.height())
            desktop = QtWidgets.QApplication.instance().desktop()
            self.resize(self.width(), desktop.availableGeometry().height())
            QtCore.QTimer.singleShot(100, self._remember_height)
        self.move(self.pos().x(), 0)

    def update_windows_menu(self, open_windows):
        self.ui.menuWindows.clear()
        self.ui.menuWindows.addAction(self.ui.actionZoom_height)
        self.ui.menuWindows.addSeparator()
        self.ui.menuWindows.addMenu(self.ui.menuTools)
        self.ui.menuWindows.addSeparator()
        for win in open_windows:
            action = QtWidgets.QAction(self)
            if win == self:
                action.setDisabled(True)
            action.setText(win.windowTitle())
            action.setData(win)
            action.triggered.connect(self._show_window_from_action)
            self.ui.menuWindows.addAction(action)

    def update_recents_menu(self):
        self.menu_recents.update_actions()

    def _show_window_from_action(self):
        window = self.sender().data()
        QtWidgets.QApplication.instance().setActiveWindow(window)

    def _on_new_file_triggered(self):
        self.save_state()
        self.app.create_script_window()

    def _on_open_file_triggered(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open script', filter='Python files (*.py)')
        if path:
            self.app.create_script_window(path)

    def _show_prev_window(self):
        i = self.app.windows.index(self)
        if i - 1 >= 0:
            window = self.app.windows[i - 1]
            window.show()
            window.activateWindow()
            window.raise_()

    def _show_next_window(self):
        i = self.app.windows.index(self)
        if i + 1 < len(self.app.windows):
            window = self.app.windows[i + 1]
            window.show()
            window.activateWindow()
            window.raise_()

    def _show_python_docs(self):
        QtGui.QDesktopServices.openUrl(
            QtCore.QUrl('https://docs.python.org/3/'))

    def _quit(self):
        # not sure why but if we don't do that using a timer we get a segfault
        QtCore.QTimer.singleShot(1, self.app.qapp.closeAllWindows)

    def _close(self):
        # not sure why but if we don't do that using a timer we get a segfault
        QtCore.QTimer.singleShot(1, self.close)
