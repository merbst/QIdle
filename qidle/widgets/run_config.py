import os
import sys
from pyqode.qt import QtWidgets
from qidle import icons
from qidle.forms import widget_run_cfg_ui
from qidle.widgets.utils import load_interpreters


class RunConfigWidget(QtWidgets.QWidget):
    """
    Widget used to edit a run configuration.
    """
    def __init__(self, parent=None, mode=0):
        super(RunConfigWidget, self).__init__(parent)
        self._mode = mode
        self.ui = widget_run_cfg_ui.Ui_Form()
        self.ui.setupUi(self)
        # self.ui.tableWidgetEnvVars.horizontalHeader().setResizeMode(
        #     QtWidgets.QHeaderView.ResizeToContents)
        self.ui.toolButtonRemove.setDisabled(True)
        self.ui.pickerWorkingDir.pick_dirs = True
        self.ui.toolButtonAdd.clicked.connect(self._add_row)
        self.ui.tableWidgetEnvVars.currentCellChanged.connect(
            self._table_env_var_sel_changed)
        self.ui.toolButtonRemove.clicked.connect(self._rm_current_row)
        self.ui.toolButtonRemove.setIcon(icons.list_remove)
        self.ui.toolButtonAdd.setIcon(icons.list_add)
        self.ui.pickerScript.line_edit.textChanged.connect(
            self._update_working_dir)
        self.set_mode(mode)

    def set_mode(self, mode=0):
        """
        Sets the widget mode: Script or Project. Depending on the mode some
        widgets will be hidden or shown.

        :param mode: Mode: Script = 0, Project = 1.
        """
        if mode == 0:
            # Script Mode
            self.ui.lblInterpreter.show()
            self.ui.comboBoxInterpreter.show()
            self.ui.lineEditName.hide()
            self.ui.lblName.hide()
        else:
            # Project Mode
            self.ui.lineEditName.show()
            self.ui.lblName.show()
            self.ui.lblInterpreter.hide()
            self.ui.comboBoxInterpreter.hide()
            self.ui.pickerScript.line_edit.textChanged.connect(
                self._update_name)
        self._mode = mode

    def _update_name(self):
        if self.ui.lineEditName.text().strip() in ['Unnamed', '']:
            path = self.ui.pickerScript.path
            if os.path.exists(path) and os.path.isfile(path):
                self.ui.lineEditName.setText(
                    os.path.splitext(os.path.split(path)[1])[0])

    def _rm_current_row(self):
        self.ui.tableWidgetEnvVars.removeRow(
            self.ui.tableWidgetEnvVars.currentRow())

    def _table_env_var_sel_changed(self, current_row, _, prev_row, *args):
        if current_row != prev_row:
            self.ui.toolButtonRemove.setEnabled(current_row != -1)

    def _add_row(self):
        self.ui.tableWidgetEnvVars.insertRow(
            self.ui.tableWidgetEnvVars.rowCount())

    def _get_env_vars(self):
        env_vars = {}
        for i in range(self.ui.tableWidgetEnvVars.rowCount()):
            name_item = self.ui.tableWidgetEnvVars.item(i, 0)
            val_item = self.ui.tableWidgetEnvVars.item(i, 1)
            if name_item and val_item:
                env_vars[name_item.text()] = val_item.text()
        return env_vars

    def _update_working_dir(self, text):
        if os.path.exists(text) and os.path.isfile(text):
            self.ui.pickerWorkingDir.path = os.path.dirname(text)

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
        if self._mode == 0:
            interpreter = config['interpreter']
            load_interpreters(self.ui.comboBoxInterpreter, default=interpreter)
        else:
            self.ui.lineEditName.setText(config['name'])
        interpreter_options = config['interpreter_options']
        self.ui.lineEdidInterpreterOpts.setText(' '.join(interpreter_options))
        working_dir = config['working_dir']
        if working_dir is None:
            working_dir = os.path.dirname(config['script'])
        self.ui.pickerWorkingDir.path = working_dir
        self.ui.tableWidgetEnvVars.setRowCount(0)
        for key, value in config['env_vars'].items():
            index = self.ui.tableWidgetEnvVars.rowCount()
            self.ui.tableWidgetEnvVars.insertRow(index)
            self.ui.tableWidgetEnvVars.setItem(
                index, 0, QtWidgets.QTableWidgetItem(key))
            self.ui.tableWidgetEnvVars.setItem(
                index, 1, QtWidgets.QTableWidgetItem(value))

    def get_config(self):
        config = {
            'script': self.ui.pickerScript.path,
            'script_parameters':
                self.ui.lineEditScriptParams.text().split(' ') if
                self.ui.lineEditScriptParams.text() else '',
            'interpreter_options':
                self.ui.lineEdidInterpreterOpts.text().split(' ') if
                self.ui.lineEdidInterpreterOpts.text() else '',
            'working_dir': self.ui.pickerWorkingDir.path,
            'env_vars': self._get_env_vars(),
        }
        if self._mode == 0:
            config['interpreter'] = self.ui.comboBoxInterpreter.currentText()
        else:
            config['name'] = self.ui.lineEditName.text()
        return config
