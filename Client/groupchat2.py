import socket
from PyQt6 import QtCore, QtGui, QtWidgets
from Ui_groupchat import *
import sys
import ast
import threading

class MyGroupChat(Ui_GroupChat, QtWidgets.QWidget):
    def __init__(self, username:str, group:str, parent=None):
        super(MyGroupChat, self).__init__(parent)
        self.setupUi(self)
        self.onlineusers=set()
        self.username=username
        self.group=group
        try:
            self.soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.soc.connect(('127.0.0.1',8099))
            username='usr'+','+group+','+username
            self.index=0
            self.soc.send(username.encode('utf-8'))
            self.onlineusers=ast.literal_eval(self.soc.recv(1024).decode('utf-8'))
            mes=ast.literal_eval(self.soc.recv(1024).decode('utf-8'))
            self.user=ast.literal_eval(self.soc.recv(1024).decode('utf-8'))
            self.textBrowser_message.append("<b><font color='red'>欢迎来到群聊！</font></b>")
            self.message=[]
            for i in mes:
                if i[0]>self.index:
                    self.index=i[0]
                    self.textBrowser_message.append("<b><font size='5'><font color='blue'>"+self.user[i[2]-1][1]+"</font>:"+(i[3])+"</font></b>")
        except socket.error as e:
            print(e)
        finally:
            print('Socket connected')
        self.label_groups.setText(str(group))
        self.listWidget.addItems(self.onlineusers)
        self.pushButton_send.clicked.connect(self.sendMsg)
        self.pushButton_refresh.clicked.connect(self.refresh)
        self.pushButton_exit.clicked.connect(self.exit)
    def sendMsg(self):
        msg=self.textEdit.toPlainText()
        self.textEdit.clear()
        try:
            msg='mes'+','+self.group+','+self.username+','+msg
            self.soc.send(msg.encode('utf-8'))
            QtWidgets.QMessageBox.information(self, "提示", "发送成功！")
            self.refresh()
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.information(self, "提示", "发送失败！请检查网络连接！")  
    def refresh(self): 
        try:
            req='refresh'+','+self.group
            self.soc.send(req.encode('utf-8'))
            # QtWidgets.QMessageBox.information(self, "提示", "刷新成功！")
            self.onlineusers=ast.literal_eval(self.soc.recv(1024).decode('utf-8'))
            self.listWidget.clear()
            self.listWidget.addItems(self.onlineusers)
            mes=ast.literal_eval(self.soc.recv(1024).decode('utf-8'))
            for i in mes: 
                if i[0]>self.index:
                    self.index=i[0]
                    self.textBrowser_message.append("<b><font size='5'><font color='blue'>"+self.user[i[2]-1][1]+"</font>:"+(i[3])+"</font></b>")
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.information(self, "提示", "刷新失败！请检查网络连接！")
            threading.Timer(2,self.refresh).start()
    # def ShowOnlineUsers(self): #
    #     try:
    #         self.soc.send('getusers'.encode('utf-8'))
    #         self.users=ast.literal_eval(self.soc.recv(1024).decode('utf-8'))
    #     except Exception as e:
    #         print(e)
    def exit(self):
        self.close()
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myGroupChat = MyGroupChat('admin','Group1')
    myGroupChat.show()
    sys.exit(app.exec())