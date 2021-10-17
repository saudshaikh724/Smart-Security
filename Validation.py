import re
from PyQt5.QtWidgets import QMessageBox
import pygame
import pymysql
class Validation(object):

    def check_name(self,name,flname):
        if re.search('(\A[a-zA-Z]\D[a-zA-Z]*\Z)',name):
            return True
        else:
            self.qmsg(flname+' is not valid',1)
            return False



    def check_for_symbol(self,email):
        if re.search("[@.]", email) is None:
            return False
        else:
            return True


    def check_length(self, num, length):
        if len(num) >= length:
            return True
        else:
            return False


    def check_email_exist(self,email):
        connection = pymysql.connect("localhost", "root", "rootpass", "project")
        cursor = connection.cursor()
        cursor.execute("select count(*) from signup")
        row = cursor.fetchone()
        total_row = int(row[0])
        if total_row==0:
            self.check_email(email)
        else:
            sql = "Select * from signup where email='%s'" % (email)
            cursor.execute(sql)
            result = cursor.fetchall()
            if int(len(result)) == 0:
                self.check_email(email)
            else:
                self.qmsg("Email Already Exist", 1)

    def email_exist_signup(self,email):
        connection = pymysql.connect("localhost", "root", "rootpass", "project")
        cursor = connection.cursor()
        count = cursor.execute('select * from signup where email=%s',email)
        if count == 0:
            symbol = self.check_for_symbol(email)
            length = self.check_length(email, 12)
            if length is False or symbol is False:
                self.qmsg("Your email is not valid.", 1)
                return False

            if length and symbol is True:
                return True
        else:
            print('exist')
            self.qmsg("Email Already Exist",1)

    def email_exist_inform(self,email):
        connection = pymysql.connect("localhost", "root", "rootpass", "project")
        cursor = connection.cursor()
        count = cursor.execute('select * from inform where email=%s',email)
        if count == 0:
            symbol = self.check_for_symbol(email)
            length = self.check_length(email, 12)
            if length is False or symbol is False:
                self.qmsg("Your email is not valid.", 1)
                return False

            if length and symbol is True:
                return True
        else:
            print('exist')
            self.qmsg("Email Already Exist",1)

    def check_email(self,email):
        symbol = self.check_for_symbol(email)
        length = self.check_length(email, 12)
        if length is False or symbol is False:
            self.qmsg("Your email is not valid.", 1)
            return False

        if length and symbol is True:
            return True


    def check_age(self,age):

        if re.search('(^([1-9]\d?)?$)', age) and age != '':


            if (int(age) >= 18 and int(age) <= 60):
                return True
            elif (int(age)<18 and int(age)>=61):
                self.qmsg("Age should be between 18 to 60", 1)
                return False
        else:
            self.qmsg("Your age is not valid.",1)
            return False

    def check_distort(self,num):
        num = int(num)
        if (num>=1 and num<=100):
            return True
        elif (num<=0 or num>100):
                self.qmsg("Distort value should be between 1 to 100",1)
                return False
        else:
            self.qmsg('Number is not valid',1)
            return False

    def check_scaled(self,num):
        num = int(num)
        if num==1 or num==2:
            return True
        elif (num<1 or num>2):
            self.qmsg("Scaled value should be between 1 and 2",1)
            return False
        else:
            self.qmsg('Number is not valid',1)
            return False

    def check_pss(self,pwd):
        pass_len = self.check_length(pwd, 10)
        pss = pwd
        pass_bolean = pss.isalnum()
        if pass_len and pass_bolean:
            return True
        else:
            self.qmsg("Password must be atleast 10 Alphanumeric character", 1)
            return False

    def check_uname(self,uname):
        uname_len = self.check_length(uname, 8)
        uname_bolean = uname.isalnum()
        if uname_len and uname_bolean:
            #self.qmsg("Username must be atleast 8 Alphanumeric character", 1)
            return True
        else:
            self.qmsg("Username must be atleast 8 Alphanumeric character", 1)
            return False

    def qmsg(self,msg,check):
        qmsgBox = QMessageBox()
        qmsgBox.move(((qmsgBox.width()) // 2+60) , ((qmsgBox.height()) // 2- 50))
        qmsgBox.setStyleSheet(
                    'QMessageBox {background-color: #2b5b84; color: white;}\nQLabel{color: white;}\nQPushButton{color: white; font-size: 16px; background-color: #1d1d1d; border-radius: 10px; padding: 10px; text-align: center;}\n QPushButton:hover{color: #2b5b84;}')
        if check == 0:

            QMessageBox.information(qmsgBox, 'Message', msg)
        else:
            self.sound(1)
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

