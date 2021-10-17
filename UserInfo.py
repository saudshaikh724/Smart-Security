# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Userinfo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtWidgets import QMessageBox
class Ui_User(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 435)
        MainWindow.setStyleSheet("*{\n"
"    background:rgb(46, 52, 54);\n"
"}\n"
"QLabel{\n"
"color:rgb(238, 238, 236);\n"
"}\n"
"QLineEdit{\n"
"    color:rgb(238, 238, 236);\n"
"    border:2px solid white;\n"
"    border-radius:10px;    \n"
"    font: 13pt \"URW Gothic L\";\n"
"    background:transparent;\n"
"}\n"
"QLineEdit:hover{\n"
"    border:2px solid rgb(0, 0, 0);\n"
"}\n"
"QRadioButton{\n"
"    border:none;\n"
"    background:none;\n"
"    color:rgb(238, 238, 236);\n"
"font: 13pt \"URW Gothic L\";\n"
"}\n"
"QPushButton{\n"
"    background:rgb(186, 189, 182);\n"
"}\n"
"QPushButton:hover{\n"
"    border:1px solid rgb(85, 87, 83);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 20, 301, 41))
        self.label.setStyleSheet("QLabel{\n"
"    font: 25pt \"URW Gothic L\";\n"
"    background:none;\n"
"    border:none;\n"
"}")
        self.label.setObjectName("label")
        self.lineEdit_fname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fname.setGeometry(QtCore.QRect(40, 90, 271, 41))
        self.lineEdit_fname.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_fname.setObjectName("lineEdit_fname")
        self.lineEdit_lname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_lname.setGeometry(QtCore.QRect(350, 90, 281, 41))
        self.lineEdit_lname.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_lname.setObjectName("lineEdit_lname")
        self.lineEdit_age = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_age.setGeometry(QtCore.QRect(40, 160, 271, 41))
        self.lineEdit_age.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.radioButton_m = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_m.setGeometry(QtCore.QRect(450, 170, 61, 23))
        self.radioButton_m.setObjectName("radioButton_m")
        self.radioButton_f = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_f.setGeometry(QtCore.QRect(540, 170, 81, 23))
        self.radioButton_f.setObjectName("radioButton_f")
        self.lineEdit_uname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_uname.setGeometry(QtCore.QRect(40, 230, 271, 41))
        self.lineEdit_uname.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_uname.setObjectName("lineEdit_uname")
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pwd.setGeometry(QtCore.QRect(360, 230, 271, 41))
        self.lineEdit_pwd.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.lineEdit_ea = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ea.setGeometry(QtCore.QRect(150, 300, 371, 41))
        self.lineEdit_ea.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ea.setObjectName("lineEdit_ea")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 170, 91, 21))
        self.label_2.setStyleSheet("QLabel{\n"
"    font: 14pt \"URW Gothic L\";\n"
"    background:none;\n"
"    border:none;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.btn_edit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edit.setGeometry(QtCore.QRect(190, 380, 121, 31))
        self.btn_edit.setObjectName("btn_edit")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(360, 380, 121, 31))
        self.btn_save.setObjectName("btn_save")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.lock(True)
        self.btn_edit.clicked.connect(self.lock,False)
        self.btn_save.clicked.connect(self.update_record)
        self.lineEdit_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
    def lock(self,boolean):
        self.lineEdit_lname.setDisabled(boolean)
        self.lineEdit_fname.setDisabled(boolean)
        self.lineEdit_age.setDisabled(boolean)
        self.radioButton_f.setDisabled(boolean)
        self.radioButton_m.setDisabled(boolean)
        self.lineEdit_uname.setDisabled(boolean)
        self.lineEdit_pwd.setDisabled(boolean)
        self.lineEdit_ea.setDisabled(boolean)


    def qmsg(self,msg,check):
        qmsgBox = QMessageBox()
        qmsgBox.move(((qmsgBox.width()) // 2+60) , ((qmsgBox.height()) // 2- 50))
        qmsgBox.setStyleSheet(
                    'QMessageBox {background-color: #2b5b84; color: white;}\nQLabel{color: white;}\nQPushButton{color: white; font-size: 16px; background-color: #1d1d1d; border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: #2b5b84;}')
        if check == 0:
            QMessageBox.information(qmsgBox, 'PyQt5 message', msg)
        if check == 1:
            QMessageBox.critical(qmsgBox, 'PyQt5 message', msg)

    def update_record(self):
        FNAME = self.lineEdit_fname.text()
        LNAME = self.lineEdit_lname.text()
        AGE = self.lineEdit_age.text()
        GENDER = None
        if self.radioButton_m.isChecked():
            GENDER="Male"
        else:
            GENDER="Female"
        UNAME = self.lineEdit_uname.text()
        PWD = self.lineEdit_pwd.text()
        EA = self.lineEdit_ea.text()
        connection = pymysql.connect("localhost","root","rootpass","project")
        cursor = connection.cursor()
        update_query = "update signup set fname = '%s', lname = '%s', age = %d, gender = '%s',uname = '%s', pwd = '%s',email = '%s' where uname ='%s'" \
        %(FNAME,LNAME,int(AGE),GENDER,UNAME,PWD,EA,UNAME)


        cursor.execute(update_query)
        connection.commit()
        connection.close()
        self.qmsg('Updated Successfully',0)



    def userinfo(self,UNAME):
        connection = pymysql.connect("localhost", "root", "rootpass", "project")
        cursor = connection.cursor()
        select_query = "select * from signup where uname = '%s'"%(UNAME)
        cursor.execute(select_query)
        row = cursor.fetchone()

        self.lineEdit_fname.setText(str(row[0]))
        self.lineEdit_lname.setText(row[1])
        self.lineEdit_age.setText(str(row[2]))
        self.lineEdit_uname.setText(row[4])
        self.lineEdit_pwd.setText(row[5])
        self.lineEdit_ea.setText(row[6])
        if self.radioButton_m.text() == row[3]:
            self.radioButton_m.setChecked(True)
        else:
            self.radioButton_f.setChecked(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "User Information"))
        self.label.setText(_translate("MainWindow", "ᴜsᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ"))
        self.lineEdit_fname.setPlaceholderText(_translate("MainWindow", "Firstname"))
        self.lineEdit_lname.setPlaceholderText(_translate("MainWindow", "Lastname"))
        self.lineEdit_age.setPlaceholderText(_translate("MainWindow", "Age"))
        self.radioButton_m.setText(_translate("MainWindow", "Male"))
        self.radioButton_f.setText(_translate("MainWindow", "Female"))
        self.lineEdit_uname.setPlaceholderText(_translate("MainWindow", "Username"))
        self.lineEdit_pwd.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lineEdit_ea.setPlaceholderText(_translate("MainWindow", "Email Address"))
        self.label_2.setText(_translate("MainWindow", "Gender:"))
        self.btn_edit.setText(_translate("MainWindow", "Edit"))
        self.btn_save.setText(_translate("MainWindow", "Save"))

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_User()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
