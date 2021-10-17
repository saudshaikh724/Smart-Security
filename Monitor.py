# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from DlibFunction import *
from PyQt5.QtWidgets import QMessageBox
import pickle
import numpy as np
import multiprocessing
import pygame
import datetime
import time
import pymysql
import cv2
from Alert_Area1 import Ui_Alert1
from Alert_Area2 import Ui_Alert2

# Load face encodings
with open('Dataset.dat','rb') as f:
	all_face_encodings = pickle.load(f)

# Grab the list of names and the list of encodings
face_names = list(all_face_encodings.keys())
face_encodingspkl = np.array(list(all_face_encodings.values()))

vol1=[]
name_list1 = []
name_con1 = []

curr_dt = datetime.datetime.now()
fourcc = cv2.VideoWriter_fourcc(*'XVID')
obj_detect1 = cv2.VideoWriter('rec/Area1_'+str(curr_dt)+'.avi', fourcc, 20.0, (640, 480))
obj_detect2 = cv2.VideoWriter('rec/Area2_'+str(curr_dt)+'.avi', fourcc, 20.0, (640, 480))


class Ui_Monitor(object):
    add_sec1= None
    rec_flag1 = None
    rec_flag2 = None

    def sound(self, check):

        if check == 0:
            pygame.mixer.init()
            pygame.mixer.music.load('Sound/login.mp3')
            pygame.mixer.music.play(0)

        else:
            pygame.mixer.init()
            pygame.mixer.music.load('Sound/error.mp3')
            pygame.mixer.music.play(0)

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
            self.add_sec1 = 20 + self.add_sec1

    def __init__(self):
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 768)
        MainWindow.setStyleSheet("*{\n"
"    background:url(:/background/wallpaper/monitor_720.jpg);;\n"
"}\n"
"QLabel{\n"
"    border:1px solid black;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_img1 = QtWidgets.QLabel(self.centralwidget)
        self.label_img1.setGeometry(QtCore.QRect(20, 90, 651, 491))
        self.label_img1.setStyleSheet("QLabel{\n"
"    background: rgba(0, 0, 0,0.5);\n"
"    border: 3px solid rgb(211, 215, 207);\n"
"    color:rgb(186, 189, 182);\n"
"    font-size:35px;\n"
"    \n"
"}")
        self.label_img1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img1.setObjectName("label_img1")
        self.label_img2 = QtWidgets.QLabel(self.centralwidget)
        self.label_img2.setGeometry(QtCore.QRect(700, 90, 651, 491))
        self.label_img2.setStyleSheet("QLabel{\n"
"    background: rgba(0, 0, 0,0.5);\n"
"    border: 3px solid rgb(211, 215, 207);\n"
"    color:rgb(186, 189, 182);\n"
"    font-size:35px;\n"
"    \n"
"}")
        self.label_img2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img2.setObjectName("label_img2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 0, 301, 71))
        self.label.setStyleSheet("QLabel{\n"
"    color:rgb(211, 215, 207);\n"
"    font: 63 50pt \"URW Gothic L\";\n"
"    background:transparent;\n"
"    border:none;\n"
"}")
        self.label.setObjectName("label")
        self.btn_start_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start_stop.setGeometry(QtCore.QRect(630, 590, 111, 111))
        self.btn_start_stop.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    border:10px solid white;\n"
"    border-radius: 47px;\n"
"}")
        self.btn_start_stop.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/wallpaper/Start_Stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_start_stop.setIcon(icon)
        self.btn_start_stop.setIconSize(QtCore.QSize(110, 110))
        self.btn_start_stop.setObjectName("btn_start_stop")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.btn_back.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    border:none;    \n"
"}\n"
"QPushButton:hover{\n"
"    border:6px solid white;\n"
"    border-radius:25px;    \n"
"}")
        self.btn_back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/wallpaper/Btn_Back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_back.setIcon(icon1)
        self.btn_back.setIconSize(QtCore.QSize(70, 70))
        self.btn_back.setObjectName("btn_back")
        self.btn_cap2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cap2.setGeometry(QtCore.QRect(930, 620, 71, 71))
        self.btn_cap2.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    border:5px solid white;\n"
"    border-radius: 35px;\n"
"}")
        self.btn_cap2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/wallpaper/Image-Capture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cap2.setIcon(icon2)
        self.btn_cap2.setIconSize(QtCore.QSize(70, 70))
        self.btn_cap2.setObjectName("btn_cap2")
        self.btn_rec2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rec2.setGeometry(QtCore.QRect(1200, 620, 71, 71))
        self.btn_rec2.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    border:5px solid white;\n"
