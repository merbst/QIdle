# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/QIdle/forms/dlg_create_virtualenv.ui'
#
# Created: Tue Sep 16 14:52:28 2014
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
        Dialog.resize(404, 185)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/interpreter-venv.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineedit_name = QtGui.QLineEdit(Dialog)
        self.lineedit_name.setObjectName(_fromUtf8("lineedit_name"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineedit_name)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.dir_picker = FilePicker(Dialog)
        self.dir_picker.setObjectName(_fromUtf8("dir_picker"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.dir_picker)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.combo_interpreters = QtGui.QComboBox(Dialog)
        self.combo_interpreters.setObjectName(_fromUtf8("combo_interpreters"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.combo_interpreters)
        self.label_4 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_full_path = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_full_path.setFont(font)
        self.label_full_path.setObjectName(_fromUtf8("label_full_path"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_full_path)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.check_box_site_packages = QtGui.QCheckBox(Dialog)
        self.check_box_site_packages.setObjectName(_fromUtf8("check_box_site_packages"))
        self.gridLayout.addWidget(self.check_box_site_packages, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create virtual environment", None))
        self.label.setText(_translate("Dialog", "Name:", None))
        self.label_2.setText(_translate("Dialog", "Directory:", None))
        self.label_3.setText(_translate("Dialog", "Base interpreter:", None))
        self.label_4.setText(_translate("Dialog", "Fullpath:", None))
        self.label_full_path.setText(_translate("Dialog", "path", None))
        self.check_box_site_packages.setText(_translate("Dialog", "Inherit global site-packages", None))

from qidle.widgets.picker import FilePicker
from . import qidle_rc
