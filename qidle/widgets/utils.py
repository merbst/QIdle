from pyqode.qt import QtGui
from qidle import icons
from qidle.python import detect_system_interpreters
from qidle.preferences import Preferences


def load_interpreters(combo, default=None, locals=True, virtualenvs=True):
    def _add(combo, interpreters, default, default_index=None, icon=None):
        if icon is None:
            icon = icons.python_interpreter
        for interpreter in sorted(interpreters):
            index = combo.count()
            try:
                combo.addItem(icon, interpreter)
            except TypeError:
                pass
            else:
                if interpreter == default:
                    default_index = index
        return default_index

    combo.clear()
    if default is None:
        default = Preferences().interpreters.default
    default_index = _add(
        combo, detect_system_interpreters(), default)
    if virtualenvs:
        default_index = _add(
            combo, Preferences().interpreters.virtual_envs, default,
            default_index, icon=icons.python_virtualenv)
    if locals:
        default_index = _add(
            combo, Preferences().interpreters.locals, default, default_index)
    combo.setCurrentIndex(default_index if default_index is not None else 0)
