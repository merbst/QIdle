"""
Contains the application class.

"""
import os
import sys
from pyqode import qt
from PyQt4 import QtGui, QtCore
from pyqode.core.widgets import RecentFilesManager
from qidle import icons, version
from qidle.dialogs.ask_open import DlgAskOpenScript
from qidle.preferences import Preferences
from qidle.system import embed_package_into_zip, get_library_zip_path
from qidle.windows import ScripWindow

import logging
logging.basicConfig(level=logging.DEBUG)


# dependencies frozen into a zip file on startup:
import jedi, pep8, pyqode, pyqode.core, pyqode.python, pyqode.qt, qidle,\
       frosted, pies, versiontools


class Application:
    """
    Defines the QIdle applications. This is where we manage the collection of
    open windows.

    """
    def __init__(self):
        self.windows = []
        self.qapp = QtGui.QApplication(sys.argv)
        icons.init()
        self._init_libraries()
        self.recent_files_manager = RecentFilesManager('QIdle', 'QIdle')

    def _init_libraries(self):
        if not '.dev' in str(version) and os.path.exists(get_library_zip_path()):
            return
        else:
            embed_package_into_zip(
                [jedi, pep8, pyqode, pyqode.core, pyqode.python, pyqode.qt, qidle,
                 versiontools, frosted, pies])

    def update_windows_menu(self):
        for w in self.windows:
            w.update_windows_menu(self.windows)

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
                    w.show()
                    self.qapp.setActiveWindow(w)
                    w.raise_()
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
        window.show()
        self.qapp.setActiveWindow(window)
        window.raise_()
        window._configure_shortcuts()
        return window

    def _on_window_closed(self, window):
        self.windows.remove(window)
        self.update_windows_menu()

    def remember_path(self, path):
        """
        Adds the path to the list of recent paths.
        """
        self.recent_files_manager.open_file(path)
        for w in self.windows:
            w.update_recents_menu()

    def _open_in_new(self, path, script):
        if script:
            self.create_script_window(path)

    def _open_in_current(self, path, script):
        win = self.qapp.activeWindow()
        if win is None:
            win = self.windows[0]
        if ((script and isinstance(win, ScripWindow) or
                 (not script and not isinstance(self, ScripWindow)))):
            win.open(path)
        else:
            self._open_in_new(path, script)

    def open_recent(self, path):
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

    def run(self):
        """
        Runs the application.
        """
        if Preferences().general.reopen_last_window:
            try:
                path = self.recent_files_manager.last_file()
            except IndexError:
                self.create_script_window()
            else:
                # todo create the correct window type based on the file path
                self.create_script_window(path)
        else:
            # create untitled script window
            self.create_script_window()
        self.qapp.exec_()
