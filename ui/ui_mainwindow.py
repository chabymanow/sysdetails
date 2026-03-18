# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1329, 846)
        MainWindow.setMinimumSize(QSize(1200, 700))
        MainWindow.setStyleSheet(u"")
        self.actionCPU_info = QAction(MainWindow)
        self.actionCPU_info.setObjectName(u"actionCPU_info")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSystem_Info = QAction(MainWindow)
        self.actionSystem_Info.setObjectName(u"actionSystem_Info")
        self.actionBasic_Info = QAction(MainWindow)
        self.actionBasic_Info.setObjectName(u"actionBasic_Info")
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName(u"actionLight")
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.actionRunning_Apps = QAction(MainWindow)
        self.actionRunning_Apps.setObjectName(u"actionRunning_Apps")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_9 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.basicPage = QWidget()
        self.basicPage.setObjectName(u"basicPage")
        self.gridLayout_3 = QGridLayout(self.basicPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.basicFrame = QFrame(self.basicPage)
        self.basicFrame.setObjectName(u"basicFrame")
        self.basicFrame.setFrameShape(QFrame.NoFrame)
        self.basicFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.basicFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_2 = QGroupBox(self.basicFrame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.userInfo = QPlainTextEdit(self.groupBox_2)
        self.userInfo.setObjectName(u"userInfo")
        self.userInfo.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.userInfo)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 3, 1, 1)

        self.groupBox_4 = QGroupBox(self.basicFrame)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.discUsageInfo = QPlainTextEdit(self.groupBox_4)
        self.discUsageInfo.setObjectName(u"discUsageInfo")
        self.discUsageInfo.setMinimumSize(QSize(500, 0))
        self.discUsageInfo.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.discUsageInfo)


        self.gridLayout.addWidget(self.groupBox_4, 4, 1, 1, 1)

        self.groupBox = QGroupBox(self.basicFrame)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sysInfo = QPlainTextEdit(self.groupBox)
        self.sysInfo.setObjectName(u"sysInfo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sysInfo.sizePolicy().hasHeightForWidth())
        self.sysInfo.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.sysInfo)


        self.gridLayout.addWidget(self.groupBox, 3, 1, 1, 1)

        self.groupBox_10 = QGroupBox(self.basicFrame)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.networkInfo = QPlainTextEdit(self.groupBox_10)
        self.networkInfo.setObjectName(u"networkInfo")
        self.networkInfo.setReadOnly(True)

        self.verticalLayout_11.addWidget(self.networkInfo)


        self.gridLayout.addWidget(self.groupBox_10, 4, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.basicFrame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.basicPage)
        self.Hardware = QWidget()
        self.Hardware.setObjectName(u"Hardware")
        self.verticalLayout_2 = QVBoxLayout(self.Hardware)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Hardware)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.groupBox_6 = QGroupBox(self.frame)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.CPU_info = QPlainTextEdit(self.groupBox_6)
        self.CPU_info.setObjectName(u"CPU_info")

        self.verticalLayout_7.addWidget(self.CPU_info)

        self.groupBox_5 = QGroupBox(self.groupBox_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.sensorInfo = QPlainTextEdit(self.groupBox_5)
        self.sensorInfo.setObjectName(u"sensorInfo")
        self.sensorInfo.setMinimumSize(QSize(500, 0))
        self.sensorInfo.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.sensorInfo)


        self.verticalLayout_7.addWidget(self.groupBox_5)


        self.gridLayout_6.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.RAMInfo = QPlainTextEdit(self.groupBox_3)
        self.RAMInfo.setObjectName(u"RAMInfo")

        self.verticalLayout_4.addWidget(self.RAMInfo)

        self.groupBox_9 = QGroupBox(self.groupBox_3)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.UptimeInfo = QPlainTextEdit(self.groupBox_9)
        self.UptimeInfo.setObjectName(u"UptimeInfo")

        self.verticalLayout_10.addWidget(self.UptimeInfo)


        self.verticalLayout_4.addWidget(self.groupBox_9)


        self.gridLayout_6.addWidget(self.groupBox_3, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.stackedWidget.addWidget(self.Hardware)
        self.SystemPage = QWidget()
        self.SystemPage.setObjectName(u"SystemPage")
        self.gridLayout_5 = QGridLayout(self.SystemPage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.groupBox_7 = QGroupBox(self.SystemPage)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy2)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.kernelInfo = QPlainTextEdit(self.groupBox_7)
        self.kernelInfo.setObjectName(u"kernelInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.kernelInfo.sizePolicy().hasHeightForWidth())
        self.kernelInfo.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.kernelInfo)


        self.gridLayout_5.addWidget(self.groupBox_7, 0, 1, 1, 1)

        self.kernelRefresh = QPushButton(self.SystemPage)
        self.kernelRefresh.setObjectName(u"kernelRefresh")

        self.gridLayout_5.addWidget(self.kernelRefresh, 1, 1, 1, 1)

        self.groupBox_8 = QGroupBox(self.SystemPage)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.kernelModuleInfo = QPlainTextEdit(self.groupBox_8)
        self.kernelModuleInfo.setObjectName(u"kernelModuleInfo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.kernelModuleInfo.sizePolicy().hasHeightForWidth())
        self.kernelModuleInfo.setSizePolicy(sizePolicy4)

        self.verticalLayout_8.addWidget(self.kernelModuleInfo)


        self.gridLayout_5.addWidget(self.groupBox_8, 3, 0, 1, 2)

        self.stackedWidget.addWidget(self.SystemPage)
        self.runningAppPage = QWidget()
        self.runningAppPage.setObjectName(u"runningAppPage")
        self.gridLayout_4 = QGridLayout(self.runningAppPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_11 = QGroupBox(self.runningAppPage)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setFlat(True)
        self.gridLayout_7 = QGridLayout(self.groupBox_11)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.autoUpdateCheck = QRadioButton(self.groupBox_11)
        self.autoUpdateCheck.setObjectName(u"autoUpdateCheck")

        self.gridLayout_7.addWidget(self.autoUpdateCheck, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.updateRunningProcesses = QPushButton(self.groupBox_11)
        self.updateRunningProcesses.setObjectName(u"updateRunningProcesses")

        self.gridLayout_7.addWidget(self.updateRunningProcesses, 2, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 2, 5, 1, 1)

        self.runningAppInfo = QPlainTextEdit(self.groupBox_11)
        self.runningAppInfo.setObjectName(u"runningAppInfo")
        self.runningAppInfo.setFrameShadow(QFrame.Plain)
        self.runningAppInfo.setReadOnly(True)

        self.gridLayout_7.addWidget(self.runningAppInfo, 3, 0, 1, 6)


        self.gridLayout_4.addWidget(self.groupBox_11, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.runningAppPage)

        self.verticalLayout_9.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1329, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuTheme = QMenu(self.menuSettings)
        self.menuTheme.setObjectName(u"menuTheme")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuInfo.addAction(self.actionBasic_Info)
        self.menuInfo.addAction(self.actionCPU_info)
        self.menuInfo.addAction(self.actionSystem_Info)
        self.menuInfo.addAction(self.actionRunning_Apps)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuSettings.addAction(self.menuTheme.menuAction())
        self.menuTheme.addAction(self.actionLight)
        self.menuTheme.addAction(self.actionDark)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"System Info", None))
        self.actionCPU_info.setText(QCoreApplication.translate("MainWindow", u"Hardware Info", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSystem_Info.setText(QCoreApplication.translate("MainWindow", u"Kernel Info", None))
        self.actionBasic_Info.setText(QCoreApplication.translate("MainWindow", u"Basic Info", None))
        self.actionLight.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.actionRunning_Apps.setText(QCoreApplication.translate("MainWindow", u"Active Processes", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"User Details", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Drives", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"System Details", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Network", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"CPU Details", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Temperatures", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"RAM", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Uptime", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Kernel Info", None))
        self.kernelRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh Kernel Modules", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Kernel modules", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Running Processes", None))
        self.autoUpdateCheck.setText(QCoreApplication.translate("MainWindow", u"Auto Update", None))
        self.updateRunningProcesses.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
    # retranslateUi

