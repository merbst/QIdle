# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/QIdle/forms/settings_page_editor.ui'
#
# Created: Tue Sep 30 12:12:14 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(466, 569)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.header = QtGui.QLabel(Form)
        self.header.setStyleSheet(_fromUtf8("border-radius: 3px;\n"
"background-color: rgb(161, 161, 161);\n"
"padding: 10px;"))
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName(_fromUtf8("header"))
        self.verticalLayout.addWidget(self.header)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label)
        self.sb_tab_len = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sb_tab_len.sizePolicy().hasHeightForWidth())
        self.sb_tab_len.setSizePolicy(sizePolicy)
        self.sb_tab_len.setProperty("value", 4)
        self.sb_tab_len.setObjectName(_fromUtf8("sb_tab_len"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.sb_tab_len)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_2)
        self.sb_margin_pos = QtGui.QSpinBox(self.groupBox)
        self.sb_margin_pos.setMaximum(200)
        self.sb_margin_pos.setProperty("value", 120)
        self.sb_margin_pos.setObjectName(_fromUtf8("sb_margin_pos"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.sb_margin_pos)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.cb_caret_cope = QtGui.QCheckBox(self.groupBox)
        self.cb_caret_cope.setText(_fromUtf8(""))
        self.cb_caret_cope.setObjectName(_fromUtf8("cb_caret_cope"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.cb_caret_cope)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.cb_spaces_instead_of_tabs = QtGui.QCheckBox(self.groupBox)
        self.cb_spaces_instead_of_tabs.setText(_fromUtf8(""))
        self.cb_spaces_instead_of_tabs.setObjectName(_fromUtf8("cb_spaces_instead_of_tabs"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.cb_spaces_instead_of_tabs)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.cb_convert_tabs_to_spaces = QtGui.QCheckBox(self.groupBox_3)
        self.cb_convert_tabs_to_spaces.setObjectName(_fromUtf8("cb_convert_tabs_to_spaces"))
        self.verticalLayout_3.addWidget(self.cb_convert_tabs_to_spaces)
        self.cb_clean_trailing = QtGui.QCheckBox(self.groupBox_3)
        self.cb_clean_trailing.setObjectName(_fromUtf8("cb_clean_trailing"))
        self.verticalLayout_3.addWidget(self.cb_clean_trailing)
        self.cb_restore_cursor = QtGui.QCheckBox(self.groupBox_3)
        self.cb_restore_cursor.setObjectName(_fromUtf8("cb_restore_cursor"))
        self.verticalLayout_3.addWidget(self.cb_restore_cursor)
        self.cb_safe_save = QtGui.QCheckBox(self.groupBox_3)
        self.cb_safe_save.setObjectName(_fromUtf8("cb_safe_save"))
        self.verticalLayout_3.addWidget(self.cb_safe_save)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.sb_cc_trigger_len = QtGui.QSpinBox(self.groupBox_2)
        self.sb_cc_trigger_len.setObjectName(_fromUtf8("sb_cc_trigger_len"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.sb_cc_trigger_len)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.cb_cc_tooltips = QtGui.QCheckBox(self.groupBox_2)
        self.cb_cc_tooltips.setText(_fromUtf8(""))
        self.cb_cc_tooltips.setObjectName(_fromUtf8("cb_cc_tooltips"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cb_cc_tooltips)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
        self.cb_cc_case_sensitive = QtGui.QCheckBox(self.groupBox_2)
        self.cb_cc_case_sensitive.setText(_fromUtf8(""))
        self.cb_cc_case_sensitive.setObjectName(_fromUtf8("cb_cc_case_sensitive"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.cb_cc_case_sensitive)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.header.setText(_translate("Form", "Configure editor settings", None))
        self.groupBox.setTitle(_translate("Form", "General", None))
        self.label.setText(_translate("Form", "Tab lenght (nb spaces):", None))
        self.label_2.setText(_translate("Form", "Margin position:", None))
        self.label_4.setText(_translate("Form", "Highlight caret scope:", None))
        self.label_5.setText(_translate("Form", "Use spaces instead of tabs:", None))
        self.groupBox_3.setTitle(_translate("Form", "File manager", None))
        self.cb_convert_tabs_to_spaces.setText(_translate("Form", "Convert tab to spaces", None))
        self.cb_clean_trailing.setText(_translate("Form", "Clean trailing whitespaces", None))
        self.cb_restore_cursor.setText(_translate("Form", "Restore cursor position", None))
        self.cb_safe_save.setText(_translate("Form", "Safe save (save to a temporary file first)", None))
        self.groupBox_2.setTitle(_translate("Form", "Code completion", None))
        self.label_3.setText(_translate("Form", "Trigger length:", None))
        self.label_6.setText(_translate("Form", "Show tooltips:", None))
        self.label_7.setText(_translate("Form", "Case sensitive:", None))

