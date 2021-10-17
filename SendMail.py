# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Validation import Validation
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import *
import pygame
import smtplib
import os
import pymysql
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
images = []
class Ui_Mail(object):
    count = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 425)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 581, 451))
        self.tabWidget.setStyleSheet("*{\n"
"    \n"
"\n"
"    background:url(:/background/wallpaper/background_purple.jpg);\n"
"}\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("QLineEdit{\n"
"    font-size:18px;\n"
"    background:transparent;\n"
"    border:none;\n"
"    color:rgb(238, 238, 236);\n"
"    border-bottom: 1px solid #717072;\n"
"     padding-bottom: 10px;\n"
"}")
        self.tab.setObjectName("tab")
        self.lineEdit_reci = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_reci.setGeometry(QtCore.QRect(60, 90, 351, 41))
        self.lineEdit_reci.setObjectName("lineEdit_reci")
        self.lineEdit_sub = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_sub.setGeometry(QtCore.QRect(60, 150, 451, 41))
        self.lineEdit_sub.setObjectName("lineEdit_sub")
        self.lineEdit_msg = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_msg.setGeometry(QtCore.QRect(60, 210, 451, 41))
        self.lineEdit_msg.setObjectName("lineEdit_msg")
        self.lineEdit_fn = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_fn.setGeometry(QtCore.QRect(60, 270, 351, 41))
        self.lineEdit_fn.setStyleSheet("QLineEdit{\n"
"    font-size:18px;\n"
"    background:transparent;\n"
"    border:1px solid white;\n"
"    color:rgb(238, 238, 236);\n"
"     padding-bottom: 5px;\n"
"    padding-left:3px;\n"
"}")
        self.lineEdit_fn.setObjectName("lineEdit_fn")
        self.btn_fn = QtWidgets.QPushButton(self.tab)
        self.btn_fn.setGeometry(QtCore.QRect(430, 270, 31, 41))
        self.btn_fn.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(115,210,22);\n"
"    border: 1px solid rgb(115, 210, 22);\n"
"}")
        self.btn_fn.setObjectName("btn_fn")
        self.btn_clr = QtWidgets.QPushButton(self.tab)
        self.btn_clr.setGeometry(QtCore.QRect(480, 270, 31, 41))
        self.btn_clr.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;\n"
