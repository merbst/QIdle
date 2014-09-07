"""
Provides an easy way to access the application preferences.

"""
import json
import sys
from PyQt4 import QtCore
from PyQt4.QtGui import QKeySequence


class Section:
    def __init__(self, settings, prefix):
        self._settings = settings
        self.prefix = prefix

    def get_value(self, key, default=None):
        return self._settings.value('%s/%s' % (self.prefix, key), default)

    def set_value(self, key, value):
        self._settings.setValue('%s/%s' % (self.prefix, key), value)


class MainWindow(Section):
    def __init__(self, settings):
        super().__init__(settings, 'main_window')

    @property
    def script_window_geometry(self):
        v = self.get_value('script_window_geometry')
        if v:
            return bytes(v)
        return b''

    @script_window_geometry.setter
    def script_window_geometry(self, value):
        self.set_value('script_window_geometry', value)

    @property
    def script_window_state(self):
        v = self.get_value('script_window_state')
        if v:
            return bytes(v)
        return b''

    @script_window_state.setter
    def script_window_state(self, value):
        self.set_value('script_window_state', value)


class KeyBindings(Section):
    def __init__(self, settings):
        super().__init__(settings, 'key_bindings')
        self.default_shortcuts = {
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

    def dict(self):
        def get_default_key_bindings():
            if self.default_shortcuts['actionConfigure_IDLE'].toString() == '':
                self.default_shortcuts['actionConfigure_IDLE'] = 'Ctrl+Alt+S'

            return self.default_shortcuts
        try:
            map = json.loads(self.get_value('values'))
        except TypeError:
            map = get_default_key_bindings()
        return map


class Cache(Section):
    def __init__(self, settings):
        super().__init__(settings, 'cache')

    @property
    def run_configs(self):
        """
        Returns the dictionary of run configurations. A run configuration is
        just a list of arguments to append to the run command.

        This is internally stored as a json object

        """
        string = self.get_value('run_configs', '{}')
        return json.loads(string)

    @run_configs.setter
    def run_configs(self, value):
        self.set_value('run_configs', json.dumps(value))

    def get_run_config_for_file(self, filename):
        try:
            dic = self.run_configs
            config = dic[filename]
        except KeyError:
            config = {
                'script': filename,
                'script_parameters': [],
                'interpreter': sys.executable,
                'interpreter_options': [],
                'working_dir': None,
                'env_vars': {
                    'PYTHONUNBUFFERED': '1'
                }
            }
            self.set_run_config_for_file(filename, config)
        return config

    def set_run_config_for_file(self, filename, config):
        dic = self.run_configs
        dic[filename] = config
        self.run_configs = dic

class Preferences(QtCore.QSettings):
    def __init__(self):
        super().__init__('QIdle', 'QIdle')
        self.main_window = MainWindow(self)
        self.key_bindings = KeyBindings(self)
        self.cache = Cache(self)
