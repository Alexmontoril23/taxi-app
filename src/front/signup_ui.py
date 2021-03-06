# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_signup_dialog(object):
    def setupUi(self, signup_dialog):
        signup_dialog.setObjectName("signup_dialog")
        signup_dialog.resize(729, 629)
        signup_dialog.setMinimumSize(QtCore.QSize(729, 629))
        signup_dialog.setMaximumSize(QtCore.QSize(729, 629))
        font = QtGui.QFont()
        font.setPointSize(19)
        signup_dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/app-logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        signup_dialog.setWindowIcon(icon)
        self.signup_frame = QtWidgets.QFrame(signup_dialog)
        self.signup_frame.setGeometry(QtCore.QRect(190, 130, 381, 391))
        self.signup_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.signup_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.signup_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.signup_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.signup_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.signup_frame.setObjectName("signup_frame")
        self.username_lineEdit = QtWidgets.QLineEdit(self.signup_frame)
        self.username_lineEdit.setGeometry(QtCore.QRect(170, 120, 171, 20))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.email_lineEdit = QtWidgets.QLineEdit(self.signup_frame)
        self.email_lineEdit.setGeometry(QtCore.QRect(170, 200, 171, 20))
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.username_label = QtWidgets.QLabel(self.signup_frame)
        self.username_label.setGeometry(QtCore.QRect(60, 120, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.email_label = QtWidgets.QLabel(self.signup_frame)
        self.email_label.setGeometry(QtCore.QRect(60, 200, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")
        self.signup_button = QtWidgets.QPushButton(self.signup_frame)
        self.signup_button.setGeometry(QtCore.QRect(150, 330, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.signup_button.setFont(font)
        self.signup_button.setObjectName("signup_button")
        self.phone_label = QtWidgets.QLabel(self.signup_frame)
        self.phone_label.setGeometry(QtCore.QRect(60, 280, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.phone_label.setFont(font)
        self.phone_label.setObjectName("phone_label")
        self.phone_lineEdit = QtWidgets.QLineEdit(self.signup_frame)
        self.phone_lineEdit.setGeometry(QtCore.QRect(170, 280, 171, 20))
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.card_label = QtWidgets.QLabel(self.signup_frame)
        self.card_label.setGeometry(QtCore.QRect(60, 240, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.card_label.setFont(font)
        self.card_label.setObjectName("card_label")
        self.card_lineEdit = QtWidgets.QLineEdit(self.signup_frame)
        self.card_lineEdit.setGeometry(QtCore.QRect(170, 240, 171, 20))
        self.card_lineEdit.setObjectName("card_lineEdit")
        self.app_title_label = QtWidgets.QLabel(self.signup_frame)
        self.app_title_label.setGeometry(QtCore.QRect(20, 40, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.app_title_label.setFont(font)
        self.app_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.app_title_label.setObjectName("app_title_label")
        self.passwd_lineEdit = QtWidgets.QLineEdit(self.signup_frame)
        self.passwd_lineEdit.setGeometry(QtCore.QRect(170, 160, 171, 20))
        self.passwd_lineEdit.setObjectName("passwd_lineEdit")
        self.passwd_label = QtWidgets.QLabel(self.signup_frame)
        self.passwd_label.setGeometry(QtCore.QRect(60, 160, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.passwd_label.setFont(font)
        self.passwd_label.setObjectName("passwd_label")
        self.background_img_label = QtWidgets.QLabel(signup_dialog)
        self.background_img_label.setGeometry(QtCore.QRect(0, 0, 731, 631))
        self.background_img_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background_img_label.setText("")
        self.background_img_label.setPixmap(QtGui.QPixmap("../images/background.jpg"))
        self.background_img_label.setObjectName("background_img_label")
        self.background_img_label.raise_()
        self.signup_frame.raise_()

        self.retranslateUi(signup_dialog)
        QtCore.QMetaObject.connectSlotsByName(signup_dialog)

    def retranslateUi(self, signup_dialog):
        _translate = QtCore.QCoreApplication.translate
        signup_dialog.setWindowTitle(_translate("signup_dialog", "Sign up"))
        self.username_lineEdit.setPlaceholderText(_translate("signup_dialog", "Please enter your name"))
        self.email_lineEdit.setPlaceholderText(_translate("signup_dialog", "Please enter your email"))
        self.username_label.setText(_translate("signup_dialog", "Username"))
        self.email_label.setText(_translate("signup_dialog", "Email"))
        self.signup_button.setText(_translate("signup_dialog", "Sign up"))
        self.phone_label.setText(_translate("signup_dialog", "Phone number"))
        self.phone_lineEdit.setPlaceholderText(_translate("signup_dialog", "Please enter your phone number"))
        self.card_label.setText(_translate("signup_dialog", "Card number"))
        self.card_lineEdit.setPlaceholderText(_translate("signup_dialog", "Please enter your card number"))
        self.app_title_label.setText(_translate("signup_dialog", "Welcome to Taxi App"))
        self.passwd_lineEdit.setPlaceholderText(_translate("signup_dialog", "Please enter your password"))
        self.passwd_label.setText(_translate("signup_dialog", "Password"))

