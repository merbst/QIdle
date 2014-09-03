from PyQt4 import QtCore, QtGui
from pyqode.core.api import TextHelper
from pyqode.python.modes import DocumentAnalyserMode


class ClassExplorer(QtGui.QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._analyser = None

        self.itemDoubleClicked.connect(self.on_item_double_clicked)

    def set_editor(self, editor):
        self._editor = editor
        if self._analyser:
            self._analyser.document_changed.disconnect(self.on_changed)
        try:
            analyser = editor.modes.get(DocumentAnalyserMode)
        except KeyError:
            self._analyser = None
        else:
            assert isinstance(analyser, DocumentAnalyserMode)
            self._analyser = analyser
            analyser.document_changed.connect(self.on_changed)

    def on_changed(self):
        analyser = self._analyser
        assert isinstance(analyser, DocumentAnalyserMode)
        # todo: store expanded nodes
        self.clear()
        self.addTopLevelItems(analyser.to_tree_widget_items())
        # todo: expand previously expanded nodes

    def on_item_double_clicked(self, item):
        d = item.data(0, QtCore.Qt.UserRole)
        TextHelper(self._editor).goto_line(d.block.blockNumber(), d.column)
        self._editor.setFocus(True)