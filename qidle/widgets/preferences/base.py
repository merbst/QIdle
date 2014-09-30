"""
Contains the base class for preferences pages.
"""
from PyQt4 import QtGui


HEADER_STYLE = '''border-radius: 3px;
background-color: %(bg)s;
color: %(fore)s;
padding: 10px;
'''


class Page(QtGui.QWidget):
    def __init__(self, ui, parent=None):
        super(Page, self).__init__(parent)
        self.ui = ui
        self.ui.setupUi(self)
        p = self.palette()
        assert isinstance(p, QtGui.QPalette)
        qss = HEADER_STYLE % {
            'bg': p.color(p.Highlight).name(),
            'fore': p.color(p.HighlightedText).name()
        }
        self.ui.header.setStyleSheet(qss)
        self.reset()

    def reset(self):
        raise NotImplementedError()

    def restore_defaults(self):
        raise NotImplementedError()

    def apply(self):
        raise NotImplementedError()
