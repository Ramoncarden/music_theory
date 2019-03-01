# from PySide2 import QtWidgets
#
# from main import Ui_mainWindow
#
# class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
#     def __init__(self):
#         super(MyQtApp, self).__init__()
#         self.setupUi(self)
#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication()
#     qt_app = MyQtApp()
#     qt_app.show()
#     app.exec_()

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi

class MyQtApp(QMainWindow):
    """docstring for ."""
    def __init__(self):
        super(MyQtApp, self).__init__()
        loadUi("main.ui", self)
        self.setWindowTitle("melody maker")
        self.one_chord.clicked.connect(self.play_sound)
    @pyqtSlot()
    def play_sound(self):
        print("Playing the one chord!")
        


def run():
    app = QApplication(sys.argv)
    widget = MyQtApp()
    widget.show()
    sys.exit(app.exec_())

run()
