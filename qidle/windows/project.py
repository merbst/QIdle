import logging
import os
from pyqode.qt import QtGui, QtWidgets, QtCore
from pyqode.python.widgets import PyCodeEdit
import sys

from qidle import icons, project
from qidle.dialogs.project_run_config import DlgProjectRunConfig
from qidle.forms import win_prj_ui
from qidle.preferences import Preferences
from qidle.windows.base import WindowBase
from qidle.widgets.fs_context_menu import PyFileSystemContextMenu


def _logger():
    return logging.getLogger(__name__)


class ProjectWindow(WindowBase):
    def __init__(self, app):
        self.ui = win_prj_ui.Ui_MainWindow()
        super(ProjectWindow, self).__init__(self.ui, app)
        self.restore_state()
        self.ui.dockWidgetProgramOutput.hide()
        self.ui.tabWidget.dirty_changed.connect(self._on_dirty_changed)
        self.ui.tabWidget.register_code_edit(PyCodeEdit)
        self.ui.tabWidget.current_changed.connect(
            self._on_current_editor_changed)
        self.ui.tabWidget.last_tab_closed.connect(self._on_last_tab_closed)
        self.ui.fsTree.set_context_menu(PyFileSystemContextMenu())
        self.ui.fsTree.file_deleted.connect(self._on_file_deleted)
        self.ui.fsTree.file_renamed.connect(self._on_file_renamed)
        self.ui.fsTree.file_created.connect(self._on_file_created)
        self.ui.fsTree.ignore_directories('.qidle')

        # Edit menu
        self.addActions(self.ui.menuFile.actions())

        self.ui.actionConfigureRun.triggered.connect(self.configure_run)
        self.ui.actionRun.triggered.connect(self.on_action_run_triggered)
        self.ui.textEditPgmOutput.process_finished.connect(
            self._on_script_finished)
        self.ui.textEditPgmOutput.open_file_requested.connect(
            self._goto_requested)

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
        self.ui.dockWidgetFiles.setWindowIcon(icons.folder)
        self.ui.dockWidgetPyConsole.setWindowIcon(icons.python_interpreter)
        self.apply_preferences(show_panels=False)

        self.dock_manager_right.add_dock_widget(self.ui.dockWidgetFiles)
        self.dock_manager_right.add_dock_widget(
            self.ui.dockWidgetClassExplorer)
        self.dock_manager_bottom.add_dock_widget(
            self.ui.dockWidgetProgramOutput)
        self.dock_manager_bottom.add_dock_widget(self.ui.dockWidgetPyConsole)

        self.ui.classExplorer.set_editor(None)

        self.ui.fsTree.activated.connect(self._on_tv_activated)
        self.ui.fsTree.setHeaderHidden(True)
        for i in range(1, 4):
            self.ui.fsTree.hideColumn(i)

        self._on_current_editor_changed(None)

        self._combo_run_configs = QtWidgets.QComboBox()
        self._combo_run_configs.setToolTip('Choose run configuration')
        self.ui.toolBarRun.insertWidget(self.ui.actionRun,
                                        self._combo_run_configs)
        self._combo_run_configs.activated.connect(
            self._on_run_config_activated)

    def closeEvent(self, ev):
        nb_windows = len(self._open_windows)
        _logger().debug('number of windows: %d', nb_windows)
        if nb_windows != 1 or self.quit_confirmation():
            self.ui.tabWidget.closeEvent(ev)
        if ev.isAccepted():
            self.save_state()
            self._emit_closed()
            super(ProjectWindow, self).closeEvent(ev)

    def restore_state(self):
        prefs = Preferences()
        if prefs.general.restore_scr_window_state:
            self.restoreGeometry(prefs.project_window.geometry)
            self.restoreState(prefs.project_window.state)

    def save_state(self):
        prefs = Preferences()
        prefs.project_window.geometry = self.saveGeometry()
        prefs.project_window.state = self.saveState()

    def open(self, path):
        self.ui.fsTree.set_root_path(path)
        self.app.remember_path(path)
        self.path = path
        self.setWindowTitle('%s [%s] - QIdle %s (Python %s)' % (
            os.path.split(path)[1], path, self.app.version_str,
            '.'.join([str(i) for i in sys.version_info[:3]])))
        meta_dir = os.path.join(path, '.qidle')
        if not os.path.exists(meta_dir):
            os.makedirs(meta_dir)
        self._make_combo_run_configs()

    def _on_run_config_activated(self, index):
        if index == 0:
            self.configure_run()

    def _make_combo_run_configs(self):
        self._combo_run_configs.clear()
        self._combo_run_configs.addItem('Edit configurations...')
        self._combo_run_configs.setItemIcon(0, icons.configure)
        self._combo_run_configs.insertSeparator(1)
        if self.path is None:
            return
        configs = project.get_run_configurations(self.path)
        for cfg in configs:
            i = self._combo_run_configs.count()
            self._combo_run_configs.addItem(cfg['name'])
            self._combo_run_configs.setItemIcon(i, icons.python_interpreter)
        if len(configs):
            self._combo_run_configs.setCurrentIndex(
                self._combo_run_configs.count() - 1)

    def _on_dirty_changed(self, dirty):
        self.ui.actionSave.setEnabled(dirty)

    def save_as(self):
        self.ui.tabWidget.save_current_as()

    def save(self):
        self.ui.tabWidget.save_current()

    def configure_run(self):
        DlgProjectRunConfig.edit_configs(self, self.path)
        self._make_combo_run_configs()

    def run_script(self):
        self.ui.tabWidget.save_all()
        _logger().info('running script')
        self.ui.actionRun.setText('Stop')
        self.ui.actionRun.setIcon(icons.stop)
        configs = project.get_run_configurations(self.path)
        for cfg in configs:
            if cfg['name'] == self._combo_run_configs.currentText():
                break
        _logger().info('run configuration: %r', cfg)
        opts = []
        if len(cfg['interpreter_options']):
            opts += cfg['interpreter_options']
        opts += [cfg['script']]
        if len(cfg['script_parameters']):
            opts += cfg['script_parameters']
        self.ui.textEditPgmOutput.start_process(
            Preferences().cache.get_project_interpreter(self.path), opts,
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
        if self.ui.actionRun.text() == 'Run':
            if Preferences().general.save_before_run:
                self.save()
            self.run_script()
            self.ui.dockWidgetProgramOutput.show()
            self.ui.textEditPgmOutput.setFocus(True)
        elif self.ui.actionRun.text() == 'Stop':
            self.stop_script()

    def _goto_requested(self, path, line):
        pass

    def apply_preferences(self, show_panels=True):
        pass

    def _on_tv_activated(self, index):
        def is_binary_string(path):
            textchars = (bytearray([7, 8, 9, 10, 12, 13, 27]) +
                         bytearray(range(0x20, 0x100)))
            check_if_binary = lambda bytes: bool(
                bytes.translate(None, textchars))
            with open(path, 'rb') as f:
                return check_if_binary(f.read())

        path = self.ui.fsTree.filePath(index)
        if os.path.isfile(path):
            if is_binary_string(path):
                QtWidgets.QDesktopServices.openUrl(QtCore.QUrl(path))
            else:
                self.ui.tabWidget.open_document(path)

    def _on_current_editor_changed(self, new):
        self.ui.classExplorer.set_editor(new)
        self.ui.menuEdit.setEnabled(new is not None)
        self.ui.menuEdit.clear()
        if new:
            self.ui.menuEdit.addActions(new.actions())

    def _on_last_tab_closed(self):
        self._on_current_editor_changed(None)

    def _on_file_deleted(self, path):
        self.ui.tabWidget.close_document(path)

    def _on_file_renamed(self, old_path, new_path):
        self.ui.tabWidget.rename_document(old_path, new_path)

    def _on_file_created(self, path):
        if os.path.isfile(path):
            self.ui.tabWidget.open_document(path)
