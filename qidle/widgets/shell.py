# from PyQt4.QtGui import QApplication
import logging
import os
if os.environ['QT_API'] == 'pyqt4':
    os.environ['QT_API'] = 'pyqt'
from IPython.qt.console.rich_ipython_widget import RichIPythonWidget
from IPython.qt.inprocess import QtInProcessKernelManager


def _logger():
    return logging.getLogger()


class Shell(RichIPythonWidget):
    def __init__(self, parent):
        super(Shell, self).__init__(parent)
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
            _logger().info('shell initialized')
        super(Shell, self).showEvent(e)

    def sizeHint(self):
        sh = super(Shell, self).sizeHint()
        sh.setHeight(200)
        return sh