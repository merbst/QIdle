import os
from pyqode.qt import QtCore, QtWidgets
from qidle import icons, project
from qidle.forms import dlg_prj_run_ui
from qidle.preferences import Preferences
from qidle.widgets.utils import load_interpreters


class DlgProjectRunConfig(QtWidgets.QDialog):
    def __init__(self, parent, prj_path):
        super(DlgProjectRunConfig, self).__init__(parent)
        self._current_cfg = None
        self.ui = dlg_prj_run_ui.Ui_Dialog()
        self.ui.setupUi(self)

        # enable project mode
        self.ui.cfgWidget.set_mode(1)

        # setup icons
        self.ui.pushButtonRmConfig.setIcon(icons.list_remove)
        self.ui.pushButtonAddConfig.setIcon(icons.list_add)

        # load combo box interpreters
        load_interpreters(
            self.ui.comboInterpreters,
            default=Preferences().cache.get_project_interpreter(prj_path))

        # load project run configurations
        self._configs = project.get_run_configurations(prj_path)
        for cfg in self._configs:
            self.ui.listConfigs.addItem(cfg['name'])
        self.ui.listConfigs.currentItemChanged.connect(
            self._on_current_item_changed)
        if self.ui.listConfigs.count() == 0:
            # first time configuration, create one new unamed config
            self._create_new()
            self.ui.cfgWidget.ui.lineEditName.setFocus()

        # select current config
        current_config = Preferences().cache.get_project_config(prj_path)
        if current_config is None:
            self.ui.listConfigs.setCurrentRow(0)
        else:
            items = self.ui.listConfigs.findItems(
                current_config, QtCore.Qt.MatchExactly)
            if len(items):
                item = items[0]
                self.ui.listConfigs.setCurrentItem(item)

        # configure signal/slots
        self.ui.cfgWidget.ui.lineEditName.textChanged.connect(
            self._on_name_changed)
        self.ui.pushButtonAddConfig.clicked.connect(self._create_new)
        self.ui.pushButtonRmConfig.clicked.connect(self._rm_current_cfg)

    def _rm_current_cfg(self):
        self._configs.remove(self._current_cfg)
        self._current_cfg = None
        self.ui.listConfigs.takeItem(self.ui.listConfigs.currentRow())

    def _on_name_changed(self, name):
        self._current_cfg['name'] = name
        self.ui.listConfigs.currentItem().setText(name)

    def _show_context_menu(self, pos):
        """
        Shows the configurations context menu (add/remove).
        """
        menu = QtWidgets.QMenu(self)
        menu.addAction(self.action_add_config)
        menu.addAction(self.action_rm_config)
        self.action_rm_config.setEnabled(
            self.ui.listConfigs.currentItem() is not None)
        menu.exec_(self.mapToGlobal(pos))

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
        self.ui.listConfigs.setCurrentRow(self.ui.listConfigs.count()-1)
        self.ui.cfgWidget.ui.pickerScript.tool_button.setFocus()

    def _remove_current(self):
        """
        Removes the current configuration
        """
        # todo
        pass

    def _config_from(self, name):
        for cfg in self._configs:
            if cfg['name'] == name:
                return cfg
        return None

    def _store_current_config(self):
        if self._current_cfg is None:
            return
        self._update_current_cfg(self.ui.cfgWidget.get_config())

    def _update_current_cfg(self, new_cfg):
        self._current_cfg.update(new_cfg)

    def _on_current_item_changed(self, item):
        if self._current_cfg:
            self._store_current_config()
        # update current config values
        cfg = self._config_from(item.text())
        self._current_cfg = cfg
        self.ui.cfgWidget.set_config(cfg)
        self.ui.cfgWidget.ui.lineEditName.setFocus()

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
            Preferences().cache.set_project_config(
                prj_path, dlg.ui.listConfigs.currentItem().text())
