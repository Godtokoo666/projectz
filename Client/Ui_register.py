# Form implementation generated from reading ui file 'd:\Python_Workspace\UI\register.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Register(object):
    def setupUi(self, Dialog_Register):
        Dialog_Register.setObjectName("Dialog_Register")
        Dialog_Register.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_Register.sizePolicy().hasHeightForWidth())
        Dialog_Register.setSizePolicy(sizePolicy)
        Dialog_Register.setMinimumSize(QtCore.QSize(400, 300))
        Dialog_Register.setMaximumSize(QtCore.QSize(4000, 300))
        self.label = QtWidgets.QLabel(parent=Dialog_Register)
        self.label.setGeometry(QtCore.QRect(70, 50, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog_Register)
        self.pushButton.setGeometry(QtCore.QRect(140, 230, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(parent=Dialog_Register)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 120, 241, 85))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(64, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(64, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog_Register)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Register)

    def retranslateUi(self, Dialog_Register):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Register.setWindowTitle(_translate("Dialog_Register", "注册-局域网聊天"))
        self.label.setText(_translate("Dialog_Register", "注册-局域网聊天"))
        self.pushButton.setText(_translate("Dialog_Register", "注册"))
        self.label_2.setText(_translate("Dialog_Register", "账号"))
        self.lineEdit.setPlaceholderText(_translate("Dialog_Register", "用户名"))
        self.label_3.setText(_translate("Dialog_Register", "密码"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog_Register", "密码"))
        self.label_4.setText(_translate("Dialog_Register", "确认密码"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog_Register", "重复密码"))
