# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/colin/QIdle/forms/win_script.ui'
#
# Created: Thu Sep 25 15:05:02 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(924, 971)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/QIdle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.codeEdit = PyCodeEdit(self.centralwidget)
        self.codeEdit.setObjectName(_fromUtf8("codeEdit"))
        self.gridLayout.addWidget(self.codeEdit, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidgetClassExplorer = QtGui.QDockWidget(MainWindow)
        self.dockWidgetClassExplorer.setObjectName(_fromUtf8("dockWidgetClassExplorer"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.classExplorer = ClassExplorer(self.dockWidgetContents_2)
        self.classExplorer.setObjectName(_fromUtf8("classExplorer"))
        self.classExplorer.headerItem().setText(0, _fromUtf8("1"))
        self.classExplorer.header().setVisible(False)
        self.gridLayout_3.addWidget(self.classExplorer, 0, 0, 1, 1)
        self.dockWidgetClassExplorer.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetClassExplorer)
        self.dockWidgetProgramOutput = QtGui.QDockWidget(MainWindow)
        self.dockWidgetProgramOutput.setObjectName(_fromUtf8("dockWidgetProgramOutput"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.textEditPgmOutput = PyInteractiveConsole(self.dockWidgetContents_3)
        self.textEditPgmOutput.setObjectName(_fromUtf8("textEditPgmOutput"))
        self.gridLayout_4.addWidget(self.textEditPgmOutput, 0, 0, 1, 1)
        self.dockWidgetProgramOutput.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidgetProgramOutput)
        self.dockWidgetShell = QtGui.QDockWidget(MainWindow)
        self.dockWidgetShell.setObjectName(_fromUtf8("dockWidgetShell"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.gridLayout_5 = QtGui.QGridLayout(self.dockWidgetContents_4)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.shell = Shell(self.dockWidgetContents_4)
        self.shell.setObjectName(_fromUtf8("shell"))
        self.gridLayout_5.addWidget(self.shell, 0, 0, 1, 1)
        self.dockWidgetShell.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidgetShell)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 924, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuRecents = QtGui.QMenu(self.menuFile)
        self.menuRecents.setObjectName(_fromUtf8("menuRecents"))
        self.menuRun = QtGui.QMenu(self.menubar)
        self.menuRun.setObjectName(_fromUtf8("menuRun"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuWindows = QtGui.QMenu(self.menubar)
        self.menuWindows.setObjectName(_fromUtf8("menuWindows"))
        self.menuTools = QtGui.QMenu(self.menuWindows)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBarSave = QtGui.QToolBar(MainWindow)
        self.toolBarSave.setObjectName(_fromUtf8("toolBarSave"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarSave)
        self.toolBarRun = QtGui.QToolBar(MainWindow)
        self.toolBarRun.setObjectName(_fromUtf8("toolBarRun"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarRun)
        self.toolBarTools = QtGui.QToolBar(MainWindow)
        self.toolBarTools.setObjectName(_fromUtf8("toolBarTools"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarTools)
        self.actionOpen_file = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-open"))
        self.actionOpen_file.setIcon(icon)
        self.actionOpen_file.setObjectName(_fromUtf8("actionOpen_file"))
        self.actionOpen_directory = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("folder-open"))
        self.actionOpen_directory.setIcon(icon)
        self.actionOpen_directory.setObjectName(_fromUtf8("actionOpen_directory"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("applications-x-python"))
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_as = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-save-as"))
        self.actionSave_as.setIcon(icon)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.actionClose = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("window-close"))
        self.actionClose.setIcon(icon)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionQuit = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("exit"))
        self.actionQuit.setIcon(icon)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionRun = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("media-playback-start"))
        self.actionRun.setIcon(icon)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionConfigureRun = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("system-run"))
        self.actionConfigureRun.setIcon(icon)
        self.actionConfigureRun.setObjectName(_fromUtf8("actionConfigureRun"))
        self.actionConfigure_IDLE = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("preferences-system"))
        self.actionConfigure_IDLE.setIcon(icon)
        self.actionConfigure_IDLE.setObjectName(_fromUtf8("actionConfigure_IDLE"))
        self.actionZoom_height = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("zoom-fit-best"))
        self.actionZoom_height.setIcon(icon)
        self.actionZoom_height.setObjectName(_fromUtf8("actionZoom_height"))
        self.actionAbout_QIdle = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("help-about"))
        self.actionAbout_QIdle.setIcon(icon)
        self.actionAbout_QIdle.setObjectName(_fromUtf8("actionAbout_QIdle"))
        self.actionHelp_content = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("help-contents"))
        self.actionHelp_content.setIcon(icon)
        self.actionHelp_content.setObjectName(_fromUtf8("actionHelp_content"))
        self.actionPython_docs = QtGui.QAction(MainWindow)
        self.actionPython_docs.setObjectName(_fromUtf8("actionPython_docs"))
        self.actionNew_file = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-new"))
        self.actionNew_file.setIcon(icon)
        self.actionNew_file.setObjectName(_fromUtf8("actionNew_file"))
        self.actionNew_project = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("folder-new"))
        self.actionNew_project.setIcon(icon)
        self.actionNew_project.setObjectName(_fromUtf8("actionNew_project"))
        self.menuFile.addAction(self.actionNew_file)
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew_project)
        self.menuFile.addAction(self.actionOpen_directory)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuRecents.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuRun.addAction(self.actionRun)
        self.menuRun.addAction(self.actionConfigureRun)
        self.menuOptions.addAction(self.actionConfigure_IDLE)
        self.menuWindows.addAction(self.actionZoom_height)
        self.menuWindows.addSeparator()
        self.menuWindows.addAction(self.menuTools.menuAction())
        self.menuWindows.addSeparator()
        self.menuHelp.addAction(self.actionAbout_QIdle)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionHelp_content)
        self.menuHelp.addAction(self.actionPython_docs)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBarSave.addAction(self.actionNew_file)
        self.toolBarSave.addAction(self.actionOpen_file)
        self.toolBarSave.addSeparator()
        self.toolBarSave.addAction(self.actionSave)
        self.toolBarSave.addAction(self.actionSave_as)
        self.toolBarRun.addAction(self.actionConfigureRun)
        self.toolBarRun.addAction(self.actionRun)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "QIdle", None))
        self.dockWidgetClassExplorer.setWindowTitle(_translate("MainWindow", "Class explorer", None))
        self.dockWidgetProgramOutput.setWindowTitle(_translate("MainWindow", "Program output", None))
        self.dockWidgetShell.setWindowTitle(_translate("MainWindow", "Shell", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuRecents.setTitle(_translate("MainWindow", "Recents", None))
        self.menuRun.setTitle(_translate("MainWindow", "Run", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Options", None))
        self.menuWindows.setTitle(_translate("MainWindow", "Windows", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.toolBarSave.setWindowTitle(_translate("MainWindow", "File toolbar", None))
        self.toolBarRun.setWindowTitle(_translate("MainWindow", "Run toolbar", None))
        self.toolBarTools.setWindowTitle(_translate("MainWindow", "Tools toolbar", None))
        self.actionOpen_file.setText(_translate("MainWindow", "Open file", None))
        self.actionOpen_directory.setText(_translate("MainWindow", "Open directory", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave_as.setText(_translate("MainWindow", "Save as", None))
        self.actionClose.setText(_translate("MainWindow", "Close window", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionRun.setText(_translate("MainWindow", "Run", None))
        self.actionConfigureRun.setText(_translate("MainWindow", "Configure", None))
        self.actionConfigure_IDLE.setText(_translate("MainWindow", "Configure QIdle", None))
        self.actionZoom_height.setText(_translate("MainWindow", "Zoom height", None))
        self.actionAbout_QIdle.setText(_translate("MainWindow", "About QIdle", None))
        self.actionHelp_content.setText(_translate("MainWindow", "QIdle Help", None))
        self.actionPython_docs.setText(_translate("MainWindow", "Python docs", None))
        self.actionNew_file.setText(_translate("MainWindow", "New file", None))
        self.actionNew_project.setText(_translate("MainWindow", "New project", None))

from qidle.widgets import Shell, ClassExplorer
from pyqode.python.widgets import PyInteractiveConsole, PyCodeEdit
from . import qidle_rc
