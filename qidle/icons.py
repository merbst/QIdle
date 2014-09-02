"""
This module contains the icon definitions, taking icon theme into account on
linux.

"""
from pyqode.qt import QtGui


def icon(theme, path):
    """
    Creates an icon from theme and fallback to a fully specified icon path.

    :param theme: Icon theme
    :param path: Fallback path
    :return: QIcon
    """
    return QtGui.QIcon.fromTheme(theme, QtGui.QIcon(path))




