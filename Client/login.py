import socket
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from Ui_login import *
from groupchat import *
import threading

class MyLogin(Ui_Dialog_login, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyLogin, self).__init__(parent)
        self.setupUi(self)
        self.soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.soc.connect(('127.0.0.1',8099))
        self.pushButton_login.clicked.connect(self.login)

    def login(self):
        try:
            username=self.lineEdit_Username.text()
            password=self.lineEdit_password.text()
            if username=='' or password=='':
                QtWidgets.QMessageBox.information(self, "提示", "用户名和密码不能为空！")
            else:
                req='login'+','+username+','+password
                self.soc.send(req.encode('utf-8'))
                res=self.soc.recv(1024).decode('utf-8').split(',')
                if res[1]=='True':
                    QtWidgets.QMessageBox.information(self, "提示", "登录成功！")
                    self.close()
                    info=self.soc.recv(1024).decode('utf-8').split('*')
                    group=info[0]
                    print(group)
                    user=ast.literal_eval(info[1])
                    onlineusers=ast.literal_eval(info[2])
                    chatlist=ast.literal_eval(info[3])
                    self.groupchat=MyGroupChat(username,group,user,onlineusers,chatlist,self.soc)
                    self.groupchat.show()
                    threading.Thread(target=self.groupchat.handle_msg).start()
                else:
                    QtWidgets.QMessageBox.information(self, "提示", "登录失败！请检查用户名和密码！")
                    self.lineEdit_Username.clear()
                    self.lineEdit_password.clear()
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.information(self, "提示", "登录失败！请检查网络连接！")
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = MyLogin()
    login.show()
    sys.exit(app.exec())