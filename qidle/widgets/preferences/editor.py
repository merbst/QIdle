"""
Contains the general settings page.
"""
from qidle.forms.settings_page_editor_ui import Ui_Form
from qidle.preferences import Preferences
from qidle.widgets.preferences.base import Page


class PageEditor(Page):
    def __init__(self, parent=None):
        self.ui = Ui_Form()
        super(PageEditor, self).__init__(self.ui, parent)

    def reset(self):
        editor = Preferences().editor
        self.ui.cb_caret_cope.setChecked(editor.highlight_caret_scope)
        self.ui.cb_spaces_instead_of_tabs.setChecked(
            editor.use_spaces_instead_of_tabs)
        self.ui.sb_tab_len.setValue(editor.tab_len)
        self.ui.sb_margin_pos.setValue(editor.margin_pos)
        self.ui.cb_convert_tabs_to_spaces.setChecked(
            editor.convert_tabs_to_spaces)
        self.ui.cb_clean_trailing.setChecked(editor.clean_trailing)
        self.ui.cb_restore_cursor.setChecked(editor.restore_cursor)
        self.ui.cb_safe_save.setChecked(editor.safe_save)
        self.ui.sb_cc_trigger_len.setValue(editor.cc_trigger_len)
        self.ui.cb_cc_tooltips.setChecked(editor.cc_show_tooltips)
        self.ui.cb_cc_case_sensitive.setChecked(editor.cc_case_sensitive)

    def restore_defaults(self):
        editor = Preferences().editor
        editor.cc_case_sensitive = False
        editor.cc_show_tooltips = True
        editor.cc_trigger_len = 1
        editor.clean_trailing = True
        editor.convert_tabs_to_spaces = True
        editor.highlight_caret_scope = False
        editor.margin_pos = 79
        editor.restore_cursor = True
        editor.safe_save = True
        editor.tab_len = 4
        editor.use_spaces_instead_of_tabs = True
        self.reset()

    def apply(self):
        editor = Preferences().editor
        editor.cc_show_tooltips = self.ui.cb_cc_tooltips.isChecked()
        editor.cc_case_sensitive = self.ui.cb_cc_case_sensitive.isChecked()
        editor.cc_trigger_len = self.ui.sb_cc_trigger_len.value()
        editor.clean_trailing = self.ui.cb_clean_trailing.isChecked()
        editor.convert_tabs_to_spaces = \
            self.ui.cb_convert_tabs_to_spaces.isChecked()
        editor.highlight_caret_scope = self.ui.cb_caret_cope.isChecked()
        editor.margin_pos = self.ui.sb_margin_pos.value()
        editor.restore_cursor = self.ui.cb_restore_cursor.isChecked()
        editor.safe_save = self.ui.cb_safe_save.isChecked()
        editor.tab_len = self.ui.sb_tab_len.value()
        editor.use_spaces_instead_of_tabs = \
            self.ui.cb_spaces_instead_of_tabs.isChecked()
