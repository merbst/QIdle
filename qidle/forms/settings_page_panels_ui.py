# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/QIdle/forms/settings_page_panels.ui'
#
# Created: Tue Sep 30 14:51:14 2014
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
        Form.resize(481, 300)
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
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lw_modes = QtGui.QListWidget(self.groupBox)
        self.lw_modes.setObjectName(_fromUtf8("lw_modes"))
        self.horizontalLayout.addWidget(self.lw_modes)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.header.setText(_translate("Form", "Configure editor panels", None))
        self.groupBox.setTitle(_translate("Form", "Installed panels", None))

