# from PyQt4.QtGui import QApplication
import os
if os.environ['QT_API'] == 'pyqt4':
    os.environ['QT_API'] = 'pyqt'
from IPython.qt.console.rich_ipython_widget import RichIPythonWidget
from IPython.qt.inprocess import QtInProcessKernelManager


class Shell(RichIPythonWidget):
    def __init__(self, parent):
        super().__init__(parent)
        kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel()
        # kernel = kernel_manager.kernel
        kernel_client = kernel_manager.client()
        kernel_client.start_channels()
        self.kernel_manager = kernel_manager
        self.kernel_client = kernel_client

    def sizeHint(self):
        sh = super().sizeHint()
        sh.setHeight(200)
        return sh