# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Fri Mar  1 00:28:25 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(846, 605)
        font = QtGui.QFont()
        font.setPointSize(14)
        mainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.two_chord = QtWidgets.QPushButton(self.centralwidget)
        self.two_chord.setObjectName("two_chord")
        self.gridLayout.addWidget(self.two_chord, 0, 2, 1, 1)
        self.three_chord = QtWidgets.QPushButton(self.centralwidget)
        self.three_chord.setObjectName("three_chord")
        self.gridLayout.addWidget(self.three_chord, 0, 3, 1, 1)
        self.four_chrod = QtWidgets.QPushButton(self.centralwidget)
        self.four_chrod.setObjectName("four_chrod")
        self.gridLayout.addWidget(self.four_chrod, 0, 4, 1, 1)
        self.five_chord = QtWidgets.QPushButton(self.centralwidget)
        self.five_chord.setObjectName("five_chord")
        self.gridLayout.addWidget(self.five_chord, 0, 5, 1, 1)
        self.six_chord = QtWidgets.QPushButton(self.centralwidget)
        self.six_chord.setObjectName("six_chord")
        self.gridLayout.addWidget(self.six_chord, 0, 6, 1, 1)
        self.seven_chord = QtWidgets.QPushButton(self.centralwidget)
        self.seven_chord.setObjectName("seven_chord")
        self.gridLayout.addWidget(self.seven_chord, 0, 7, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)
        self.one_chord = QtWidgets.QPushButton(self.centralwidget)
        self.one_chord.setObjectName("one_chord")
        self.gridLayout.addWidget(self.one_chord, 0, 0, 1, 1)
        self.select_key = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.select_key.setFont(font)
        self.select_key.setObjectName("select_key")
        self.select_key.addItem("")
        self.select_key.addItem("")
        self.gridLayout.addWidget(self.select_key, 1, 4, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 22))
        self.menubar.setObjectName("menubar")
        self.menuMusic_App = QtWidgets.QMenu(self.menubar)
        self.menuMusic_App.setObjectName("menuMusic_App")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(mainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(mainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMusic_App.addAction(self.actionOpen)
        self.menuMusic_App.addAction(self.actionSave)
        self.menuMusic_App.addAction(self.actionExit)
        self.menuMusic_App.addSeparator()
        self.menubar.addAction(self.menuMusic_App.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtWidgets.QApplication.translate("mainWindow", "Melody Maker", None, -1))
        self.two_chord.setText(QtWidgets.QApplication.translate("mainWindow", "II", None, -1))
        self.three_chord.setText(QtWidgets.QApplication.translate("mainWindow", "III", None, -1))
        self.four_chrod.setText(QtWidgets.QApplication.translate("mainWindow", "IV", None, -1))
        self.five_chord.setText(QtWidgets.QApplication.translate("mainWindow", "V", None, -1))
        self.six_chord.setText(QtWidgets.QApplication.translate("mainWindow", "VI", None, -1))
        self.seven_chord.setText(QtWidgets.QApplication.translate("mainWindow", "VII", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("mainWindow", "CheckBox", None, -1))
        self.one_chord.setText(QtWidgets.QApplication.translate("mainWindow", "I", None, -1))
        self.select_key.setItemText(0, QtWidgets.QApplication.translate("mainWindow", "C", None, -1))
        self.select_key.setItemText(1, QtWidgets.QApplication.translate("mainWindow", "C#", None, -1))
        self.menuMusic_App.setTitle(QtWidgets.QApplication.translate("mainWindow", "File", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("mainWindow", "Open", None, -1))
        self.actionSave.setText(QtWidgets.QApplication.translate("mainWindow", "Save", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("mainWindow", "Exit", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

