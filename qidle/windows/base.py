"""
Base implementation for windows.
"""
import logging
import os
import sys
import weakref
from pyqode.core.api import ColorScheme
from pyqode.core.modes import CheckerMode
from pyqode.qt import QtCore, QtGui, QtWidgets
from pyqode.core.widgets import MenuRecentFiles
from qidle import icons, commons
from qidle.dialogs.ask_open import DlgAskOpenScript
from qidle.icons import IconProvider
from qidle.preferences import Preferences
from qidle.dialogs import DlgPreferences
from qidle.system import get_library_zip_path
from qidle.widgets.dock_manager import DockManager


def _logger(obj):
    return logging.getLogger(__name__ + '[%s]' % obj.__class__.__name__)


class WindowBase(QtWidgets.QMainWindow):
    closed = QtCore.pyqtSignal(QtWidgets.QMainWindow)

    @property
    def app(self):
        """
        :rtype: qidle.app.Application
        """
        return self._app()

    def __init__(self, ui, app):
        super(WindowBase, self).__init__()
        self._quitting = False
        self._app = weakref.ref(app)
        self._height = None
        # path of the script, 'Untitled' if new file not saved to disk.
        self.path = None
        self.ui = ui
        self.ui.setupUi(self)
        # we need to set proper menu roles for OS X
        self.ui.actionAbout_QIdle.setMenuRole(QtWidgets.QAction.AboutRole)
        self.ui.actionQuit.setMenuRole(QtWidgets.QAction.QuitRole)
        if sys.platform == 'win32':
            self.ui.actionConfigure_IDLE.setText('Preferences')
        self.ui.actionConfigure_IDLE.setMenuRole(
            QtWidgets.QAction.PreferencesRole)
        self.ui.actionConfigureRun.setMenuRole(QtWidgets.QAction.NoRole)
        self._setup_mnu_file(app, ui)
        self._setup_windows_menu(ui)
        self._setup_help_menu()
        ui.actionConfigure_IDLE.triggered.connect(self.edit_preferences)
        self._setup_icons()
        self.dock_manager_right = DockManager(self)
        self.dock_manager_right.setObjectName('dockManagerRight')
        self.dock_manager_right.setWindowTitle('Dock manager right')
        self.addToolBar(QtCore.Qt.RightToolBarArea, self.dock_manager_right)
        self.dock_manager_bottom = DockManager(self)
        self.dock_manager_bottom.setObjectName('dockManagerBottom')
        self.dock_manager_bottom.setWindowTitle('Dock manager bottom')
        self.addToolBar(QtCore.Qt.BottomToolBarArea, self.dock_manager_bottom)

    def apply_preferences(self):
        raise NotImplementedError()

    def save(self):
        raise NotImplementedError()

    def save_as(self):
        raise NotImplementedError()

    def restore_state(self):
        raise NotImplementedError()

    def save_state(self):
        raise NotImplementedError()

    def update_recents_menu(self):
        self.menu_recents.update_actions()

    def current_interpreter(self):
        raise NotImplementedError()

    def edit_preferences(self):
        DlgPreferences.edit_preferences(
            self, callback=self.app.apply_preferences)

    def zoom_height(self):
        _logger(self).debug('zoom height')
        desktop = QtWidgets.QApplication.instance().desktop()
        if sys.platform == 'win32':
            difference = (self.frameGeometry().height() -
                          self.geometry().height())
        else:
            difference = 0
        self.resize(self.width(), desktop.availableGeometry(self).height() -
                    difference)
        self.move(self.pos().x(), 0)

    def update_windows_menu(self, open_windows):
        _logger(self).debug('update windows menu: %r' % open_windows)
        self._open_windows = open_windows
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

    def _emit_closed(self):
        self.closed.emit(self)

    def _setup_icons(self):
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
        self.lbl_cursor_pos = QtWidgets.QLabel()
        self.lbl_cursor_pos.setText('na')
        self.statusBar().addPermanentWidget(self.lbl_cursor_pos)
        self.lbl_encoding = QtWidgets.QLabel()
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
        self.menu_recents.open_requested.connect(
            self.app.open_recent)
        self.ui.menuFile.addMenu(self.menu_recents)
        self.ui.menuFile.addSeparator()
        self.ui.menuFile.addAction(self.ui.actionSave)
        self.ui.menuFile.addAction(self.ui.actionSave_as)
        self.ui.menuFile.addSeparator()
        self.ui.menuFile.addAction(self.ui.actionClose)
        self.ui.menuFile.addAction(self.ui.actionQuit)
        ui.actionNew_file.triggered.connect(self._on_new_file_triggered)
        ui.actionOpen_file.triggered.connect(self._on_open_file_triggered)
        ui.actionNew_project.triggered.connect(self._on_new_project_triggered)
        ui.actionOpen_directory.triggered.connect(
            self._on_open_project_triggered)
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

    def configure_shortcuts(self):
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

    def _show_window_from_action(self):
        window = self.sender().data()
        self.app.activate_window(window)

    def _on_new_file_triggered(self):
        _logger(self).debug('create new file')
        self.save_state()
        self.app.create_script_window()

    def _on_new_project_triggered(self):
        pass

    def _open_in_current_window(self, path, script):
        from qidle.windows.script import ScriptWindow
        if ((script and isinstance(self, ScriptWindow) or
                (not script and not isinstance(self, ScriptWindow)))):
            self.open(path)
        else:
            self._open_in_new_window(path, script)

    def _open_in_new_window(self, path, script):
        if script:
            self.app.create_script_window(path)
        else:
            self.app.create_project_window(path)

    def _on_open_file_triggered(self):
        path, filter = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open script', self.path,
            filter='Python files (*.py *.pyw)')
        if path:
            script = os.path.isfile(path)
            action = Preferences().general.open_scr_action
            if action == Preferences().general.OpenActions.NEW:
                self._open_in_new_window(path, script)
            elif action == Preferences().general.OpenActions.CURRENT:
                self._open_in_current_window(path, script)
            else:
                # ask
                val = DlgAskOpenScript.ask(self)
                if val == Preferences().general.OpenActions.NEW:
                    self._open_in_new_window(path, script)
                elif val == Preferences().general.OpenActions.CURRENT:
                    self._open_in_current_window(path, script)

    def _on_open_project_triggered(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Open project', os.path.expanduser('~'))
        if path:
            script = os.path.isfile(path)
            action = Preferences().general.open_project_action
            if action == Preferences().general.OpenActions.NEW:
                self._open_in_new_window(path, script)
            elif action == Preferences().general.OpenActions.CURRENT:
                self._open_in_current_window(path, script)
            else:
                # ask
                val = DlgAskOpenScript.ask(self)
                if val == Preferences().general.OpenActions.NEW:
                    self._open_in_new_window(path, script)
                elif val == Preferences().general.OpenActions.CURRENT:
                    self._open_in_current_window(path, script)

    def _show_prev_window(self):
        i = self.app.windows.index(self)
        i -= 1
        if i < 0:
            i = len(self.app.windows) - 1
        window = self.app.windows[i]
        self.app.activate_window(window)

    def _show_next_window(self):
        i = self.app.windows.index(self)
        i += 1
        if i >= len(self.app.windows):
            i = 0
        window = self.app.windows[i]
        self.app.activate_window(window)

    def _restart_backend(self, editor):
        """
        Restart the backend process of `editor`. The goal is to
        :param editor: pyqode.core.api.CodeEdit or subclass
        """
        editor.backend.start(
            editor.backend.server_script, self.current_interpreter(),
            [] if sys.executable == self.current_interpreter() else
            ['-s'] + [get_library_zip_path()])
        # update checker modes for the new interpreter syntax.
        for mode in editor.modes:
            if isinstance(mode, CheckerMode):
                mode.request_analysis()

    def _show_python_docs(self):
        _logger(self).info('opening python docs in the default browser')
        QtGui.QDesktopServices.openUrl(
            QtCore.QUrl('https://docs.python.org/3/'))

    def quit_confirmation(self):
        if Preferences().general.confirm_application_exit and \
                not self._quitting:
            button = QtWidgets.QMessageBox.question(
                self, "Confirm exit",
                "Are you sure you want to exit QIdle?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            res = button == QtWidgets.QMessageBox.Yes
            return res
        return True

    def _quit(self):
        if self.quit_confirmation():
            self._quitting = True
            self.app.qapp.closeAllWindows()
            self._quitting = False

    def _close(self):
        # not sure why but if we don't do that using a timer we get a segfault
        self.close()

    def _apply_editor_preferences(self, editor, show_panels):
        _logger(self).info('applying preferences on editor: %s' %
                       editor.file.path)
        prefs = Preferences()
        # appearance
        editor.font_name = prefs.editor_appearance.font
        editor.font_size = prefs.editor_appearance.font_size
        editor.show_whitespaces = prefs.editor_appearance.show_whitespaces
        scheme = ColorScheme(prefs.editor_appearance.color_scheme)
        editor.syntax_highlighter.color_scheme = scheme
        self.ui.textEditPgmOutput.apply_color_scheme(scheme)
        # editor settings
        editor.panels.get('FoldingPanel').highlight_caret_scope = \
            prefs.editor.highlight_caret_scope
        editor.use_spaces_instead_of_tabs = \
            prefs.editor.use_spaces_instead_of_tabs
        editor.modes.get('RightMarginMode').position = \
            prefs.editor.margin_pos
        editor.tab_length = prefs.editor.tab_len
        editor.file.replace_tabs_by_spaces = \
            prefs.editor.convert_tabs_to_spaces
        editor.file.clean_trailing_whitespaces = \
            prefs.editor.clean_trailing
        editor.file.fold_imports = prefs.editor.fold_imports
        editor.file.fold_docstrings = prefs.editor.fold_docstrings
        editor.file.restore_cursor = prefs.editor.restore_cursor
        editor.file.safe_save = prefs.editor.safe_save
        mode = editor.modes.get('CodeCompletionMode')
        mode.trigger_length = prefs.editor.cc_trigger_len
        mode.show_tooltips = prefs.editor.cc_show_tooltips
        mode.case_sensitive = prefs.editor.cc_case_sensitive
        editor.setCenterOnScroll(prefs.editor.center_on_scroll)
        # modes
        for m in editor.modes:
            if m.name in prefs.editor.modes:
                m.enabled = prefs.editor.modes[m.name]
            else:
                m.enabled = True

        # disable unwanted panels
        for name, state in prefs.editor.panels.items():
            try:
                panel = editor.panels.get(name)
            except KeyError:
                _logger().exception('failed to retrieve mode by name: %r' % name)
            else:
                if name not in commons.DYNAMIC_PANELS:
                    if not show_panels and state is True:
                        continue
                    panel.setEnabled(state)
                    panel.setVisible(state)


    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.path)
