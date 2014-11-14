"""
This module contains a dock manager widget and all the classes needed to make
it work.

"""
from PyQt4 import QtCore, QtGui
from pyqode.core.api.utils import drift_color


class VButton(QtGui.QPushButton):
    def __init__(self, text, parent):
        super(VButton, self).__init__(parent)
        self.setText(text)
        self.setFlat(True)
        self.setSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.setCheckable(True)

    def _on_clicked(self):
        self.clearFocus()

    def paintEvent(self, event):
        painter = QtGui.QStylePainter(self)
        painter.rotate(90)
        painter.translate(0, -self.width())
        painter.drawControl(QtGui.QStyle.CE_PushButton, self.getSyleOptions())

    def sizeHint(self):
        size = super(VButton, self).sizeHint()
        size.transpose()
        return size

    def getSyleOptions(self):
        options = QtGui.QStyleOptionButton()
        options.initFrom(self)
        size = options.rect.size()
        size.transpose()
        options.rect.setSize(size)
        if self.isFlat():
            options.features |= QtGui.QStyleOptionButton.Flat
        if self.menu():
            options.features |= QtGui.QStyleOptionButton.HasMenu
        if self.autoDefault() or self.isDefault():
            options.features |= QtGui.QStyleOptionButton.AutoDefaultButton
        if self.isDefault():
            options.features |= QtGui.QStyleOptionButton.DefaultButton
        if self.isDown() or (self.menu() and self.menu().isVisible()):
            options.state |= QtGui.QStyle.State_Sunken
        if self.isChecked():
            options.state |= QtGui.QStyle.State_On
        if not self.isFlat() and not self.isDown():
            options.state |= QtGui.QStyle.State_Raised
        options.text = self.text()
        options.icon = self.icon()
        options.iconSize = self.iconSize()
        return options


class HButton(QtGui.QPushButton):
    def __init__(self, text, parent):
        super(HButton, self).__init__(parent)
        self.setText(text)
        self.setFlat(True)
        self.setSizePolicy(
            QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.setCheckable(True)


class DockManager(QtGui.QToolBar):
    qss = """
    QToolBar{
        padding: 2px;
        spacing: 6px;
    }
    QPushButton {
        background-color: transparent;
        border: 1px transparent;
        padding: 5px;
        border-top: 3px transparent black;
        border-radius: 3px;
    }

    QPushButton:on {
        background-color: %s;
    }

    QPushButton:hover {
        background-color: %s;
    }
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet(self.qss)
        self.setMovable(False)
        self.setFloatable(False)
        self.color = drift_color(self.palette().window().color(), 120)
        self.color_hover = drift_color(self.palette().window().color(), 110)
        self.setStyleSheet(
            self.qss % (self.color.name(), self.color_hover.name()))

    def add_dock_widget(self, dock_widget):
        if self.orientation() == QtCore.Qt.Vertical:
            klass = VButton
        else:
            klass = HButton
        bt = klass(dock_widget.windowTitle(), self)
        bt.setChecked(dock_widget.isVisible())
        dock_widget.visibilityChanged.connect(bt.setChecked)
        bt.toggled.connect(dock_widget.setVisible)
        bt.setIcon(dock_widget.windowIcon())
        self.addWidget(bt)
