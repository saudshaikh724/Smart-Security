from PyQt5 import QtWidgets
import pygame
import time

from Monitor import Ui_Monitor
from Homepage import Ui_Homepage
from Login import Ui_Login
from Signup import Ui_Signup
from BlockAcess import Ui_Blockacess
from Settings import Ui_Settings
from Forgot import Ui_Forgot
from Inform import Ui_Inform
from SendMail import Ui_Mail
from Encode import Ui_Encode
from Aboutus import Ui_About
from UserInfo import Ui_User

class Log(QtWidgets.QMainWindow, Ui_Login):
    def __init__(self, parent=None):
        super(Log, self).__init__(parent)
        self.setupUi(self)
        self.btn_signup.clicked.connect(self.hide)
        self.btn_fp.clicked.connect(self.hide)

class Sign(QtWidgets.QMainWindow, Ui_Signup):
    def __init__(self, parent=None):
        super(Sign, self).__init__(parent)
        self.setupUi(self)
        self.btn_login.clicked.connect(self.hide)

class Block(QtWidgets.QMainWindow, Ui_Blockacess):
    def __init__(self, parent=None):
        super(Block, self).__init__(parent)
        self.setupUi(self)
        self.btn_back.clicked.connect(self.hide)



class Mon(QtWidgets.QMainWindow, Ui_Monitor):
    def __init__(self, parent=None):
        super(Mon, self).__init__(parent)
        self.setupUi(self)
        self.btn_back.clicked.connect(self.hide)

class Mail(QtWidgets.QMainWindow, Ui_Mail):
    def __init__(self, parent=None):
        super(Mail, self).__init__(parent)
        self.setupUi(self)

class Home(QtWidgets.QMainWindow, Ui_Homepage):
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setupUi(self)
        self.btn_monitor.clicked.connect(self.hide)
        self.btn_blockacess.clicked.connect(self.hide)
        self.btn_settings.clicked.connect(self.hide)

class Set(QtWidgets.QMainWindow, Ui_Settings):
    def __init__(self, parent=None):
        super(Set, self).__init__(parent)
        self.setupUi(self)
        self.btn_back.clicked.connect(self.hide)

class For(QtWidgets.QMainWindow, Ui_Forgot):
    def __init__(self, parent=None):
        super(For, self).__init__(parent)
        self.setupUi(self)
        self.btn_login.clicked.connect(self.hide)

class Inf(QtWidgets.QMainWindow, Ui_Inform):
    def __init__(self, parent=None):
        super(Inf, self).__init__(parent)
        self.setupUi(self)

class Pg(QtWidgets.QMainWindow, Ui_Encode):
    def __init__(self, parent=None):
        super(Pg, self).__init__(parent)
        self.setupUi(self)

class User(QtWidgets.QMainWindow, Ui_User):
    def __init__(self, parent=None):
        super(User, self).__init__(parent)
        self.setupUi(self)

class About(QtWidgets.QMainWindow, Ui_About):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.setupUi(self)


class Manager:
    def __init__(self):
        self.obj1 = Home()
        self.obj2 = Mon()
        self.obj3 = Log()
        self.obj4 = Sign()
        self.obj5 = Block()
        self.obj6 = Set()
        self.obj7 = For()
        self.obj8 = Inf()
        self.obj9 = Mail()
        self.obj10 = Pg()
        self.obj11 = User()
        self.obj12 = About()
        self.obj1.btn_monitor.clicked.connect(self.Monitor)
        self.obj1.btn_blockacess.clicked.connect(self.Blockacess)
        self.obj1.btn_inform.clicked.connect(self.Inform)
        self.obj1.btn_settings.clicked.connect(self.Settings)
        self.obj1.btn_about.clicked.connect(self.obj12.show)
        self.obj2.btn_back.clicked.connect(self.obj1.show)
        self.obj3.btn_login.clicked.connect(self.check_1)
        self.obj3.btn_signup.clicked.connect(self.Signup)
        self.obj3.btn_fp.clicked.connect(self.Forgot)
        self.obj1.btn_signout.clicked.connect(self.check_2)
        self.obj4.btn_login.clicked.connect(self.Login)
        self.obj5.btn_back.clicked.connect(self.obj1.show)
        self.obj6.btn_back.clicked.connect(self.obj1.show)
        self.obj7.btn_login.clicked.connect(self.Login)
        self.obj1.btn_sndmail.clicked.connect(self.Mail)
        self.obj6.btn_save.clicked.connect(self.save)
        self.obj2.btn_start_stop.clicked.connect(self.mon_start)
        #self.obj4.btn_signup.clicked.connect(self.Sign)
        self.obj5.btn_encode.clicked.connect(self.bock)
        self.obj1.btn_userinfo.clicked.connect(self.Userinfo)
        self.obj3.show()
    def Userinfo(self):
        self.obj11.show()
        self.obj11.userinfo(self.uname)
        self.obj11.lock(True)

    def bock(self):
        self.obj10.show()
        time.sleep(0.5)
        self.obj10.controlTimer()

    def Sign(self):
        user = self.obj4.user
        value = self.obj4.value
        if value == 0:
            self.obj4.db(user)
    def mon_start(self):
        self.obj2.getval(self.uname)
        print('Inside Getval')

    def save(self):
        self.obj6.save_chg(self.uname)

    def Mail(self):
        self.obj9.lineEdit.setText('')
        self.obj9.label.clear()
        self.obj9.load()
        self.obj9.show()
        self.clicked_sound()

    def Monitor(self):
        self.obj2.show()
        self.clicked_sound()

    def Blockacess(self):
        self.obj5.show()
        self.clicked_sound()

    def Inform(self):
        self.obj8.show()
        self.clicked_sound()

    def Settings(self):
        self.clicked_sound()
        self.obj6.showsettings(self.uname)
        self.obj6.show()


    def Signup(self):
        self.obj4.show()
        self.Switch()

    def Forgot(self):
        self.obj7.show()
        self.Switch()

    def Login(self):
        self.obj3.show()
        self.Switch()

    def Switch(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Sound/switch.mp3')
        pygame.mixer.music.play(0)

    def clicked_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load('Sound/godseye.wav')
        pygame.mixer.music.play(0)


    def check_1(self):
        if self.obj3.flag == 0:
            self.obj3.flag = 1
            self.obj1.show()
            self.obj3.close()
            self.uname = self.obj3.user

    def check_2(self):
        if self.obj1.flag == 0:
            self.obj3.show()
            self.obj1.close()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())