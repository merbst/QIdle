from PyQt4 import QtGui
from qidle.settings import Settings
from qidle.forms import dlg_script_run_config_ui
from qidle.widgets import RunConfigWidget


class ScripConfigDialog(QtGui.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = dlg_script_run_config_ui.Ui_Dialog()
        self.ui.setupUi(self)

    @classmethod
    def edit_config(cls, parent, path):
        """
        Shows and edits the script configuration.

        :param parent: parent widget
        :param path: path of the script to edit
        """
        dlg = cls(parent)
        settings = Settings()
        dlg.ui.widget.set_config(settings.get_run_config_for_file(path))
        if dlg.exec_() == dlg.Accepted:
            settings.set_run_config_for_file(path, dlg.ui.widget.get_config())
