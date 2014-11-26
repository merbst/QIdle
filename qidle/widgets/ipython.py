# from pyqode.qt.QtGui import QApplication
import logging
import os


def _logger():
    return logging.getLogger()

from pyqode.qt.QtWidgets import QLabel
from pyqode.qt.QtCore import Qt
from pyqode.core.api import ColorScheme

mem = os.environ['QT_API']
try:
    from IPython.qt.console import styles

    from qidle.preferences import Preferences
    if os.environ['QT_API'] == 'pyqt4':
        os.environ['QT_API'] = 'pyqt'
    from IPython.qt.console.rich_ipython_widget import RichIPythonWidget
    from IPython.qt.inprocess import QtInProcessKernelManager
    os.environ['QT_API'] = mem
except (ImportError, RuntimeError):
    os.environ['QT_API'] = mem
    # IPython not available for the selected QT_API
    class IPythonConsole(QLabel):
        def __init__(self, parent):
            super(IPythonConsole, self).__init__(parent)
            self.setText('IPython not found...')
            self.setAlignment(Qt.AlignCenter)

        #--- duck typing interface
        def apply_preferences(self):
            pass
else:
    class IPythonConsole(RichIPythonWidget):
        def __init__(self, parent):
            super(IPythonConsole, self).__init__(parent)
            self._initialized = False

        def showEvent(self, e):
            if not self._initialized:
                _logger().info('initializing shell')
                kernel_manager = QtInProcessKernelManager()
                kernel_manager.start_kernel()
                kernel_client = kernel_manager.client()
                kernel_client.start_channels()
                self.kernel_manager = kernel_manager
                self.kernel_client = kernel_client
                self._initialized = True
                self.apply_preferences()
                _logger().info('shell initialized')
            super(IPythonConsole, self).showEvent(e)

        def sizeHint(self):
            sh = super(IPythonConsole, self).sizeHint()
            sh.setHeight(200)
            return sh

        def apply_preferences(self):
            prefs = Preferences()
            self.font_family = prefs.appearance.font
            self.font_size = prefs.appearance.font_size
            self.syntax_style = prefs.appearance.color_scheme
            scheme = ColorScheme(self.syntax_style)
            foreground = scheme.formats['normal'].foreground().color()
            background = scheme.background
            if background.lightness() < 128:
                self.style_sheet = styles.default_dark_style_template % dict(
                    bgcolor=background.name(), fgcolor=foreground.name(),
                    select="#444")
            else:
                self.style_sheet = styles.default_light_style_template % dict(
                    bgcolor=background.name(), fgcolor=foreground.name(),
                    select="#ccc")
