# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtWidgets import QMessageBox
import os
import cv2
from Encode import Ui_Encode
import time
import pygame
import shutil
from PyQt5.QtGui import *

class Ui_Blockacess(object):
    current_position = 0
    img_select = 0



    def qmsg(self,msg,check):
        qmsgBox = QMessageBox()
        qmsgBox.move(((qmsgBox.width()) // 2+60) , ((qmsgBox.height()) // 2- 50))
        qmsgBox.setStyleSheet(
                    'QMessageBox {background-color: #2b5b84; color: white;}\nQLabel{color: white;}\nQPushButton{color: white; font-size: 16px; background-color: #1d1d1d; border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: #2b5b84;}')
        if check == 0:
            QMessageBox.information(qmsgBox, 'Message', msg)
        if check == 1:
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

    def del_img(self):
        self.path =''
        self.filename=''
        self.fileName = ''
        self.lineEdit_fn.setText('')
        self.label_img.setPixmap(QtGui.QPixmap(":/icons/wallpaper/user1.png"))

    def add_img(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "","Image Files (*.png *.jpg *jpeg *.bmp)")  # Ask for filez
        inputFilepath = self.fileName
        filename_w_ext = os.path.basename(inputFilepath)
        filename, file_extension = os.path.splitext(filename_w_ext)
        # filename = foobar
        # file_extension = .txt
        self.path, self.filename = os.path.split(self.fileName)
        self.img = cv2.imread(self.fileName, 1)
        # cv2.imshow('img',img)
        if self.fileName:  # If the user gives a file
            pixmap = QtGui.QPixmap(self.fileName)  # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.label_img.width(), self.label_img.height(),QtCore.Qt.KeepAspectRatio)  # Scale pixmap
            self.label_img.setPixmap(pixmap)  # Set the pixmap onto the label
            self.label_img.setAlignment(QtCore.Qt.AlignCenter)
            self.img_select = 1
        self.lineEdit_fn.setText(self.fileName)

    def next_position(self):
        connection = pymysql.connect("localhost", "root", "rootpass", "project")
        cursor = connection.cursor()
        self.current_position = self.current_position + 1
        cursor.execute("SELECT * FROM blockacess")
        self.row = cursor.fetchone()

        try:
            for i in range(self.current_position):
                self.lineEdit_id.setText(str(self.row[0]))
                self.lineEdit_fname.setText(self.row[1])
                self.lineEdit_lname.setText(self.row[2])
                self.lineEdit_age.setText(self.row[3])
                self.lineEdit_gender.setText(self.row[4])
                self.lineEdit_nationality.setText(self.row[5])
                self.lineEdit_other.setText(self.row[6])
                self.image_name = cv2.imread('/home/anonymous/Desktop/Project-test/Registered/' + self.row[1] + str('.jpg'),1)
                pixmap = QtGui.QPixmap('/home/anonymous/Desktop/Project-test/Registered/'+self.row[1]+'.jpg')
                pixmap = pixmap.scaled(self.label_img.width(),self.label_img.height(),QtCore.Qt.KeepAspectRatio)
                self.label_img.setPixmap(pixmap)
                self.label_img.setAlignment(QtCore.Qt.AlignCenter)
                self.row = cursor.fetchone()
        except:
            print("Last Row")
            self.qmsg('This is last record',0)
            self.current_position= self.current_position-1


        print('Next : ' + str(self.current_position))

    def previous_position(self):
        connection = pymysql.connect("localhost", "root", "rootpass", "project")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM blockacess")
        self.row = cursor.fetchone()
        self.current_position = self.current_position -1
        if self.current_position<=0:
            self.current_position=0
            self.del_img()
            self.clear()
        try:
            for i in range(self.current_position):
                self.lineEdit_id.setText(str(self.row[0]))
                self.lineEdit_fname.setText(self.row[1])
                self.lineEdit_lname.setText(self.row[2])
                self.lineEdit_age.setText(self.row[3])
                self.lineEdit_gender.setText(self.row[4])
                self.lineEdit_nationality.setText(self.row[5])
                self.lineEdit_other.setText(self.row[6])
                self.image_name = cv2.imread('/home/anonymous/Desktop/Project-test/Registered/' +self.row[1]+ str('.jpg'),1)
                pixmap = QtGui.QPixmap('/home/anonymous/Desktop/Project-test/Registered/'+self.row[1]+'.jpg')
                pixmap = pixmap.scaled(self.label_img.width(),self.label_img.height(),QtCore.Qt.KeepAspectRatio)
                self.label_img.setPixmap(pixmap)
                self.label_img.setAlignment(QtCore.Qt.AlignCenter)

                self.row = cursor.fetchone()

        except:
            print('First rows')
        print('Prev : ' + str(self.current_position))



    def clear(self):
        self.lineEdit_id.setText('')
        self.lineEdit_fname.setText('')
        self.lineEdit_lname.setText('')
        self.lineEdit_age.setText('')
        self.lineEdit_gender.setText('')
        self.lineEdit_nationality.setText('')
        self.lineEdit_other.setText('')
        self.label_img.setPixmap(QtGui.QPixmap(":/icons/wallpaper/user1.png"))

    def load(self):
        connection = pymysql.connect("localhost","root","rootpass","project")
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM blockacess''')
        self.tableWidget.setRowCount(0)
        for row, form in enumerate(cursor):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                print(str(item))
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))

    def delete_record(self):
        connection = pymysql.connect("localhost", "root", "rootpass", "project")
        cursor = connection.cursor()
        id = self.lineEdit_id.text()
        fname = self.lineEdit_fname.text()
        if id!='':
            delete_query_ba = "delete from blockacess where id = '%d'" % int(id)
            delete_query_v = "delete from view where id = '%d'" % int(id)

            try:
                cursor.execute(delete_query_ba)
                cursor.execute(delete_query_v)
                connection.commit()
                os.remove('Registered/'+fname+str('.jpg'))
                shutil.rmtree('Monitor/Registered/' + fname)
                self.del_img()
                self.load()
                self.clear()
                self.qmsg("Deleted Successfully", 0)

            except Exception as e:
                self.sound(1)
                self.qmsg(e,1)
        else:
            self.sound(1)
            self.qmsg('Check field again make sure field is not empty',1)

    def insert_record(self):

        FNAME=self.lineEdit_fname.text()
        LNAME=self.lineEdit_lname.text()
        AGE=self.lineEdit_age.text()
        GENDER=self.lineEdit_gender.text()
        NATIONALITY=self.lineEdit_nationality.text()
        OTHER_INFO=self.lineEdit_other.text()

        if AGE == '' and LNAME == '':
            AGE = 'None'
            LNAME = 'None'
        elif AGE == '':
            AGE = 'None'

        elif LNAME == '':
            LNAME = 'None'
        connection = pymysql.connect("localhost", "root", "rootpass", "project")
        cursor = connection.cursor()
        if FNAME!='' and LNAME!='' and AGE!='' and GENDER!='' and NATIONALITY!='' and OTHER_INFO!='':
            try:
                if self.img_select ==1:
                    insert_query = "insert into blockacess(fname,lname,age,nationality,gender,other_info) values('%s','%s','%s','%s','%s','%s')" \
                                   % (FNAME, LNAME, AGE, NATIONALITY, GENDER, OTHER_INFO)
                    cv2.imwrite('Registered/' + FNAME + str('.jpg'), self.img)
                    cursor.execute(insert_query)
                    connection.commit()
                    self.createFolder(FNAME)
                    self.del_img()
                    self.load()
                    self.clear()
                    self.qmsg('Record inserted Successfully',0)

                else:
                    self.sound(1)
                    self.qmsg('Please select Image',1)

            except Exception as e:
                self.sound(1)
                self.qmsg(e,1)
                connection.rollback()
        else:
            self.sound(1)
            self.qmsg("Check field again make sure field is not empty!",1)


    def createFolder(self,directory):
        try:
            if not os.path.exists('Monitor/Registered/'+directory):
                os.makedirs('Monitor/Registered/'+directory)
        except OSError:
            print('Error: Creating directory. ' + directory)


    def update_record(self):
        ID = self.lineEdit_id.text()
        FNAME = self.lineEdit_fname.text()
        LNAME = self.lineEdit_lname.text()
        AGE = self.lineEdit_age.text()
        GENDER = self.lineEdit_gender.text()
        NATIONALITY = self.lineEdit_nationality.text()
        OTHER_INFO = self.lineEdit_other.text()

        connection = pymysql.connect("localhost","root","rootpass","project")
        cursor = connection.cursor()
        if ID!='':
            update_query = "update blockacess set fname = '%s', lname = '%s', age = '%s', gender = '%s', nationality = '%s', other_info = '%s' where id ='%d'" \
            %(FNAME,LNAME,AGE,GENDER,NATIONALITY,OTHER_INFO,int(ID))
            try:
                if self.img_select ==1:
                    cv2.imwrite('Registered/' + FNAME + str('.jpg'), self.img)
                    self.img_select = 0
                    print('IF ')
                else:
                    os.rename('Registered/'+FNAME+str('.jpg'),'/home/anonymous/Desktop/Project-test/Registered/'+FNAME+str('.jpg'))

                cursor.execute(update_query)
                connection.commit()
                connection.close()
                self.load()
                self.clear()
                self.del_img()
                self.qmsg('Updated Successfully',0)
            except Exception as e:
                self.qmsg(str(e),1)
        else:
            self.sound(1)
            self.qmsg("Check field again make sure field is not empty",1)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setStyleSheet("*{\n"
"    background:url(:/background/wallpaper/gray-background.jpg);\n"
"}\n"
"QLineEdit{\n"
"    border:2px solid rgb(136, 138, 133);\n"
"    border-radius:10px;    \n"
"    font: 13pt \"URW Gothic L\";\n"
"}\n"
"QLineEdit:hover{\n"
"    border:2px solid rgb(46, 52, 54);\n"
"}\n"
"QPushButton{\n"
"    \n"
"    font: 25 15pt \"Ubuntu\";\n"
"\n"
"    }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 100, 701, 351))
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"    color:black;\n"
"    font: 25 12pt \"Ubuntu\";\n"
"}")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(870, 100, 421, 371))
        self.label_img.setStyleSheet("QLabel{\n"
"    background:white;\n"
"    border:1px solid rgb(136, 138, 133);\n"
"}")
        self.label_img.setText("")
        self.label_img.setPixmap(QtGui.QPixmap(":/icons/wallpaper/user1.png"))
        self.label_img.setScaledContents(False)
        self.label_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img.setObjectName("label_img")
        self.lineEdit_fname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fname.setGeometry(QtCore.QRect(150, 480, 241, 41))
        self.lineEdit_fname.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_fname.setObjectName("lineEdit_fname")
        self.lineEdit_lname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_lname.setGeometry(QtCore.QRect(440, 480, 261, 41))
        self.lineEdit_lname.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_lname.setObjectName("lineEdit_lname")
        self.lineEdit_age = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_age.setGeometry(QtCore.QRect(40, 550, 71, 41))
        self.lineEdit_age.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.lineEdit_gender = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_gender.setGeometry(QtCore.QRect(160, 550, 161, 41))
        self.lineEdit_gender.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_gender.setObjectName("lineEdit_gender")
        self.lineEdit_nationality = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nationality.setGeometry(QtCore.QRect(370, 550, 331, 41))
        self.lineEdit_nationality.setText("")
        self.lineEdit_nationality.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_nationality.setObjectName("lineEdit_nationality")
        self.lineEdit_other = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_other.setGeometry(QtCore.QRect(40, 620, 661, 41))
        self.lineEdit_other.setText("")
        self.lineEdit_other.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_other.setObjectName("lineEdit_other")
        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setGeometry(QtCore.QRect(40, 480, 71, 41))
        self.lineEdit_id.setText("")
        self.lineEdit_id.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_id.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(840, 530, 121, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/wallpaper/Btn_Add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add.setIcon(icon)
        self.btn_add.setIconSize(QtCore.QSize(30, 50))
        self.btn_add.setObjectName("btn_add")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(1010, 530, 131, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/wallpaper/Btn_update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_update.setIcon(icon1)
        self.btn_update.setIconSize(QtCore.QSize(25, 50))
        self.btn_update.setObjectName("btn_update")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(1190, 530, 121, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/wallpaper/Btn_Delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon2)
        self.btn_delete.setIconSize(QtCore.QSize(25, 50))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_next = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next.setGeometry(QtCore.QRect(1010, 610, 131, 51))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/wallpaper/Btn_Next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next.setIcon(icon3)
        self.btn_next.setIconSize(QtCore.QSize(25, 50))
        self.btn_next.setObjectName("btn_next")
        self.btn_previous = QtWidgets.QPushButton(self.centralwidget)
        self.btn_previous.setGeometry(QtCore.QRect(840, 610, 121, 51))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/wallpaper/Btn_Previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_previous.setIcon(icon4)
        self.btn_previous.setIconSize(QtCore.QSize(25, 50))
        self.btn_previous.setObjectName("btn_previous")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 10, 621, 61))
        self.label_2.setStyleSheet("QLabel{\n"
"    \n"
"    font: 75 45pt \"Umpush\";\n"
"    color:rgb(46, 52, 54);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lineEdit_fn = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fn.setGeometry(QtCore.QRect(870, 470, 341, 31))
        self.lineEdit_fn.setStyleSheet("QLineEdit{\n"
"    border-radius:none;\n"
"    padding-left:5px;\n"
"}")
        self.lineEdit_fn.setObjectName("lineEdit_fn")
        self.btn_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_file.setGeometry(QtCore.QRect(1210, 470, 31, 31))
        self.btn_file.setStyleSheet("QPushButton{\n"
"border:none;\n"
"background:none;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid rgb(46, 52, 54);\n"
"}")
        self.btn_file.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/wallpaper/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_file.setIcon(icon5)
        self.btn_file.setIconSize(QtCore.QSize(25, 25))
        self.btn_file.setObjectName("btn_file")
        self.btn_delfn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delfn.setGeometry(QtCore.QRect(1240, 470, 31, 31))
        self.btn_delfn.setStyleSheet("QPushButton{\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid rgb(46, 52, 54);\n"
"}")
        self.btn_delfn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/wallpaper/btn_del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delfn.setIcon(icon6)
        self.btn_delfn.setIconSize(QtCore.QSize(25, 25))
        self.btn_delfn.setObjectName("btn_delfn")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(1190, 610, 121, 51))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/wallpaper/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_clear.setIcon(icon7)
        self.btn_clear.setIconSize(QtCore.QSize(25, 50))
        self.btn_clear.setObjectName("btn_clear")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(10, 10, 61, 61))
        self.btn_back.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    border:5px solid rgb(46, 52, 54);\n"
"    border-radius:30px;\n"
"}")
        self.btn_back.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/wallpaper/Btn_Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon8)
        self.btn_back.setIconSize(QtCore.QSize(80, 80))
        self.btn_back.setObjectName("btn_back")
        self.btn_encode = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encode.setGeometry(QtCore.QRect(1270, 470, 31, 31))
        self.btn_encode.setStyleSheet("QPushButton{\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid rgb(46, 52, 54);\n"
"}")
        self.btn_encode.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/wallpaper/encode.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_encode.setIcon(icon9)
        self.btn_encode.setIconSize(QtCore.QSize(35, 25))
        self.btn_encode.setObjectName("btn_encode")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.load()

        self.lineEdit_id.setDisabled(True)
        self.btn_add.clicked.connect(self.insert_record)
        self.btn_next.clicked.connect(self.next_position)
        self.btn_previous.clicked.connect(self.previous_position)
        self.btn_update.clicked.connect(self.update_record)
        self.btn_delete.clicked.connect(self.delete_record)
        self.btn_file.clicked.connect(self.add_img)
        self.btn_delfn.clicked.connect(self.del_img)
        self.btn_clear.clicked.connect(self.clear_)
        self.btn_encode.clicked.connect(self.encode)

    def clear_(self):
        self.lineEdit_id.setText('')
        self.lineEdit_fname.setText('')
        self.lineEdit_lname.setText('')
        self.lineEdit_age.setText('')
        self.lineEdit_gender.setText('')
        self.lineEdit_nationality.setText('')
        self.lineEdit_other.setText('')
        self.label_img.setPixmap(QtGui.QPixmap(":/icons/wallpaper/user1.png"))

    def encode(self):
        win = QtWidgets.QMainWindow()
        ui = Ui_Encode()
        ui.setupUi(win)
        win.show()
        time.sleep(0.5)
        ui.controlTimer()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BlockAcess"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "FNAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "LNAME"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "AGE"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "GENDER"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "NATIONALITY"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "OTHER"))
        self.lineEdit_fname.setPlaceholderText(_translate("MainWindow", "Firstname"))
        self.lineEdit_lname.setPlaceholderText(_translate("MainWindow", "Lastname"))
        self.lineEdit_age.setPlaceholderText(_translate("MainWindow", "Age"))
        self.lineEdit_gender.setPlaceholderText(_translate("MainWindow", "Gender"))
        self.lineEdit_nationality.setPlaceholderText(_translate("MainWindow", "Nationality"))
        self.lineEdit_other.setPlaceholderText(_translate("MainWindow", "Other Information"))
        self.lineEdit_id.setPlaceholderText(_translate("MainWindow", "ID"))
        self.btn_add.setText(_translate("MainWindow", "Add"))
        self.btn_update.setText(_translate("MainWindow", "Update"))
        self.btn_delete.setText(_translate("MainWindow", "Delete"))
        self.btn_next.setText(_translate("MainWindow", "Next"))
        self.btn_previous.setText(_translate("MainWindow", "Previous"))
        self.label_2.setText(_translate("MainWindow", "🅱🅻🅾🅲🅺 🅰🅲🅴🆂🆂"))
        self.lineEdit_fn.setPlaceholderText(_translate("MainWindow", "Choose Image"))
        self.btn_file.setToolTip(_translate("MainWindow", "<html><head/><body><p>Choose Image</p></body></html>"))
        self.btn_delfn.setToolTip(_translate("MainWindow", "<html><head/><body><p>Clear</p></body></html>"))
        self.btn_clear.setText(_translate("MainWindow", "Clear"))
        self.btn_encode.setToolTip(_translate("MainWindow", "<html><head/><body><p>Encode Image</p></body></html>"))

import img

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Blockacess()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
