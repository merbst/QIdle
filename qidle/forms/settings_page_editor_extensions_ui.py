# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/renega_666/Documents/QIdle/forms/settings_page_editor_extensions.ui'
#
# Created: Fri Dec 12 22:19:59 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from pyqode.qt import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(465, 384)
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
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lw_panels = QtWidgets.QListWidget(self.groupBox_2)
        self.lw_panels.setObjectName("lw_panels")
        self.horizontalLayout_2.addWidget(self.lw_panels)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.header.setText(_translate("Form", "Configure editor modes"))
        self.groupBox.setTitle(_translate("Form", "Modes"))
        self.groupBox_2.setTitle(_translate("Form", "Panels"))
