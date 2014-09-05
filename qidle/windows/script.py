import os
import sys

from PyQt4 import QtGui
from pyqode.core.api import TextHelper
from pyqode.python.backend import server

from qidle import version
from qidle.dialogs import ScripConfigDialog
from qidle.forms import win_script_ui
from qidle.settings import Settings
from qidle.windows.base import WindowBase


class ScripWindow(WindowBase):
    def __init__(self, app):
        self.ui = win_script_ui.Ui_MainWindow()
        super().__init__(self.ui, app)
        self.ui.codeEdit.backend.start(
            server.__file__, sys.executable)
        self.ui.classExplorer.set_editor(self.ui.codeEdit)
        self.ui.dockWidgetClassExplorer.hide()
        self.ui.dockWidgetShell.hide()
        self.restore_state()
        self.ui.dockWidgetProgramOutput.hide()
        # no need for this panel, we have the class explorer tree which is more
        # convenient.
        try:
            self.ui.codeEdit.panels.remove('SymbolBrowserPanel')
        except KeyError:
            pass  # panel not installed
        self.menu_recents.open_requested.connect(self.app.create_script_window)
        self.ui.codeEdit.dirty_changed.connect(self._on_dirty_changed)

        # Edit menu
        mnu = self.ui.codeEdit.get_context_menu()
        self.addActions(self.ui.menuFile.actions())
        self.addActions(mnu.actions())
        self.ui.menuEdit.addActions(mnu.actions())

        self.ui.actionConfigureRun.triggered.connect(self.configure_run)
        self.ui.actionRun.triggered.connect(self.on_action_run_triggered)
        self.ui.textEditPgmOutput.process_finished.connect(self.stop_script)
        self.ui.textEditPgmOutput.open_file_requested.connect(
            self._open_requested)
        mode = self.ui.codeEdit.modes.get('GoToAssignmentsMode')
        mode.out_of_doc.connect(self._open_requested)

        for a in self.createPopupMenu().actions():
            if a.text() == 'Class explorer':
                a.setIcon(QtGui.QIcon(':/icons/view-tree.png'))
                self.ui.toolBarTools.addAction(a)
            if a.text() == 'Shell':
                a.setIcon(QtGui.QIcon.fromTheme(
                    'terminal',
                    QtGui.QIcon(':/icons/terminal.png')))
                self.ui.toolBarTools.addAction(a)
            if a.text() == 'Program output':
                a.setIcon(QtGui.QIcon.fromTheme(
                    'media-playback-start',
                    QtGui.QIcon(':/icons/media-playback-start.png')))

    def closeEvent(self, ev):
        if self.ui.codeEdit.dirty:
            mbox = QtGui.QMessageBox(self)
            mbox.setText("The document has been modified.")
            mbox.setInformativeText("Do you want to save your changes?")
            mbox.setStandardButtons(
                QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard |
                QtGui.QMessageBox.Cancel)
            mbox.setIcon(QtGui.QMessageBox.Warning)
            mbox.setDefaultButton(QtGui.QMessageBox.Save)
            ret = mbox.exec_()
            if ret == QtGui.QMessageBox.Cancel:
                ev.ignore()
            else:
                if ret == QtGui.QMessageBox.Save:
                    if self.save():
                        ev.accept()
                    else:
                        ev.ignore()
                else:
                    ev.accept()
        super().closeEvent(ev)
        if ev.isAccepted():
            self.ui.codeEdit.modes.clear()
            self.ui.codeEdit.panels.clear()
            self.ui.codeEdit.file.close()
            self.ui.codeEdit.backend.stop()
            self.save_state()

    def restore_state(self):
        pass
        # self.restoreGeometry(Settings().script_window_geometry)
        # self.restoreState(Settings().script_window_state)

    def save_state(self):
        pass

    def new(self):
        base_title = 'Untitled'
        counter = 0
        for w in self.app.windows:
            if w.path and base_title in w.path:
                counter += 1
        app_title = ' - QIdle %s' % version
        suffix = ' %s' % counter if counter else ''
        title = base_title + suffix + app_title
        self.setWindowTitle(title)
        self._title = self.path = title
        self._on_dirty_changed(False)
        # disabled till save as
        self.ui.actionRun.setDisabled(True)
        self.ui.actionConfigureRun.setDisabled(True)

    def open(self, path):
        self.ui.codeEdit.file.open(path)
        self._title = '%s [%s] - QIdle %s' % (
            os.path.split(path)[1], path, version)
        self.setWindowTitle(self._title)
        self._on_dirty_changed(False)
        self.path = path
        self.app.remember_path(path)

    def _on_dirty_changed(self, dirty):
        title = '* %s' % self._title if dirty else self._title
        self.setWindowTitle(title)
        self.ui.actionSave.setEnabled(dirty and os.path.exists(self.path))
        self.app.update_windows_menu()

    def save_as(self):
        path = QtGui.QFileDialog.getSaveFileName(
            self, 'Save file as', filter='Python files (*.py)')
        if path:
            if os.path.splitext(path)[1] == '':
                path += '.py'
            self.ui.codeEdit.file.save(path)
            self._title = '%s [%s] - QIdle %s' % (
                os.path.split(path)[1], path, version)
            self.setWindowTitle(self._title)
            if self.path == 'Untitled':
                self.ui.actionRun.setEnabled(True)
                self.ui.actionConfigureRun.setEnabled(True)
            self.path = path
            self._on_dirty_changed(False)
            self.app.remember_path(path)
            return True
        return False

    def save(self):
        if self.path == 'Untitled':
            return self.save_as()
        else:
            self.ui.codeEdit.file.save()
            self.app.remember_path(self.ui.codeEdit.file.path)
            return True

    def configure_run(self):
        path = self.ui.codeEdit.file.path
        ScripConfigDialog.edit_config(self, path)

    def run_script(self):
        self.ui.actionRun.setText('Stop')
        self.ui.actionRun.setIcon(QtGui.QIcon.fromTheme(
            'media-playback-stop'))
        path = self.ui.codeEdit.file.path
        cfg = Settings().get_run_config_for_file(path)
        opts = []
        if len(cfg['interpreter_options']):
            opts += cfg['interpreter_options']
        opts += [cfg['script']]
        if len(cfg['script_parameters']):
            opts += cfg['script_parameters']
        self.ui.textEditPgmOutput.start_process(
            cfg['interpreter'], opts,
            cwd=cfg['working_dir'],
            env=cfg['env_vars'])

    def stop_script(self):
        self.ui.actionRun.setText('Run')
        self.ui.actionRun.setIcon(QtGui.QIcon.fromTheme(
            'media-playback-start'))
        self.ui.textEditPgmOutput.stop_process()

    def on_action_run_triggered(self):
        if self.ui.actionRun.text() == 'Run':
            self.save()
            self.run_script()
            self.ui.dockWidgetProgramOutput.show()
            self.ui.textEditPgmOutput.setFocus(True)
        elif self.ui.actionRun.text() == 'Stop':
            self.stop_script()

    def _open_requested(self, obj, line=0):
        if isinstance(obj, str):
            path = obj
            line = line
            col = 0
        else:
            # assignment
            path = obj.module_path
            line = obj.line
            col = obj.column
        if path == self.ui.codeEdit.file.path:
            widget = self.ui.codeEdit
        else:
            window = self.app.create_script_window(path)
            widget = window.ui.codeEdit
        TextHelper(widget).goto_line(line, col)
        widget.setFocus(True)
