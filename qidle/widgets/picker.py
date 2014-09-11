"""
This module contains a set of small utility widgets, generally used as
promoted widget in Qt Designer.

"""
import os
from PyQt4 import QtCore, QtGui


class FilePicker(QtGui.QWidget):
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
        self._pick_dirs = True
        layout = QtGui.QHBoxLayout()
        layout.setMargin(0)
        self.line_edit = QtGui.QLineEdit()
        self.path = os.path.expanduser('~')
        layout.addWidget(self.line_edit)
        self.tool_button = QtGui.QToolButton()
        self.tool_button.setText('...')
        layout.addWidget(self.tool_button)
        self.setLayout(layout)
        completer = QtGui.QCompleter(self)
        self._mdl = QtGui.QDirModel(completer)
        completer.setModel(self._mdl)
        self.line_edit.setCompleter(completer)
        self.pick_dirs = False
        self.tool_button.clicked.connect(self._pick)
        self.line_edit.textChanged.connect(self._on_path_changed)

    def _pick(self):
        if self.pick_dirs:
            ret = QtGui.QFileDialog.getExistingDirectory(
                self, 'Choose a directory', self.line_edit.text())
        else:
            ret = QtGui.QFileDialog.getOpenFileName(
                self, 'Choose a file', self.line_edit.text())
        if ret:
            self.line_edit.setText(ret)

    def _on_path_changed(self, path):
        palette = self.palette()
        if not os.path.exists(path):
            palette.setColor(palette.Text, QtCore.Qt.red)
        else:
            palette.setColor(palette.Text, QtCore.Qt.black)
        self.line_edit.setPalette(palette)
