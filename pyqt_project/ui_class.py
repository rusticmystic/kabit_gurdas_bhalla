# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kabit_ui.ui'
#
# Created: Mon Aug  8 23:02:40 2016
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
        MainWindow.resize(921, 596)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textEdit = QtGui.QTextEdit(self.frame)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pun_button = QtGui.QPushButton(self.frame_2)
        self.pun_button.setObjectName(_fromUtf8("pun_button"))
        self.horizontalLayout_2.addWidget(self.pun_button)
        self.hin_button = QtGui.QPushButton(self.frame_2)
        self.hin_button.setObjectName(_fromUtf8("hin_button"))
        self.horizontalLayout_2.addWidget(self.hin_button)
        self.eng_button = QtGui.QPushButton(self.frame_2)
        self.eng_button.setObjectName(_fromUtf8("eng_button"))
        self.horizontalLayout_2.addWidget(self.eng_button)
        self.horizontalSlider = QtGui.QSlider(self.frame_2)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.lineEdit = QtGui.QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.ok_button = QtGui.QPushButton(self.frame_2)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout_2.addWidget(self.ok_button)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 921, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuKabit_UI = QtGui.QMenu(self.menubar)
        self.menuKabit_UI.setObjectName(_fromUtf8("menuKabit_UI"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuKabit_UI.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lineEdit.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pun_button.setText(_translate("MainWindow", "Punjabi", None))
        self.hin_button.setText(_translate("MainWindow", "Hindi", None))
        self.eng_button.setText(_translate("MainWindow", "English", None))
        self.ok_button.setText(_translate("MainWindow", "OK", None))
        self.menuKabit_UI.setTitle(_translate("MainWindow", "Kabit UI", None))

