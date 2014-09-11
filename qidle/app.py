"""
Contains the application class.

"""
import os
import sys
from pyqode import qt
from PyQt4 import QtGui, QtCore
from pyqode.core.widgets import RecentFilesManager
from qidle import icons
from qidle.windows import ScripWindow


import logging
logging.basicConfig(level=logging.INFO)


class Application:
    """
    Defines the QIdle applications. This is where we manage the collection of
    open windows.

    """
    def __init__(self):
        self.windows = []
        self.qapp = QtGui.QApplication(sys.argv)
        icons.init()
        self.recent_files_manager = RecentFilesManager('QIdle', 'QIdle')

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
                    self.qapp.setActiveWindow(w)
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

    def run(self):
        """
        Runs the application.
        """
        try:
            path = self.recent_files_manager.last_file()
        except IndexError:
            self.create_script_window()
        else:
            self.create_script_window(path)
        self.qapp.exec_()
