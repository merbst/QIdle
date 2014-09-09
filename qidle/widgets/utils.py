from PyQt4 import QtGui
from qidle.interpreter import detect_system_interpreters
from qidle.preferences import Preferences


def add_interpreter_list(combo, interpreters, default, default_index=None, icon=None):
    if icon is None:
        icon = QtGui.QIcon(':/icons/interpreter-sys.png')
    for interpreter in sorted(interpreters):
        index =combo.count()
        combo.addItem(icon, interpreter)
        if interpreter == default:
            default_index = index
    return default_index


def load_interpreters(combo, default=None):
    if default is None:
        default = Preferences().interpreters.default
    default_index = add_interpreter_list(
        combo, detect_system_interpreters(), default)
    default_index = add_interpreter_list(
        combo, Preferences().interpreters.virtual_envs, default,
        default_index, icon=QtGui.QIcon(':/icons/interpreter-venv.png'))
    default_index = add_interpreter_list(
        combo, Preferences().interpreters.locals, default, default_index)
    combo.setCurrentIndex(default_index)
