# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/Desktop/QIdle/forms/settings_page_appearance.ui'
#
# Created: Fri Nov 14 18:44:36 2014
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
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.header = QtGui.QLabel(Form)
        self.header.setStyleSheet(_fromUtf8("border-radius: 3px;\n"
"background-color: rgb(161, 161, 161);\n"
"padding: 10px;"))
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName(_fromUtf8("header"))
        self.verticalLayout.addWidget(self.header)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.list_color_schemes = QtGui.QListWidget(Form)
        self.list_color_schemes.setObjectName(_fromUtf8("list_color_schemes"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.list_color_schemes)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.checkbox_whitespaces = QtGui.QCheckBox(Form)
        self.checkbox_whitespaces.setText(_fromUtf8(""))
        self.checkbox_whitespaces.setObjectName(_fromUtf8("checkbox_whitespaces"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.checkbox_whitespaces)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.spinbox_font_size = QtGui.QSpinBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinbox_font_size.sizePolicy().hasHeightForWidth())
        self.spinbox_font_size.setSizePolicy(sizePolicy)
        self.spinbox_font_size.setObjectName(_fromUtf8("spinbox_font_size"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.spinbox_font_size)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.line_edit_font = QtGui.QLineEdit(Form)
        self.line_edit_font.setObjectName(_fromUtf8("line_edit_font"))
        self.horizontalLayout_2.addWidget(self.line_edit_font)
        self.bt_font = QtGui.QToolButton(Form)
        self.bt_font.setObjectName(_fromUtf8("bt_font"))
        self.horizontalLayout_2.addWidget(self.bt_font)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.edit_preview = PyCodeEdit(self.groupBox_2)
        self.edit_preview.setObjectName(_fromUtf8("edit_preview"))
        self.gridLayout.addWidget(self.edit_preview, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.header.setText(_translate("Form", "Configure appearance", None))
        self.label_4.setText(_translate("Form", "Color scheme:", None))
        self.label_2.setText(_translate("Form", "Show whitespaces:", None))
        self.label_3.setText(_translate("Form", "Font size:", None))
        self.label.setText(_translate("Form", "Font:", None))
        self.bt_font.setText(_translate("Form", "...", None))
        self.groupBox_2.setTitle(_translate("Form", "Preview", None))

from pyqode.python.widgets import PyCodeEdit
