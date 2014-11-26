"""
This module contains a dock manager widget and all the classes needed to make
it work.

"""
from pyqode.qt import QtCore, QtGui, QtWidgets
from pyqode.core.api.utils import drift_color


class VButton(QtWidgets.QPushButton):
    def __init__(self, text, parent):
        super(VButton, self).__init__(parent)
        self.setText(text)
        self.setFlat(True)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.setCheckable(True)

    def _on_clicked(self):
        self.clearFocus()

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        painter.rotate(90)
        painter.translate(0, -self.width())
        painter.drawControl(QtWidgets.QStyle.CE_PushButton, self.getSyleOptions())

    def sizeHint(self):
        size = super(VButton, self).sizeHint()
        size.transpose()
        return size

    def getSyleOptions(self):
        options = QtWidgets.QStyleOptionButton()
        options.initFrom(self)
        size = options.rect.size()
        size.transpose()
        options.rect.setSize(size)
        if self.isFlat():
            options.features |= QtWidgets.QStyleOptionButton.Flat
        if self.menu():
            options.features |= QtWidgets.QStyleOptionButton.HasMenu
        if self.autoDefault() or self.isDefault():
            options.features |= QtWidgets.QStyleOptionButton.AutoDefaultButton
        if self.isDefault():
            options.features |= QtWidgets.QStyleOptionButton.DefaultButton
        if self.isDown() or (self.menu() and self.menu().isVisible()):
            options.state |= QtWidgets.QStyle.State_Sunken
        if self.isChecked():
            options.state |= QtWidgets.QStyle.State_On
        if not self.isFlat() and not self.isDown():
            options.state |= QtWidgets.QStyle.State_Raised
        options.text = self.text()
        options.icon = self.icon()
        options.iconSize = self.iconSize()
        return options


class HButton(QtWidgets.QPushButton):
    def __init__(self, text, parent):
        super(HButton, self).__init__(parent)
        self.setText(text)
        self.setFlat(True)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.setCheckable(True)


class DockManager(QtWidgets.QToolBar):
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
        super(DockManager, self).__init__(parent)
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
