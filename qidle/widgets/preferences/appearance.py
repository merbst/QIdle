"""
Contains the general settings page.
"""
from PyQt4 import QtGui
from pyqode.core.api.syntax_highlighter import PYGMENTS_STYLES, ColorScheme
from pyqode.python.backend import server
from qidle.forms.settings_page_appearance_ui import Ui_Form
from qidle.preferences import Preferences
from qidle.widgets.preferences.base import Page


class PageAppearance(Page):
    demo = r'''@decorator(param=1)
def f(x):
    """ Syntax Highlighting Demo
        @param x Parameter"""
    s = ("Test", 2+3, {'a': 'b'}, x)   # Comment
    print s[0].lower()

class Foo:
    def __init__(self):
        byte_string = 'newline:\n also newline:\x0a'
        text_string = u"Cyrillic Я is \u042f."
        self.makeSense(whatever=1)

    def makeSense(self, whatever):
        self.sense = whatever

x = len('abc')
print(f.__doc__)
'''

    def __init__(self, parent=None):
        self.ui = Ui_Form()
        super(PageAppearance, self).__init__(self.ui, parent)
        self.ui.edit_preview.setPlainText(self.demo)
        self.ui.edit_preview.backend.start(
            server.__file__, Preferences().interpreters.default)
        self.ui.bt_font.clicked.connect(self._choose_font)
        self.ui.spinbox_font_size.valueChanged.connect(
            self._on_font_size_changed)
        self.ui.checkbox_whitespaces.stateChanged.connect(
            self._on_show_whitespaces_changed)
        self.ui.list_color_schemes.currentItemChanged.connect(
            self._on_color_scheme_changed)

    def _on_color_scheme_changed(self, item):
        self.ui.edit_preview.syntax_highlighter.color_scheme = ColorScheme(
            item.text())

    def _on_show_whitespaces_changed(self, state):
        self.ui.edit_preview.show_whitespaces = state
        self.ui.edit_preview.rehighlight()

    def _on_font_size_changed(self):
        self.ui.edit_preview.font_size = self.ui.spinbox_font_size.value()

    def _choose_font(self):
        font, ok = QtGui.QFontDialog.getFont(
            self.ui.edit_preview.font(), self)
        self.ui.line_edit_font.setText(font.family())
        self.ui.edit_preview.font_name = font.family()

    def reset(self):
        appearance = Preferences().appearance
        self.ui.line_edit_font.setText(appearance.font)
        self.ui.spinbox_font_size.setValue(appearance.font_size)
        self.ui.checkbox_whitespaces.setChecked(appearance.show_whitespaces)
        self.ui.list_color_schemes.clear()
        current_index = 0
        for style in PYGMENTS_STYLES:
            self.ui.list_color_schemes.addItem(style)
            if style == appearance.color_scheme:
                current_index = self.ui.list_color_schemes.count() - 1
        self.ui.list_color_schemes.setCurrentRow(current_index)

    def restore_defaults(self):
        appearance = Preferences().appearance
        appearance.font = 'Source Code Pro'
        appearance.font_size = 10
        appearance.show_whitespaces = False
        appearance.color_scheme = 'qt'
        self.reset()

    def apply(self):
        appearance = Preferences().appearance
        appearance.font = self.ui.line_edit_font.text()
        appearance.font_size = self.ui.spinbox_font_size.value()
        appearance.color_scheme = \
            self.ui.list_color_schemes.currentItem().text()
        appearance.show_whitespaces = self.ui.checkbox_whitespaces.isChecked()
