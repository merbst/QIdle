"""
Contains the base class for preferences pages.
"""
from PyQt4 import QtGui


class Page(QtGui.QWidget):
    def __init__(self, ui, parent=None):
        super(Page, self).__init__(parent)
        self.ui = ui
        self.ui.setupUi(self)
        self.reset()

    def reset(self):
        raise NotImplementedError()

    def restore_defaults(self):
        raise NotImplementedError()

    def apply(self):
        raise NotImplementedError()
