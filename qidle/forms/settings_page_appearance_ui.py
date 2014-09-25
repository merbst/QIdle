# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/QIdle/forms/settings_page_appearance.ui'
#
# Created: Thu Sep 25 13:48:12 2014
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
        Form.resize(668, 645)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.checkbox_whitespaces = QtGui.QCheckBox(self.groupBox)
        self.checkbox_whitespaces.setText(_fromUtf8(""))
        self.checkbox_whitespaces.setObjectName(_fromUtf8("checkbox_whitespaces"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.checkbox_whitespaces)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.spinbox_font_size = QtGui.QSpinBox(self.groupBox)
        self.spinbox_font_size.setObjectName(_fromUtf8("spinbox_font_size"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinbox_font_size)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.line_edit_font = QtGui.QLineEdit(self.groupBox)
        self.line_edit_font.setObjectName(_fromUtf8("line_edit_font"))
        self.horizontalLayout_2.addWidget(self.line_edit_font)
        self.bt_font = QtGui.QToolButton(self.groupBox)
        self.bt_font.setObjectName(_fromUtf8("bt_font"))
        self.horizontalLayout_2.addWidget(self.bt_font)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.list_color_schemes = QtGui.QListWidget(self.groupBox)
        self.list_color_schemes.setObjectName(_fromUtf8("list_color_schemes"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.list_color_schemes)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.edit_preview = PyCodeEdit(Form)
        self.edit_preview.setObjectName(_fromUtf8("edit_preview"))
        self.gridLayout.addWidget(self.edit_preview, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Appearance", None))
        self.label.setText(_translate("Form", "Font:", None))
        self.label_2.setText(_translate("Form", "Show whitespaces:", None))
        self.label_3.setText(_translate("Form", "Font size:", None))
        self.bt_font.setText(_translate("Form", "...", None))
        self.label_4.setText(_translate("Form", "Color scheme:", None))
        self.groupBox_2.setTitle(_translate("Form", "Preview", None))

from pyqode.python.widgets import PyCodeEdit
