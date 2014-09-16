"""
This module contains the icon definitions, taking icon theme into account on
linux.

"""
from PyQt4 import QtGui


def icon(path, theme=None):
    """
    Creates an icon from theme and fallback to a fully specified icon path.

    Theme can be None if you don't want use icons from system theme.

    :param path: fallback icon, in case the icon could not be found in the
        icons theme
    :param theme: Icon theme

    :return: QIcon
    """
    if theme and path:
        return QtGui.QIcon.fromTheme(theme, QtGui.QIcon(path))
    else:
        assert path is not None
        return QtGui.QIcon(path)

new_file = None
open_file = None
new_folder = None
open_folder = None
save = None
save_as = None
run = None
stop = None
python_mimetype = None
python_interpreter = None
python_virtualenv = None
preferences = None
help_about = None
help_contents = None
clear = None
configure = None
terminal = None
class_browser = None
window_close = None
application_exit = None
list_add = None
list_remove = None
go_up = None
go_down = None
qidle = None


def init():
    global new_file
    global open_file
    global new_folder
    global open_folder
    global save
    global save_as
    global run
    global stop
    global python_mimetype
    global python_interpreter
    global python_virtualenv
    global preferences
    global help_about
    global help_contents
    global clear
    global configure
    global terminal
    global class_browser
    global window_close
    global application_exit
    global list_add
    global list_remove
    global go_up
    global go_down
    global qidle

    new_file = icon(':/icons/document-new.png', 'document-new')
    open_file = icon(':/icons/document-open.png', 'document-open')
    new_folder = icon(':/icons/folder-new.png',               'folder-new')
    open_folder = icon(':/icons/folder-open.png', 'folder-open')
    save = icon(':/icons/document-save.png', 'document-save')
    save_as = icon(':/icons/document-save-as.png', 'document-save-as')
    run = icon(':/icons/media-playback-start.png', 'media-playback-start')
    stop = icon(':/icons/media-playback-stop.png', 'media-playback-stop')
    python_mimetype = icon(':/icons/application-x-python.png', 'text-x-python')
    python_interpreter = icon(':/icons/interpreter-sys.png')
    python_virtualenv = icon(':/icons/interpreter-venv.png')
    preferences = icon(':/icons/Preferences-system.png', 'preferences-system')
    help_about = icon(':/icons/dialog-information.png', 'help-about')
    help_contents = icon(':/icons/help.png', 'help-contents')
    clear = icon(':/icons/edit-clear.png', 'edit-clear')
    configure = icon(':/icons/system-run.png', 'system-run')
    terminal = icon(':/icons/terminal.png')
    class_browser = icon(':/icons/view-tree.png')
    window_close = icon(':/icons/dialog-close.png', 'window-close')
    application_exit = icon(':/icons/exit.png', 'exit')
    list_add = icon(':/icons/list-add.png', 'list-add')
    list_remove = icon(':/icons/list-remove.png', 'list-remove')
    go_up = icon(':/icons/go-up.png', 'go-up')
    go_down = icon(':/icons/go-up.png', 'go-down')
    qidle = icon(':/icons/QIdle.png')


class IconProvider(QtGui.QFileIconProvider):
    def icon(self, file_infos):
        global python_mimetype
        if file_infos.suffix() == 'py':
            return python_mimetype
        return super(IconProvider, self).icon(file_infos)
