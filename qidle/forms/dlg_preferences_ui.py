# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/dev/QIdle/forms/dlg_preferences.ui'
#
# Created: Wed Nov 26 13:26:39 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from pyqode.qt import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(933, 539)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Preferences-system.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.categories = QtWidgets.QTreeWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categories.sizePolicy().hasHeightForWidth())
        self.categories.setSizePolicy(sizePolicy)
        self.categories.setObjectName("categories")
        item_0 = QtWidgets.QTreeWidgetItem(self.categories)
        icon = QtGui.QIcon.fromTheme("preferences-system")
        item_0.setIcon(0, icon)
        item_0 = QtWidgets.QTreeWidgetItem(self.categories)
        icon = QtGui.QIcon.fromTheme("applications-graphics")
        item_0.setIcon(0, icon)
        item_0 = QtWidgets.QTreeWidgetItem(self.categories)
        icon = QtGui.QIcon.fromTheme("accessories-text-editor")
        item_0.setIcon(0, icon)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.categories)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/interpreter-sys.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon1)
        self.categories.header().setVisible(False)
        self.horizontalLayout.addWidget(self.categories)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.pages = QtWidgets.QStackedWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy)
        self.pages.setObjectName("pages")
        self.pageNotFound = QtWidgets.QWidget()
        self.pageNotFound.setObjectName("pageNotFound")
        self.gridLayout = QtWidgets.QGridLayout(self.pageNotFound)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.pageNotFound)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pages.addWidget(self.pageNotFound)
        self.horizontalLayout.addWidget(self.pages)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttons = QtWidgets.QDialogButtonBox(Dialog)
        self.buttons.setOrientation(QtCore.Qt.Horizontal)
        self.buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttons.setObjectName("buttons")
        self.verticalLayout.addWidget(self.buttons)

        self.retranslateUi(Dialog)
        self.buttons.accepted.connect(Dialog.accept)
        self.buttons.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Preferences"))
        self.categories.headerItem().setText(0, _translate("Dialog", "item"))
        __sortingEnabled = self.categories.isSortingEnabled()
        self.categories.setSortingEnabled(False)
        self.categories.topLevelItem(0).setText(0, _translate("Dialog", "General"))
        self.categories.topLevelItem(1).setText(0, _translate("Dialog", "Appearance"))
        self.categories.topLevelItem(2).setText(0, _translate("Dialog", "Editor"))
        self.categories.topLevelItem(2).child(0).setText(0, _translate("Dialog", "Modes"))
        self.categories.topLevelItem(2).child(1).setText(0, _translate("Dialog", "Panels"))
        self.categories.topLevelItem(3).setText(0, _translate("Dialog", "Interpreters"))
        self.categories.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Dialog", "This page does not exist yet"))

from . import qidle_rc