"""
This module contains the preferences dialog implementation.

"""
from PyQt4 import QtGui, QtCore
from qidle.forms.dlg_preferences_ui import Ui_Dialog
from qidle.widgets.preferences import (
    PageAppearance, PageGeneral, PageInterpreters
)


class DlgPreferences(QtGui.QDialog):
    def __init__(self, parent, apply_callback):
        super(DlgPreferences, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self._apply_callback = apply_callback

        # general
        page = PageGeneral(self.ui.pages)
        self.ui.pages.addWidget(page)
        general = self.ui.categories.findItems(
            'General', QtCore.Qt.MatchExactly)[0]
        general.setData(0, QtCore.Qt.UserRole, page)
        self.ui.pages.setCurrentIndex(0)

        # appearance
        page = PageAppearance(self.ui.pages)
        self.ui.pages.addWidget(page)
        general = self.ui.categories.findItems(
            'Appearance', QtCore.Qt.MatchExactly)[0]
        general.setData(0, QtCore.Qt.UserRole, page)

        # appearance
        page = PageInterpreters(self.ui.pages)
        self.ui.pages.addWidget(page)
        general = self.ui.categories.findItems(
            'Interpreters', QtCore.Qt.MatchExactly)[0]
        general.setData(0, QtCore.Qt.UserRole, page)

        # show general settings
        self.ui.pages.setCurrentIndex(1)

        self.ui.categories.currentItemChanged.connect(self._on_category_changed)

    def _on_category_changed(self, cat):
        page = cat.data(0, QtCore.Qt.UserRole)
        if page:
            self.ui.pages.setCurrentWidget(page)
        else:
            self.ui.pages.setCurrentIndex(0)

    def apply(self):
        # apply the settings of every page, this mean writing in QSettings
        for i in range(self.ui.pages.count()):
            try:
                self.ui.pages.widget(i).apply()
            except AttributeError:
                # temp page for page not already implemented
                pass
        # let the application apply new settings on open windows
        if self._apply_callback is not None:
            self._apply_callback()

    @classmethod
    def edit_preferences(cls, parent):
        dlg = cls(parent, None)
        if dlg.exec_() == DlgPreferences.Accepted:
            dlg.apply()
