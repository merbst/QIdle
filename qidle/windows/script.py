import logging
import os
import sys

from pyqode.qt import QtGui, QtWidgets

from pyqode.core.api import TextHelper, ColorScheme
from pyqode.core.modes import RightMarginMode, CodeCompletionMode
from pyqode.core.panels import FoldingPanel
from pyqode.python.backend import server

from qidle import icons
from qidle.dialogs import DlgScriptRunConfig
from qidle.forms import win_script_ui
from qidle.preferences import Preferences
from qidle.system import get_library_zip_path
from qidle.windows.base import WindowBase


def _logger():
    return logging.getLogger(__name__)


class ScriptWindow(WindowBase):
    def __init__(self, app):
        self.ui = win_script_ui.Ui_MainWindow()
        super(ScriptWindow, self).__init__(self.ui, app)
        self.setMinimumWidth(600)
        self.setMinimumHeight(480)
        args = []
        interpreter = Preferences().interpreters.default
        if sys.executable != interpreter:
            args = ['-s'] + [get_library_zip_path()]
        self.ui.codeEdit.backend.start(server.__file__, interpreter, args)
        self.ui.classExplorer.set_editor(self.ui.codeEdit)
        self.restore_state()
        self.ui.dockWidgetProgramOutput.hide()
        self.ui.codeEdit.dirty_changed.connect(self._on_dirty_changed)

        # Edit menu
        mnu = self.ui.codeEdit.get_context_menu()
        self.addActions(self.ui.menuFile.actions())
        self.addActions(mnu.actions())
        self.ui.menuEdit.addActions(self.ui.codeEdit.actions())

        self.ui.actionConfigureRun.triggered.connect(self.configure_run)
        self.ui.actionRun.triggered.connect(self.on_action_run_triggered)
        self.ui.textEditPgmOutput.process_finished.connect(
            self._on_script_finished)
        self.ui.textEditPgmOutput.open_file_requested.connect(
            self._goto_requested)
        mode = self.ui.codeEdit.modes.get('GoToAssignmentsMode')
        mode.out_of_doc.connect(self._goto_requested)

        for a in self.createPopupMenu().actions():
            if a.text() == 'Structure':
                a.setIcon(icons.class_browser)
            if a.text() == 'Python console':
                a.setIcon(icons.python_interpreter)
            if a.text() == 'Program output':
                a.setIcon(QtGui.QIcon.fromTheme(
                    'media-playback-start',
                    QtGui.QIcon(':/icons/media-playback-start.png')))
        self.ui.dockWidgetClassExplorer.setWindowIcon(icons.class_browser)
        self.ui.dockWidgetProgramOutput.setWindowIcon(icons.run)
        self.ui.dockWidgetPyConsole.setWindowIcon(icons.python_interpreter)
        self.apply_preferences(show_panels=False)

        self.dock_manager_right.add_dock_widget(
            self.ui.dockWidgetClassExplorer)
        self.dock_manager_bottom.add_dock_widget(
            self.ui.dockWidgetProgramOutput)
        self.dock_manager_bottom.add_dock_widget(self.ui.dockWidgetPyConsole)

    def _perform_close_event(self, ev):
        if self.ui.codeEdit.dirty:
            mbox = QtWidgets.QMessageBox(self)
            mbox.setText("The document has been modified.")
            mbox.setInformativeText("Do you want to save your changes?")
            mbox.setStandardButtons(
                QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard |
                QtWidgets.QMessageBox.Cancel)
            mbox.setIcon(QtWidgets.QMessageBox.Warning)
            mbox.setDefaultButton(QtWidgets.QMessageBox.Save)
            ret = mbox.exec_()
            ev.accept()
            # cancel may come from the mbox or from the save file dialog
            if ret == QtWidgets.QMessageBox.Cancel or (
                    ret == QtWidgets.QMessageBox.Save and not self.save()):
                ev.ignore()

    def closeEvent(self, ev):
        nb_windows = len(self._open_windows)
        _logger().debug('number of windows: %d', nb_windows)
        quit = True
        if nb_windows == 1:
            quit = self.quit_confirmation()
        if quit:
            self._perform_close_event(ev)
        else:
            ev.ignore()
        if ev.isAccepted():
            self.ui.codeEdit.modes.clear()
            self.ui.codeEdit.panels.clear()
            self.ui.codeEdit.file.close()
            self.ui.codeEdit.backend.stop()
            self.save_state()
            self._emit_closed()
            super(ScriptWindow, self).closeEvent(ev)

    def restore_state(self):
        prefs = Preferences()
        if prefs.general.restore_scr_window_state:
            self.restoreGeometry(prefs.script_window.geometry)
            self.restoreState(prefs.script_window.state)

    def save_state(self):
        prefs = Preferences()
        prefs.script_window.geometry = self.saveGeometry()
        prefs.script_window.state = self.saveState()

    def new(self):
        base_title = 'Untitled'
        counter = 0
        for w in self.app.windows:
            if w.path and base_title in w.path:
                counter += 1
        app_title = ' - QIdle %s (Python %s)' % (
            self.app.version_str, '.'.join(
                [str(i) for i in sys.version_info[:3]]))
        suffix = ' %s' % counter if counter else ''
        title = base_title + suffix + app_title
        self.setWindowTitle(title)
        self._title = title
        self.path = base_title
        self._on_dirty_changed(False)
        # disabled till save as
        self.ui.actionRun.setDisabled(True)
        self.ui.actionConfigureRun.setDisabled(True)
        _logger().debug('new file created')
        self.ui.codeEdit.show()
        self.ui.codeEdit.panels.refresh()

    def open(self, path):
        self._title = '%s [%s] - QIdle %s (Python %s)' % (
            os.path.split(path)[1], path, self.app.version_str,
            '.'.join([str(i) for i in sys.version_info[:3]]))
        self.path = path
        self.ui.codeEdit.file.open(path)
        self.setWindowTitle(self._title)
        self._on_dirty_changed(False)
        self.app.remember_path(path)
        _logger().debug('file opened: %s' % path)

    def _on_dirty_changed(self, dirty):
        # adds a star to the title to mark dirty files.
        title = '* %s' % self._title if dirty else self._title
        self.setWindowTitle(title)
        self.ui.actionSave.setEnabled(dirty and os.path.exists(self.path))
        self.app.update_windows_menu()

    def save_as(self):
        path, filter = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Save file as', filter='Python files (*.py)',
            directory=self.path)
        if path:
            if os.path.splitext(path)[1] == '':
                path += '.py'
            _logger().info('save as: %s' % path)
            self.ui.codeEdit.file.save(path)
            self._title = '%s [%s] - QIdle %s (Python %s)' % (
                os.path.split(path)[1], path, self.app.version_str,
                '.'.join([str(i) for i in sys.version_info[:3]]))
            self.setWindowTitle(self._title)
            if self.path == 'Untitled':
                self.ui.actionRun.setEnabled(True)
                self.ui.actionConfigureRun.setEnabled(True)
            self.path = path
            self._on_dirty_changed(False)
            self.app.remember_path(path)
            return True
        return False

    def save(self, ignore_os_errors=False):
        _logger().info('save file: %s' % self.path)
        if self.path == 'Untitled':
            return self.save_as()
        else:
            self.app.remember_path(self.ui.codeEdit.file.path)
            try:
                self.ui.codeEdit.file.save()
            except OSError as e:
                if not ignore_os_errors:
                    QtWidgets.QMessageBox.warning(
                        self, 'Failed to save file',
                        'Failed to save file.\n\n%s' % e)
                    return False
            return True


    def configure_run(self):
        path = self.ui.codeEdit.file.path
        DlgScriptRunConfig.edit_config(self, path)
        _logger().info('run configuration edited')

    def run_script(self):
        _logger().info('running script')
        self.ui.actionRun.setText('Stop')
        self.ui.actionRun.setIcon(icons.stop)
        path = self.ui.codeEdit.file.path
        cfg = Preferences().cache.get_run_config_for_file(path)
        _logger().info('run configuration: %r', cfg)
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

    def _on_script_finished(self):
        _logger().info('script finished')
        self.ui.actionRun.setText('Run')
        self.ui.actionRun.setIcon(icons.run)

    def stop_script(self):
        _logger().info('stopping script')
        self.ui.actionRun.setText('Run')
        self.ui.actionRun.setIcon(icons.run)
        self.ui.textEditPgmOutput.stop_process()

    def on_action_run_triggered(self):
        if 'Run' in self.ui.actionRun.text():
            if Preferences().general.save_before_run:
                self.save(ignore_os_errors=True)
            self.run_script()
            self.ui.dockWidgetProgramOutput.show()
            self.ui.textEditPgmOutput.setFocus(True)
        elif 'Stop' in self.ui.actionRun.text():
            self.stop_script()

    def _goto_requested(self, obj, line=0):
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
            window = self
            widget = self.ui.codeEdit
        else:
            window = self.app.create_script_window(path)
            widget = window.ui.codeEdit
        self.app.activate_window(window)
        self.app.qapp.processEvents()
        TextHelper(widget).goto_line(line, col)
        widget.setFocus(True)

    def apply_preferences(self, show_panels=True):
        _logger().info('applying preferences on editor: %s' %
                       self.ui.codeEdit.file.path)
        prefs = Preferences()
        # appearance
        self.ui.codeEdit.font_name = prefs.appearance.font
        self.ui.codeEdit.font_size = prefs.appearance.font_size
        self.ui.codeEdit.show_whitespaces = prefs.appearance.show_whitespaces
        scheme = ColorScheme(prefs.appearance.color_scheme)
        self.ui.codeEdit.syntax_highlighter.color_scheme = scheme
        self.ui.textEditPgmOutput.apply_color_scheme(scheme)
        # editor settings
        self.ui.codeEdit.panels.get(FoldingPanel).highlight_caret_scope = \
            prefs.editor.highlight_caret_scope
        self.ui.codeEdit.use_spaces_instead_of_tabs = \
            prefs.editor.use_spaces_instead_of_tabs
        self.ui.codeEdit.modes.get(RightMarginMode).position = \
            prefs.editor.margin_pos
        self.ui.codeEdit.tab_length = prefs.editor.tab_len
        self.ui.codeEdit.file.replace_tabs_by_spaces = \
            prefs.editor.convert_tabs_to_spaces
        self.ui.codeEdit.file.clean_trailing_whitespaces = \
            prefs.editor.clean_trailing
        self.ui.codeEdit.file.fold_imports = prefs.editor.fold_imports
        self.ui.codeEdit.file.fold_docstrings = prefs.editor.fold_docstrings
        self.ui.codeEdit.file.restore_cursor = prefs.editor.restore_cursor
        self.ui.codeEdit.file.safe_save = prefs.editor.safe_save
        mode = self.ui.codeEdit.modes.get(CodeCompletionMode)
        mode.trigger_length = prefs.editor.cc_trigger_len
        mode.show_tooltips = prefs.editor.cc_show_tooltips
        mode.case_sensitive = prefs.editor.cc_case_sensitive

        self.ui.codeEdit.setCenterOnScroll(prefs.editor.center_on_scroll)

        # modes
        for m in self.ui.codeEdit.modes:
            if m.name in prefs.editor.modes:
                m.enabled = prefs.editor.modes[m.name]
            else:
                m.enabled = True

        # panels
        for m in self.ui.codeEdit.panels:
            if m.name in prefs.editor.panels:
                m.enabled = prefs.editor.panels[m.name]
            else:
                m.enabled = True
            if m.name in ['EncodingPanel', 'QuickDocPanel',
                          'SearchAndReplacePanel']:
                m.setVisible(False)
            elif show_panels:
                m.setVisible(m.enabled)

    def setFocus(self, reason=None):
        _logger().debug('setFocus: %r', reason)
        if reason:
            self.ui.codeEdit.setFocus(reason)
        else:
            self.ui.codeEdit.setFocus()