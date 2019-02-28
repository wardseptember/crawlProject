#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'WatchVIPVideo.ui'
# Created by: PyQt5 UI code generator 5.10.1
# @Time:2018/7/16 14:05
# @Author: wardseptember
# @File: VIPVideoWatch.py

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QLabel,QGridLayout,QLineEdit,QMainWindow,QMessageBox,
    QComboBox, QApplication)
from PyQt5.QtGui import QIcon,QColor
from PyQt5.QtCore import Qt
import sys
import webbrowser
class VIPVideo(QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(447, 338)
        Form.setWindowIcon(QIcon('cat.ico'))
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(200, 60, 171, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("Channel 1")
        self.comboBox_2.addItem("Channel 2")
        self.comboBox_2.addItem("Channel 3")
        self.comboBox_2.addItem("Channel 4")
        self.comboBox_2.addItem("Channel 5")
        self.comboBox_2.addItem("Channel 6")
        self.comboBox_2.addItem("Channel 7")
        self.comboBox_2.addItem("Channel 8")
        self.comboBox_2.addItem("Channel 9")
        self.comboBox_2.addItem("Channel 10")
        self.comboBox_2.addItem("Channel 11")
        self.comboBox_2.addItem("Channel 12")
        self.comboBox_2.addItem("Channel 13")
        self.comboBox_2.addItem("Channel 14")
        self.comboBox_2.addItem("Channel 15")
        self.comboBox_2.addItem("Channel 16")
        self.comboBox_2.addItem("Channel 17")
        self.comboBox_2.addItem("Channel 18")
        self.comboBox_2.setEditable(False)
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(70, 60, 121, 21))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 121, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 110, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(70, 210, 301, 111))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setEnabled(False)


        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.OpenUrl)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 160, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.close)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setFixedSize(Form.width(),Form.height())


        Form.show()
    def OpenUrl(self,Form):
        str=""
        str1=self.lineEdit.text()
        str2=self.comboBox_2.currentText()
        if str2=="Channel 1":
            str="http://www.wmxz.wang/video.php?url="
        elif str2=="Channel 2":
            str="http://goudidiao.com/?url="
        elif str2 == "Channel 3":
            str="http://api.baiyug.cn/vip/index.php?url="
        elif str2 == "Channel 4":
            str="http://www.a305.org/weixin.php?url="
        elif str2=="Channel 5":
            str="http://www.vipjiexi.com/tong.php?url="
        elif str2 == "Channel 6":
            str="http://jx.aeidu.cn/index.php?url="
        elif str2 == "Channel 7":
            str="http://www.sonimei.cn/?url="
        elif str2=="Channel 8":
            str="https://api.vparse.org/?url="
        elif str2 == "Channel 9":
            str="https://jx.maoyun.tv/index.php?id="
        elif str2 == "Channel 10":
            str="http://pupudy.com/play?make=url&id="
        elif str2=="Channel 11":
            str="http://www.qxyingyuan.vip/play?make=url&id="
        elif str2 == "Channel 12":
            str="http://appapi.svipv.kuuhui.com/svipjx/liulanqichajian/browserplugin/qhjx/qhjx.php?id="
        elif str2 == "Channel 13":
            str="http://api.xfsub.com/index.php?url="
        elif str2 == "Channel 14":
            str="https://jiexi.071811.cc/jx.php?url="
        elif str2 == "Channel 15":
            str="http://q.z.vip.totv.72du.com/?url="
        elif str2=="Channel 16":
            str="http://jx.api.163ren.com/vod.php?url="
        elif str2 == "Channel 17":
            str="http://www.sfsft.com/admin.php?url="
        elif str2 == "Channel 18":
            str="http://v.renrenfabu.com/jiexi.php?url="
        else:
            str="https://api.vparse.org/?url="
        if str1=="":
            reply = QMessageBox.question(self, 'Message',
                                         "Please correctly input url !",
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
        else:
            webbrowser.open(str+str1)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "WatchVIPVideo"))
        self.label_1.setText(_translate("Form", "Select a channel:"))
        self.label_2.setText(_translate("Form", "Input VIPVideo URL:"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;color:red;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Note: This software is for learning technology only and should not be used for any commercial purposes.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Recommendation: It is recommended to set the Chrome browser as the default browser.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Author:wardseptember</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Author\'s email:wardseptember@163.com</p></body></html>"))
        self.pushButton.setText(_translate("Form", "Play"))
        self.pushButton_2.setText(_translate("Form", "Exit"))
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = VIPVideo()
    sys.exit(app.exec_())


