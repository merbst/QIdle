# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/Desktop/QIdle/forms/widget_run_cfg.ui'
#
# Created: Sun Sep  7 17:49:47 2014
#      by: PyQt4 UI code generator 4.11.1
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
        Form.resize(558, 381)
        self.formLayout = QtGui.QFormLayout(Form)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.pickerScript = FilePicker(Form)
        self.pickerScript.setObjectName(_fromUtf8("pickerScript"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.pickerScript)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditScriptParams = QtGui.QLineEdit(Form)
        self.lineEditScriptParams.setObjectName(_fromUtf8("lineEditScriptParams"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditScriptParams)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.comboBoxInterpreter = QtGui.QComboBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxInterpreter.sizePolicy().hasHeightForWidth())
        self.comboBoxInterpreter.setSizePolicy(sizePolicy)
        self.comboBoxInterpreter.setObjectName(_fromUtf8("comboBoxInterpreter"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBoxInterpreter)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEdidInterpreterOpts = QtGui.QLineEdit(Form)
        self.lineEdidInterpreterOpts.setObjectName(_fromUtf8("lineEdidInterpreterOpts"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdidInterpreterOpts)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_5)
        self.pickerWorkingDir = FilePicker(Form)
        self.pickerWorkingDir.setObjectName(_fromUtf8("pickerWorkingDir"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.pickerWorkingDir)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tableWidgetEnvVars = QtGui.QTableWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableWidgetEnvVars.sizePolicy().hasHeightForWidth())
        self.tableWidgetEnvVars.setSizePolicy(sizePolicy)
        self.tableWidgetEnvVars.setAlternatingRowColors(False)
        self.tableWidgetEnvVars.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetEnvVars.setRowCount(0)
        self.tableWidgetEnvVars.setObjectName(_fromUtf8("tableWidgetEnvVars"))
        self.tableWidgetEnvVars.setColumnCount(2)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetEnvVars.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetEnvVars.setHorizontalHeaderItem(1, item)
        self.tableWidgetEnvVars.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetEnvVars.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetEnvVars.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.tableWidgetEnvVars)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButtonAdd = QtGui.QPushButton(Form)
        self.pushButtonAdd.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("list-add"))
        self.pushButtonAdd.setIcon(icon)
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.verticalLayout.addWidget(self.pushButtonAdd)
        self.pushButtonRemove = QtGui.QPushButton(Form)
        self.pushButtonRemove.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("list-remove"))
        self.pushButtonRemove.setIcon(icon)
        self.pushButtonRemove.setObjectName(_fromUtf8("pushButtonRemove"))
        self.verticalLayout.addWidget(self.pushButtonRemove)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.formLayout.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Script:", None))
        self.label_2.setText(_translate("Form", "Script parameters:", None))
        self.label_3.setText(_translate("Form", "Interpreter:", None))
        self.label_4.setText(_translate("Form", "Interpreter options:", None))
        self.label_5.setText(_translate("Form", "Working directory:", None))
        self.label_6.setText(_translate("Form", "Environment variables", None))
        item = self.tableWidgetEnvVars.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name", None))
        item = self.tableWidgetEnvVars.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Value", None))

from qidle.widgets.utils import FilePicker
