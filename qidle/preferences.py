"""
Provides an easy way to access the application preferences.

"""
import json
import os
import sys
from PyQt4 import QtCore
from PyQt4.QtGui import QKeySequence
from qidle.python import detect_system_interpreters


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
        super(MainWindow, self).__init__(settings, self.__class__.__name__)

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
                self.default_shortcuts['actionConfigure_IDLE'] = 'F2'

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
                'interpreter': self._settings.interpreters.default,
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
        super(Interpreters, self).__init__(settings, self.__class__.__name__)

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
        values = list(set(eval(self.get_value('virtual_envs', '[]'))))
        ret_val = []
        for val in values:
            if os.path.exists(val):
                ret_val.append(val)
        self.set_value('virtual_envs', repr(list(set(ret_val))))
        return ret_val

    @virtual_envs.setter
    def virtual_envs(self, virtual_envs):
        self.set_value('virtual_envs', repr(list(set(virtual_envs))))

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


class General(Section):
    class OpenActions:
        NEW = 0
        CURRENT = 1
        ASK = 2

    def __init__(self, settings):
        super(General, self).__init__(settings, '')

    @property
    def confirm_application_exit(self):
        return eval(self.get_value('confirm_application_exit', 'True'))

    @confirm_application_exit.setter
    def confirm_application_exit(self, value):
        self.set_value('confirm_application_exit', repr(value))

    @property
    def reopen_last_window(self):
        return eval(self.get_value('reopen_last_window', 'True'))

    @reopen_last_window.setter
    def reopen_last_window(self, value):
        self.set_value('reopen_last_window', repr(value))

    @property
    def open_scr_action(self):
        return int(self.get_value(
            'open_scr_action', repr(self.OpenActions.NEW)))

    @open_scr_action.setter
    def open_scr_action(self, value):
        self.set_value('open_scr_action', repr(value))

    @property
    def restore_scr_window_state(self):
        return eval(self.get_value('restore_scr_window_state', 'False'))

    @restore_scr_window_state.setter
    def restore_scr_window_state(self, value):
        self.set_value('restore_scr_window_state', repr(value))

    @property
    def save_before_run(self):
        return eval(self.get_value('save_before_run', 'True'))

    @save_before_run.setter
    def save_before_run(self, value):
        self.set_value('save_before_run', repr(value))


class Appearance(Section):
    def __init__(self, settings):
        super(Appearance, self).__init__(settings, self.__class__.__name__)

    @property
    def font(self):
        return self.get_value('font', 'Source Code Pro')

    @font.setter
    def font(self, value):
        self.set_value('font', value)

    @property
    def font_size(self):
        return int(self.get_value('font_size', '10'))

    @font_size.setter
    def font_size(self, value):
        self.set_value('font_size', value)

    @property
    def show_whitespaces(self):
        return eval(self.get_value('show_whitespaces', 'False'))

    @show_whitespaces.setter
    def show_whitespaces(self, value):
        self.set_value('show_whitespaces', repr(value))

    @property
    def color_scheme(self):
        return self.get_value('color_scheme', 'qt')

    @color_scheme.setter
    def color_scheme(self, value):
        self.set_value('color_scheme', value)


