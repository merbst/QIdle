import os
from pyqode.qt import QtCore, QtWidgets
from qidle import icons, project
from qidle.forms import dlg_prj_run_ui
from qidle.preferences import Preferences
from qidle.widgets.utils import load_interpreters


class DlgProjectRunConfig(QtWidgets.QDialog):
    def __init__(self, parent, prj_path, current_config=None):
        super(DlgProjectRunConfig, self).__init__(parent)
        self._current_cfg = None
        self.ui = dlg_prj_run_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.toolButtonRemove.setIcon(icons.list_remove)
        self.ui.toolButtonAdd.setIcon(icons.list_add)
        self.ui.pickerWorkingDir.pick_dirs = True
        self.ui.listConfigs.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.listConfigs.customContextMenuRequested.connect(
            self._show_context_menu)
        load_interpreters(
            self.ui.comboInterpreters,
            default=Preferences().cache.get_project_interpreter(prj_path))
        self._configs = project.get_run_configurations(prj_path)
        for cfg in self._configs:
            self.ui.listConfigs.addItem(cfg['name'])
        self.ui.listConfigs.currentItemChanged.connect(
            self._on_current_item_changed)
        self.ui.pickerScript.default_directory = prj_path
        self.ui.pickerWorkingDir.default_directory = prj_path
        if self.ui.listConfigs.count() == 0:
            self._create_new()
            self.ui.lineEditName.setFocus()
        if current_config is None:
            self.ui.listConfigs.setCurrentRow(0)
        self.ui.pickerScript.line_edit.textChanged.connect(
            self._on_script_changed)
        self.ui.lineEditName.textChanged.connect(self._on_name_changed)
        self.ui.toolButtonAdd.clicked.connect(self._add_row)
        self.ui.tableWidgetEnvVars.itemSelectionChanged.connect(
            self._table_env_var_sel_changed)
        self.ui.toolButtonRemove.clicked.connect(self._rm_current_row)

    def _rm_current_row(self):
        self.ui.tableWidgetEnvVars.removeRow(
            self.ui.tableWidgetEnvVars.currentRow())

    def _table_env_var_sel_changed(self):
        self.ui.toolButtonRemove.setEnabled(
            len(self.ui.tableWidgetEnvVars.selectedItems()))

    def _add_row(self):
        self.ui.tableWidgetEnvVars.insertRow(
            self.ui.tableWidgetEnvVars.rowCount())

    def _on_name_changed(self, name):
        self._current_cfg['name'] = name
        self.ui.listConfigs.currentItem().setText(name)

    def _on_script_changed(self, script):
        if not os.path.exists(script):
            return
        if self.ui.lineEditName.text() == 'Unnamed':
            self.ui.lineEditName.setText(
                os.path.splitext(os.path.split(script)[1])[0])
        if self.ui.pickerWorkingDir.line_edit.text() == '':
            self.ui.pickerWorkingDir.path = os.path.dirname(script)

    def _show_context_menu(self, pos):
        """
        Shows the configurations context menu (add/remove).
        """
        # todo: show context menu and implement add/remove config

    def _create_new(self):
        """
        Creates a new configuration
        """
        config = {
            'name': 'Unnamed',
            'script': '',
            'script_parameters': [],
            'interpreter_options': [],
            'working_dir': '',
            'env_vars': {
                'PYTHONUNBUFFERED': '1'
            }
        }
        self._configs.append(config)
        self.ui.listConfigs.addItem(config['name'])

    def _remove_current(self):
        """
        Removes the current configuration
        """
        pass

    def _config(self, name):
        for cfg in self._configs:
            if cfg['name'] == name:
                return cfg
        return None

    def _get_env_vars(self):
        env_vars = {}
        for i in range(self.ui.tableWidgetEnvVars.rowCount()):
            name_item = self.ui.tableWidgetEnvVars.item(i, 0)
            val_item = self.ui.tableWidgetEnvVars.item(i, 1)
            if name_item and val_item:
                env_vars[name_item.text()] = val_item.text()
        return env_vars

    def _store_current_config(self):
        self._current_cfg['name'] = self.ui.lineEditName.text()
        self._current_cfg['script'] = self.ui.pickerScript.path
        if self.ui.lineEditScriptParams.text():
            self._current_cfg['script_parameters'] = \
                self.ui.lineEditScriptParams.text().split(' ')
        else:
            self._current_cfg['script_parameters'] = []
        self._current_cfg['working_dir'] = self.ui.pickerWorkingDir.path
        if self.ui.lineEdidInterpreterOpts.text():
            self._current_cfg['interpreter_options'] = \
                self.ui.lineEdidInterpreterOpts.text().split(' ')
        else:
            self._current_cfg['interpreter_options'] = []
        self._current_cfg['env_vars'] = self._get_env_vars()

    def _on_current_item_changed(self, item):
        if self._current_cfg:
            self._store_current_config()
        # update current config values
        cfg = self._config(item.text())
        self.ui.lineEditName.setText(cfg['name'])
        self.ui.pickerScript.path = cfg['script']
        self.ui.lineEditScriptParams.setText(
            ' '.join(cfg['script_parameters']))
        self.ui.pickerWorkingDir.path = cfg['working_dir']
        self.ui.lineEdidInterpreterOpts.setText(
            ' '.join(cfg['interpreter_options']))
        for key, value in cfg['env_vars'].items():
            index = self.ui.tableWidgetEnvVars.rowCount()
            self.ui.tableWidgetEnvVars.insertRow(index)
            self.ui.tableWidgetEnvVars.setItem(
                index, 0, QtWidgets.QTableWidgetItem(key))
            self.ui.tableWidgetEnvVars.setItem(
                index, 1, QtWidgets.QTableWidgetItem(value))
        self._current_cfg = cfg

    @classmethod
    def edit_configs(cls, parent, prj_path):
        """
        Edit project run configurations.

        :param parent: parent widget
        :param prj_path: project path
        """
        dlg = cls(parent, prj_path)
        if dlg.exec_() == dlg.Accepted:
            dlg._store_current_config()
            project.set_run_configurations(prj_path, dlg._configs)
            Preferences().cache.set_project_interpreter(
                prj_path, dlg.ui.comboInterpreters.currentText())
