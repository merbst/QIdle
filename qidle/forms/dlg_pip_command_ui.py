# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/QIdle/forms/dlg_pip_command.ui'
#
# Created: Tue Sep 16 15:54:17 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(356, 176)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.operation = QtGui.QLabel(Dialog)
        self.operation.setObjectName(_fromUtf8("operation"))
        self.verticalLayout.addWidget(self.operation)
        self.stackedWidget = QtGui.QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout_2 = QtGui.QGridLayout(self.page)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.movie = QtGui.QLabel(self.page)
        self.movie.setAlignment(QtCore.Qt.AlignCenter)
        self.movie.setObjectName(_fromUtf8("movie"))
        self.gridLayout_2.addWidget(self.movie, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout = QtGui.QGridLayout(self.page_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.output = QtGui.QPlainTextEdit(self.page_2)
        self.output.setObjectName(_fromUtf8("output"))
        self.gridLayout.addWidget(self.output, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.operation.setText(_translate("Dialog", "Operation", None))
        self.movie.setText(_translate("Dialog", "TextLabel", None))

