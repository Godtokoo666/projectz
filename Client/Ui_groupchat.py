# Form implementation generated from reading ui file 'd:\Python_Workspace\Client\groupchat.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GroupChat(object):
    def setupUi(self, GroupChat):
        GroupChat.setObjectName("GroupChat")
        GroupChat.resize(810, 649)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(GroupChat)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_groupsundisplay = QtWidgets.QLabel(parent=GroupChat)
        self.label_groupsundisplay.setMaximumSize(QtCore.QSize(80, 30))
        self.label_groupsundisplay.setObjectName("label_groupsundisplay")
        self.horizontalLayout_2.addWidget(self.label_groupsundisplay)
        self.label_groups = QtWidgets.QLabel(parent=GroupChat)
        self.label_groups.setMaximumSize(QtCore.QSize(120, 30))
        self.label_groups.setObjectName("label_groups")
        self.horizontalLayout_2.addWidget(self.label_groups)
        self.label_usersdisplay = QtWidgets.QLabel(parent=GroupChat)
        self.label_usersdisplay.setMaximumSize(QtCore.QSize(80, 30))
        self.label_usersdisplay.setObjectName("label_usersdisplay")
        self.horizontalLayout_2.addWidget(self.label_usersdisplay)
        self.label_users = QtWidgets.QLabel(parent=GroupChat)
        self.label_users.setMaximumSize(QtCore.QSize(180, 30))
        self.label_users.setObjectName("label_users")
        self.horizontalLayout_2.addWidget(self.label_users)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.textBrowser_message = QtWidgets.QTextBrowser(parent=GroupChat)
        self.textBrowser_message.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser_message.setObjectName("textBrowser_message")
        self.verticalLayout.addWidget(self.textBrowser_message)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=GroupChat)
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(parent=GroupChat)
        self.listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(parent=GroupChat)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_refresh = QtWidgets.QPushButton(parent=GroupChat)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.verticalLayout_2.addWidget(self.pushButton_refresh)
        self.pushButton_send = QtWidgets.QPushButton(parent=GroupChat)
        self.pushButton_send.setObjectName("pushButton_send")
        self.verticalLayout_2.addWidget(self.pushButton_send)
        self.pushButton_exit = QtWidgets.QPushButton(parent=GroupChat)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.verticalLayout_2.addWidget(self.pushButton_exit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(GroupChat)
        QtCore.QMetaObject.connectSlotsByName(GroupChat)

    def retranslateUi(self, GroupChat):
        _translate = QtCore.QCoreApplication.translate
        GroupChat.setWindowTitle(_translate("GroupChat", "群聊-局域网聊天"))
        self.label_groupsundisplay.setText(_translate("GroupChat", "当前群组："))
        self.label_groups.setText(_translate("GroupChat", "1"))
        self.label_usersdisplay.setText(_translate("GroupChat", "欢迎您："))
        self.label_users.setText(_translate("GroupChat", "1"))
        self.label.setText(_translate("GroupChat", "在线用户："))
        self.pushButton_refresh.setText(_translate("GroupChat", "刷新消息"))
        self.pushButton_send.setText(_translate("GroupChat", "发送"))
        self.pushButton_exit.setText(_translate("GroupChat", "退出"))
