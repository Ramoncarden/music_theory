# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 605)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(360, 380, 121, 34))
        self.comboBox.setMaximumSize(QtCore.QSize(16777214, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.viewChords = QtWidgets.QPushButton(self.centralwidget)
        self.viewChords.setGeometry(QtCore.QRect(360, 430, 121, 32))
        self.viewChords.setObjectName("viewChords")
        self.seventh_chord = QtWidgets.QPushButton(self.centralwidget)
        self.seventh_chord.setGeometry(QtCore.QRect(360, 480, 121, 32))
        self.seventh_chord.setAutoFillBackground(False)
        self.seventh_chord.setStyleSheet("background-color: rgb(70, 196, 186);")
        self.seventh_chord.setCheckable(False)
        self.seventh_chord.setChecked(False)
        self.seventh_chord.setAutoDefault(False)
        self.seventh_chord.setDefault(False)
        self.seventh_chord.setObjectName("seventh_chord")
        self.two_chord = QtWidgets.QPushButton(self.centralwidget)
        self.two_chord.setGeometry(QtCore.QRect(121, 280, 121, 32))
        self.two_chord.setObjectName("two_chord")
        self.four_chrod = QtWidgets.QPushButton(self.centralwidget)
        self.four_chrod.setGeometry(QtCore.QRect(361, 280, 121, 32))
        self.four_chrod.setObjectName("four_chrod")
        self.five_chord = QtWidgets.QPushButton(self.centralwidget)
        self.five_chord.setGeometry(QtCore.QRect(481, 280, 121, 32))
        self.five_chord.setObjectName("five_chord")
        self.six_chord = QtWidgets.QPushButton(self.centralwidget)
        self.six_chord.setGeometry(QtCore.QRect(601, 280, 121, 32))
        self.six_chord.setObjectName("six_chord")
        self.seven_chord = QtWidgets.QPushButton(self.centralwidget)
        self.seven_chord.setGeometry(QtCore.QRect(721, 280, 121, 32))
        self.seven_chord.setObjectName("seven_chord")
        self.three_chord = QtWidgets.QPushButton(self.centralwidget)
        self.three_chord.setGeometry(QtCore.QRect(241, 280, 121, 32))
        self.three_chord.setObjectName("three_chord")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(31, 250, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setText("")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.one_chord = QtWidgets.QPushButton(self.centralwidget)
        self.one_chord.setGeometry(QtCore.QRect(1, 280, 121, 32))
        self.one_chord.setAutoExclusive(False)
        self.one_chord.setAutoRepeatDelay(295)
        self.one_chord.setObjectName("one_chord")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(151, 250, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(271, 250, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(391, 250, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(511, 250, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(631, 250, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(730, 250, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.recButton = QtWidgets.QPushButton(self.centralwidget)
        self.recButton.setGeometry(QtCore.QRect(270, 130, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.recButton.setFont(font)
        self.recButton.setStyleSheet("#recButton {\n"
"color: rgb(255, 77, 63);\n"
"border: 2px solid #555;\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"background-color: rgb(247, 244, 250);\n"
"padding: 5px;\n"
"}\n"
"\n"
"#recButton:pressed {\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-color: beige;\n"
"font: bold 18px;\n"
"color: white;\n"
"min-width: 8em;\n"
"background-color: rgb(255, 77, 63);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"    ")
        self.recButton.setCheckable(False)
        self.recButton.setChecked(False)
        self.recButton.setObjectName("recButton")
        self.playButton = QtWidgets.QToolButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(370, 140, 101, 41))
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("#playButton {\n"
"background-color: rgb(0, 222, 0);\n"
"border: 1px solid black;\n"
"font: 14pt \".SF NS Text\";\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#playButton:pressed {\n"
"color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 20px;\n"
"min-width: 8em;\n"
"}\n"
"")
        self.playButton.setText("")
        self.playButton.setIconSize(QtCore.QSize(15, 15))
        self.playButton.setCheckable(False)
        self.playButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.playButton.setAutoRaise(False)
        self.playButton.setArrowType(QtCore.Qt.RightArrow)
        self.playButton.setObjectName("playButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 0, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Chalkboard")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(520, 135, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet("background-color: rgb(255, 139, 69);")
        self.stopButton.setObjectName("stopButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 22))
        self.menubar.setObjectName("menubar")
        self.menuMusic_App = QtWidgets.QMenu(self.menubar)
        self.menuMusic_App.setObjectName("menuMusic_App")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNight_Mode = QtWidgets.QAction(MainWindow)
        self.actionNight_Mode.setObjectName("actionNight_Mode")
        self.menuMusic_App.addAction(self.actionOpen)
        self.menuMusic_App.addAction(self.actionSave)
        self.menuMusic_App.addAction(self.actionExit)
        self.menuMusic_App.addSeparator()
        self.menubar.addAction(self.menuMusic_App.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Melody Maker"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Gb"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Db"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Ab"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Eb"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Bb"))
        self.comboBox.setItemText(5, _translate("MainWindow", "F"))
        self.comboBox.setItemText(6, _translate("MainWindow", "C"))
        self.comboBox.setItemText(7, _translate("MainWindow", "G"))
        self.comboBox.setItemText(8, _translate("MainWindow", "D"))
        self.comboBox.setItemText(9, _translate("MainWindow", "A"))
        self.comboBox.setItemText(10, _translate("MainWindow", "E"))
        self.comboBox.setItemText(11, _translate("MainWindow", "B"))
        self.comboBox.setItemText(12, _translate("MainWindow", "F#"))
        self.viewChords.setText(_translate("MainWindow", "View Chords"))
        self.seventh_chord.setText(_translate("MainWindow", "7th Chords"))
        self.two_chord.setText(_translate("MainWindow", "II"))
        self.two_chord.setShortcut(_translate("MainWindow", "S"))
        self.four_chrod.setText(_translate("MainWindow", "IV"))
        self.four_chrod.setShortcut(_translate("MainWindow", "F"))
        self.five_chord.setText(_translate("MainWindow", "V"))
        self.five_chord.setShortcut(_translate("MainWindow", "G"))
        self.six_chord.setText(_translate("MainWindow", "VI"))
        self.six_chord.setShortcut(_translate("MainWindow", "H"))
        self.seven_chord.setText(_translate("MainWindow", "VII"))
        self.seven_chord.setShortcut(_translate("MainWindow", "J"))
        self.three_chord.setText(_translate("MainWindow", "III"))
        self.three_chord.setShortcut(_translate("MainWindow", "D"))
        self.one_chord.setText(_translate("MainWindow", "I"))
        self.one_chord.setShortcut(_translate("MainWindow", "A"))
        self.recButton.setText(_translate("MainWindow", "Rec"))
        self.label.setText(_translate("MainWindow", "Melody Maker"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.menuMusic_App.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionNight_Mode.setText(_translate("MainWindow", "Night Mode"))


