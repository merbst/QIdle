"""
Contains the general settings page.
"""
from qidle.forms.settings_page_general_ui import Ui_Form
from qidle.preferences import Preferences
from qidle.widgets.preferences.base import Page


class PageGeneral(Page):
    def __init__(self, parent=None):
        self.ui = Ui_Form()
        super(PageGeneral, self).__init__(self.ui, parent)

    def reset(self):
        prefs = Preferences()
        self.ui.cb_confirm_exit.setChecked(
            prefs.general.confirm_application_exit)
        self.ui.cb_reopen.setChecked(prefs.general.reopen_last_window)
        self.ui.cb_restore_prev_scrwin_state.setChecked(
            prefs.general.restore_scr_window_state)
        oa = prefs.general.open_scr_action
        if oa == prefs.general.OpenActions.NEW:
            self.ui.rb_open_scr_in_new.setChecked(True)
        elif oa == prefs.general.OpenActions.CURRENT:
            self.ui.rb_open_scr_in_same.setChecked(True)
        elif oa == prefs.general.OpenActions.ASK:
            self.ui.rb_open_scr_ask.setChecked(True)
        self.ui.cb_save_before_run.setChecked(prefs.general.save_before_run)

    def restore_defaults(self):
        prefs = Preferences()
        prefs.general.confirm_application_exit = True
        prefs.general.reopen_last_window = True
        prefs.general.open_scr_action = prefs.general.OpenActions.NEW
        prefs.general.restore_scr_window_state = False
        prefs.general.save_before_run = True
        self.reset()

    def apply(self):
        prefs = Preferences()
        prefs.general.save_before_run = self.ui.cb_save_before_run.isChecked()
        prefs.general.confirm_application_exit = \
            self.ui.cb_confirm_exit.isChecked()
        prefs.general.reopen_last_window = self.ui.cb_reopen.isChecked()
        prefs.general.restore_scr_window_state = \
            self.ui.cb_restore_prev_scrwin_state.isChecked()
        if self.ui.rb_open_scr_in_new.isChecked():
            prefs.general.open_scr_action = prefs.general.OpenActions.NEW
        elif self.ui.rb_open_scr_in_same.isChecked():
            prefs.general.open_scr_action = prefs.general.OpenActions.CURRENT
        else:
            prefs.general.open_scr_action = prefs.general.OpenActions.ASK
