import socket
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from Ui_register import *

class MyRegister(Ui_Dialog_Register, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyRegister, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_register.clicked.connect(self.register)

    def register(self, username:str, password:str):
        try:
            self.soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.soc.connect(('127.0.0.1',8099))
            self.
            username='register'+','+username+','+password