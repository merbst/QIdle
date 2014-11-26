# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/dev/QIdle/forms/dlg_create_virtualenv.ui'
#
# Created: Wed Nov 26 13:26:39 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from pyqode.qt import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(404, 185)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/interpreter-venv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineedit_name = QtWidgets.QLineEdit(Dialog)
        self.lineedit_name.setObjectName("lineedit_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineedit_name)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.dir_picker = FilePicker(Dialog)
        self.dir_picker.setObjectName("dir_picker")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dir_picker)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.combo_interpreters = QtWidgets.QComboBox(Dialog)
        self.combo_interpreters.setObjectName("combo_interpreters")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.combo_interpreters)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_full_path = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_full_path.setFont(font)
        self.label_full_path.setObjectName("label_full_path")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_full_path)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.check_box_site_packages = QtWidgets.QCheckBox(Dialog)
        self.check_box_site_packages.setObjectName("check_box_site_packages")
        self.gridLayout.addWidget(self.check_box_site_packages, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Create virtual environment"))
        self.label.setText(_translate("Dialog", "Name:"))
        self.label_2.setText(_translate("Dialog", "Directory:"))
        self.label_3.setText(_translate("Dialog", "Base interpreter:"))
        self.label_4.setText(_translate("Dialog", "Fullpath:"))
        self.label_full_path.setText(_translate("Dialog", "path"))
        self.check_box_site_packages.setText(_translate("Dialog", "Inherit global site-packages"))

from qidle.widgets.picker import FilePicker
from . import qidle_rc