# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blochGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1258, 856)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.combo_input1 = QtWidgets.QComboBox(self.centralwidget)
        self.combo_input1.setEnabled(False)
        self.combo_input1.setMinimumSize(QtCore.QSize(200, 30))
        self.combo_input1.setMaximumSize(QtCore.QSize(400, 100))
        self.combo_input1.setAcceptDrops(False)
        self.combo_input1.setIconSize(QtCore.QSize(20, 20))
        self.combo_input1.setObjectName("combo_input1")
        self.combo_input1.addItem("")
        self.combo_input1.addItem("")
        self.combo_input1.addItem("")
        self.combo_input1.addItem("")
        self.combo_input1.addItem("")
        self.verticalLayout_5.addWidget(self.combo_input1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 500))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.img1_updated = ImageView(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img1_updated.sizePolicy().hasHeightForWidth())
        self.img1_updated.setSizePolicy(sizePolicy)
        self.img1_updated.setMinimumSize(QtCore.QSize(0, 0))
        self.img1_updated.setObjectName("img1_updated")
        self.gridLayout.addWidget(self.img1_updated, 1, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.load_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load_btn.setMaximumSize(QtCore.QSize(400, 100))
        self.load_btn.setObjectName("load_btn")
        self.verticalLayout_6.addWidget(self.load_btn)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 500))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.img1_original = ImageView(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img1_original.sizePolicy().hasHeightForWidth())
        self.img1_original.setSizePolicy(sizePolicy)
        self.img1_original.setMinimumSize(QtCore.QSize(0, 0))
        self.img1_original.setObjectName("img1_original")
        self.gridLayout_2.addWidget(self.img1_original, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_img1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_img1.setFont(font)
        self.label_img1.setStyleSheet("")
        self.label_img1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_img1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_img1.setObjectName("label_img1")
        self.gridLayout_5.addWidget(self.label_img1, 0, 0, 1, 1)
        self.generatebutton = QtWidgets.QPushButton(self.centralwidget)
        self.generatebutton.setObjectName("generatebutton")
        self.gridLayout_5.addWidget(self.generatebutton, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.nonUniWidget = PlotWidget(self.groupBox_3)
        self.nonUniWidget.setMinimumSize(QtCore.QSize(700, 0))
        self.nonUniWidget.setMaximumSize(QtCore.QSize(16777215, 500))
        self.nonUniWidget.setObjectName("nonUniWidget")
        self.gridLayout_6.addWidget(self.nonUniWidget, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 1, 0, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 1, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_5.setMaximumSize(QtCore.QSize(300, 16777215))
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.fSlider = QtWidgets.QSlider(self.groupBox_5)
        self.fSlider.setMaximumSize(QtCore.QSize(300, 16777215))
        self.fSlider.setMaximum(6)
        self.fSlider.setOrientation(QtCore.Qt.Horizontal)
        self.fSlider.setObjectName("fSlider")
        self.horizontalLayout_2.addWidget(self.fSlider)
        self.fLabel = QtWidgets.QLabel(self.groupBox_5)
        self.fLabel.setObjectName("fLabel")
        self.horizontalLayout_2.addWidget(self.fLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.t1Slider = QtWidgets.QSlider(self.groupBox_5)
        self.t1Slider.setMaximumSize(QtCore.QSize(300, 16777215))
        self.t1Slider.setMaximum(10)
        self.t1Slider.setOrientation(QtCore.Qt.Horizontal)
        self.t1Slider.setObjectName("t1Slider")
        self.horizontalLayout_3.addWidget(self.t1Slider)
        self.t1Label = QtWidgets.QLabel(self.groupBox_5)
        self.t1Label.setObjectName("t1Label")
        self.horizontalLayout_3.addWidget(self.t1Label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.t2Slider = QtWidgets.QSlider(self.groupBox_5)
        self.t2Slider.setMaximumSize(QtCore.QSize(300, 16777215))
        self.t2Slider.setMaximum(10)
        self.t2Slider.setOrientation(QtCore.Qt.Horizontal)
        self.t2Slider.setObjectName("t2Slider")
        self.horizontalLayout_4.addWidget(self.t2Slider)
        self.t2Label = QtWidgets.QLabel(self.groupBox_5)
        self.t2Label.setObjectName("t2Label")
        self.horizontalLayout_4.addWidget(self.t2Label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout_7.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.gridLayout_8.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_bloch = QtWidgets.QLabel(self.frame)
        self.label_bloch.setMaximumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_bloch.setFont(font)
        self.label_bloch.setStyleSheet("")
        self.label_bloch.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_bloch.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_bloch.setObjectName("label_bloch")
        self.verticalLayout.addWidget(self.label_bloch)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout_8.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.blochWidget = PlotWidget(self.frame)
        self.blochWidget.setMinimumSize(QtCore.QSize(800, 500))
        self.blochWidget.setObjectName("blochWidget")
        self.gridLayout_8.addWidget(self.blochWidget, 1, 1, 2, 1)
        self.horizontalLayout_6.addWidget(self.frame)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.gridLayout_9.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1258, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.combo_input1.setItemText(0, _translate("MainWindow", "Choose FT Component"))
        self.combo_input1.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.combo_input1.setItemText(2, _translate("MainWindow", "Phase"))
        self.combo_input1.setItemText(3, _translate("MainWindow", "Real"))
        self.combo_input1.setItemText(4, _translate("MainWindow", "Imaginary"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Updated Image"))
        self.load_btn.setText(_translate("MainWindow", "Load Image"))
        self.groupBox.setTitle(_translate("MainWindow", "Original Image"))
        self.label_img1.setText(_translate("MainWindow", "Non-Uniform Bo"))
        self.generatebutton.setText(_translate("MainWindow", "Generate"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Parameters"))
        self.label_6.setText(_translate("MainWindow", "F"))
        self.fLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "T1"))
        self.t1Label.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "T2"))
        self.t2Label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "Simulate"))
        self.label_bloch.setText(_translate("MainWindow", "Bloch Equation Simulation"))
from pyqtgraph import ImageView, PlotWidget