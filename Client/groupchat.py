import socket
from PyQt6 import QtCore, QtGui, QtWidgets
from Ui_groupchat import *
import sys
import time
import ast
from PyQt6.QtWidgets import QWidget

class MyGroupChat(Ui_GroupChat, QWidget):
    def __init__(self, username:str, group:str,user,onlineusers,chalist ,soc, parent=None):
        '''
        初始化群聊界面
        传入参数在login.py中预处理过
        soc是一个socket对象，由login.py传入
        客户端所有的操作，都是基于这个对象，它作为一个全局变量，被所有的类共享
        '''
        super().__init__(parent)
        self.setupUi(self)
        self.onlineusers=set()
        self.username=username
        self.group=group
        self.soc=soc
        self.user=user
        self.onlineusers=onlineusers
        onlineusers=list(onlineusers)
        self.listWidget.addItems(onlineusers)
        for i in chalist:
            self.textBrowser_message.append("<b><font size='5'><font color='blue'>"+self.user[i[2]-1][1]+"</font>:"+(i[3])+"</font></b>") #显示历史消息，可使用html标签
        self.textBrowser_message.append("<b><font color='red' size ='5' align='center'>-----以上为历史消息------</font></b>")
        self.label_groups.setText(str(group)) #显示群组名
        self.label_users.setText(str(username)) #显示登录的用户名
        self.pushButton_send.clicked.connect(self.sendMsg)
        self.pushButton_refresh.clicked.connect(self.refresh)
        self.pushButton_exit.clicked.connect(self.exit)


    def handle_msg(self):
        '''
        处理消息
        这是一个被动的方法，它会一直等待服务器发来的消息
        '''
        try:
            while True:
                ee=self.soc.recv(1024).decode('utf-8')
                type=ee[:ee.find(',')] #截取第一个','之前的字符串，用于判断消息类型
                print(ee)
                if type=='onuser':
                    mes=ast.literal_eval(ee[ee.find(',')+1:])
                    self.onlineusers=mes
                    self.listWidget.clear()
                    onlineusers=list(self.onlineusers) #更新在线用户列表
                    self.listWidget.addItems(onlineusers)
                elif type=='mainlist':
                    self.user=ast.literal_eval(ee[ee.find(',')+1:]) #更新用户列表，作为消息的发送者的显示
                elif type=='newmes':
                    mes=ee.split(',') 
                    '''
                    更新消息，不同的是，这里的消息是服务器转发的，
                    而不是从数据库中读取的，所以它仅仅是一个字符串，只进行分割即可
                    '''
                    self.textBrowser_message.append("<b><font size='5'><font color='blue'>"+mes[1]+"</font>:"+mes[2]+"</font></b>")
        except Exception as e:
            print(e)

    def sendMsg(self):
        '''
        发送消息
        由按钮触发
        '''
        msg=self.textEdit.toPlainText()
        self.textEdit.clear()
        try:
            msg='mes'+','+self.group+','+self.username+','+msg
            self.soc.send(msg.encode('utf-8'))
            QtWidgets.QMessageBox.information(self, "提示", "发送成功！")
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.information(self, "提示", "发送失败！请检查网络连接！")
    def refresh(self): 
        '''刷新消息'''
        try:
            req='refresh'+','+self.group
            self.soc.send(req.encode('utf-8'))
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.information(self, "提示", "刷新失败！请检查网络连接！")
    def exit(self):
        '''退出'''
        self.soc.close()
        self.close()