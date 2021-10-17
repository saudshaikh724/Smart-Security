# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import pymysql
from PyQt5.QtCore import QTimer
import time
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import multiprocessing
import datetime

class Ui_Alert3(object):
    update = 1
    count = 0
    tw = time.time()
    flag = False

    def __init__(self, num):
        self.num = num
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewcam)
        # set control_bt callback clicked  function

    def viewcam(self):
        t1 = time.time()

        print('###############',self.num)
        if t1 - self.tw >= self.update:
            self.count += 1
            con = self.num - self.count
            self.btn_sndmail.setText('Send Mail ' + str(con))
            print(con)
            if con == 0:
                print('Send Mail')
                self.count = 0
                self.btn_sndmail.setText('Send')
                self.timer.stop()
                P1 = multiprocessing.Process(target=self.send_mail)
                P1.start()

            self.tw = time.time()

    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            self.timer.start(20)



    def stop_(self):
        self.btn_sndmail.setText('Send Mail')
        self.timer.stop()

    def send_mail(self):
        print('Mail has been Send')

    def display_profile(self,f_name,f_name2):
        self.curr_dt = str(datetime.datetime.now())
        connnection = pymysql.connect("localhost","root","rootpass","project")
        cursor = connnection.cursor()
        select_query = "select * from blockacess where fname ='%s'" %(f_name)
        cursor.execute(select_query)
        row = cursor.fetchone()
        self.lineEdit_id.setText(str(row[0]))
        self.lineEdit_name.setText(row[1])
        self.lineEdit_age.setText(row[3])
        self.lineEdit_gender.setText(row[4])
        self.lineEdit_nationality.setText(row[5])
        self.lineEdit_other.setText(row[6])
        self.lineEdit_datetime.setText(self.curr_dt)
        #self.lineEdit_date.setText(curdate())
        #self.lineEdit_time.setText(curtime())
        self.enrolled_img = 'Registered/' + f_name + '.jpg'
        self.lastmatch_img = 'Monitor/Registered/'+f_name+'/' + f_name2
        pixmap = QtGui.QPixmap('/home/anonymous/Desktop/Project-test/Registered/' + f_name + '.jpg')
        pixmap = pixmap.scaled(self.label_img1.width(), self.label_img1.height(), QtCore.Qt.KeepAspectRatio)
        self.label_img1.setPixmap(pixmap)
        self.label_img1.setAlignment(QtCore.Qt.AlignCenter)

        pixmap = QtGui.QPixmap('/home/anonymous/Desktop/Project-test/Monitor/Registered/'+f_name+'/' + f_name2)
        pixmap = pixmap.scaled(self.label_img2.width(), self.label_img2.height(), QtCore.Qt.KeepAspectRatio)
        self.label_img2.setPixmap(pixmap)
        self.label_img2.setAlignment(QtCore.Qt.AlignCenter)
        P1 = multiprocessing.Process(target=self.view)
        P1.start()

    def view(self):
        ID = int(self.lineEdit_id.text())
        connnection = pymysql.connect("localhost", "root", "rootpass", "project")
        cursor = connnection.cursor()
        select_query = ("select count(*) from view where id =%d") % (ID)
        cursor.execute(select_query)
        r = cursor.fetchone()
        v = int(r[0]) + 1
        insert_query = "insert into view(id,curr_time,curr_date,visit) values(%d,curtime(),curdate(),%d)" % (ID, v)
        cursor.execute(insert_query)
        connnection.commit()
        connnection.close()




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 343)
        MainWindow.setStyleSheet("*{\n"
"    color:rgb(186, 189, 182);\n"
"    background:rgb(46, 52, 54);\n"
"    font: 12pt \"URW Gothic L\";\n"
"}\n"
"QLineEdit{\n"
"    color:rgb(238, 238, 236);\n"
"    border:1px solid rgb(186, 189, 182);\n"
"    \n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_img1 = QtWidgets.QLabel(self.centralwidget)
        self.label_img1.setGeometry(QtCore.QRect(20, 80, 151, 161))
        self.label_img1.setStyleSheet("QLabel{\n"
"    border:1px solid rgb(211, 215, 207);\n"
"}")
        self.label_img1.setText("")
        self.label_img1.setObjectName("label_img1")
        self.label_img2 = QtWidgets.QLabel(self.centralwidget)
        self.label_img2.setGeometry(QtCore.QRect(190, 80, 151, 161))
        self.label_img2.setStyleSheet("QLabel{\n"
"    border:1px solid rgb(211, 215, 207);\n"
"}")
        self.label_img2.setText("")
        self.label_img2.setObjectName("label_img2")
        self.btn_stopsiren = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stopsiren.setGeometry(QtCore.QRect(110, 290, 171, 41))
        self.btn_stopsiren.setStyleSheet("QPushButton{\n"
"    border:1px solid red;    \n"
"    background:rgb(239, 41, 41);\n"
"    border-radius:15px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid white;\n"
"}")
        self.btn_stopsiren.setObjectName("btn_stopsiren")
        self.btn_sndmail = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sndmail.setGeometry(QtCore.QRect(360, 290, 181, 41))
        self.btn_sndmail.setStyleSheet("QPushButton{\n"
"    border:1px solid rgb(52, 101, 164);    \n"
"    background:rgb(52, 101, 164);\n"
"    border-radius:15px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 1px solid white;\n"
"}")
        self.btn_sndmail.setObjectName("btn_sndmail")
        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setGeometry(QtCore.QRect(390, 60, 41, 21))
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(520, 60, 141, 21))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_age = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_age.setGeometry(QtCore.QRect(410, 100, 51, 21))
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.lineEdit_gender = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_gender.setGeometry(QtCore.QRect(552, 100, 111, 21))
        self.lineEdit_gender.setObjectName("lineEdit_gender")
        self.lineEdit_nationality = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nationality.setGeometry(QtCore.QRect(460, 140, 201, 21))
        self.lineEdit_nationality.setObjectName("lineEdit_nationality")
        self.lineEdit_other = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_other.setGeometry(QtCore.QRect(450, 180, 211, 21))
        self.lineEdit_other.setObjectName("lineEdit_other")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 60, 21, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(460, 60, 51, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(360, 100, 41, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(480, 100, 67, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 140, 91, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(360, 180, 81, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(360, 220, 91, 17))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(130, 40, 121, 31))
        self.label_11.setStyleSheet("QLabel{\n"
"    color:rgb(115, 210, 22);\n"
"    border:1px solid red;\n"
"}")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(280, 0, 121, 41))
        self.label_12.setStyleSheet("QLabel{\n"
"    color:white;    \n"
"    font: 63 23pt \"URW Gothic L\";\n"
"}")
        self.label_12.setObjectName("label_12")
        self.lineEdit_datetime = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_datetime.setGeometry(QtCore.QRect(450, 220, 211, 21))
        self.lineEdit_datetime.setObjectName("lineEdit_datetime")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(40, 250, 111, 21))
        self.label_13.setStyleSheet("QLabel{\n"
"    color:white;\n"
"}")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(220, 250, 91, 21))
        self.label_14.setStyleSheet("QLabel{\n"
"    color:white;\n"
"}")
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        pygame.mixer.init()
        pygame.mixer.music.load('Sound/siren.wav')
        pygame.mixer.music.play(0)

        self.P2 = multiprocessing.Process(target=self.send_mail)
        self.btn_sndmail.clicked.connect(self.P2.start)
        self.btn_stopsiren.clicked.connect(self.stop_)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_stopsiren.setText(_translate("MainWindow", "Stop Siren/Mail"))
        self.btn_sndmail.setText(_translate("MainWindow", "Send Mail"))
        self.label_3.setText(_translate("MainWindow", "ID"))
        self.label_4.setText(_translate("MainWindow", "Name "))
        self.label_5.setText(_translate("MainWindow", "Age"))
        self.label_6.setText(_translate("MainWindow", "Gender"))
        self.label_7.setText(_translate("MainWindow", "Nationality"))
        self.label_8.setText(_translate("MainWindow", "Other Info"))
        self.label_9.setText(_translate("MainWindow", "Date/Time"))
        self.label_11.setText(_translate("MainWindow", "Match Found"))
        self.label_12.setText(_translate("MainWindow", "ALERT!!!"))
        self.label_13.setText(_translate("MainWindow", "Enrolled Photo"))
        self.label_14.setText(_translate("MainWindow", "Last Match"))

import img
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Alert()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())