# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from DlibFunction import *
import pickle
import numpy as np
import multiprocessing
import pygame
import datetime
import cv2
from AlertSettings import Ui_Alert3
from PyQt5.QtWidgets import QMessageBox
import os
import pymysql
from Validation import Validation
# Load face encodings
with open('Dataset.dat', 'rb') as f:
	all_face_encodings = pickle.load(f)

# Grab the list of names and the list of encodings
face_names = list(all_face_encodings.keys())
face_encodingspkl = np.array(list(all_face_encodings.values()))

vol1=[]
name_list1 = []
name_con1 = []

curr_dt = datetime.datetime.now()

class Ui_Settings(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setStyleSheet("QLabel{\n"
"    \n"
"    font: 63 12pt \"URW Gothic L\";\n"
"    background:transparent;\n"
"    border:none;\n"
"}\n"
"QRadioButton{\n"
"    font: 63 15pt \"URW Gothic L\";\n"
"    background:none;\n"
"}\n"
"*{\n"
"    background:url(:/background/wallpaper/gray-background.jpg);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_preview = QtWidgets.QPushButton(self.centralwidget)
        self.btn_preview.setGeometry(QtCore.QRect(920, 640, 141, 41))
        self.btn_preview.setObjectName("btn_preview")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(670, 640, 161, 41))
        self.btn_save.setObjectName("btn_save")
        self.label_img1 = QtWidgets.QLabel(self.centralwidget)
        self.label_img1.setGeometry(QtCore.QRect(660, 80, 641, 481))
        self.label_img1.setStyleSheet("QLabel{\n"
"    background: rgba(0, 0, 0,0.5);\n"
"    border: 3px solid rgb(211, 215, 207);\n"
"    color:rgb(186, 189, 182);\n"
"    font-size:35px;\n"
"    \n"
"}")
        self.label_img1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img1.setObjectName("label_img1")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 0, 241, 71))
        self.label_7.setStyleSheet("QLabel{\n"
"    \n"
"    font: 25 38pt \"Ubuntu\";\n"
"}")
        self.label_7.setObjectName("label_7")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 440, 581, 221))
        self.frame_2.setStyleSheet("QFrame{\n"
"    border:1px solid red;\n"
"}\n"
"QLabel{\n"
"    font: 63 10pt \"URW Gothic L\";\n"
"    border:none;\n"
"    background:none;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(40, 110, 151, 41))
        self.label_4.setStyleSheet("QLabel{\n"
"    font-size:17px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.lineEdit_upsample = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_upsample.setGeometry(QtCore.QRect(220, 120, 161, 31))
        self.lineEdit_upsample.setObjectName("lineEdit_upsample")
        self.lineEdit_distort = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_distort.setGeometry(QtCore.QRect(220, 160, 161, 31))
        self.lineEdit_distort.setObjectName("lineEdit_distort")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(40, 150, 121, 41))
        self.label_5.setStyleSheet("QLabel{\n"
"    font-size:17px;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(70, 10, 491, 31))
        self.label_6.setStyleSheet("QLabel{\n"
"    font-size:15px;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 561, 31))
        self.label_8.setStyleSheet("QLabel{\n"
"    font-size:15px;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 551, 31))
        self.label_9.setStyleSheet("QLabel{\n"
"    font-size:15px;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.label_10.setStyleSheet("QLabel{\n"
"    font-size:17px;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 80, 581, 191))
        self.frame.setStyleSheet("QFrame{\n"
"    border:1px solid rgb(115, 210, 22);\n"
"}\n"
"QLabel{\n"
"    border:none;\n"
"    background:none;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_value = QtWidgets.QLabel(self.frame)
        self.label_value.setGeometry(QtCore.QRect(270, 100, 41, 17))
        self.label_value.setStyleSheet("QLabel{\n"
"    font-size:20px;\n"
"}")
        self.label_value.setObjectName("label_value")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 10, 211, 31))
        self.label.setStyleSheet("QLabel{\n"
"    font-size:22px;\n"
"}")
        self.label.setObjectName("label")
        self.horizontalSlider = QtWidgets.QSlider(self.frame)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 50, 511, 41))
        self.horizontalSlider.setStyleSheet("QhorizontalSlider{\n"
"    color:black;\n"
"}")
        self.horizontalSlider.setMinimum(40)
        self.horizontalSlider.setMaximum(60)
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setSliderPosition(50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(90, 140, 81, 41))
        self.label_14.setStyleSheet("QLabel{\n"
"    font-size:22px;\n"
"}")
        self.label_14.setObjectName("label_14")
        self.radioButton_hog = QtWidgets.QRadioButton(self.frame)
        self.radioButton_hog.setGeometry(QtCore.QRect(220, 150, 71, 23))
        self.radioButton_hog.setStyleSheet("")
        self.radioButton_hog.setObjectName("radioButton_hog")
        self.radioButton_cnn = QtWidgets.QRadioButton(self.frame)
        self.radioButton_cnn.setGeometry(QtCore.QRect(330, 150, 81, 23))
        self.radioButton_cnn.setObjectName("radioButton_cnn")
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/wallpaper/Btn_Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setIconSize(QtCore.QSize(80, 80))
        self.btn_back.setObjectName("btn_back")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(29, 280, 581, 151))
        self.frame_3.setStyleSheet("QCheckBox{\n"
"    \n"
"    font: 63 13pt \"URW Gothic L\";\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox.setGeometry(QtCore.QRect(20, 10, 161, 41))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 80, 171, 41))
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalSlider_reset = QtWidgets.QSlider(self.frame_3)
        self.horizontalSlider_reset.setGeometry(QtCore.QRect(210, 20, 311, 21))
        self.horizontalSlider_reset.setMinimum(15)
        self.horizontalSlider_reset.setMaximum(60)
        self.horizontalSlider_reset.setProperty("value", 30)
        self.horizontalSlider_reset.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_reset.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_reset.setTickInterval(1)
        self.horizontalSlider_reset.setObjectName("horizontalSlider_reset")
        self.horizontalSlider_mail = QtWidgets.QSlider(self.frame_3)
        self.horizontalSlider_mail.setGeometry(QtCore.QRect(210, 90, 311, 21))
        self.horizontalSlider_mail.setMinimum(10)
        self.horizontalSlider_mail.setMaximum(30)
        self.horizontalSlider_mail.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_mail.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_mail.setTickInterval(1)
        self.horizontalSlider_mail.setObjectName("horizontalSlider_mail")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(360, 50, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_reset = QtWidgets.QLabel(self.frame_3)
        self.label_reset.setGeometry(QtCore.QRect(330, 50, 31, 17))
        self.label_reset.setObjectName("label_reset")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(360, 120, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_mail = QtWidgets.QLabel(self.frame_3)
        self.label_mail.setGeometry(QtCore.QRect(330, 120, 31, 17))
        self.label_mail.setObjectName("label_mail")
        self.lineEdit_fn = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fn.setGeometry(QtCore.QRect(660, 560, 551, 31))
        self.lineEdit_fn.setStyleSheet("QLineEdit{\n"
"    border-radius:none;\n"
"    padding-left:5px;\n"
"}")
        self.lineEdit_fn.setObjectName("lineEdit_fn")
        self.btn_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_file.setGeometry(QtCore.QRect(1220, 560, 31, 31))
        self.btn_file.setStyleSheet("QPushButton{\n"
"border:none;\n"
"background:none;\n"
"}")
        self.btn_file.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/wallpaper/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_file.setIcon(icon1)
        self.btn_file.setIconSize(QtCore.QSize(25, 25))
        self.btn_file.setObjectName("btn_file")
        self.btn_delfn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delfn.setGeometry(QtCore.QRect(1260, 560, 31, 31))
        self.btn_delfn.setStyleSheet("QPushButton{\n"
"background:transparent;\n"
"border:none;\n"
"}")
        self.btn_delfn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/wallpaper/btn_del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delfn.setIcon(icon2)
        self.btn_delfn.setIconSize(QtCore.QSize(25, 25))
        self.btn_delfn.setObjectName("btn_delfn")
        self.btn_default = QtWidgets.QPushButton(self.centralwidget)
        self.btn_default.setGeometry(QtCore.QRect(1150, 640, 141, 41))
        self.btn_default.setObjectName("btn_default")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.horizontalSlider.valueChanged.connect(self.threshold)
        self.horizontalSlider_reset.valueChanged.connect(self.reset)
        self.horizontalSlider_mail.valueChanged.connect(self.mail)
        self.radioButton_hog.setChecked(True)
        # self.radioButton_cam1.setChecked(True)
        self.btn_preview.clicked.connect(self.controlTimer)
        #self.btn_save.clicked.connect(self.save_chg)
        self.checkBox.setChecked(True)
        self.checkBox_2.setChecked(True)
        self.btn_file.clicked.connect(self.add_video)
        self.btn_delfn.clicked.connect(self.del_video)
        self.btn_default.clicked.connect(self.defaultsetting)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Settings"))
        self.btn_preview.setText(_translate("MainWindow", "Start"))
        self.btn_save.setText(_translate("MainWindow", "Save"))
        self.label_img1.setText(_translate("MainWindow", "Preview"))
        self.label_7.setText(_translate("MainWindow", "SETTINGS"))
        self.label_4.setText(_translate("MainWindow", "UpSample Image"))
        self.label_5.setText(_translate("MainWindow", "Distort Image"))
        self.label_6.setText(_translate("MainWindow", " This setting will cause everything to run much more slower or some-"))
        self.label_8.setText(_translate("MainWindow", "-times it will crash the application, if the System Specification  is low."))
        self.label_9.setText(_translate("MainWindow", "* Alteast CPU Clock Speed Should be above 3.5GHZ."))
        self.label_10.setText(_translate("MainWindow", "Note :"))
        self.label_value.setText(_translate("MainWindow", "0.50"))
        self.label.setText(_translate("MainWindow", "Change Threshold "))
        self.label_14.setText(_translate("MainWindow", "Model :"))
        self.radioButton_hog.setText(_translate("MainWindow", "HOG"))
        self.radioButton_cnn.setText(_translate("MainWindow", "CNN"))
        self.checkBox.setText(_translate("MainWindow", "Reset Counter"))
        self.checkBox_2.setText(_translate("MainWindow", "Automatic Mail"))
        self.label_2.setText(_translate("MainWindow", "Seconds"))
        self.label_reset.setText(_translate("MainWindow", "15"))
        self.label_3.setText(_translate("MainWindow", "Seconds"))
        self.label_mail.setText(_translate("MainWindow", "10"))
        self.lineEdit_fn.setPlaceholderText(_translate("MainWindow", "Choose Video"))
        self.btn_default.setText(_translate("MainWindow", "Default Setting"))

    def del_video(self):
        self.path =''
        self.filename=''
        self.fileName = ''
        self.lineEdit_fn.setText('')
        self.label_img1.clear()
        self.label_img1.setText('Preview')

    def qmsg(self, msg, check):
        qmsgBox = QMessageBox()
        qmsgBox.move(((qmsgBox.width()) // 2 + 60), ((qmsgBox.height()) // 2 - 50))
        qmsgBox.setStyleSheet(
            'QMessageBox {background-color: #2b5b84; color: white;}\nQLabel{color: white;}\nQPushButton{color: white; font-size: 16px; background-color: #1d1d1d; border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: #2b5b84;}')
        if check == 0:
            QMessageBox.information(qmsgBox, 'PyQt5 message', msg)

        else:
            QMessageBox.critical(qmsgBox, 'PyQt5 message', msg)

    def add_video(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "","Image Files (*.avi)")  # Ask for filez
        inputFilepath = self.fileName
        filename_w_ext = os.path.basename(inputFilepath)
        filename, file_extension = os.path.splitext(filename_w_ext)
        # filename = foobar
        # file_extension = .txt
        self.path, self.filename = os.path.split(self.fileName)
        self.lineEdit_fn.setText(self.fileName)

    def threshold(self):
        size = str(self.horizontalSlider.value())
        self.label_value.setText('0.'+size)
        self.chgval_threshold = float('0.'+size)
        self.chg_flag_T = 0

    def reset(self):
        size = str(self.horizontalSlider_reset.value())
        self.label_reset.setText(size)
        self.chgval_reset = int(size)
        self.chg_flag_R = 0

    def mail(self):
        size = str(self.horizontalSlider_mail.value())
        self.label_mail.setText(size)
        self.chgval_mail = int(size)
        self.chg_flag_M = 0

    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.btn_save.setText('Stop')
            self.cap1 = cv2.VideoCapture(self.fileName)
            self.frame_counter = 0
            # start timer
            self.timer.start(20)
            curr = datetime.datetime.now()
            sec1 = int(curr.strftime("%S"))


        # if timer is started
        else:
            self.btn_save.setText('Start')
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap1.release()
            #self.cap2.release()

    curr = None
    sec1 = None

    #sec_mail = 10
    #add_sec1 = 30 + sec1
    chg_flag_T = None
    chg_flag_R = None
    chg_flag_M = None

    def defaultsetting(self):
        self.horizontalSlider.setValue(50)
        self.horizontalSlider_mail.setValue(10)
        self.horizontalSlider_reset.setValue(30)
        self.lineEdit_upsample.setText('1')
        self.lineEdit_distort.setText('1')

    def showsettings(self,uname):
        connection = pymysql.connect('localhost', 'root', 'rootpass', 'project')
        cursor = connection.cursor()
        select_query = "select * from settings where uname = '%s'" % (uname)
        cursor.execute(select_query)
        row = cursor.fetchone()
        self.horizontalSlider.setValue(int(row[0]))
        model = row[1]
        if 'hog' == model:
            self.radioButton_hog.setChecked(True)
        else:
            self.radioButton_cnn.setChecked(True)
        self.horizontalSlider_mail.setValue(row[3])
        self.horizontalSlider_reset.setValue(int(row[2]))
        self.lineEdit_upsample.setText(str(row[4]))
        self.lineEdit_distort.setText(str(row[5]))

    def cam1_counter(self):
        curr_time = datetime.datetime.now()
        sec_match = int(curr_time.strftime("%S"))


        if self.add_sec1 >= 60:
            self.add_sec1 = self.add_sec1 - 60

        print(str(sec_match) + '  ' + str(self.add_sec1))
        if sec_match == self.add_sec1:
            vol1.clear()
            name_con1.clear()
            name_list1.clear()
            self.add_sec1 = self.chgval_reset + self.add_sec1

    def __init__(self):
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)

    def viewCam(self):
        try:

            P1 = multiprocessing.Process(target=self.cam1_show())
            P2 = multiprocessing.Process(target=self.cam1_core())
            P1.start()
            P2.start()
            if self.checkBox.isChecked():
                P3 = multiprocessing.Process(target=self.cam1_counter())
                P3.start()

        except Exception:
            self.timer.stop()
            self.cap1.release()
            self.label_img1.clear()
            self.btn_save.setText('Start')

    def cam1_show(self):
        dt = datetime.datetime.now()
        current_time = dt.strftime("%I:%M:%S %p")
        # read image in BGR format
        ret, image = self.cap1.read()


        NAME = 'CAPTURE'
        Name_X_pos = 5
        Name_y_pos = 40
        cv2.rectangle(image, (Name_X_pos - 2, Name_y_pos - 100),
                      (Name_X_pos + 70 + (len(current_time) * 8), Name_y_pos - 5), (0, 0, 0),
                      -2)  # Draw a Black Rectangle over the face frame
        cv2.rectangle(image, (Name_X_pos - 2, Name_y_pos - 100),
                      (Name_X_pos + 70 + (len(current_time) * 8), Name_y_pos - 5), [255, 255, 255], 1)
        cv2.putText(image, str(current_time), (Name_X_pos + 5, Name_y_pos - 14), cv2.FONT_HERSHEY_DUPLEX, .7,
                    [255, 255, 255])

        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.label_img1.setPixmap(QPixmap.fromImage(qImg))

    def save_chg(self,UNAME):
        obj = Validation()
        self.num2 = self.lineEdit_upsample.text()
        self.num1 = self.lineEdit_distort.text()
        if obj.check_scaled(self.num2):
            self.num2=self.num2

        else:
            self.num2=1
            self.qmsg(' Your System Specification is low', 1)
            self.lineEdit_upsample.setStyleSheet("QLineEdit{\n"
                                                 "    background:transparent;\n"
                                                 "    border:1px solid red;\n"
                                                 "}")

        if obj.check_distort(self.num1):
            self.num1=self.num1
        else:
            self.num1=1
            self.qmsg(' Your System Specification is low', 1)
            self.lineEdit_distort.setStyleSheet("QLineEdit{\n"
                                                "    background:transparent;\n"
                                                "    border:1px solid red;\n"
                                                "}")

        if self.radioButton_cnn.isChecked():
            self.model = "cnn"
        else:
            self.model = "hog"

        self.db(UNAME)

    def db(self,UNAME):
        THRESOLD = self.horizontalSlider.value()
        MODEL = self.model
        RESETCOUNTER = self.horizontalSlider_reset.value()
        AUTOMAIL = self.horizontalSlider_mail.value()
        SCALED = self.num2
        DISTORT = self.num1

        connection = pymysql.connect('localhost', 'root', 'rootpass', 'project')
        cursor = connection.cursor()
        select_query = "select * from settings where uname = '%s'"%(UNAME)
        cursor.execute(select_query)
        row = cursor.fetchone()
        if row[6]==UNAME:
            #update
            update_query = "update settings set thresold = %d, model = '%s', resetcounter = %d, automail = %d, scaled = %d, distort = %d where uname ='%s'" \
                           % (THRESOLD, MODEL, RESETCOUNTER,AUTOMAIL, int(SCALED), int(DISTORT), UNAME)
            cursor.execute(update_query)
            connection.commit()

        else:
            #insert
            insert_query = "insert into settings(thresold,model,resetcounter,automail,scaled,distort,uname) values(%d,'%s',%d,%d,%d,%d,'%s')" \
                           % (THRESOLD, MODEL, RESETCOUNTER, AUTOMAIL, int(SCALED), int(DISTORT), UNAME)
            cursor.execute(insert_query)
            connection.commit()
        connection.close()






    def cam1_core(self):
        dt = datetime.datetime.now()
        count = 0
        # Grab a single frame of video
        ret, frame1 = self.cap1.read()
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame1 = frame1[:, :, ::-1]
        # Find all the faces and face enqcodings in the frame of video
        face_locations1 = face_locations(rgb_frame1, int(self.num2), self.model)
        face_encodings1 = face_encodings(rgb_frame1, face_locations1, int(self.num1))
        # Loop through each face in this frame of video
        for (top, right, bottom, left), face_encoding1 in zip(face_locations1, face_encodings1):
            # See if the face is a match for the known face(s)
            matches = compare_faces(face_encodingspkl, face_encoding1, self.chgval_threshold)
            name = "Unknown"
            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = face_names[first_match_index]

            if name != "Unknown":
                self.window = QtWidgets.QMainWindow()
                if self.checkBox.isChecked():
                    vol1.append(name)
                    name2 = name + '_' + str(dt) + str('.jpg')
                    print(vol1)
                    for num in vol1:
                        if num not in name_list1:
                            name_list1.append(num)
                            name_con1.append(True)
                            count = len(name_list1) - 1
                        else:
                            vol1.clear()

                    if name_con1[count]:
                        cv2.imwrite('Monitor/Registered/' + '/' + name + '/' + name2, frame1)
                        print('Name  : ', name_list1, '   Condition    : ', name_con1)
                        name_con1[count] = False

                        self.ui = Ui_Alert3(self.chgval_mail)
                        self.ui.setupUi(self.window)
                        self.ui.display_profile(name, name2)
                        self.window.show()
                        if self.checkBox_2.isChecked():
                            self.ui.controlTimer()

                else:
                    name2 = name + '_' + str(dt) + str('.jpg')
                    cv2.imwrite('Monitor/Registered/' + '/' + name + '/' + name2, frame1)
                    ui = Ui_Alert3(self.chgval_mail)
                    ui.setupUi(self.window)
                    ui.display_profile(name, name2)
                    self.window.show()
                    if self.checkBox_2.isChecked():
                        ui.controlTimer()

import img
