# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Validation import Validation
import pymysql
from PyQt5.QtWidgets import QMessageBox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pygame
class Ui_Forgot(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setStyleSheet("*\n"
"{\n"
"    background:url(:/background/wallpaper/background_red.jpg);\n"
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
        self.frame.setGeometry(QtCore.QRect(460, 110, 501, 461))
        self.frame.setStyleSheet("QFrame{\n"
"    background:rgba(0,0,0,0.5);\n"
"    border:1px solid black;    \n"
"    border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_email = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_email.setGeometry(QtCore.QRect(50, 190, 401, 51))
        self.lineEdit_email.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.btn_sndpass = QtWidgets.QPushButton(self.frame)
        self.btn_sndpass.setGeometry(QtCore.QRect(60, 280, 381, 51))
        self.btn_sndpass.setStyleSheet("QPushButton{\n"
"    background:rgb(186, 189, 182);\n"
"    font-size:19px;\n"
"    color:rgb(46, 52, 54);\n"
"    border: 1px solid black;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid white;\n"
"}")
        self.btn_sndpass.setObjectName("btn_sndpass")
        self.btn_login = QtWidgets.QPushButton(self.frame)
        self.btn_login.setGeometry(QtCore.QRect(180, 390, 151, 21))
        self.btn_login.setStyleSheet("QPushButton{\n"
"    background:none;\n"
"    border: none;\n"
"    font-size:18px;\n"
"    color:rgb(237, 212, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    color:white;\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(150, 40, 211, 41))
        self.label_3.setStyleSheet("QLabel{\n"
"    font-size:27px;\n"
"    color:white;\n"
"    background:none;\n"
"    border:none;\n"
"}")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_sndpass.clicked.connect(self.sendpwd)

    def sendpwd(self):
        obj = Validation()
        mail = self.lineEdit_email.text()
        if mail == '':
            self.sound(1)
            self.qmsg('Error !!!, Filed Is Empty.', 1)

        else:
            if obj.check_emailforgot(mail):
                connection = pymysql.connect("localhost", "root", "rootpass", "project")
                cursor = connection.cursor()
                select_query = "select fname,pwd from signup where email = '%s'"%mail
                try:
                    cursor.execute(select_query)
                    row = cursor.fetchone()


                    email = 'faizk2651@gmail.com'
                    password = '9892338308'
                    send_mail = mail
                    subject = 'Forgot Password'
                    message = 'Hi ' + str(row[0]) + ' your password is ' + str(row[1])

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_mail
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_mail, text)
                    server.quit()
                    self.lineEdit_email.setText('')
                    self.sound(0)
                    self.qmsg("Please check your mail, password has been successfully send to you",0)

                except Exception:
                    self.sound(1)
                    self.qmsg("Please Enter correct Email Address",1)

            else:
                print('Wrong')


    def qmsg(self, msg, check):
        qmsgBox = QMessageBox()
        qmsgBox.move(((qmsgBox.width()) // 2 + 60), ((qmsgBox.height()) // 2 - 50))
        qmsgBox.setStyleSheet(
            'QMessageBox {background-color: #2b5b84; color: white;}\nQLabel{color: white;}\nQPushButton{color: white; font-size: 16px; background-color: #1d1d1d; border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: #2b5b84;}')
        if check == 0:
            QMessageBox.information(qmsgBox, 'PyQt5 message', msg)

        else:
            QMessageBox.critical(qmsgBox, 'PyQt5 message', msg)

    def sound(self, check):

        if check == 0:
            pygame.mixer.init()
            pygame.mixer.music.load('Sound/login.mp3')
            pygame.mixer.music.play(0)

        else:
            pygame.mixer.init()
            pygame.mixer.music.load('Sound/error.mp3')
            pygame.mixer.music.play(0)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Forgot Password"))
        self.lineEdit_email.setPlaceholderText(_translate("MainWindow", "Email Address"))
        self.btn_sndpass.setText(_translate("MainWindow", "Send Password "))
        self.btn_login.setText(_translate("MainWindow", "Return to Login"))
        self.label_3.setText(_translate("MainWindow", "Forgot Password"))


import img
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Forgot()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

