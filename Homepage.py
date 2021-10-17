# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import *

class Ui_Homepage(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setStyleSheet("*{\n"
"    \n"
"    \n"
"    \n"
"    font: 17pt \"URW Gothic L\";\n"
"    background:url(:/background/wallpaper/homepage.jpg);\n"
"}\n"
"QPushButton{\n"
"    border:none;\n"
"    background:transparent;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border: 1px solid blue;\n"
"}\n"
"QLabel{\n"
"    background:transparent;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_monitor = QtWidgets.QPushButton(self.centralwidget)
        self.btn_monitor.setGeometry(QtCore.QRect(590, 210, 201, 211))
        self.btn_monitor.setStyleSheet("QPushButton:hover{\n"
"    border:6px solid white;\n"
"    border-radius:85px;\n"
"}\n"
"")
        self.btn_monitor.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/wallpaper/monitor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_monitor.setIcon(icon)
        self.btn_monitor.setIconSize(QtCore.QSize(220, 220))
        self.btn_monitor.setObjectName("btn_monitor")
        self.btn_inform = QtWidgets.QPushButton(self.centralwidget)
        self.btn_inform.setGeometry(QtCore.QRect(270, 240, 221, 161))
        self.btn_inform.setStyleSheet("QPushButton:hover{\n"
"    border:6px solid white;\n"
"    border-radius:50px;\n"
"}\n"
"")
        self.btn_inform.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/wallpaper/infom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_inform.setIcon(icon1)
        self.btn_inform.setIconSize(QtCore.QSize(220, 220))
        self.btn_inform.setObjectName("btn_inform")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 430, 91, 31))
        self.label.setObjectName("label")
        self.btn_blockacess = QtWidgets.QPushButton(self.centralwidget)
        self.btn_blockacess.setGeometry(QtCore.QRect(20, 230, 191, 181))
        self.btn_blockacess.setStyleSheet("QPushButton:hover{\n"
"    border:6px solid white;\n"
"    border-radius:85px;\n"
"}\n"
"")
        self.btn_blockacess.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/wallpaper/block_user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_blockacess.setIcon(icon2)
        self.btn_blockacess.setIconSize(QtCore.QSize(220, 220))
        self.btn_blockacess.setObjectName("btn_blockacess")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 420, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 420, 151, 31))
        self.label_3.setObjectName("label_3")
        self.btn_signout = QtWidgets.QPushButton(self.centralwidget)
        self.btn_signout.setGeometry(QtCore.QRect(1090, 620, 231, 51))
        self.btn_signout.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    border:1px solid red;    \n"
"border-radius:15px;\n"
"    \n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:white;\n"
"    border-radius:15px;\n"
"    background:red;\n"
"}")
        self.btn_signout.setObjectName("btn_signout")
        self.btn_sndmail = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sndmail.setGeometry(QtCore.QRect(890, 250, 191, 151))
        self.btn_sndmail.setStyleSheet("QPushButton:hover{\n"
"    border:9px solid white;\n"
"    border-radius:15px;\n"
"}\n"
"")
        self.btn_sndmail.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/wallpaper/gmail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_sndmail.setIcon(icon3)
        self.btn_sndmail.setIconSize(QtCore.QSize(220, 200))
        self.btn_sndmail.setObjectName("btn_sndmail")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(930, 420, 111, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, -10, 1321, 91))
        self.label_6.setStyleSheet("QLabel{\n"
"    color:white;\n"
"    font-size:50px;\n"
"}")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.btn_userinfo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_userinfo.setGeometry(QtCore.QRect(1200, 10, 61, 61))
        self.btn_userinfo.setStyleSheet("QPushButton:hover{\n"
"    border:4px solid white;\n"
"    border-radius: 30px;\n"
"}\n"
"")
        self.btn_userinfo.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/wallpaper/user_profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_userinfo.setIcon(icon4)
        self.btn_userinfo.setIconSize(QtCore.QSize(70, 70))
        self.btn_userinfo.setObjectName("btn_userinfo")
        self.btn_about = QtWidgets.QPushButton(self.centralwidget)
        self.btn_about.setGeometry(QtCore.QRect(1280, 10, 61, 61))
        self.btn_about.setStyleSheet("QPushButton:hover{\n"
"    border:4px solid white;\n"
"    border-radius: 30px;\n"
"}\n"
"")
        self.btn_about.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/wallpaper/aboutus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_about.setIcon(icon5)
        self.btn_about.setIconSize(QtCore.QSize(60, 70))
        self.btn_about.setObjectName("btn_about")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1200, 420, 111, 31))
        self.label_7.setObjectName("label_7")
        self.btn_settings = QtWidgets.QPushButton(self.centralwidget)
        self.btn_settings.setGeometry(QtCore.QRect(1170, 240, 171, 171))
        self.btn_settings.setStyleSheet("QPushButton:hover{\n"
"    border:9px solid white;\n"
"    border-radius:50px;\n"
"}\n"
"")
        self.btn_settings.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/wallpaper/Apple_Settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_settings.setIcon(icon6)
        self.btn_settings.setIconSize(QtCore.QSize(168, 168))
        self.btn_settings.setObjectName("btn_settings")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_signout.clicked.connect(self.quit)

    def quit(self):
        qmsgBox = QMessageBox()
        qmsgBox.move(((qmsgBox.width()) // 2 + 60), ((qmsgBox.height()) // 2 - 50))
        qmsgBox.setStyleSheet(
                    'QMessageBox {background-color: #2b5b84; color: white;}\nQLabel{color: white;}\nQPushButton{color: white; font-size: 16px; background-color: #1d1d1d; border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: #2b5b84;}')

        buttonReply = QMessageBox.question(qmsgBox, 'Log out', "Do you want to Logout?", QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
                self.flag = 0
        if buttonReply == QMessageBox.No:
                self.flag = 1


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Homepage"))
        self.label.setText(_translate("MainWindow", "Monitor"))
        self.label_2.setText(_translate("MainWindow", "Inform"))
        self.label_3.setText(_translate("MainWindow", "Block Acess"))
        self.btn_signout.setText(_translate("MainWindow", "Log out"))
        self.label_5.setText(_translate("MainWindow", "Send Mail"))
        self.label_6.setText(_translate("MainWindow", "sᴍᴀʀᴛ sᴇᴄᴜʀɪᴛʏ sʏsᴛᴇᴍ"))
        self.label_7.setText(_translate("MainWindow", "Settings"))

import img
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Homepage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
