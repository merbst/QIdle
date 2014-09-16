"""
Contains the general settings page.
"""
from qidle.forms.settings_page_interpreters_ui import Ui_Form
from qidle.widgets.preferences.base import Page


class PageAppearance(Page):
    def __init__(self, parent=None):
        self.ui = Ui_Form()
        super(PageAppearance, self).__init__(self.ui, parent)

    def reset(self):
        pass

    def restore_defaults(self):
        pass

    def apply(self):
        pass