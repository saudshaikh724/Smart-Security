# -*- coding: utf-8 -*-

import time
from DlibFunction import *
import pickle
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer



class Ui_Encode(object):
    def __init__(self):

        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.onButtonClick)



    def controlTimer(self):
        if not self.timer.isActive():
            self.timer.start(20)

    def onButtonClick(self):
        all_face_encodings = {}

        images = os.listdir('Registered')
        count_img = len(images)
        inc = 0
        count = 0
        self.progressBar.setValue(inc)

        for image in images:
            # load the image
            time.sleep(0.5)
            current_image = load_image_file("Registered/" + image)
            filename, file_extension = os.path.splitext(image)
            self.label_2.setText('Encoding . . . . . . . . . . . . . '+str(filename))
            all_face_encodings[filename] = face_encodings(current_image)[0]
            step =(100 / count_img)
            inc = inc + step
            self.progressBar.setValue(inc)
            print(inc)
            time.sleep(0.5)
            count+=1
            print(count)
            if count == count_img:
                self.label.setText('Completed!')
                self.label_2.setText(str(count)+' images Successfully Encoded')


        with open('Dataset.dat', 'wb') as f:
            print(all_face_encodings)
            pickle.dump(all_face_encodings, f)
            self.timer.stop()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 180)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("*{\n"
"    \n"
"    background:rgb(85, 87, 83);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 100, 711, 41))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    \n"
"    color :white;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 721, 17))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    font: 63 11pt \"URW Gothic L\";\n"
"    color: rgb(138, 226, 52);\n"
"    font-size:20px;\n"
"    \n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 701, 21))
        self.label_2.setStyleSheet("QLabel{\n"
"    color: rgb(211, 215, 207);\n"
"font-size:18px;\n"
"}")
        self.label_2.setObjectName("label_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Encoding Image"))
        self.label.setText(_translate("MainWindow", "Wait..."))

        self.label_2.setText(_translate("MainWindow", "Checking files..."))



if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Encode()
    ui.setupUi(MainWindow)
    MainWindow.show()
    time.sleep(0.5)
    ui.controlTimer()
    sys.exit(app.exec_())
