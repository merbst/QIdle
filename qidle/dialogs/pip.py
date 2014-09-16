from PyQt4 import QtGui
from pyqode.core.managers import BackendManager
from pyqode.python.backend import server
from qidle.forms.dlg_pip_command_ui import Ui_Dialog
from qidle.system import get_library_zip_path


class DlgPipCommand(QtGui.QDialog):
    """
    Runs a pip command in a backend process, show  an animated gif while the
    command is running and finally display the pip output in a text edit
    when the command returned.

    """
    @classmethod
    def run_command(cls, parent, interpreter, worker_function, package,
                    operation_str):
        dlg = cls(parent, worker_function, package, interpreter,
                  operation_str)
        dlg.exec_()
        return dlg.status == 0

    def __init__(self, parent, worker, package, interpreter, operation_str):
        super(DlgPipCommand, self).__init__(parent)
        self.status = True
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.operation.setText(operation_str)
        self.movie = QtGui.QMovie(':/icons/loader.gif')
        self.ui.movie.setMovie(self.movie)
        self.backend = None
        self._worker = worker
        self._package = package
        self.movie.start()
        self._start_backend(interpreter)

    def _stop_backend(self):
        if self.backend is not None:
            self.backend.stop()
            self.backend = None

    def _start_backend(self, interpreter):
        self._stop_backend()
        self.backend = BackendManager(self)
        self.backend.start(
            server.__file__, interpreter=interpreter,
            args=['-s'] + [get_library_zip_path()])
        self.backend.socket.connected.connect(self._run_command)
        print('backend started')

    def _run_command(self):
        print('connected')
        self.backend.send_request(self._worker, self._package,
                                  on_receive=self._on_command_finished)

    def _on_command_finished(self, status, output):
        self.movie.stop()
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.output.setPlainText(output)
        if status:
            self.ui.operation.setText('Operation succeeded')
        else:
            self.ui.operation.setText('Operation failed')
        self.status = status
