"""
This module contains the editor modes confifuration widget.
"""
from pyqode.qt import QtCore, QtWidgets
from pyqode.python.widgets import PyCodeEdit
from qidle.forms.settings_page_panels_ui import Ui_Form
from qidle.preferences import Preferences
from qidle.widgets.preferences.base import Page


class PageEditorPanels(Page):
    def __init__(self, parent=None):
        self.ui = Ui_Form()
        super(PageEditorPanels, self).__init__(self.ui, parent)

    def extract_doc(self, m):
        if m.__doc__:
            d = m.__doc__.strip()
            return d.splitlines()[0]
        else:
            return ''

    def _get_installed_panels(self):
        code_edit = PyCodeEdit()
        modes = [(m.name, self.extract_doc(m))
                 for m in code_edit.panels if m.name != 'SymbolBrowserPanel']
        code_edit.close()
        code_edit.delete()
        del code_edit
        return modes

    def reset(self):
        self.ui.lw_modes.clear()
        editor = Preferences().editor
        installed_panels = self._get_installed_panels()
        for mode, description in installed_panels:
            enabled = True
            if mode in editor.panels.keys():
                enabled = editor.panels[mode]
            item = QtWidgets.QListWidgetItem(mode, self.ui.lw_modes)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(
                QtCore.Qt.Checked if enabled else QtCore.Qt.Unchecked)
            self.ui.lw_modes.addItem(item)
            item.setToolTip(description)

    def restore_defaults(self):
        editor = Preferences().editor
        installed_modes = self._get_installed_panels()
        d = {}
        for mode, _ in installed_modes:
            d[mode] = True
        editor.panels = d
        self.reset()

    def apply(self):
        editor = Preferences().editor
        d = {}
        for i in range(self.ui.lw_modes.count()):
            item = self.ui.lw_modes.item(i)
            d[item.text()] = item.checkState() == QtCore.Qt.Checked
        editor.panels = d
