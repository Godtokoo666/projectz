import socket
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from Ui_register import *
from login import MyLogin

class MyRegister(Ui_Dialog_Register, QtWidgets.QWidget):
    def __init__(self, soc,groupList,parent=None):
        '''初始化注册界面'''
        super().__init__(parent)
        self.setupUi(self)
        self.soc=soc
        self.grouplist=[x[1] for x in groupList]
        self.comboBox_grouplist.addItems(self.grouplist)
        self.pushButton_register.clicked.connect(self.Register)
        self.pushButton_login.clicked.connect(self.PointLogin)
    def Register(self):
        '''注册'''
        try:
            username=self.lineEdit_username.text()
            password=self.lineEdit_password.text()
            repassword=self.lineEdit_repassword.text()
            group=self.comboBox_grouplist.currentText()
            if username=='' or password=='':
                QtWidgets.QMessageBox.information(self, "提示", "用户名和密码不能为空！")
            else:
                if repassword != password:
                    QtWidgets.QMessageBox.information(self, "提示", "两次密码不一致！")
                    self.lineEdit_username.clear()
                    self.lineEdit_password.clear()
                    self.lineEdit_repassword.clear()
                    self.comboBox_grouplist.setCurrentIndex(0)
                else:
                    req='register'+','+username+','+password+','+group
                    self.soc.send(req.encode('utf-8'))
                    res=self.soc.recv(1024).decode('utf-8').split(',')
                    if res[1]=='True':
                        QtWidgets.QMessageBox.information(self, "提示", "注册成功！即将跳转登录界面！")
                        self.close()
                        self.login=MyLogin(self.soc) #注册成功后跳转登录界面,并把socket对象传入
                        self.login.show()
                    else:
                        QtWidgets.QMessageBox.information(self, "提示", "注册失败！请检查用户名和密码！")
                        self.lineEdit_username.clear()
                        self.lineEdit_password.clear()
                        self.lineEdit_repassword.clear()
                        self.comboBox_grouplist.setCurrentIndex(0)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.information(self, "提示", "注册失败！请检查网络连接！")
    def PointLogin(self):
        '''跳转登录'''
        self.close()
        self.login = MyLogin(self.soc) #跳转登录界面,并把socket对象传入
        self.login.show()