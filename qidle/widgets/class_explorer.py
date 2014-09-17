"""
This module contains the class explorer implementation.
"""
from PyQt4 import QtCore, QtGui
from pyqode.core.api import TextHelper
from pyqode.python.modes import DocumentAnalyserMode


class ClassExplorer(QtGui.QTreeWidget):
    """
    Displays the structure of an editor (classes/functions/methods)

    To use this widget, just set the current editor using ``set_editor``.
    """
    def __init__(self, parent=None):
        super(ClassExplorer, self).__init__(parent)
        self._analyser = None
        self._expanded_items = []
        self.itemDoubleClicked.connect(self.on_item_double_clicked)
        self.itemExpanded.connect(self._expanded_items.append)
        self.itemCollapsed.connect(self._expanded_items.remove)

    def set_editor(self, editor):
        """
        Sets the current editor. The widget display the structure of that
        editor.

        :param editor: PyCodeEdit
        """
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
        """
        Update the tree items
        """
        analyser = self._analyser
        assert isinstance(analyser, DocumentAnalyserMode)
        to_expand = [item.text(0) for item in self._expanded_items]
        self._expanded_items[:] = []
        self.clear()
        self.addTopLevelItems(analyser.to_tree_widget_items())
        # restore expanded items
        for text in to_expand:
            items = self.findItems(
                text, QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive)
            for item in items:
                self.expandItem(item)

    def on_item_double_clicked(self, item):
        """
        Go to the item position in the editor.
        """
        d = item.data(0, QtCore.Qt.UserRole)
        TextHelper(self._editor).goto_line(d.block.blockNumber(), d.column)
        self._editor.setFocus(True)
