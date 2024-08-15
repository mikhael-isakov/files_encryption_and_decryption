# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 280)
        MainWindow.setStyleSheet(u"background-color: rgb(25, 35, 45);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(149, 20, 620, 30))
        font = QFont()
        font.setFamily(u"Courier")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 191);\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(30, 20, 100, 100))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 240, 740, 30))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 191);\n"
"")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 60, 620, 20))
        font2 = QFont()
        font2.setFamily(u"Courier")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(150, 150, 150);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(449, 90, 321, 30))
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet(u"color: rgb(176, 230, 134);\n"
"background-color: rgb(70, 70, 80);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 140, 220, 30))
        font3 = QFont()
        font3.setFamily(u"Courier")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: rgb(176, 230, 134);")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_1 = QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setGeometry(QRect(260, 140, 300, 30))
        font4 = QFont()
        font4.setFamily(u"Courier")
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setWeight(75)
        self.lineEdit_1.setFont(font4)
        self.lineEdit_1.setStyleSheet(u"color: rgb(255, 255, 191);\n"
"background-color: rgb(70, 70, 80);")
        self.lineEdit_1.setMaxLength(50)
        self.lineEdit_1.setEchoMode(QLineEdit.Password)
        self.lineEdit_1.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 190, 220, 30))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: rgb(176, 230, 134);")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(260, 190, 300, 30))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"color: rgb(176, 230, 134);\n"
"background-color: rgb(70, 70, 80);")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(580, 140, 190, 80))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"color: rgb(176, 230, 134);\n"
"background-color: rgb(70, 70, 80);")
        self.comboBox_1 = QComboBox(self.centralwidget)
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.setObjectName(u"comboBox_1")
        self.comboBox_1.setGeometry(QRect(260, 90, 171, 30))
        self.comboBox_1.setFont(font4)
        self.comboBox_1.setCursor(QCursor(Qt.ArrowCursor))
        self.comboBox_1.setStyleSheet(u"color: rgb(255, 255, 191);\n"
"background-color: rgb(70, 70, 80);\n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 90, 100, 30))
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(176, 230, 134);")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(740, 90, 30, 30))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(530, 140, 30, 30))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(530, 190, 30, 30))
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_10.raise_()
        self.label_9.raise_()
        self.label_8.raise_()
        self.label_2.raise_()
        self.label_1.raise_()
        self.label_7.raise_()
        self.label_3.raise_()
        self.pushButton_1.raise_()
        self.label_5.raise_()
        self.lineEdit_1.raise_()
        self.label_6.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.comboBox_1.raise_()
        self.label_4.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Encrypting files using the AES standard", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"logo", None))
        self.label_7.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"version 2024.08.10", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Enter Password:", None))
        self.lineEdit_1.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Select Key File:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Select Key File", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.comboBox_1.setItemText(0, QCoreApplication.translate("MainWindow", u"encrypt", None))
        self.comboBox_1.setItemText(1, QCoreApplication.translate("MainWindow", u"decrypt", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
    # retranslateUi
