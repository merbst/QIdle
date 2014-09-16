"""
This module contains the create virtualenv dialog.
"""
import os
from PyQt4 import QtGui
from qidle.forms.dlg_create_virtualenv_ui import Ui_Dialog
from qidle.system import WINDOWS
from qidle.widgets.utils import load_interpreters


class DlgCreateVirtualEnv(QtGui.QDialog):
    def __init__(self, parent):
        super(DlgCreateVirtualEnv, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        load_interpreters(self.ui.combo_interpreters,
                          locals=False, virtualenvs=False)
        self.ui.lineedit_name.textChanged.connect(
            self._update_full_path)
        self.ui.lineedit_name.setText('unnamed')
        self.ui.dir_picker.pick_dirs = True
        self.ui.dir_picker.line_edit.setText(
            os.path.join(os.path.expanduser('~')))
        self.ui.dir_picker.line_edit.textChanged.connect(
            self._update_full_path)

    @staticmethod
    def _set_widget_background_color(widget, color):
        """
        Changes the base color of a widget (background).
        :param widget: widget to modify
        :param color: the color to apply
        """
        pal = widget.palette()
        pal.setColor(pal.Base, color)
        widget.setPalette(pal)

    def _update_full_path(self):
        path = os.path.join(self.ui.dir_picker.path,
                            self.ui.lineedit_name.text())
        exists = os.path.exists(path)
        self.ui.buttonBox.button(self.ui.buttonBox.Ok).setEnabled(not exists)
        self.ui.label_full_path.setText(path)
        color = QtGui.QColor('#FFCCCC') if exists else self.palette().color(
            self.palette().Base)
        self._set_widget_background_color(self.ui.lineedit_name, color)
        self.ui.lineedit_name.setToolTip(
            'Path already exists' if exists else '')

    @classmethod
    def get_virtualenv_creation_params(cls, parent):
        """
        Show the dialog and return the information needed to create the
        virtualenv. Returns None if the dialog has been canceled.
        """
        dlg = cls(parent)
        if dlg.exec_() == dlg.Accepted:
            path = dlg.ui.label_full_path.text()
            interprerer = dlg.ui.combo_interpreters.currentText()
            system_site_packages = dlg.ui.check_box_site_packages.isChecked()
            return path, interprerer, system_site_packages
        else:
            return None