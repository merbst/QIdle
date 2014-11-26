# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/dev/QIdle/forms/settings_page_modes.ui'
#
# Created: Wed Nov 26 13:26:40 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from pyqode.qt import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(481, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QLabel(Form)
        self.header.setStyleSheet("border-radius: 3px;\n"
"background-color: rgb(161, 161, 161);\n"
"padding: 10px;")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.verticalLayout.addWidget(self.header)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lw_modes = QtWidgets.QListWidget(self.groupBox)
        self.lw_modes.setObjectName("lw_modes")
        self.horizontalLayout.addWidget(self.lw_modes)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.header.setText(_translate("Form", "Configure editor modes"))
        self.groupBox.setTitle(_translate("Form", "Installed modes"))
