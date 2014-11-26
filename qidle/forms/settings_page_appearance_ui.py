# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/dev/QIdle/forms/settings_page_appearance.ui'
#
# Created: Wed Nov 26 13:26:38 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from pyqode.qt import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(668, 645)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QLabel(Form)
        self.header.setStyleSheet("border-radius: 3px;\n"
"background-color: rgb(161, 161, 161);\n"
"padding: 10px;")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.verticalLayout.addWidget(self.header)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.list_color_schemes = QtWidgets.QListWidget(Form)
        self.list_color_schemes.setObjectName("list_color_schemes")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.list_color_schemes)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.checkbox_whitespaces = QtWidgets.QCheckBox(Form)
        self.checkbox_whitespaces.setText("")
        self.checkbox_whitespaces.setObjectName("checkbox_whitespaces")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkbox_whitespaces)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spinbox_font_size = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinbox_font_size.sizePolicy().hasHeightForWidth())
        self.spinbox_font_size.setSizePolicy(sizePolicy)
        self.spinbox_font_size.setObjectName("spinbox_font_size")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spinbox_font_size)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_edit_font = QtWidgets.QLineEdit(Form)
        self.line_edit_font.setObjectName("line_edit_font")
        self.horizontalLayout_2.addWidget(self.line_edit_font)
        self.bt_font = QtWidgets.QToolButton(Form)
        self.bt_font.setObjectName("bt_font")
        self.horizontalLayout_2.addWidget(self.bt_font)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.edit_preview = PyCodeEdit(self.groupBox_2)
        self.edit_preview.setObjectName("edit_preview")
        self.gridLayout.addWidget(self.edit_preview, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.header.setText(_translate("Form", "Configure appearance"))
        self.label_4.setText(_translate("Form", "Color scheme:"))
        self.label_2.setText(_translate("Form", "Show whitespaces:"))
        self.label_3.setText(_translate("Form", "Font size:"))
        self.label.setText(_translate("Form", "Font:"))
        self.bt_font.setText(_translate("Form", "..."))
        self.groupBox_2.setTitle(_translate("Form", "Preview"))

from pyqode.python.widgets import PyCodeEdit