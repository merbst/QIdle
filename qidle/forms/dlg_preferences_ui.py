# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/Desktop/QIdle/forms/dlg_preferences.ui'
#
# Created: Wed Sep 10 14:01:42 2014
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
        Dialog.resize(933, 539)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.categories = QtGui.QTreeWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categories.sizePolicy().hasHeightForWidth())
        self.categories.setSizePolicy(sizePolicy)
        self.categories.setObjectName(_fromUtf8("categories"))
        item_0 = QtGui.QTreeWidgetItem(self.categories)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("preferences-system"))
        item_0.setIcon(0, icon)
        item_0 = QtGui.QTreeWidgetItem(self.categories)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("applications-graphics"))
        item_0.setIcon(0, icon)
        item_0 = QtGui.QTreeWidgetItem(self.categories)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("text"))
        item_0.setIcon(0, icon)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.categories)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/interpreter-sys.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon)
        self.categories.header().setVisible(False)
        self.horizontalLayout.addWidget(self.categories)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.pages = QtGui.QStackedWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy)
        self.pages.setObjectName(_fromUtf8("pages"))
        self.pageNotFound = QtGui.QWidget()
        self.pageNotFound.setObjectName(_fromUtf8("pageNotFound"))
        self.gridLayout = QtGui.QGridLayout(self.pageNotFound)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.pageNotFound)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pages.addWidget(self.pageNotFound)
        self.horizontalLayout.addWidget(self.pages)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttons = QtGui.QDialogButtonBox(Dialog)
        self.buttons.setOrientation(QtCore.Qt.Horizontal)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Reset|QtGui.QDialogButtonBox.RestoreDefaults)
        self.buttons.setObjectName(_fromUtf8("buttons"))
        self.verticalLayout.addWidget(self.buttons)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttons, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttons, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.categories.headerItem().setText(0, _translate("Dialog", "item", None))
        __sortingEnabled = self.categories.isSortingEnabled()
        self.categories.setSortingEnabled(False)
        self.categories.topLevelItem(0).setText(0, _translate("Dialog", "General", None))
        self.categories.topLevelItem(1).setText(0, _translate("Dialog", "Appearance", None))
        self.categories.topLevelItem(2).setText(0, _translate("Dialog", "Editor", None))
        self.categories.topLevelItem(2).child(0).setText(0, _translate("Dialog", "Modes", None))
        self.categories.topLevelItem(2).child(1).setText(0, _translate("Dialog", "Panels", None))
        self.categories.topLevelItem(3).setText(0, _translate("Dialog", "Interpreters", None))
        self.categories.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Dialog", "This page does not exist yet", None))

from . import qidle_rc
