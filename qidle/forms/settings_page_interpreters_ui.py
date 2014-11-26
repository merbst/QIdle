# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/dev/QIdle/forms/settings_page_interpreters.ui'
#
# Created: Wed Nov 26 13:26:40 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from pyqode.qt import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(594, 487)
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
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.combo_interpreters = QtWidgets.QComboBox(self.groupBox)
        self.combo_interpreters.setObjectName("combo_interpreters")
        self.horizontalLayout.addWidget(self.combo_interpreters)
        self.bt_cfg = QtWidgets.QToolButton(self.groupBox)
        icon = QtGui.QIcon.fromTheme("system-run")
        self.bt_cfg.setIcon(icon)
        self.bt_cfg.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.bt_cfg.setArrowType(QtCore.Qt.NoArrow)
        self.bt_cfg.setObjectName("bt_cfg")
        self.horizontalLayout.addWidget(self.bt_cfg)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.table_packages = QtWidgets.QTableWidget(self.groupBox_2)
        self.table_packages.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_packages.setAlternatingRowColors(True)
        self.table_packages.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_packages.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_packages.setObjectName("table_packages")
        self.table_packages.setColumnCount(3)
        self.table_packages.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_packages.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_packages.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_packages.setHorizontalHeaderItem(2, item)
        self.table_packages.horizontalHeader().setCascadingSectionResizes(False)
        self.table_packages.horizontalHeader().setStretchLastSection(True)
        self.table_packages.verticalHeader().setVisible(False)
        self.table_packages.verticalHeader().setCascadingSectionResizes(False)
        self.horizontalLayout_2.addWidget(self.table_packages)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bt_install_package = QtWidgets.QToolButton(self.groupBox_2)
        self.bt_install_package.setText("")
        icon = QtGui.QIcon.fromTheme("list-add")
        self.bt_install_package.setIcon(icon)
        self.bt_install_package.setObjectName("bt_install_package")
        self.verticalLayout_2.addWidget(self.bt_install_package)
        self.bt_uninstall_package = QtWidgets.QToolButton(self.groupBox_2)
        self.bt_uninstall_package.setText("")
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.bt_uninstall_package.setIcon(icon)
        self.bt_uninstall_package.setObjectName("bt_uninstall_package")
        self.verticalLayout_2.addWidget(self.bt_uninstall_package)
        self.bt_upgrade_package = QtWidgets.QToolButton(self.groupBox_2)
        self.bt_upgrade_package.setText("")
        icon = QtGui.QIcon.fromTheme("up")
        self.bt_upgrade_package.setIcon(icon)
        self.bt_upgrade_package.setObjectName("bt_upgrade_package")
        self.verticalLayout_2.addWidget(self.bt_upgrade_package)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.widgetInfos = QtWidgets.QWidget(self.groupBox_2)
        self.widgetInfos.setObjectName("widgetInfos")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widgetInfos)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.layout_infos = QtWidgets.QHBoxLayout()
        self.layout_infos.setContentsMargins(-1, 0, -1, -1)
        self.layout_infos.setObjectName("layout_infos")
        self.lblMovie = QtWidgets.QLabel(self.widgetInfos)
        self.lblMovie.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMovie.setObjectName("lblMovie")
        self.layout_infos.addWidget(self.lblMovie)
        self.lblInfos = QtWidgets.QLabel(self.widgetInfos)
        self.lblInfos.setObjectName("lblInfos")
        self.layout_infos.addWidget(self.lblInfos)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_infos.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.layout_infos, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.widgetInfos)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.header.setText(_translate("Form", "Configure python interpreters"))
        self.groupBox.setTitle(_translate("Form", "Default interpreter"))
        self.combo_interpreters.setToolTip(_translate("Form", "Choose the default python interpreter"))
        self.combo_interpreters.setStatusTip(_translate("Form", "Choose the default interpreter that will be used for the first run"))
        self.bt_cfg.setToolTip(_translate("Form", "Configure  interpreters"))
        self.bt_cfg.setStatusTip(_translate("Form", "Add/remove interpreters"))
        self.bt_cfg.setText(_translate("Form", "..."))
        self.groupBox_2.setTitle(_translate("Form", "Installed packages"))
        item = self.table_packages.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Package"))
        item = self.table_packages.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Version"))
        item = self.table_packages.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Path"))
        self.bt_install_package.setToolTip(_translate("Form", "Install new packages"))
        self.bt_install_package.setStatusTip(_translate("Form", "Install new packages (package names should be separated by a space)"))
        self.bt_uninstall_package.setToolTip(_translate("Form", "Remove package"))
        self.bt_uninstall_package.setStatusTip(_translate("Form", "Remove the selected package"))
        self.bt_upgrade_package.setToolTip(_translate("Form", "Upgrade package"))
        self.bt_upgrade_package.setStatusTip(_translate("Form", "Upgrade the selected package"))
        self.lblMovie.setText(_translate("Form", "mov"))
        self.lblInfos.setText(_translate("Form", "Refreshing packages list"))

from . import qidle_rc