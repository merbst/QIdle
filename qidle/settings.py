"""
Provides an easy way to access the application settings.

"""
import json
from pyqode.qt import QtCore
from pyqode.qt.QtGui import QKeySequence


class Settings:
    def __init__(self):
        self._settings = QtCore.QSettings()
        # self._settings.clear()

    @property
    def script_window_geometry(self):
        v = self._settings.value('script_window_geometry')
        if v:
            return bytes(v)
        return b''

    @script_window_geometry.setter
    def script_window_geometry(self, value):
        self._settings.setValue('script_window_geometry', value)

    @property
    def script_window_state(self):
        v = self._settings.value('script_window_state')
        if v:
            return bytes(v)
        return b''

    @script_window_state.setter
    def script_window_state(self, value):
        self._settings.setValue('script_window_state', value)

    @property
    def key_bindings(self):
        def get_default_key_bindings():
            default_key_bindings = {
                'actionNew_file': QKeySequence(QKeySequence.New),
                'actionNew_project': QKeySequence('Ctrl+Shift+N'),
                'actionOpen_file': QKeySequence(QKeySequence.Open),
                'actionOpen_directory': QKeySequence('Ctrl+Shift+O'),
                'actionSave': QKeySequence(QKeySequence.Save),
                'actionSave_as': QKeySequence(QKeySequence.SaveAs),
                'actionQuit': QKeySequence(QKeySequence.Quit),
                'actionRun': QKeySequence('F5'),
                'actionConfigureRun': QKeySequence('F8'),
                'actionConfigure_IDLE': QKeySequence(QKeySequence.Preferences),
                'actionZoom_height': QKeySequence('Alt+Z'),
                'actionHelp_content': QKeySequence.HelpContents,
                'actionPython_docs': QKeySequence('Shift+F1')
            }

            if default_key_bindings['actionConfigure_IDLE'].toString() == '':
                default_key_bindings['actionConfigure_IDLE'] = 'F2'

            return default_key_bindings
        try:
            map = json.loads(self._settings.value('key_bindings'))
        except TypeError:
            map = get_default_key_bindings()
        return map

    @property
    def run_configs(self):
        """
        Returns the dictionary of run configurations. A run configuration is
        just a list of arguments to append to the run command.

        This is internally stored as a json object

        """
        string = self._settings.value('run_configs', '{}')
        return json.loads(string)

    @run_configs.setter
    def run_configs(self, value):
        self._settings.setValue('run_configs', json.dumps(value))

    def get_run_config_for_file(self, filename):
        try:
            dic = self.run_configs
            config = dic[filename]
        except KeyError:
            config = []
            self.set_run_config_for_file(filename, config)
        return config

    def set_run_config_for_file(self, filename, config):
        dic = self.run_configs
        dic[filename] = config
        self.run_configs = dic
