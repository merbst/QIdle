"""
This module contains the editor modes confifuration widget.
"""
from pyqode.qt import QtCore, QtWidgets
from pyqode.python.widgets import PyCodeEdit
from qidle.forms.settings_page_modes_ui import Ui_Form
from qidle.preferences import Preferences
from qidle.widgets.preferences.base import Page


class PageEditorModes(Page):
    def __init__(self, parent=None):
        self.ui = Ui_Form()
        super(PageEditorModes, self).__init__(self.ui, parent)

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

    def reset(self):
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

    def restore_defaults(self):
        editor = Preferences().editor
        installed_modes = self._get_installed_modes()
        d = {}
        for mode, _ in installed_modes:
            d[mode] = True
        editor.modes = d
        self.reset()

    def apply(self):
        editor = Preferences().editor
        d = {}
        for i in range(self.ui.lw_modes.count()):
            item = self.ui.lw_modes.item(i)
            d[item.text()] = item.checkState() == QtCore.Qt.Checked
        editor.modes = d
