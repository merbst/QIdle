# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/QIdle/forms/settings_page_interpreters.ui'
#
# Created: Tue Sep 30 12:12:14 2014
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
        Form.resize(594, 487)
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
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.combo_interpreters = QtGui.QComboBox(self.groupBox)
        self.combo_interpreters.setObjectName(_fromUtf8("combo_interpreters"))
        self.horizontalLayout.addWidget(self.combo_interpreters)
        self.bt_cfg = QtGui.QToolButton(self.groupBox)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("system-run"))
        self.bt_cfg.setIcon(icon)
        self.bt_cfg.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.bt_cfg.setArrowType(QtCore.Qt.NoArrow)
        self.bt_cfg.setObjectName(_fromUtf8("bt_cfg"))
        self.horizontalLayout.addWidget(self.bt_cfg)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.table_packages = QtGui.QTableWidget(self.groupBox_2)
        self.table_packages.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_packages.setAlternatingRowColors(True)
        self.table_packages.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table_packages.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_packages.setObjectName(_fromUtf8("table_packages"))
        self.table_packages.setColumnCount(3)
        self.table_packages.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table_packages.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_packages.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_packages.setHorizontalHeaderItem(2, item)
        self.table_packages.horizontalHeader().setCascadingSectionResizes(False)
        self.table_packages.horizontalHeader().setStretchLastSection(True)
        self.table_packages.verticalHeader().setVisible(False)
        self.table_packages.verticalHeader().setCascadingSectionResizes(False)
        self.horizontalLayout_2.addWidget(self.table_packages)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.bt_install_package = QtGui.QToolButton(self.groupBox_2)
        self.bt_install_package.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("list-add"))
        self.bt_install_package.setIcon(icon)
        self.bt_install_package.setObjectName(_fromUtf8("bt_install_package"))
        self.verticalLayout_2.addWidget(self.bt_install_package)
        self.bt_uninstall_package = QtGui.QToolButton(self.groupBox_2)
        self.bt_uninstall_package.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("list-remove"))
        self.bt_uninstall_package.setIcon(icon)
        self.bt_uninstall_package.setObjectName(_fromUtf8("bt_uninstall_package"))
        self.verticalLayout_2.addWidget(self.bt_uninstall_package)
        self.bt_upgrade_package = QtGui.QToolButton(self.groupBox_2)
        self.bt_upgrade_package.setText(_fromUtf8(""))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("up"))
        self.bt_upgrade_package.setIcon(icon)
        self.bt_upgrade_package.setObjectName(_fromUtf8("bt_upgrade_package"))
        self.verticalLayout_2.addWidget(self.bt_upgrade_package)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.widgetInfos = QtGui.QWidget(self.groupBox_2)
        self.widgetInfos.setObjectName(_fromUtf8("widgetInfos"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widgetInfos)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.layout_infos = QtGui.QHBoxLayout()
        self.layout_infos.setContentsMargins(-1, 0, -1, -1)
        self.layout_infos.setObjectName(_fromUtf8("layout_infos"))
        self.lblMovie = QtGui.QLabel(self.widgetInfos)
        self.lblMovie.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMovie.setObjectName(_fromUtf8("lblMovie"))
        self.layout_infos.addWidget(self.lblMovie)
        self.lblInfos = QtGui.QLabel(self.widgetInfos)
        self.lblInfos.setObjectName(_fromUtf8("lblInfos"))
        self.layout_infos.addWidget(self.lblInfos)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.layout_infos.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.layout_infos, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.widgetInfos)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.header.setText(_translate("Form", "Configure python interpreters", None))
        self.groupBox.setTitle(_translate("Form", "Default interpreter", None))
        self.combo_interpreters.setToolTip(_translate("Form", "Choose the default python interpreter", None))
        self.combo_interpreters.setStatusTip(_translate("Form", "Choose the default interpreter that will be used for the first run", None))
        self.bt_cfg.setToolTip(_translate("Form", "Configure  interpreters", None))
        self.bt_cfg.setStatusTip(_translate("Form", "Add/remove interpreters", None))
        self.bt_cfg.setText(_translate("Form", "...", None))
        self.groupBox_2.setTitle(_translate("Form", "Installed packages", None))
        item = self.table_packages.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Package", None))
        item = self.table_packages.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Version", None))
        item = self.table_packages.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Path", None))
        self.bt_install_package.setToolTip(_translate("Form", "Install new packages", None))
        self.bt_install_package.setStatusTip(_translate("Form", "Install new packages (package names should be separated by a space)", None))
        self.bt_uninstall_package.setToolTip(_translate("Form", "Remove package", None))
        self.bt_uninstall_package.setStatusTip(_translate("Form", "Remove the selected package", None))
        self.bt_upgrade_package.setToolTip(_translate("Form", "Upgrade package", None))
        self.bt_upgrade_package.setStatusTip(_translate("Form", "Upgrade the selected package", None))
        self.lblMovie.setText(_translate("Form", "mov", None))
        self.lblInfos.setText(_translate("Form", "Refreshing packages list", None))

from . import qidle_rc
