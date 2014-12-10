"""
Contains the file system context menu used in the project window.
"""
import logging
import os
from pyqode.qt import QtGui, QtWidgets
from pyqode.core.widgets import FileSystemContextMenu
from qidle import icons, project
from qidle.preferences import Preferences


def _logger():
    return logging.getLogger(__name__)


class PyFileSystemContextMenu(FileSystemContextMenu):
    def __init__(self, window):
        super(PyFileSystemContextMenu, self).__init__()
        self.window = window

        # Create run config action
        self.action_create_run_cfg = QtWidgets.QAction(
            '&Create run configuration', self)
        self.action_create_run_cfg.setIcon(QtGui.QIcon(icons.configure))
        self.action_create_run_cfg.triggered.connect(
            self._on_action_create_run_cfg_triggered)

        # Run script action
        self.action_run = QtWidgets.QAction('&Run', self)
        self.action_run.setIcon(QtGui.QIcon(icons.run))
        self.action_run.triggered.connect(
            self._on_action_run_triggered)
        self.addSeparator()
        self.addAction(self.action_create_run_cfg)
        self.addAction(self.action_run)

    def get_new_user_actions(self):
        # New module
        self.action_new_module = QtWidgets.QAction('&Module', self)
        self.action_new_module.setIcon(QtGui.QIcon(
            icons.python_mimetype))
        self.action_new_module.triggered.connect(
            self._on_new_module_triggered)
        # New package
        self.action_new_package = QtWidgets.QAction('&Package', self)
        self.action_new_package.setIcon(QtGui.QIcon(
            icons.folder))
        self.action_new_package.triggered.connect(
            self._on_new_package_triggered)
        # separator with the regular entries
        action = QtWidgets.QAction(self)
        action.setSeparator(True)
        return [self.action_new_module, self.action_new_package, action]

    def _on_new_module_triggered(self):
        src = self.tree_view.helper.get_current_path()
        if os.path.isfile(src):
            src = os.path.dirname(src)
        name, status = QtWidgets.QInputDialog.getText(
            self.tree_view, 'Create new python module', 'Module name:',
            QtWidgets.QLineEdit.Normal, 'my_module')
        if status:
            if not os.path.splitext(name)[1]:
                name += '.py'
            path = os.path.join(src, name)
            with open(path, 'w'):
                pass
            self.tree_view.file_created.emit(path)

    def _on_new_package_triggered(self):
        src = self.tree_view.helper.get_current_path()
        if os.path.isfile(src):
            src = os.path.dirname(src)
        name, status = QtWidgets.QInputDialog.getText(
            self.tree_view, 'Create new python package', 'Package name:',
            QtWidgets.QLineEdit.Normal, 'my_package')
        if status:
            path = os.path.join(src, name)
            os.makedirs(path)
            path = os.path.join(path, '__init__.py')
            with open(path, 'w'):
                pass
            self.tree_view.file_created.emit(path)

    def exec_(self, *__args):
        path = self.tree_view.helper.get_current_path()
        name = self.name_from_path(path)
        enable = os.path.isfile(path)
        self.action_create_run_cfg.setText('Create/Edit %r' % name)
        self.action_run.setText('Run %r' % name)
        self.action_create_run_cfg.setEnabled(enable)
        self.action_run.setEnabled(enable)
        super().exec_(*__args)

    @staticmethod
    def name_from_path(src):
        return os.path.splitext(os.path.split(src)[1])[0]

    def _on_action_run_triggered(self):
        self._set_current_config()
        # trigger main window's run action
        self.window.run_script()

    def _create_default_working_config(self, configs, src):
        _logger().debug('creating new config')
        config = {
            'name': self.name_from_path(src),
            'script': src,
            'script_parameters': [],
            'interpreter': Preferences().cache.get_project_interpreter(
                self.window.path),
            'interpreter_options': [],
            'working_dir': os.path.dirname(src),
            'env_vars': {'PYTHONUNBUFFERED': '1'}
        }
        configs.append(config)
        project.set_run_configurations(self.window.path, configs)
        return config

    def find_config_from_script(self, configs, src):
        config = None
        for cfg in configs:
            if cfg['script'] == src:
                config = cfg
                break
        return config

    def _set_current_config(self):
        configs = project.get_run_configurations(self.window.path)
        src = self.tree_view.helper.get_current_path()
        config = self.find_config_from_script(configs, src)
        if config is None:
            config = self._create_default_working_config(configs, src)
        # change current config
        Preferences().cache.set_project_config(
            self.window.path, config['name'])
        self.window.update_combo_run_configs()

    def _on_action_create_run_cfg_triggered(self):
        self._set_current_config()
        # trigger main window's configure run action
        self.window.configure_run()