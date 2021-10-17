# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtWidgets import QMessageBox
import pygame
from Validation import Validation
class Ui_Inform(object):

    current_position = 0

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

    def next_position(self):
        connection = pymysql.connect("localhost", "root", "rootpass", "project")
        cursor = connection.cursor()
        self.current_position = self.current_position + 1
        cursor.execute("SELECT * FROM inform")
        row = cursor.fetchone()
        try:
            for i in range(self.current_position):

                self.lineEdit_id.setText(str(row[0]))
                self.lineEdit_name.setText(row[1])
                self.lineEdit_email.setText(row[2])
                self.lineEdit_info.setText(row[3])
                row = cursor.fetchone()
        except:
            print("Last Row")
            self.qmsg('This is last record',0)
            self.current_position= self.current_position-1


        print('Next : ' + str(self.current_position))

    def previous_position(self):
        connection = pymysql.connect("localhost", "root", "rootpass", "project")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM inform")
        row = cursor.fetchone()
        self.current_position = self.current_position -1
        if self.current_position<=0:
            self.current_position=0
            self.clear()
        try:
            for i in range(self.current_position):
                self.lineEdit_id.setText(str(row[0]))
                self.lineEdit_name.setText(row[1])
                self.lineEdit_email.setText(row[2])
                self.lineEdit_info.setText(row[3])
                row = cursor.fetchone()

        except:
            print('First rows')
        print('Prev : ' + str(self.current_position))



    def clear(self):
        self.lineEdit_id.setText('')
        self.lineEdit_name.setText('')
        self.lineEdit_email.setText('')
        self.lineEdit_info.setText('')

    def load(self):
        connection = pymysql.connect("localhost","root","rootpass","project")
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM inform''')
        self.tableWidget.setRowCount(0)
        for row, form in enumerate(cursor):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                print(str(item))
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))

    def delete_record(self):
        connection = pymysql.connect("localhost", "root", "rootpass", "project")
        cursor = connection.cursor()
        ID = self.lineEdit_id.text()
        if ID!='':
            delete_query = "delete from inform where id = '%d'" % int(ID)
            try:
                cursor.execute(delete_query)
                connection.commit()
                self.load()
                self.clear()
                self.qmsg("Deleted Successfully", 0)

            except Exception as e:
                self.sound(1)
                self.qmsg(e, 1)
        else:
            self.sound(1)
            self.qmsg("Check field again make sure field is not empty",1)
    def insert_record(self):
        NAME=self.lineEdit_name.text()
        EMAIL =self.lineEdit_email.text()
        OTHERINFO = self.lineEdit_info.text()
        obj = Validation()

        if NAME!='' and EMAIL!='' and OTHERINFO!='':
            connection = pymysql.connect("localhost","root","rootpass","project")
            cursor = connection.cursor()
            insert_query = "insert into inform(name,email,otherinfo) values('%s','%s','%s')"%(NAME,EMAIL,OTHERINFO)
            if obj.email_exist_inform(EMAIL):
                try:
                    cursor.execute(insert_query)
                    connection.commit()
                    self.load()
                    self.clear()
                    self.qmsg('Record inserted Successfully',0)

                except Exception as e:
                    self.sound(1)
                    self.qmsg(e,1)

        else:
            self.sound(1)
            self.qmsg("Check field again make sure field is not empty",1)
    def update_record(self):
        ID = self.lineEdit_id.text()
        NAME = self.lineEdit_name.text()
        EMAIL = self.lineEdit_email.text()
        OTHERINFO = self.lineEdit_info.text()
        if ID!='':
            connection = pymysql.connect("localhost","root","rootpass","project")
            cursor = connection.cursor()
            update_query = "update inform set name = '%s', email = '%s', otherinfo = '%s' where id ='%d'"%(NAME,EMAIL,OTHERINFO,int(ID))
            try:
                cursor.execute(update_query)
                connection.commit()
                connection.close()
                self.load()
                self.clear()
                self.qmsg('Updated Successfully',0)
            except Exception as e:
                print('Exception : ',e)
        else:
            self.sound(1)
            self.qmsg("Check field again make sure field is not empty",1)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 439)
        MainWindow.setStyleSheet("*{\n"
"    background:url(:/background/wallpaper/background_black_shade.jpg);\n"
"}\n"
"QPushButton{\n"
"    background:white;\n"
"}\n"
"QLineEdit{\n"
"    color:rgb(238, 238, 236);\n"
"    border:2px solid rgb(136, 138, 133);\n"
"    border-radius:10px;    \n"
"    font: 13pt \"URW Gothic L\";\n"
"}\n"
"QLineEdit:hover{\n"
"    border:2px solid rgb(46, 52, 54);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(570, 90, 421, 321))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setGeometry(QtCore.QRect(50, 90, 111, 41))
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(180, 90, 361, 41))
        self.lineEdit_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(50, 150, 491, 41))
        self.lineEdit_email.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_info = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_info.setGeometry(QtCore.QRect(50, 210, 491, 41))
        self.lineEdit_info.setText("")
        self.lineEdit_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_info.setObjectName("lineEdit_info")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 10, 261, 51))
        self.label.setStyleSheet("QLabel{\n"
"    \n"
"    font: 63 30pt \"URW Gothic L\";\n"
"    color:white;\n"
"    background:transparent;\n"
"    border:none;\n"
"}")
        self.label.setObjectName("label")
        self.btn_previous = QtWidgets.QPushButton(self.centralwidget)
        self.btn_previous.setGeometry(QtCore.QRect(60, 350, 111, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/wallpaper/Btn_Previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_previous.setIcon(icon)
        self.btn_previous.setIconSize(QtCore.QSize(25, 50))
        self.btn_previous.setObjectName("btn_previous")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(420, 350, 111, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/wallpaper/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_clear.setIcon(icon1)
        self.btn_clear.setIconSize(QtCore.QSize(25, 50))
        self.btn_clear.setObjectName("btn_clear")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(240, 280, 121, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/wallpaper/Btn_update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_update.setIcon(icon2)
        self.btn_update.setIconSize(QtCore.QSize(25, 50))
        self.btn_update.setObjectName("btn_update")
        self.btn_next = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next.setGeometry(QtCore.QRect(240, 350, 121, 41))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/wallpaper/Btn_Next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next.setIcon(icon3)
        self.btn_next.setIconSize(QtCore.QSize(25, 50))
        self.btn_next.setObjectName("btn_next")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(420, 280, 111, 41))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/wallpaper/Btn_Delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon4)
        self.btn_delete.setIconSize(QtCore.QSize(25, 50))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(60, 280, 111, 41))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/wallpaper/Btn_Add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add.setIcon(icon5)
        self.btn_add.setIconSize(QtCore.QSize(30, 50))
        self.btn_add.setObjectName("btn_add")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.lineEdit_id.setDisabled(True)
        self.btn_add.clicked.connect(self.insert_record)
        self.btn_update.clicked.connect(self.update_record)
        self.btn_delete.clicked.connect(self.delete_record)
        self.btn_previous.clicked.connect(self.previous_position)
        self.btn_next.clicked.connect(self.next_position)
        self.btn_clear.clicked.connect(self.clear)
        self.load()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Inform"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "EMAIL"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "OTHER INFO"))
        self.lineEdit_id.setPlaceholderText(_translate("MainWindow", "ID"))
        self.lineEdit_name.setPlaceholderText(_translate("MainWindow", "Name"))
        self.lineEdit_email.setPlaceholderText(_translate("MainWindow", "Email"))
        self.lineEdit_info.setPlaceholderText(_translate("MainWindow", "Other Information"))
        self.label.setText(_translate("MainWindow", " 🅸🅽🅵🅾🆁🅼 "))
        self.btn_previous.setText(_translate("MainWindow", "Previous"))
        self.btn_clear.setText(_translate("MainWindow", "Clear"))
        self.btn_update.setText(_translate("MainWindow", "Update"))
        self.btn_next.setText(_translate("MainWindow", "Next"))
        self.btn_delete.setText(_translate("MainWindow", "Delete"))
        self.btn_add.setText(_translate("MainWindow", "Add"))


import img
