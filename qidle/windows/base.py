"""
Base implementation for windows.
"""
import sys
import weakref
from PyQt4 import QtCore, QtGui
from pyqode.core.widgets import MenuRecentFiles
from qidle import icons
from qidle.icons import IconProvider
from qidle.preferences import Preferences
from qidle.dialogs import DlgPreferences


class WindowBase(QtGui.QMainWindow):
    closed = QtCore.Signal(QtGui.QMainWindow)

    @property
    def app(self):
        """
        :rtype: qidle.app.Application
        """
        return self._app()

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
        self._setup_status_bar()
        ui.actionConfigure_IDLE.triggered.connect(self.edit_preferences)
        self.setup_icons()

    def setup_icons(self):
        self.ui.actionNew_file.setIcon(icons.new_file)
        self.ui.actionNew_project.setIcon(icons.new_folder)
        self.ui.actionOpen_file.setIcon(icons.open_file)
        self.ui.actionOpen_directory.setIcon(icons.open_folder)
        self.ui.actionSave.setIcon(icons.save)
        self.ui.actionSave_as.setIcon(icons.save_as)
        self.ui.actionPython_docs.setIcon(icons.python_interpreter)
        self.ui.actionAbout_QIdle.setIcon(icons.help_about)
        self.ui.actionHelp_content.setIcon(icons.help_contents)
        self.ui.actionConfigure_IDLE.setIcon(icons.preferences)
        self.ui.actionConfigureRun.setIcon(icons.configure)
        self.ui.actionRun.setIcon(icons.run)
        self.ui.actionClose.setIcon(icons.window_close)
        self.ui.actionQuit.setIcon(icons.application_exit)

    def _setup_status_bar(self):
        self.lbl_cursor_pos = QtGui.QLabel()
        self.lbl_cursor_pos.setText('na')
        self.statusBar().addPermanentWidget(self.lbl_cursor_pos)
        self.lbl_encoding = QtGui.QLabel()
        self.lbl_encoding.setText('na')
        self.statusBar().addPermanentWidget(self.lbl_encoding)

    def _setup_mnu_file(self, app, ui):
        self.ui.menuFile.clear()
        self.ui.menuFile.addAction(self.ui.actionNew_file)
        self.ui.menuFile.addAction(self.ui.actionOpen_file)
        self.ui.menuFile.addSeparator()
        self.ui.menuFile.addAction(self.ui.actionNew_project)
        self.ui.menuFile.addAction(self.ui.actionOpen_directory)
        self.ui.menuFile.addSeparator()
        self.menu_recents = MenuRecentFiles(
            self, app.recent_files_manager, title='Recents',
            icon_provider=IconProvider())
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
        action_prev_window = QtGui.QAction(self)
        action_prev_window.setShortcut('Alt+Up')
        action_prev_window.triggered.connect(self._show_prev_window)
        self.addAction(action_prev_window)
        action_next_window = QtGui.QAction(self)
        action_next_window.setShortcut('Alt+Down')
        action_next_window.triggered.connect(self._show_next_window)
        self.addAction(action_next_window)

    def _setup_help_menu(self):
        self.ui.actionPython_docs.triggered.connect(self._show_python_docs)

    def _configure_shortcuts(self):
        self.addActions(self.ui.menuFile.actions())
        # menu edit already added
        self.addActions(self.ui.menuRun.actions())
        self.addActions(self.ui.menuOptions.actions())
        self.addActions(self.ui.menuWindows.actions())
        self.addActions(self.ui.menuHelp.actions())
        key_bindings = Preferences().key_bindings.dict()
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

    def zoom_height(self):
        desktop = QtGui.QApplication.instance().desktop()
        if sys.platform == 'win32':
            difference = (self.frameGeometry().height() -
                          self.geometry().height())
        else:
            difference = 0
        self.resize(self.width(), desktop.availableGeometry(self).height() -
                    difference)
        self.move(self.pos().x(), 0)

    def update_windows_menu(self, open_windows):
        self.ui.menuWindows.clear()
        self.ui.menuWindows.addAction(self.ui.actionZoom_height)
        self.ui.menuWindows.addSeparator()
        self.ui.menuWindows.addMenu(self.ui.menuTools)
        self.ui.menuWindows.addSeparator()
        for win in open_windows:
            action = QtGui.QAction(self)
            if win == self:
                action.setDisabled(True)
            action.setText(win.windowTitle())
            action.setData(win)
            action.triggered.connect(self._show_window_from_action)
            self.ui.menuWindows.addAction(action)

    def update_recents_menu(self):
        self.menu_recents.update_actions()

    def edit_preferences(self):
        DlgPreferences.edit_preferences(self)

    def _show_window_from_action(self):
        window = self.sender().data()
        QtGui.QApplication.instance().setActiveWindow(window)

    def _on_new_file_triggered(self):
        self.save_state()
        self.app.create_script_window()

    def _on_open_file_triggered(self):
        path = QtGui.QFileDialog.getOpenFileName(
            self, 'Open script', self.path, filter='Python files (*.py)')
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
