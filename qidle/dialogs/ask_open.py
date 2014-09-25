"""
This module contains the dialog use to aks the opening mode.
"""
from PyQt4 import QtGui
from qidle.forms import dlg_ask_open_script_ui
from qidle.preferences import Preferences


class DlgAskOpenScript(QtGui.QDialog):
    def __init__(self, parent):
        super(DlgAskOpenScript, self).__init__(parent)
        self.ui = dlg_ask_open_script_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Open script')

    @classmethod
    def ask(cls, parent):
        ret_val = None
        dlg = cls(parent)
        if dlg.exec_() == dlg.Accepted:
            if dlg.ui.rb_new.isChecked():
                ret_val = Preferences().general.OpenActions.NEW
            else:
                ret_val = Preferences().general.OpenActions.CURRENT
        return ret_val