class Editor(Section):
    def __init__(self, settings):
        super(Editor, self).__init__(settings, self.__class__.__name__)

    @property
    def highlight_caret_scope(self):
        return eval(self.get_value('highlight_caret_scope', 'False'))

    @highlight_caret_scope.setter
    def highlight_caret_scope(self, value):
        self.set_value('highlight_caret_scope', repr(value))

    @property
    def use_spaces_instead_of_tabs(self):
        return eval(self.get_value('use_spaces_instead_of_tabs', 'True'))

    @use_spaces_instead_of_tabs.setter
    def use_spaces_instead_of_tabs(self, value):
        self.set_value('use_spaces_instead_of_tabs', repr(value))

    @property
    def tab_len(self):
        return eval(self.get_value('tab_len', '4'))

    @tab_len.setter
    def tab_len(self, value):
        self.set_value('tab_len', repr(value))

    @property
    def margin_pos(self):
        return eval(self.get_value('margin_pos', '79'))

    @margin_pos.setter
    def margin_pos(self, value):
        self.set_value('margin_pos', repr(value))

    @property
    def convert_tabs_to_spaces(self):
        return eval(self.get_value('convert_tab_to_spaces', 'True'))

    @convert_tabs_to_spaces.setter
    def convert_tabs_to_spaces(self, value):
        self.set_value('convert_tab_to_spaces', repr(value))

    @property
    def clean_trailing(self):
        return eval(self.get_value('clean_trailing', 'True'))

    @clean_trailing.setter
    def clean_trailing(self, value):
        self.set_value('convert_tab_to_spaces', repr(value))

    @property
    def restore_cursor(self):
        return eval(self.get_value('restore_cursor', 'True'))

    @restore_cursor.setter
    def restore_cursor(self, value):
        self.set_value('restore_cursor', repr(value))

    @property
    def safe_save(self):
        return eval(self.get_value('safe_save', 'True'))

    @safe_save.setter
    def safe_save(self, value):
        self.set_value('safe_save', repr(value))

    @property
    def cc_trigger_len(self):
        return eval(self.get_value('cc_trigger_len', '1'))

    @cc_trigger_len.setter
    def cc_trigger_len(self, value):
        self.set_value('cc_trigger_len', repr(value))

    @property
    def cc_show_tooltips(self):
        return eval(self.get_value('cc_show_tooltips', 'True'))

    @cc_show_tooltips.setter
    def cc_show_tooltips(self, value):
        self.set_value('cc_show_tooltips', repr(value))

    @property
    def cc_case_sensitive(self):
        return eval(self.get_value('cc_case_sensitive', 'False'))

    @cc_case_sensitive.setter
    def cc_case_sensitive(self, value):
        self.set_value('cc_case_sensitive', repr(value))

    @property
    def modes(self):
        default = {
            'CalltipsMode': True,
            'CaretLineHighlighterMode': True,
            'CodeCompletionMode': True,
            'CommentsMode': True,
            'DocumentAnalyserMode': True,
            'ExtendedSelectionMode': True,
            'FileWatcherMode': True,
            'FrostedCheckerMode': True,
            'GoToAssignmentsMode': True,
            'OccurrencesHighlighterMode': True,
            'PEP8CheckerMode': True,
            'PyAutoCompleteMode': True,
            'PyAutoIndentMode': True,
            'PyIndenterMode': True,
            'PythonSH': True,
            'RightMarginMode': True,
            'SmartBackSpaceMode': True,
            'SymbolMatcherMode': True,
            'ZoomMode': True
        }
        return eval(self.get_value('modes', repr(default)))

    @modes.setter
    def modes(self, value):
        self.set_value('modes', repr(value))

    @property
    def panels(self):
        default = {
            'EncodingPanel': True,
            'LineNumberPanel': True,
            'CheckerPanel': True,
            'FoldingPanel': True,
            'GlobalCheckerPanel': True,
            'QuickDocPanel': True,
            'SearchAndReplacePanel': True,
            'CalltipsMode': True
        }
        return eval(self.get_value('panels', repr(default)))

    @panels.setter
    def panels(self, value):
        self.set_value('panels', repr(value))


class Preferences(QtCore.QSettings):
    #: settings version, updated it to clear user settings for the next
    # release
    version = ''
    names = ('QIdle', 'QIdle%s' % version)

    def __init__(self):
        super(Preferences, self).__init__(*self.names)
        self.main_window = MainWindow(self)
        self.key_bindings = KeyBindings(self)
        self.cache = Cache(self)
        self.interpreters = Interpreters(self)
        self.general = General(self)
        self.appearance = Appearance(self)
        self.editor = Editor(self)