"    color:white;\n"
"}\n"
"QPushButton:hover{\n"
"    border: 1px solid rgb(204, 0, 0);\n"
"    color: rgb(204,0,0);\n"
"}")
        self.btn_clr.setObjectName("btn_clr")
        self.btn_snd = QtWidgets.QPushButton(self.tab)
        self.btn_snd.setGeometry(QtCore.QRect(410, 340, 111, 31))
        self.btn_snd.setStyleSheet("QPushButton{\n"
"    font-size:17px;\n"
"    border: 1px solid rgb(52, 101, 164);\n"
"    color:white;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background:rgb(52, 101, 164);\n"
"}")
        self.btn_snd.setObjectName("btn_snd")
        self.lineEdit_id = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_id.setGeometry(QtCore.QRect(60, 40, 41, 31))
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(160, 20, 411, 351))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setStyleSheet("QTableWidget{\n"
                                   "    color:white;\n"
                                   "}")
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(20, 100, 121, 161))
        self.label.setStyleSheet("QLabel{\n"
"    border:1px solid rgb(136, 138, 133);\n"
"}")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 101, 25))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(30, 290, 101, 25))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.load()
        self.btn_snd.clicked.connect(self.sndmail)
        self.btn_clr.clicked.connect(self.clear)
        self.btn_fn.clicked.connect(self.setImage)
        self.pushButton.clicked.connect(self.loadimg)


    def loadimg(self):
        ID = int(self.lineEdit.text())
        connection = pymysql.connect("localhost", "root", "rootpass", "project")
        cursor = connection.cursor()
        select_query = "select * from blockacess where id =%d"%(ID)
        cursor.execute(select_query)
        row = cursor.fetchone()

        #self.image_name = cv2.imread('/home/anonymous/Desktop/Project-test/Registered/' + row[0] + str('.jpg'), 1)
        pixmap = QtGui.QPixmap('/home/anonymous/Desktop/Project-test/Registered/' + row[1] + '.jpg')
        pixmap = pixmap.scaled(self.label.width(), self.label.height(), QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.setAlignment(QtCore.Qt.AlignCenter)


    def load(self):
        connection = pymysql.connect("localhost","root","rootpass","project")
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM view''')
        self.tableWidget.setRowCount(0)
        for row, form in enumerate(cursor):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                print(str(item))
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))


    def setImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "","Image Files (*.png *.jpg *jpeg *.bmp)")  # Ask for filez
        inputFilepath = fileName
        filename_w_ext = os.path.basename(inputFilepath)
        filename, file_extension = os.path.splitext(filename_w_ext)
        # filename = foobar
        # file_extension = .txt
        self.path, self.filename = os.path.split(fileName)
        print(self.path)
        print(self.filename)

        self.count += 1
        if self.count == 1:
            self.name_list = self.filename
            self.lineEdit_fn.setText(self.name_list)
            images.append(self.filename)
        else:
            self.name_list= self.name_list+', '+str(self.filename)
            self.lineEdit_fn.setText(self.name_list)
            images.append(self.filename)
        # path = path/to/file
        # filename = foobar.txt

    def clear(self):
        self.lineEdit_reci.setText('')
        self.lineEdit_sub.setText('')
        self.lineEdit_msg.setText('')
        self.lineEdit_fn.setText('')
        self.lineEdit_id.setText('')
        images.clear()




    def sndmail(self):
        obj = Validation()
        mail = self.lineEdit_reci.text()
        connnection = pymysql.connect("localhost", "root", "rootpass", "project")
        cursor = connnection.cursor()
        ID = int(self.lineEdit_id.text())
        select_query1 = "select * from blockacess where id =%d" % (ID)
        cursor.execute(select_query1)
        row = cursor.fetchone()

        select_query2 = "select count(*) from view where id =%d" % (ID)
        cursor.execute(select_query2)
        row2 = cursor.fetchone()

        name = 'Name : ' +row[1]+', '
        age = 'Age : ' +row[3]+ ', '
        gender = 'Gender : ' +row[4]+ ', '
        citizen = 'Nationality : '+row[5]+', '
        other = 'OtherInfo : ' + row[6] +', '
        visit = 'Visited : '+str(row2[0])+'.'
        address = 'Address : Goregaon(W),Patkar College'
        table = 'Suspect Information : '+name+age+gender+citizen+other+visit

        if self.lineEdit_id.text() != '' and self.lineEdit_reci.text()!='' and self.lineEdit_sub.text()!='' and self.lineEdit_msg.text()!='' and self.lineEdit_fn.text()!='':

            if obj.check_email(mail):
                email = ''
                password = ''
                send_to_email = str(self.lineEdit_reci.text())
                subject = str(self.lineEdit_sub.text())
                message = table+' Message : '+(self.lineEdit_msg.text())
                dir_path = self.path
                files = images

                msg = MIMEMultipart()
                msg['To'] = send_to_email
                msg['From'] = email
                msg['Subject'] = subject

                body = MIMEText(message, 'html', 'utf-8')
                msg.attach(body)  # add message body (text or html)

                for f in files:  # add files to the message
                    file_path = os.path.join(dir_path, f)
                    attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
                    attachment.add_header('Content-Disposition', 'attachment', filename=f)
                    msg.attach(attachment)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(send_to_email, password)
                text = msg.as_string()
                server.sendmail(send_to_email, send_to_email, text)
                server.quit()
                self.sound(0)
                self.qmsg('Mail has been successfully send',1)
                self.clear()


            else:
                self.sound(1)
        else:
            self.sound(1)
            self.qmsg('Error !!! Check Entries Again .Make Sure No Filed Is Empty.', 1)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Mail"))
        self.lineEdit_reci.setPlaceholderText(_translate("MainWindow", "Recipient"))
        self.lineEdit_sub.setPlaceholderText(_translate("MainWindow", "Subject"))
        self.lineEdit_msg.setPlaceholderText(_translate("MainWindow", "Message"))
        self.lineEdit_fn.setPlaceholderText(_translate("MainWindow", "Choose image"))
        self.btn_fn.setText(_translate("MainWindow", "..."))
        self.btn_clr.setText(_translate("MainWindow", "X"))
        self.btn_snd.setText(_translate("MainWindow", "Send"))
        self.lineEdit_id.setPlaceholderText(_translate("MainWindow", "ID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Mail"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DATE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TIME"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "VISIT"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter ID"))
        self.pushButton.setText(_translate("MainWindow", "Search ID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "View"))


import img