"    border-radius: 35px;\n"
"}")
        self.btn_rec2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/wallpaper/rec.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_rec2.setIcon(icon3)
        self.btn_rec2.setIconSize(QtCore.QSize(65, 65))
        self.btn_rec2.setObjectName("btn_rec2")
        self.btn_cap1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cap1.setGeometry(QtCore.QRect(350, 620, 71, 71))
        self.btn_cap1.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    border:5px solid white;\n"
"    border-radius: 35px;\n"
"}")
        self.btn_cap1.setText("")
        self.btn_cap1.setIcon(icon2)
        self.btn_cap1.setIconSize(QtCore.QSize(70, 70))
        self.btn_cap1.setObjectName("btn_cap1")
        self.btn_rec1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rec1.setGeometry(QtCore.QRect(80, 620, 71, 71))
        self.btn_rec1.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    border:5px solid white;\n"
"    border-radius: 35px;\n"
"}")
        self.btn_rec1.setText("")
        self.btn_rec1.setIcon(icon3)
        self.btn_rec1.setIconSize(QtCore.QSize(65, 65))
        self.btn_rec1.setObjectName("btn_rec1")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_start_stop.clicked.connect(self.controlTimer)

        self.btn_rec1.clicked.connect(self.record_1)
        self.btn_cap1.clicked.connect(self.capture_1)
        self.btn_rec2.clicked.connect(self.record_2)
        self.btn_cap2.clicked.connect(self.capture_2)

    def qmsg(self,msg,check):
        qmsgBox = QMessageBox()
        qmsgBox.move(((qmsgBox.width()) // 2+60) , ((qmsgBox.height()) // 2- 50))
        qmsgBox.setStyleSheet(
                    'QMessageBox {background-color: #2b5b84; color: white;}\nQLabel{color: white;}\nQPushButton{color: white; font-size: 16px; background-color: #1d1d1d; border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: #2b5b84;}')
        if check == 0:
            QMessageBox.information(qmsgBox, 'Success', msg)
        if check == 1:
            QMessageBox.critical(qmsgBox, 'Failed', msg)


    def getval(self,uname):
        connection = pymysql.connect('localhost', 'root', 'rootpass', 'project')
        cursor = connection.cursor()
        select_query = "select * from settings where uname = '%s'"%(uname)
        cursor.execute(select_query)
        row = cursor.fetchone()
        self.T = int(row[0])
        self.M = row[1]
        self.RC = int(row[2])
        self.AM = int(row[3])
        self.S= int(row[4])
        self.D= int(row[5])

    def capture_1(self):
        if self.timerflag== 0:
            self.cap_sound()
            self.cap_1('Cap1_')
        else:
            self.sound(1)
            self.qmsg("First Start Monitor and try again!", 1)
    def capture_2(self):
        if self.timerflag== 0:

            self.cap_sound()
            self.cap_2('Cap2_')
        else:
            self.sound(1)
            self.qmsg("First Start Monitor and try again!", 1)
    def cap_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Sound/cap.wav')
        pygame.mixer.music.play(0)

    def cap_1(self,capt):
        dt = datetime.datetime.now()
        ret, frame = self.cap1.read()
        cv2.imwrite('Monitor/Unknown/' +capt+ str(dt) + '.jpg', frame)


    def cap_2(self,capt):
        dt = datetime.datetime.now()
        ret, frame = self.cap2.read()
        cv2.imwrite('Monitor/Unknown/' +capt+ str(dt) + '.jpg', frame)

    def record_1(self):
        if self.timerflag==0:
            self.rec_sound()
            self.rec1()
        else:
            self.sound(1)
            self.qmsg("First Start Monitor and try again!",1)
    def record_2(self):
        if self.timerflag==0:
            self.rec_sound()
            self.rec2()
        else:
            self.sound(1)
            self.qmsg("First Start Monitor and try again!", 1)
    def rec_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Sound/rec.wav')
        pygame.mixer.music.play(0)

    def rec1(self):
        if self.rec_flag1 == 0:
            self.rec_flag1=1
            self.btn_rec1.setStyleSheet("QPushButton{\n"
                                                "    border:5px solid red;\n"
                                                "    border-radius: 35px;\n"
                                                "}")
        elif self.rec_flag1 == 1:
            self.rec_flag1 = 0
            obj_detect1.release()
            self.btn_rec1.setStyleSheet("QPushButton{\n"
                                        "    background:transparent;\n"
                                        "    border:none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    border:5px solid white;\n"
                                        "    border-radius: 35px;\n"
                                        "}")

    def rec_close1(self):
        obj_detect1.release()
        self.btn_rec1.setStyleSheet("QPushButton{\n"
                                        "    background:transparent;\n"
                                        "    border:none;\n"
                                        "}")

    def rec2(self):
        if self.rec_flag2 == 0:
            self.rec_flag2=1
            self.btn_rec2.setStyleSheet("QPushButton{\n"
                                                "    border:5px solid red;\n"
                                                "    border-radius: 35px;\n"
                                                "}")
        elif self.rec_flag2 == 1:
            self.rec_flag2 = 0
            obj_detect2.release()
            self.btn_rec2.setStyleSheet("QPushButton{\n"
                                        "    background:transparent;\n"
                                        "    border:none;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "    border:5px solid white;\n"
                                        "    border-radius: 35px;\n"
                                        "}")

    def rec_close2(self):
        obj_detect2.release()
        self.btn_rec2.setStyleSheet("QPushButton{\n"
                                        "    background:transparent;\n"
                                        "    border:none;\n"
                                        "}")


    def viewCam(self):
        P1 = multiprocessing.Process(target=self.cam1_show())
        P2 = multiprocessing.Process(target=self.cam1_core())
        P3 = multiprocessing.Process(target=self.cam1_counter())
        P4 = multiprocessing.Process(target=self.cam2_show())
        P5 = multiprocessing.Process(target=self.cam2_core())

        P1.start()
        P2.start()
        P3.start()
        P4.start()
        P5.start()



    def cam1_show(self):
        dt = datetime.datetime.now()
        current_time = dt.strftime("%I:%M:%S %p")
        # read image in BGR format
        ret, image = self.cap1.read()
        NAME = 'CAPTURE'
        Name_X_pos = 5
        Name_y_pos = 40
        cv2.rectangle(image, (Name_X_pos - 5, Name_y_pos - 40), (Name_X_pos + 70 + (len(current_time) * 8), Name_y_pos - 5),(0, 0, 0), -2)  # Draw a Black Rectangle over the face frame
        cv2.rectangle(image, (Name_X_pos - 5, Name_y_pos - 40), (Name_X_pos + 70 + (len(current_time) * 8), Name_y_pos - 5),[255,255,255], 1)
        cv2.putText(image, str(current_time), (Name_X_pos+5, Name_y_pos - 14), cv2.FONT_HERSHEY_DUPLEX, .7, [255,255,255])
        if self.rec_flag1 == 1:
            obj_detect1.write(image)

        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.label_img1.setPixmap(QPixmap.fromImage(qImg))

    def getval(self,uname):
        connection = pymysql.connect('localhost', 'root', 'rootpass', 'project')
        cursor = connection.cursor()
        select_query = "select * from settings where uname = '%s'"%(uname)
        cursor.execute(select_query)
        row = cursor.fetchone()
        self.T = int(row[0])
        self.M = row[1]
        self.RC = int(row[2])
        self.AM = int(row[3])
        self.S= int(row[4])
        self.D= int(row[5])

    def cam1_core(self):
        dt = datetime.datetime.now()
        count = 0
        # Grab a single frame of video
        ret, frame1 = self.cap1.read()
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame1 = frame1[:, :, ::-1]
        # Find all the faces and face enqcodings in the frame of video
        face_locations1 = face_locations(rgb_frame1,self.S,self.M)
        face_encodings1 = face_encodings(rgb_frame1, face_locations1,self.D)
        # Loop through each face in this frame of video
        for (top, right, bottom, left), face_encoding1 in zip(face_locations1, face_encodings1):
            # See if the face is a match for the known face(s)
            matches = compare_faces(face_encodingspkl, face_encoding1,float('0.'+str(self.T)))
            name = "Unknown"
            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = face_names[first_match_index]

            if name != "Unknown":
                self.rec_flag1 = 0
                self.rec_flag2 = 0
                self.rec1()
                self.rec2()
                vol1.append(name)
                name2 = name+'_'+str(dt)+str('.jpg')
                print(vol1)
                for num in vol1:
                    if num not in name_list1:
                        name_list1.append(num)
                        name_con1.append(True)
                        count = len(name_list1) - 1
                    else:
                        vol1.clear()

                if name_con1[count]:

                    cv2.imwrite('Monitor/Registered/'+'/'+name+'/'+name2,frame1)
                    print('Name  : ', name_list1, '   Condition    : ', name_con1)
                    name_con1[count] = False
                    self.window1 = QtWidgets.QMainWindow()
                    self.ui1 = Ui_Alert1(self.AM)
                    self.ui1.setupUi(self.window1)
                    self.ui1.display_profile(name,name2)
                    self.ui1.controlTimer()
                    self.window1.show()



    def cam2_show(self):
        dt = datetime.datetime.now()
        current_time = dt.strftime("%I:%M:%S %p")
        # read image in BGR format
        ret, image = self.cap2.read()
        NAME = 'CAPTURE'
        Name_X_pos = 5
        Name_y_pos = 40
        cv2.rectangle(image, (Name_X_pos - 5, Name_y_pos - 40),(Name_X_pos + 70 + (len(current_time) * 8), Name_y_pos - 5), (0, 0, 0),-2)  # Draw a Black Rectangle over the face frame
        cv2.rectangle(image, (Name_X_pos - 5, Name_y_pos - 40),(Name_X_pos + 70 + (len(current_time) * 8), Name_y_pos - 5), [255, 255, 255], 1)
        cv2.putText(image, str(current_time), (Name_X_pos+5, Name_y_pos - 14), cv2.FONT_HERSHEY_DUPLEX, .7, [255,255,255])
        if self.rec_flag2 == 1:
            obj_detect2.write(image)

        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.label_img2.setPixmap(QPixmap.fromImage(qImg))


    def cam2_core(self):
        dt = datetime.datetime.now()
        count = 0
        # Grab a single frame of video
        ret, frame1 = self.cap2.read()
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame1 = frame1[:, :, ::-1]
        # Find all the faces and face enqcodings in the frame of video
        face_locations1 = face_locations(rgb_frame1,self.S,self.M)
        face_encodings1 = face_encodings(rgb_frame1, face_locations1,self.D)
        # Loop through each face in this frame of video
        for (top, right, bottom, left), face_encoding1 in zip(face_locations1, face_encodings1):
            # See if the face is a match for the known face(s)
            matches = compare_faces(face_encodingspkl, face_encoding1,float('0.'+str(self.T)))
            name = "Unknown"
            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = face_names[first_match_index]

            if name != "Unknown":
                self.rec_flag1 = 0
                self.rec_flag2 = 0
                self.rec1()
                self.rec2()
                vol1.append(name)
                name2 = name+'_'+str(dt)+str('.jpg')
                print(vol1)
                for num in vol1:
                    if num not in name_list1:
                        name_list1.append(num)
                        name_con1.append(True)
                        count = len(name_list1) - 1
                    else:
                        vol1.clear()

                if name_con1[count]:
                    cv2.imwrite('Monitor/Registered/'+'/'+name+'/'+name2,frame1)
                    print('Name  : ', name_list1, '   Condition    : ', name_con1)
                    name_con1[count] = False
                    self.window2 = QtWidgets.QMainWindow()
                    self.ui2 = Ui_Alert2(self.AM)
                    self.ui2.setupUi(self.window2)
                    self.ui2.display_profile(name,name2)
                    self.ui2.controlTimer()
                    self.window2.show()
    timerflag=None
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            self.clicked_sound()
            # create video capture
            self.cap1 = cv2.VideoCapture(0)
            self.cap2 = cv2.VideoCapture(1)
            # start timer
            self.timer.start(20)
            self.rec_flag1 = 0
            self.rec_flag2 = 0
            self.timerflag=0
            curr = datetime.datetime.now()
            sec1 = int(curr.strftime("%S"))
            self.add_sec1 = 30 + sec1

        # if timer is started
        else:
            # stop timer
            self.clicked_sound()
            self.timer.stop()
            # release video capture
            self.cap1.release()
            self.cap2.release()
            self.rec_close1()
            self.rec_close2()
            self.label_img1.clear()
            self.label_img2.clear()
            self.label_img1.setText("Area 1")
            self.label_img2.setText("Area 2")
            self.timerflag=1

    def clicked_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Sound/godseye.wav')
        pygame.mixer.music.play(0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Monitor"))
        self.label_img1.setText(_translate("MainWindow", "Area 1"))
        self.label_img2.setText(_translate("MainWindow", "Area 2"))
        self.label.setText(_translate("MainWindow", "ᴍᴏɴɪᴛᴏʀ"))


import img
