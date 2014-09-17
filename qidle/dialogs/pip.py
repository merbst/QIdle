from PyQt4 import QtGui
from pyqode.core.api.client import _ServerProcess
from pyqode.core.managers import BackendManager
from pyqode.python.backend import server
from qidle.forms.dlg_pip_command_ui import Ui_Dialog
from qidle.system import get_library_zip_path, LINUX, \
    get_authentication_program


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
        self.ui.buttonBox.button(self.ui.buttonBox.Ok).setDisabled(True)

    def _stop_backend(self):
        if self.backend is not None:
            self.backend.stop()
            self.backend = None

    def _need_root_perms(self, interpreter):
        if LINUX and not interpreter.startswith('/home'):
            return True
        return False

    def _start_backend(self, interpreter):
        self._stop_backend()
        self.backend = BackendManager(self)
        if self._need_root_perms(interpreter):
            # self.backend.start()
            process = _ServerProcess(self.parent())
            self.backend.socket._process = process
            server_script = server.__file__.replace('.pyc', '.py')
            port = self.backend.socket.pick_free_port()
            self.backend.socket._port = port
            cmd = '%s "%s %s %s --syspath %s"' % (
                get_authentication_program(), interpreter, server_script,
                str(port), get_library_zip_path())
            process.started.connect(self.backend.socket._on_process_started)
            process.start(cmd)
        else:
            self.backend.start(
                server.__file__, interpreter=interpreter,
                args=['-s'] + [get_library_zip_path()])
        self.backend.socket.connected.connect(self._run_command)

    def _run_command(self):
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
        self.ui.buttonBox.button(self.ui.buttonBox.Ok).setEnabled(True)
        self.backend.stop()
