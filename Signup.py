from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtWidgets import QMessageBox
import pygame
import re
from Validation import Validation

class Ui_Signup(object):

    user = None
    value = 1
    def Signup(self):
        try:
            obj = Validation()
            FNAME = self.lineEdit_fname.text()
            LNAME = self.lineEdit_lname.text()
            AGE = self.lineEdit_age.text()
            GENDER = ''
            if self.radioButton_m.isChecked():
                GENDER = 'Male'
            if self.radioButton_f.isChecked():
                GENDER = 'Female'
            UNAME = self.lineEdit_uname.text()
            PASS = (self.lineEdit_pass.text())
            EMAIL = (self.lineEdit_ea.text())

            if FNAME!='' and LNAME!='' and AGE!='' and GENDER!='' and UNAME!='' and PASS!='':
                connection = pymysql.connect('localhost', 'root', 'rootpass', 'project')
                cursor = connection.cursor()
                if obj.check_name(FNAME,'Firstname') and obj.check_name(LNAME,'Lastname') and obj.check_age(AGE) and obj.check_uname(UNAME) and obj.check_pss(PASS) and obj.email_exist_signup(EMAIL):
                    insert_query = "insert into signup(fname,lname,age,gender,uname,pwd,email) values('%s','%s',%d,'%s','%s','%s','%s')" \
                                   % (FNAME, LNAME, int(AGE), GENDER, UNAME, PASS, EMAIL)
                    cursor.execute(insert_query)
                    connection.commit()
                    connection.close()
                    self.sound(0)
                    self.clear()
                    self.qmsg('Account Created Successfully', 0)
                    self.user = UNAME
                    self.db(UNAME)

                else:
                    self.sound(1)
            else:
                self.sound(1)
                self.qmsg('Error !!! Check Entries Again .Make Sure No Filed Is Empty.',1)



        except Exception as e:
            self.sound(1)
            print(e)
            self.qmsg('Username Already Exist!',1)

    def db(self,UNAME):
        THRESOLD = 50
        MODEL = 'hog'
        RESETCOUNTER = 30
        AUTOMAIL = 10
        SCALED = 1
        DISTORT = 1
        connection = pymysql.connect('localhost', 'root', 'rootpass', 'project')
        cursor = connection.cursor()
        insert_query = "insert into settings(thresold,model,resetcounter,automail,scaled,distort,uname) values(%d,'%s',%d,%d,%d,%d,'%s')" \
        %(THRESOLD, MODEL, RESETCOUNTER, AUTOMAIL, SCALED, DISTORT, UNAME)
        cursor.execute(insert_query)
        connection.commit()
        connection.close()
        self.value = 1

    def clear(self):
        self.lineEdit_fname.setText('')
        self.lineEdit_lname.setText('')
        self.lineEdit_age.setText('')
        self.lineEdit_uname.setText('')
        self.lineEdit_pass.setText('')
        self.lineEdit_ea.setText('')

    def qmsg(self,msg,check):
        qmsgBox = QMessageBox()
        qmsgBox.move(((qmsgBox.width()) // 2+60) , ((qmsgBox.height()) // 2- 50))
        qmsgBox.setStyleSheet(
                    'QMessageBox {background-color: #2b5b84; color: white;}\nQLabel{color: white;}\nQPushButton{color: white; font-size: 16px; background-color: #1d1d1d; border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: #2b5b84;}')
        if check == 0:
            QMessageBox.information(qmsgBox, 'Success', msg)
        else:
            QMessageBox.critical(qmsgBox, 'Failed', msg)


    def sound(self,check):

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
"    background:url(:/background/wallpaper/Blue-And-Black-Wallpaper-25-1920x1080.jpg);\n"
"}\n"
"QLineEdit{\n"
"font-size: 22px;\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:white;\n"
"    border-bottom: 1px solid rgb(85, 87, 83);\n"
"     padding-bottom: 15px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border-bottom:1px solid rgb(46, 52, 54);\n"
"}\n"
"QRadioButton{\n"
"    color:rgb(180, 180, 180);\n"
"    font-size:21px;\n"
"    background:none;\n"
"    border:none;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(300, 70, 811, 611))
        self.frame.setStyleSheet("QFrame{\n"
"    background:rgba(0,0,0,0.5);\n"
"    border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(280, 550, 221, 21))
        self.label_2.setStyleSheet("QLabel{\n"
"    color:white;\n"
"    font-size:18px;\n"
"    background:transparent;\n"
"    border:none;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(370, 50, 91, 41))
        self.label_3.setStyleSheet("QLabel{\n"
"    font-size:27px;\n"
"    color:white;\n"
"    background:none;\n"
"    border:none;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(440, 230, 101, 41))
        self.label.setStyleSheet("QLabel{\n"
"    font-size:22px;\n"
"    border:none;\n"
"    color:rgb(190,190,190);\n"
"    background:none;\n"
"}")
        self.label.setObjectName("label")
        self.lineEdit_fname = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_fname.setGeometry(QtCore.QRect(60, 150, 331, 51))
        self.lineEdit_fname.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_fname.setObjectName("lineEdit_fname")
        self.lineEdit_lname = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_lname.setGeometry(QtCore.QRect(420, 150, 331, 51))
        self.lineEdit_lname.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_lname.setObjectName("lineEdit_lname")
        self.lineEdit_age = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_age.setGeometry(QtCore.QRect(60, 220, 331, 51))
        self.lineEdit_age.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.radioButton_m = QtWidgets.QRadioButton(self.frame)
        self.radioButton_m.setGeometry(QtCore.QRect(550, 240, 81, 23))
        self.radioButton_m.setObjectName("radioButton_m")
        self.radioButton_f = QtWidgets.QRadioButton(self.frame)
        self.radioButton_f.setGeometry(QtCore.QRect(640, 240, 101, 23))
        self.radioButton_f.setObjectName("radioButton_f")
        self.lineEdit_uname = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_uname.setGeometry(QtCore.QRect(80, 290, 311, 51))
        self.lineEdit_uname.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_uname.setObjectName("lineEdit_uname")
        self.lineEdit_pass = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_pass.setGeometry(QtCore.QRect(420, 290, 331, 51))
        self.lineEdit_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.lineEdit_ea = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_ea.setGeometry(QtCore.QRect(180, 370, 471, 61))
        self.lineEdit_ea.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ea.setObjectName("lineEdit_ea")
        self.btn_signup = QtWidgets.QPushButton(self.frame)
        self.btn_signup.setGeometry(QtCore.QRect(230, 460, 381, 51))

        self.btn_signup.setStyleSheet("QPushButton{\n"
"    background:rgb(211, 215, 207);\n"
"    font-size:19px;\n"
"    color:black;\n"
"    border: 1px solid black;\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid rgb(211, 215, 207);\n"
"}")
        self.btn_signup.setObjectName("btn_signup")
        self.btn_login = QtWidgets.QPushButton(self.frame)
        self.btn_login.setGeometry(QtCore.QRect(500, 544, 61, 31))
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
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(660, 10, 101, 101))
        self.toolButton.setStyleSheet("QToolButton{\n"
"    background:rgb(211, 215, 207);\n"
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

        self.btn_signup.clicked.connect(self.Signup)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Already have account?"))
        self.label_3.setText(_translate("MainWindow", "Signup"))
        self.label.setText(_translate("MainWindow", "Gender"))
        self.lineEdit_fname.setPlaceholderText(_translate("MainWindow", "Firstname"))
        self.lineEdit_lname.setPlaceholderText(_translate("MainWindow", "Lastname"))
        self.lineEdit_age.setPlaceholderText(_translate("MainWindow", "Age"))
        self.radioButton_m.setText(_translate("MainWindow", "Male"))
        self.radioButton_f.setText(_translate("MainWindow", "Female"))
        self.lineEdit_uname.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_pass.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_ea.setPlaceholderText(_translate("MainWindow", "Email Address"))
        self.btn_signup.setText(_translate("MainWindow", "Signup"))
        self.btn_login.setText(_translate("MainWindow", "Login"))
        self.toolButton.setText(_translate("MainWindow", "..."))

import img
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Signup()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())