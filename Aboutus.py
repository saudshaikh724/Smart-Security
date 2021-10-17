# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 254)
        MainWindow.setStyleSheet("QLabel{\n"
"    \n"
"    font: 25 10pt \"Umpush\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 20, 191, 31))
        self.label.setStyleSheet("QLabel{\n"
"    \n"
"    \n"
"    \n"
"    font: 18pt \"URW Gothic L\";\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 60, 351, 21))
        self.label_2.setStyleSheet("QLabel{\n"
"    \n"
"    font: 11pt \"URW Gothic L\";\n"
"}")
        self.label_2.setObjectName("label_2")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(0, 10, 211, 231))
        self.toolButton.setStyleSheet("QToolButton{\n"
"    border:none;\n"
"    background:none;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/wallpaper/FR.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(350, 350))
        self.toolButton.setObjectName("toolButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(250, 90, 361, 141))
        self.frame.setStyleSheet("QFrame{\n"
"    border:1px solid rgb(85, 87, 83);\n"
"    \n"
"}\n"
"QLabel{\n"
"    border:none;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(40, 60, 261, 31))
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 40, 311, 31))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 20, 241, 31))
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 91, 31))
        self.label_3.setStyleSheet("QLabel{\n"
"    \n"
"    font: 57 11pt \"Ubuntu\";\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(40, 80, 301, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(40, 100, 301, 31))
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aboutus"))
        self.label.setText(_translate("MainWindow", "SMART SECURITY"))
        self.label_2.setText(_translate("MainWindow", "Written using Python Programming Language."))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_9.setText(_translate("MainWindow", "3.Support Both Manual and Auto Mode"))
        self.label_4.setText(_translate("MainWindow", "2.Trigger Events if face is recognize"))
        self.label_7.setText(_translate("MainWindow", "1.Works on Real time with dual Camera"))
        self.label_3.setText(_translate("MainWindow", "Featuring:"))
        self.label_10.setText(_translate("MainWindow", "4.A Default Monitoring setting is assign to operator ,"))
        self.label_11.setText(_translate("MainWindow", "which can be change further."))

import img
