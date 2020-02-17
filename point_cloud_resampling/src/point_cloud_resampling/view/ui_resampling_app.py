# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_resampling_app.ui'
#
# Created: Tue Feb 18 08:55:26 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 378)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 250))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../brain/codes/python_packages/PyQt-Image-Viewer/icons/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.source_path = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.source_path.setFont(font)
        self.source_path.setStyleSheet("")
        self.source_path.setObjectName("source_path")
        self.horizontalLayout.addWidget(self.source_path)
        self.open_pushButton = QtGui.QPushButton(self.centralwidget)
        self.open_pushButton.setObjectName("open_pushButton")
        self.horizontalLayout.addWidget(self.open_pushButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.showOriginal_pushButton = QtGui.QPushButton(self.centralwidget)
        self.showOriginal_pushButton.setObjectName("showOriginal_pushButton")
        self.horizontalLayout_2.addWidget(self.showOriginal_pushButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.resamplingLayout = QtGui.QHBoxLayout()
        self.resamplingLayout.setObjectName("resamplingLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.resamplingLayout.addItem(spacerItem2)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.resamplingLayout.addWidget(self.label)
        self.resampling_doubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.resampling_doubleSpinBox.setObjectName("resampling_doubleSpinBox")
        self.resamplingLayout.addWidget(self.resampling_doubleSpinBox)
        self.resample_pushButton = QtGui.QPushButton(self.centralwidget)
        self.resample_pushButton.setObjectName("resample_pushButton")
        self.resamplingLayout.addWidget(self.resample_pushButton)
        self.gridLayout.addLayout(self.resamplingLayout, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.showResampled_pushButton = QtGui.QPushButton(self.centralwidget)
        self.showResampled_pushButton.setObjectName("showResampled_pushButton")
        self.horizontalLayout_4.addWidget(self.showResampled_pushButton)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 36, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 6, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.reset_pushButton = QtGui.QPushButton(self.centralwidget)
        self.reset_pushButton.setObjectName("reset_pushButton")
        self.horizontalLayout_3.addWidget(self.reset_pushButton)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.save = QtGui.QPushButton(self.centralwidget)
        self.save.setObjectName("save")
        self.horizontalLayout_3.addWidget(self.save)
        self.gridLayout.addLayout(self.horizontalLayout_3, 7, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Image Pre-processing", None, QtGui.QApplication.UnicodeUTF8))
        self.source_path.setText(QtGui.QApplication.translate("MainWindow", "Please select the source file", None, QtGui.QApplication.UnicodeUTF8))
        self.open_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.showOriginal_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Show original data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Resampling", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Radius", None, QtGui.QApplication.UnicodeUTF8))
        self.resample_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Resample", None, QtGui.QApplication.UnicodeUTF8))
        self.showResampled_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Show resampled data", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_pushButton.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
