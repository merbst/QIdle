# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/Desktop/QIdle/forms/preferences/page_general.ui'
#
# Created: Sun Sep  7 18:17:52 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(714, 544)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_5 = QtGui.QGroupBox(Form)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.groupBox = QtGui.QGroupBox(self.groupBox_5)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.cb_reopen = QtGui.QCheckBox(self.groupBox)
        self.cb_reopen.setChecked(True)
        self.cb_reopen.setObjectName(_fromUtf8("cb_reopen"))
        self.verticalLayout_3.addWidget(self.cb_reopen)
        self.cb_confirm_exit = QtGui.QCheckBox(self.groupBox)
        self.cb_confirm_exit.setChecked(True)
        self.cb_confirm_exit.setObjectName(_fromUtf8("cb_confirm_exit"))
        self.verticalLayout_3.addWidget(self.cb_confirm_exit)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_5)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.rb_open_scr_in_new = QtGui.QRadioButton(self.groupBox_2)
        self.rb_open_scr_in_new.setChecked(True)
        self.rb_open_scr_in_new.setObjectName(_fromUtf8("rb_open_scr_in_new"))
        self.verticalLayout_4.addWidget(self.rb_open_scr_in_new)
        self.rb_open_scr_in_same = QtGui.QRadioButton(self.groupBox_2)
        self.rb_open_scr_in_same.setChecked(False)
        self.rb_open_scr_in_same.setObjectName(_fromUtf8("rb_open_scr_in_same"))
        self.verticalLayout_4.addWidget(self.rb_open_scr_in_same)
        self.cb_restore_prev_scrwin_state = QtGui.QCheckBox(self.groupBox_2)
        self.cb_restore_prev_scrwin_state.setObjectName(_fromUtf8("cb_restore_prev_scrwin_state"))
        self.verticalLayout_4.addWidget(self.cb_restore_prev_scrwin_state)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_5)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.rb_open_proj_in_new = QtGui.QRadioButton(self.groupBox_3)
        self.rb_open_proj_in_new.setChecked(True)
        self.rb_open_proj_in_new.setObjectName(_fromUtf8("rb_open_proj_in_new"))
        self.verticalLayout_5.addWidget(self.rb_open_proj_in_new)
        self.rb_open_proj_in_same = QtGui.QRadioButton(self.groupBox_3)
        self.rb_open_proj_in_same.setObjectName(_fromUtf8("rb_open_proj_in_same"))
        self.verticalLayout_5.addWidget(self.rb_open_proj_in_same)
        self.cb_restore_prev_projwin_state = QtGui.QCheckBox(self.groupBox_3)
        self.cb_restore_prev_projwin_state.setChecked(True)
        self.cb_restore_prev_projwin_state.setObjectName(_fromUtf8("cb_restore_prev_projwin_state"))
        self.verticalLayout_5.addWidget(self.cb_restore_prev_projwin_state)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_5)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.cb_save_on_focus_lost = QtGui.QCheckBox(self.groupBox_4)
        self.cb_save_on_focus_lost.setChecked(True)
        self.cb_save_on_focus_lost.setObjectName(_fromUtf8("cb_save_on_focus_lost"))
        self.verticalLayout_6.addWidget(self.cb_save_on_focus_lost)
        self.cb_save_before_run = QtGui.QCheckBox(self.groupBox_4)
        self.cb_save_before_run.setChecked(True)
        self.cb_save_before_run.setObjectName(_fromUtf8("cb_save_before_run"))
        self.verticalLayout_6.addWidget(self.cb_save_before_run)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.gridLayout.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox_5.setTitle(_translate("Form", "General", None))
        self.groupBox.setTitle(_translate("Form", "Startup/Shutdown", None))
        self.cb_reopen.setText(_translate("Form", "Reopen last window (project or script) on startup", None))
        self.cb_confirm_exit.setText(_translate("Form", "Confirm application exit ", None))
        self.groupBox_2.setTitle(_translate("Form", "Script opening", None))
        self.rb_open_scr_in_new.setText(_translate("Form", "Open script in a new window", None))
        self.rb_open_scr_in_same.setText(_translate("Form", "Open script in the same window (replace current script)", None))
        self.cb_restore_prev_scrwin_state.setText(_translate("Form", "Restore state of previous window", None))
        self.groupBox_3.setTitle(_translate("Form", "Project opening", None))
        self.rb_open_proj_in_new.setText(_translate("Form", "Open project in new window", None))
        self.rb_open_proj_in_same.setText(_translate("Form", "Open project in the same window (replace current project)", None))
        self.cb_restore_prev_projwin_state.setText(_translate("Form", "Restore state of previous window", None))
        self.groupBox_4.setTitle(_translate("Form", "Save", None))
        self.cb_save_on_focus_lost.setText(_translate("Form", "Save editors when window loose focus", None))
        self.cb_save_before_run.setText(_translate("Form", "Save editors before run", None))

