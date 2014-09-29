"""
Contains the application class.

"""
import logging
import os
import sys
from pyqode.python.widgets import PyCodeEdit
from versiontools import Version
from PyQt4 import QtGui
from pyqode.core.widgets import RecentFilesManager
from qidle import icons, __version__, logger
from qidle.dialogs.ask_open import DlgAskOpenScript
from qidle.preferences import Preferences
from qidle.system import embed_package_into_zip, get_library_zip_path
from qidle.windows import ScripWindow


def _logger():
    return logging.getLogger(__name__)


class Application:
    """
    Defines the QIdle applications. This is where we manage the collection of
    open windows.

    """
    @property
    def version_str(self):
        return str(Version(*__version__))

    def __init__(self):
        logger.setup()
        _logger().info('QIdle v%s', self.version_str)
        self.windows = []
        self.qapp = QtGui.QApplication(sys.argv)
        icons.init()
        self._init_libraries()
        self.recent_files_manager = RecentFilesManager('QIdle', 'QIdle')
        self._current = None
        self.qapp.focusChanged.connect(self.on_focus_changed)

    def on_focus_changed(self, prev, new):
        if new and isinstance(new, PyCodeEdit):
            parent = new.parent()
            while (not isinstance(parent, QtGui.QMainWindow) and
                    parent is not None):
                parent = parent.parent()
            if self._current != parent:
                self._current = parent
                _logger().info('current window changed: %s', parent.path)

    def _init_libraries(self):
        if (not '.dev' in self.version_str and
                os.path.exists(get_library_zip_path())):
            _logger().info('libraries.zip is up to date')
            return
        else:
            # dependencies frozen into a zip file on startup:
            import jedi
            import pep8
            import pyqode
            import pyqode.core
            import pyqode.python
            import pyqode.qt
            import qidle
            import frosted
            import pies
            import versiontools
            _logger().info('updating libraries.zip')
            embed_package_into_zip(
                [jedi, pep8, pyqode, pyqode.core, pyqode.python, pyqode.qt, qidle,
                 versiontools, frosted, pies])

    def update_windows_menu(self):
        for w in self.windows:
            w.update_windows_menu(self.windows)

    def activate_window(self, window):
        window.show()
        self.qapp.setActiveWindow(window)
        window.raise_()
        self._current = window
        _logger().debug('showing window: %s' % window.path)

    def create_script_window(self, path=None):
        """
        Creates a new script window.

        :param path: Optional file to open in the script window. None to
                     create a new file in memory.

        :return: ScriptWindow
        """
        # first look if the requested path is not already open
        if path:
            for w in self.windows:
                if w.path == path:
                    self.activate_window(w)
                    return w
        active_window = self.qapp.activeWindow()
        if active_window:
            active_window.save_state()

        window = ScripWindow(self)
        window.closed.connect(self._on_window_closed)
        self.windows.append(window)
        if path and os.path.exists(path):
            window.open(path)
        else:
            window.new()
        self.update_windows_menu()
        self.activate_window(window)
        window._configure_shortcuts()
        return window

    def _on_window_closed(self, window):
        _logger().info('window closed: %s' % window.path)
        self.windows.remove(window)
        self.update_windows_menu()

    def remember_path(self, path):
        """
        Adds the path to the list of recent paths.
        """
        _logger().debug('remember path: %s', path)
        self.recent_files_manager.open_file(path)
        for w in self.windows:
            w.update_recents_menu()

    def _open_in_new(self, path, script):
        if script:
            self.create_script_window(path)
        else:
            # todo create project window
            pass

    def _open_in_current(self, path, script):
        win = self._current
        assert win is not None
        # ensure types are corresponding (if we want to open a project from
        # a script window, a new proj window must be created)
        if ((script and isinstance(win, ScripWindow) or
                (not script and not isinstance(self, ScripWindow)))):
            win.open(path)
        else:
            self._open_in_new(path, script)

    def open_recent(self, path):
        _logger().info('open recent file: %s', path)
        script = os.path.isfile(path)
        action = Preferences().general.open_scr_action
        if action == Preferences().general.OpenActions.NEW:
            self._open_in_new(path, script)
        elif action == Preferences().general.OpenActions.CURRENT:
            self._open_in_current(path, script)
        else:
            if script:
                # ask
                val = DlgAskOpenScript.ask(self.qapp.activeWindow())
                if val == Preferences().general.OpenActions.NEW:
                    self._open_in_new(path, script)
                elif val == Preferences().general.OpenActions.CURRENT:
                    self._open_in_current(path, script)
            else:
                # todo ask for projects
                pass

    def apply_preferences(self):
        for w in self.windows:
            w.apply_preferences()

    def init(self):
        if Preferences().general.reopen_last_window:
            try:
                path = self.recent_files_manager.last_file()
            except IndexError:
                self.create_script_window()
            else:
                _logger().info('reopen last window: %s' % path)
                # todo create the correct window type based on the file path
                self.create_script_window(path)
        else:
            # create untitled script window
            self.create_script_window()

    def run(self):
        """
        Runs the application.
        """
        self.init()
        self.qapp.exec_()
