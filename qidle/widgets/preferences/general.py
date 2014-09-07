"""
Contains the general settings page.
"""
from qidle.forms.preferences.page_general_ui import Ui_Form
from qidle.widgets.preferences.base import Page


class PageGeneral(Page):
    def __init__(self, parent=None):
        self.ui = Ui_Form()
        super().__init__(self.ui, parent)

    def reset(self):
        pass

    def restore_defaults(self):
        pass

    def apply(self):
        pass