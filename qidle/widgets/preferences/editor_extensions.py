"""
This module contains the editor modes confifuration widget.
"""
from pyqode.qt import QtCore, QtWidgets
from pyqode.python.widgets import PyCodeEdit
from qidle import commons
from qidle.forms.settings_page_editor_extensions_ui import Ui_Form
from qidle.preferences import Preferences
from qidle.widgets.preferences.base import Page


class PageEditorExtensions(Page):
    def __init__(self, parent=None):
        self.ui = Ui_Form()
        super(PageEditorExtensions, self).__init__(self.ui, parent)

    def extract_doc(self, m):
        if m.__doc__:
            d = m.__doc__.strip()
            return d.splitlines()[0]
        else:
            return ''

    def _get_installed_modes(self):
        code_edit = PyCodeEdit()
        installed_modes = [(m.name, self.extract_doc(m))
                           for m in code_edit.modes]
        code_edit.close()
        code_edit.delete()
        del code_edit
        return installed_modes

    def _get_installed_panels(self):
        code_edit = PyCodeEdit()
        modes = [
            (m.name, self.extract_doc(m)) for m in code_edit.panels
            if m.name not in commons.DYNAMIC_PANELS
        ]
        code_edit.close()
        code_edit.delete()
        del code_edit
        return modes

    def _reset_modes(self):
        self.ui.lw_modes.clear()
        editor = Preferences().editor
        installed_modes = self._get_installed_modes()
        for mode, description in installed_modes:
            enabled = True
            if mode in editor.modes.keys():
                enabled = editor.modes[mode]
            item = QtWidgets.QListWidgetItem(mode, self.ui.lw_modes)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(
                QtCore.Qt.Checked if enabled else QtCore.Qt.Unchecked)
            self.ui.lw_modes.addItem(item)
            item.setToolTip(description)

    def _reset_panels(self):
        self.ui.lw_panels.clear()
        editor = Preferences().editor
        installed_panels = self._get_installed_panels()
        for mode, description in installed_panels:
            enabled = True
            if mode in editor.panels.keys():
                enabled = editor.panels[mode]
            item = QtWidgets.QListWidgetItem(mode, self.ui.lw_panels)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(
                QtCore.Qt.Checked if enabled else QtCore.Qt.Unchecked)
            self.ui.lw_panels.addItem(item)
            item.setToolTip(description)

    def reset(self):
        self._reset_modes()
        self._reset_panels()

    def _restore_default_modes(self):
        editor = Preferences().editor
        installed_modes = self._get_installed_modes()
        d = {}
        for mode, _ in installed_modes:
            d[mode] = True
        editor.modes = d

    def _restore_default_panels(self):
        editor = Preferences().editor
        installed_modes = self._get_installed_panels()
        d = {}
        for mode, _ in installed_modes:
            d[mode] = True
        editor.panels = d

    def restore_defaults(self):
        self._restore_default_modes()
        self._restore_default_panels()
        self.reset()

    def collect_modes_states(self, list_widget):
        d = {}
        for i in range(list_widget.count()):
            item = list_widget.item(i)
            d[item.text()] = item.checkState() == QtCore.Qt.Checked
        return d

    def apply(self):
        editor_preferences = Preferences().editor
        editor_preferences.modes = self.collect_modes_states(self.ui.lw_modes)
        editor_preferences.panels = self.collect_modes_states(self.ui.lw_panels)
