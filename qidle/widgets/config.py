import os
from PyQt4 import QtGui
import sys
from qidle.forms import widget_run_cfg_ui


class RunConfigWidget(QtGui.QWidget):
    """
    Widget used to edit a run configuration.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = widget_run_cfg_ui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButtonRemove.setDisabled(True)
        self.ui.pickerWorkingDir.pick_dirs = True
        self.ui.pushButtonAdd.clicked.connect(self._add_row)
        self.ui.tableWidgetEnvVars.itemSelectionChanged.connect(
            self._table_env_var_sel_changed)

    def _table_env_var_sel_changed(self):
        self.ui.pushButtonRemove.setEnabled(
            len(self.ui.tableWidgetEnvVars.selectedItems()))

    def _add_row(self):
        self.ui.tableWidgetEnvVars.insertRow(
            self.ui.tableWidgetEnvVars.rowCount())

    def _get_env_vars(self):
        env_vars = {}
        for i in range(self.ui.tableWidgetEnvVars.rowCount()):
            name = self.ui.tableWidgetEnvVars.item(i, 0).text()
            val = self.ui.tableWidgetEnvVars.item(i, 1).text()
            env_vars[name] = val
        return env_vars

    def set_config(self, config):
        """
        Sets the config to edit.

        Config is a dist with the following entries:
            - script: script path
            - script_parameters: list of script parameters
            - interpreter: path to the python interpreter to use to run the
                           program
            - interpreter_options: list of interpreter options
            - working_dir: can be None, in this case the dirname of the
              script is used.
            - env_vars: dict of envirnonment variables to setup
                when running the program.

        :param config: Config dict
        """
        self.ui.pickerScript.path = config['script']
        self.ui.lineEditScriptParams.setText(
            ' '.join(config['script_parameters']))
        # todo when we have an interpreter settings dialog
        interpreter = config['interpreter']
        interpreter_options = config['interpreter_options']
        working_dir = config['working_dir']
        if working_dir is None:
            working_dir = os.path.dirname(config['script'])
        self.ui.pickerWorkingDir.path = working_dir
        for key, value in config['env_vars'].items():
            index = self.ui.tableWidgetEnvVars.rowCount()
            self.ui.tableWidgetEnvVars.insertRow(index)
            self.ui.tableWidgetEnvVars.setItem(
                index, 0, QtGui.QTableWidgetItem(key))
            self.ui.tableWidgetEnvVars.setItem(
                index, 1, QtGui.QTableWidgetItem(value))

    def get_config(self):
        config = {
            'script': self.ui.pickerScript.path,
            'script_parameters':
                self.ui.lineEditScriptParams.text().split(' ') if
                self.ui.lineEditScriptParams.text() else '',
            'interpreter': sys.executable,
            'interpreter_options':
                self.ui.lineEdidInterpreterOpts.text().split(' ') if
                self.ui.lineEdidInterpreterOpts.text() else '',
            'working_dir': self.ui.pickerWorkingDir.path,
            'env_vars': self._get_env_vars(),
        }
        return config
