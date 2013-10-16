# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizer.ui'
#
# Created: Tue Oct  8 23:27:09 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 597)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.animationTab = QtGui.QWidget()
        self.animationTab.setObjectName("animationTab")
        self.tabWidget.addTab(self.animationTab, "")
        self.plotTab = QtGui.QWidget()
        self.plotTab.setObjectName("plotTab")
        self.tabWidget.addTab(self.plotTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 24))
        self.menubar.setObjectName("menubar")
        self.menuSimulation = QtGui.QMenu(self.menubar)
        self.menuSimulation.setObjectName("menuSimulation")
        self.menuQuit = QtGui.QMenu(self.menubar)
        self.menuQuit.setObjectName("menuQuit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPre_calculate = QtGui.QAction(MainWindow)
        self.actionPre_calculate.setObjectName("actionPre_calculate")
        self.actionRun_with_background_calculations = QtGui.QAction(MainWindow)
        self.actionRun_with_background_calculations.setObjectName("actionRun_with_background_calculations")
        self.actionCalculate_and_run = QtGui.QAction(MainWindow)
        self.actionCalculate_and_run.setObjectName("actionCalculate_and_run")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuSimulation.addAction(self.actionPre_calculate)
        self.menuSimulation.addAction(self.actionRun_with_background_calculations)
        self.menuSimulation.addSeparator()
        self.menuSimulation.addAction(self.actionCalculate_and_run)
        self.menuSimulation.addSeparator()
        self.menuSimulation.addAction(self.actionQuit)
        self.menuQuit.addAction(self.actionHelp)
        self.menuQuit.addSeparator()
        self.menuQuit.addAction(self.actionAbout)
        self.menubar.addAction(self.menuSimulation.menuAction())
        self.menubar.addAction(self.menuQuit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Visualizer", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.animationTab), QtGui.QApplication.translate("MainWindow", "Animation", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plotTab), QtGui.QApplication.translate("MainWindow", "Plots", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSimulation.setTitle(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.menuQuit.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPre_calculate.setText(QtGui.QApplication.translate("MainWindow", "Pre-calculate", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun_with_background_calculations.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCalculate_and_run.setText(QtGui.QApplication.translate("MainWindow", "Calculate and run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

