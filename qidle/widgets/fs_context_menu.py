"""
Contains the file system context menu used in the project window.
"""
import os
from PyQt4 import QtGui
from pyqode.core.widgets import FileSystemContextMenu
from qidle import icons


class PyFileSystemContextMenu(FileSystemContextMenu):
    def get_new_user_actions(self):
        # New module
        self.action_new_module = QtGui.QAction('&Module', self)
        self.action_new_module.setIcon(QtGui.QIcon(
            icons.python_mimetype))
        self.action_new_module.triggered.connect(
            self._on_new_module_triggered)
        # New package
        self.action_new_package = QtGui.QAction('&Package', self)
        self.action_new_package.setIcon(QtGui.QIcon(
            icons.folder))
        self.action_new_package.triggered.connect(
            self._on_new_package_triggered)
        # separator with the regular entries
        action = QtGui.QAction(self)
        action.setSeparator(True)
        return [self.action_new_module, self.action_new_package, action]

    def _on_new_module_triggered(self):
        src = self.tree_view.helper.get_current_path()
        if os.path.isfile(src):
            src = os.path.dirname(src)
        name, status = QtGui.QInputDialog.getText(
            self.tree_view, 'Create new python module', 'Module name:',
            QtGui.QLineEdit.Normal, 'my_module')
        if status:
            if not os.path.splitext(name)[1]:
                name += '.py'
            path = os.path.join(src, name)
            with open(path, 'w'):
                pass
            self.tree_view.file_created.emit(path)

    def _on_new_package_triggered(self):
        src = self.tree_view.helper.get_current_path()
        if os.path.isfile(src):
            src = os.path.dirname(src)
        name, status = QtGui.QInputDialog.getText(
            self.tree_view, 'Create new python package', 'Package name:',
            QtGui.QLineEdit.Normal, 'my_package')
        if status:
            path = os.path.join(src, name)
            os.makedirs(path)
            path = os.path.join(path, '__init__.py')
            with open(path, 'w'):
                pass
            self.tree_view.file_created.emit(path)
