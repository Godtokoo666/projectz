import socket
from PyQt6 import QtCore, QtGui, QtWidgets
from Ui_groupchat import *
import sys
import time
import ast
from PyQt6.QtWidgets import QWidget

class MyGroupChat(Ui_GroupChat, QWidget):
    def __init__(self, username:str, group:str,user,onlineusers,chalist ,soc, parent=None):
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
            self.textBrowser_message.append("<b><font size='5'><font color='blue'>"+self.user[i[2]-1][1]+"</font>:"+(i[3])+"</font></b>")
        self.textBrowser_message.append("<b><font color='red' size ='5' align='center'>-----以上为历史消息------</font></b>")
            # self.soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            # self.soc.connect(('127.0.0.1',8099))
            # username='usr'+','+group+','+username
            # self.index=0
            # self.soc.send(username.encode('utf-8'))
            # self.onlineusers=ast.literal_eval(self.soc.recv(1024).decode('utf-8'))
            # mes=ast.literal_eval(self.soc.recv(1024).decode('utf-8'))
            # self.user=ast.literal_eval(self.soc.recv(1024).decode('utf-8'))
            # self.textBrowser_message.append("<b><font color='red'>欢迎来到群聊！</font></b>")
            # self.message=[]
            # for i in mes:
            #     if i[0]>self.index:
            #         self.index=i[0]
            #         self.textBrowser_message.append("<b><font size='5'><font color='blue'>"+self.user[i[2]-1][1]+"</font>:"+(i[3])+"</font></b>")
        self.label_groups.setText(str(group))
        self.label_users.setText(str(username))
        self.pushButton_send.clicked.connect(self.sendMsg)
        self.pushButton_refresh.clicked.connect(self.refresh)
        self.pushButton_exit.clicked.connect(self.exit)


    def handle_msg(self):
        try:
            while True:
                ee=self.soc.recv(1024).decode('utf-8')
                type=ee[:ee.find(',')]
                print(ee)
                if type=='onuser':
                    mes=ast.literal_eval(ee[ee.find(',')+1:])
                    self.onlineusers=mes
                    self.listWidget.clear()
                    onlineusers=list(self.onlineusers)
                    self.listWidget.addItems(onlineusers)
                elif type=='mainlist':
                    self.user=ast.literal_eval(ee[ee.find(',')+1:])
                elif type=='newmes':
                    mes=ee.split(',')
                    self.textBrowser_message.append("<b><font size='5'><font color='blue'>"+mes[1]+"</font>:"+mes[2]+"</font></b>")
        except Exception as e:
            print(e)

    def sendMsg(self):
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
        try:
            req='refresh'+','+self.group
            self.soc.send(req.encode('utf-8'))
            # QtWidgets.QMessageBox.information(self, "提示", "刷新成功！")
            # self.onlineusers=ast.literal_eval(self.soc.recv(1024).decode('utf-8'))
            # self.listWidget.clear()
            # self.listWidget.addItems(self.onlineusers)
            # mes=self.soc.recv(1024).decode('utf-8')
            # if mes[:3]=='':
            #     for i in mes: 
            #         if i[0]>self.index:
            #             self.index=i[0]
            #             self.textBrowser_message.append("<b><font size='5'><font color='blue'>"+self.user[i[2]-1][1]+"</font>:"+(i[3])+"</font></b>")
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.information(self, "提示", "刷新失败！请检查网络连接！")
    def exit(self):
        self.soc.close()
        self.close()