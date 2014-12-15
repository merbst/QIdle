"""
This module contains the preferences dialog implementation.

"""
import logging
from pyqode.qt import QtCore, QtWidgets
from qidle import icons
from qidle.forms.dlg_preferences_ui import Ui_Dialog
from qidle.preferences import Preferences
from qidle.widgets.preferences import (
    PageAppearance, PageGeneral, PageInterpreters, PageEditor,
    PageEditorExtensions
)


def _logger():
    return logging.getLogger(__name__)


class DlgPreferences(QtWidgets.QDialog):
    def __init__(self, parent, apply_callback):
        super(DlgPreferences, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self._apply_callback = apply_callback
        self.setWindowIcon(icons.preferences)
        self._pages = []
        self._items = []

        # setup pages
        self.general = self.add_page(
            PageGeneral(self.ui.pages), 'General', icons.preferences)
        self.editor = self.add_page(
            PageEditor(self.ui.pages), 'Editor', icons.text_edit)
        self.editor_appearance = self.add_page(
            PageAppearance(self.ui.pages), 'Appearance', icons.appearance)
        self.editor_extensions = self.add_page(
            PageEditorExtensions(self.ui.pages), 'Extensions',
            icons.preferences_plugin)
        self.interpreters = self.add_page(
            PageInterpreters(self.ui.pages), 'Interpreters',
            icons.python_interpreter)
        self.ui.categories.currentItemChanged.connect(
            self._on_category_changed)
        self.ui.buttons.button(self.ui.buttons.Reset).clicked.connect(
            self.reset)
        self.ui.buttons.button(
            self.ui.buttons.RestoreDefaults).clicked.connect(
            self.restore_defaults)
        self.ui.categories.expandAll()
        self.ui.categories.adjustSize()
        self.restore_state()

    def close(self):
        self.editor_appearance.ui.edit_preview.close()
        self.interpreters.stop_backend()
        self.save_state()

    def add_page(self, page, categorie, icon, child_index=0):
        self.ui.pages.addWidget(page)
        item = self.ui.categories.findItems(
            categorie, QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive)[child_index]
        page.item = item
        item.setData(0, QtCore.Qt.UserRole, page)
        item.setIcon(0, icon)
        self._pages.append(page)
        self._items.append(item)
        return page

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
    def edit_preferences(cls, parent, callback=None):
        dlg = cls(parent, callback)
        if dlg.exec_() == DlgPreferences.Accepted:
            dlg.apply()
        dlg.close()
        dlg.deleteLater()

    def reset(self):
        w = self.ui.pages.currentWidget()
        try:
            w.reset()
        except NotImplementedError:
            _logger.exception(
                'reset not implemented for widget %s' % w.objectName())

    def restore_defaults(self):
        w = self.ui.pages.currentWidget()
        try:
            self.ui.pages.currentWidget().restore_defaults()
        except NotImplementedError:
            _logger().exception(
                'restore_defaults not implemented for widget %s' %
                w.objectName())

    def restore_state(self):
        prefs = Preferences()
        self.restoreGeometry(prefs.preferences_dialog.geometry)
        self.ui.categories.setCurrentItem(self._items[prefs.preferences_dialog.index])

    def save_state(self):
        prefs = Preferences()
        prefs.preferences_dialog.geometry = self.saveGeometry()
        prefs.preferences_dialog.index = self.ui.pages.currentIndex() - 1
