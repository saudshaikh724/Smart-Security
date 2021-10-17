# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtWidgets import QMessageBox
import pygame


class Ui_Login(object):
    flag = 1
    user = None
    def clear(self):
        self.lineEdit_uname.setText('')
        self.lineEdit_pass.setText('')

    def Login(self):
        username = self.lineEdit_uname.text()
        password = self.lineEdit_pass.text()
        connection = pymysql.connect('localhost', 'root', 'rootpass', 'project')
        if username == "" and password == "":
            self.sound(1)
            self.qmsg('Error !!! Check Entries Again .Make Sure No Filed Is Empty.', 1)
        else:

            cursor = connection.cursor()
            sql = "Select * from signup where uname='%s' and pwd='%s'" % (username, password)
            cursor.execute(sql)
            result = cursor.fetchall()
            if int(len(result)) <= 0:
                self.sound(1)
                self.qmsg('No Account With That Username And Password. Please Provide a valid Username and Password to Continue.', 1)
            else:
                self.sound(0)
                self.qmsg('Successfully Login', 0)
                self.flag = 0
                self.user = username
                self.clear()

    def db(self,UNAME):
        THRESOLD = 50
        MODEL = 'hog'
        RESETCOUNTER = 30
        AUTOMAIL = 10
        SCALED = 1
        DISTORT = 1

        connection = pymysql.connect('localhost', 'root', 'rootpass', 'project')
        cursor = connection.cursor()
        select_query = "select uname from settings where uname = '%s'"%(UNAME)
        cursor.execute(select_query)
        row = cursor.fetchone()
        if row[0]!=UNAME:
            #insert
            insert_query = "insert into settings(thresold,model,resetcounter,automail,scaled,distort,uname) values(%d,'%s',%d,%d,%d,%d,'%s')" \
                           % (THRESOLD, MODEL, RESETCOUNTER, AUTOMAIL, SCALED, DISTORT, UNAME)
            cursor.execute(insert_query)
            connection.commit()
        connection.close()

    def qmsg(self, msg, check):
        qmsgBox = QMessageBox()
        qmsgBox.move(((qmsgBox.width()) // 2 + 60), ((qmsgBox.height()) // 2 - 50))
        qmsgBox.setStyleSheet(
            'QMessageBox {background-color: #2b5b84; color: white;}\nQLabel{color: white;}\nQPushButton{color: white; font-size: 16px; background-color: #1d1d1d; border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: #2b5b84;}')
        if check == 0:
            QMessageBox.information(qmsgBox, 'Success', msg)

        else:
            QMessageBox.critical(qmsgBox, 'Failed', msg)

    def sound(self, check):

        if check == 0:
            pygame.mixer.init()
            pygame.mixer.music.load('Sound/login.mp3')
            pygame.mixer.music.play(0)

        else:
            pygame.mixer.init()
            pygame.mixer.music.load('Sound/error.mp3')
            pygame.mixer.music.play(0)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setStyleSheet("*{\n"
"    \n"
"    font: 22pt \"URW Gothic L\";\n"
"    background:url(:/background/wallpaper/background_purple.jpg);\n"
"}\n"
"QLineEdit{\n"
"font-size: 22px;\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:white;\n"
"    border-bottom: 1px solid #717072;\n"
"     padding-bottom: 15px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border-bottom:1px solid rgb(238, 238, 236);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(440, 100, 501, 541))
        self.frame.setStyleSheet("QFrame{\n"
"    \n"
"    border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 470, 191, 20))
        self.label_2.setStyleSheet("QLabel{\n"
"    color:white;\n"
"    font-size:18px;\n"
"    background:transparent;\n"
"    border:none;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(210, 40, 91, 41))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"    \n"
"    \n"
"    font: 32px;\n"
"    \n"
"    \n"
"    \n"
"    \n"
"    color:white;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.lineEdit_uname = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_uname.setGeometry(QtCore.QRect(50, 170, 401, 51))
        self.lineEdit_uname.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_uname.setObjectName("lineEdit_uname")
        self.lineEdit_pass = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_pass.setGeometry(QtCore.QRect(50, 240, 401, 51))
        self.lineEdit_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.btn_login = QtWidgets.QPushButton(self.frame)
        self.btn_login.setGeometry(QtCore.QRect(60, 330, 381, 51))
        self.btn_login.setStyleSheet("QPushButton{\n"
"    background:rgb(85, 87, 83);\n"
"    font-size:19px;\n"
"    color:white;\n"
"    border: 1px solid rgb(85, 87, 83);\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid white;\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.btn_fp = QtWidgets.QPushButton(self.frame)
        self.btn_fp.setGeometry(QtCore.QRect(310, 400, 141, 21))
        self.btn_fp.setStyleSheet("QPushButton{\n"
"    background:none;\n"
"    border: none;\n"
"    font-size:16px;\n"
"    color:rgb(237, 212, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"}")
        self.btn_fp.setObjectName("btn_fp")
        self.btn_signup = QtWidgets.QPushButton(self.frame)
        self.btn_signup.setGeometry(QtCore.QRect(300, 470, 71, 21))
        self.btn_signup.setStyleSheet("QPushButton{\n"
"    background:none;\n"
"    border: none;\n"
"    font-size:18px;\n"
"    color:rgb(237, 212, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"}")
        self.btn_signup.setObjectName("btn_signup")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(640, 40, 101, 101))
        self.toolButton.setStyleSheet("QToolButton{\n"
"    background:#717072;\n"
"    border-radius:50px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/wallpaper/user_border.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setObjectName("toolButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_login.clicked.connect(self.Login)

        self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_2.setText(_translate("MainWindow", "Don\'t have account?"))
        self.label_3.setText(_translate("MainWindow", "Login"))
        self.lineEdit_uname.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_pass.setPlaceholderText(_translate("MainWindow", "Password"))
        self.btn_login.setText(_translate("MainWindow", "Login"))
        self.btn_fp.setText(_translate("MainWindow", "ForgetPassword?"))
        self.btn_signup.setText(_translate("MainWindow", "Signup"))
        self.toolButton.setText(_translate("MainWindow", "..."))


import img

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())