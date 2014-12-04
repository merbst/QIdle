"""
This module contains a set of small utility widgets, generally used as
promoted widget in Qt Designer.

"""
import os
from pyqode.qt import QtCore, QtGui, QtWidgets


class FilePicker(QtWidgets.QWidget):
    """
    File picker widget combines a line edit and a tool button. It lets you
    choose a file by clicking on the tool button or by typing the path in the
    line edit (typing is assisted by a file system completer).

    You can get/set the path by using the ``path`` property.

    The widget is able to pick files or directories. The default is to pick
    files. To pick directories, just set the ``pick_dirs`` property to True.
    """
    @property
    def path(self):
        return self.line_edit.text()

    @path.setter
    def path(self, value):
        self.line_edit.setText(value)
        self._on_path_changed(value)

    @property
    def default_directory(self):
        return self._default_dir

    @default_directory.setter
    def default_directory(self, value):
        self._default_dir = value

    @property
    def pick_dirs(self):
        return self._pick_dirs

    @pick_dirs.setter
    def pick_dirs(self, value):
        self._pick_dirs = value
        if value:
            self._mdl.setFilter(QtCore.QDir.Dirs | QtCore.QDir.NoDotAndDotDot)
        else:
            self._mdl.setFilter(QtCore.QDir.AllEntries |
                                QtCore.QDir.NoDotAndDotDot)

    def __init__(self, parent=None):
        super(FilePicker, self).__init__(parent)
        self._default_dir = os.path.expanduser('~')
        self._pick_dirs = True
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.line_edit = QtWidgets.QLineEdit()
        self.path = os.path.expanduser('~')
        layout.addWidget(self.line_edit)
        self.tool_button = QtWidgets.QToolButton()
        self.tool_button.setText('...')
        layout.addWidget(self.tool_button)
        self.setLayout(layout)
        completer = QtWidgets.QCompleter(self)
        self._mdl = QtWidgets.QDirModel(completer)
        completer.setModel(self._mdl)
        self.line_edit.setCompleter(completer)
        self.pick_dirs = False
        self.tool_button.clicked.connect(self._pick)
        self.line_edit.textChanged.connect(self._on_path_changed)

    def _pick(self):
        directory = self.line_edit.text()
        if not directory:
            directory = self.default_directory
        if self.pick_dirs:
            path = QtWidgets.QFileDialog.getExistingDirectory(
                self, 'Choose a directory', directory)
        else:
            path, filter = QtWidgets.QFileDialog.getOpenFileName(
                self, 'Choose a file', directory)
        if path:
            self.line_edit.setText(path)

    def _on_path_changed(self, path):
        palette = self.palette()
        if not os.path.exists(path):
            palette.setColor(palette.Text, QtCore.Qt.red)
        else:
            palette.setColor(palette.Text, QtCore.Qt.black)
        self.line_edit.setPalette(palette)
