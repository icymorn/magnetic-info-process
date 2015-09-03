# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jason/2015室内定位系统/project/from jiang/magnetic-info-process/tools/Window.ui'
#
# Created: Sat Aug 29 19:49:11 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1000, 544)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.qwtPlot = QwtPlot(self.centralWidget)
        self.qwtPlot.setGeometry(QtCore.QRect(10, 20, 961, 451))
        self.qwtPlot.setProperty("propertiesDocument", _fromUtf8(""))
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(30, 475, 941, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_20 = QtGui.QLabel(self.centralWidget)
        self.label_20.setGeometry(QtCore.QRect(740, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.centralWidget)
        self.label_21.setGeometry(QtCore.QRect(830, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.centralWidget)
        self.label_22.setGeometry(QtCore.QRect(900, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.centralWidget)
        self.label_23.setGeometry(QtCore.QRect(720, 10, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self.centralWidget)
        self.label_24.setGeometry(QtCore.QRect(810, 10, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(self.centralWidget)
        self.label_25.setGeometry(QtCore.QRect(880, 10, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "机器人粒子滤波定位", None))
        self.label_20.setText(_translate("MainWindow", "Center", None))
        self.label_21.setText(_translate("MainWindow", "Max", None))
        self.label_22.setText(_translate("MainWindow", "Simulate", None))
        self.label_23.setText(_translate("MainWindow", "绿", None))
        self.label_24.setText(_translate("MainWindow", "红", None))
        self.label_25.setText(_translate("MainWindow", "蓝", None))

from PyQt4.Qwt5 import *

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

