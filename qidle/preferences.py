"""
Provides an easy way to access the application preferences.

"""
import json
import os
import sys
from PyQt4 import QtCore
from PyQt4.QtGui import QKeySequence
from qidle.interpreter import detect_system_interpreters


class Section(object):
    def __init__(self, settings, prefix):
        self._settings = settings
        self.prefix = prefix

    def get_value(self, key, default=None):
        return self._settings.value('%s/%s' % (self.prefix, key), default)

    def set_value(self, key, value):
        self._settings.setValue('%s/%s' % (self.prefix, key), value)


class MainWindow(Section):
    def __init__(self, settings):
        super(MainWindow, self).__init__(settings, 'main_window')

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
        super(KeyBindings, self).__init__(settings, 'key_bindings')
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
        super(Cache, self).__init__(settings, 'cache')

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


class Interpreters(Section):
    def __init__(self, settings):
        super(Interpreters, self).__init__(
            settings, self.__class__.__name__.lower())

    @property
    def locals(self):
        """
        Gets/Sets the list of local interpreters, the one added
        manually by the user.

        :return: list of str
        """
        return eval(self.get_value('locals', '[]'))

    @locals.setter
    def locals(self, local_interpreters):
        self.set_value('locals', repr(local_interpreters))

    @property
    def virtual_envs(self):
        """
        Gets/sets the list of virtual envs
        :return:
        """
        return eval(self.get_value('virtual_envs', '[]'))

    @virtual_envs.setter
    def virtual_envs(self, virtual_envs):
        self.set_value('virtual_envs', repr(virtual_envs))

    @property
    def default(self):
        """
        Gets/Sets the default interpreter.
        """
        return self.get_value('default_interpreter',
                              os.path.realpath(sys.executable))

    @default.setter
    def default(self, interpreter):
        self.set_value('default_interpreter', interpreter)


class Preferences(QtCore.QSettings):
    def __init__(self):
        super(Preferences, self).__init__('QIdle', 'QIdle')
        self.main_window = MainWindow(self)
        self.key_bindings = KeyBindings(self)
        self.cache = Cache(self)
        self.interpreters = Interpreters(self)
