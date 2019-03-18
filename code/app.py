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
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtSql, QtGui, QtCore, QtWidgets
from main import Ui_mainWindow
import sqlite3
import os.path
from pprint import pprint
from PyQt5.QtGui import QColor
from pygame import mixer




class MusicApp():
    """docstring for ."""
    def __init__(self):
        app = QApplication(sys.argv)
        # super(MusicApp, self).__init__()
        self.MainWindow = QMainWindow()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self.MainWindow)
        # loadUi("main.ui", self)
        # self.setWindowTitle("melody maker")
        self.ui.one_chord.clicked.connect(self.play_sound_one)
        self.ui.two_chord.clicked.connect(self.play_sound_two)
        self.ui.three_chord.clicked.connect(self.play_sound_three)
        self.ui.four_chrod.clicked.connect(self.play_sound_four)
        self.ui.five_chord.clicked.connect(self.play_sound_five)
        self.ui.six_chord.clicked.connect(self.play_sound_six)
        self.ui.seven_chord.clicked.connect(self.play_sound_seven)
        self.ui.viewChords.clicked.connect(self.print_data)
        self.model = None
        self.ui.viewChords.clicked.connect(self.sql_tableview_model)
        self.ui.viewChords.clicked.connect(self.sql_add_row)
        self.ui.viewChords.clicked.connect(self.sql_delete_row)
        self.ui.viewChords.clicked.connect(self.create_key_db)

        self.MainWindow.show()
        sys.exit(app.exec_())



    def play_sound_one(self):
        mixer.init()
        mixer.music.load("sounds/Cmaj.ogg")
        mixer.music.play()

    def play_sound_two(self):
        mixer.init()
        mixer.music.load("sounds/Dm.ogg")
        mixer.music.play()

    def play_sound_three(self):
        mixer.init()
        mixer.music.load("sounds/Em.ogg")
        mixer.music.play()

    def play_sound_four(self):
        mixer.init()
        mixer.music.load("sounds/Fmaj.ogg")
        mixer.music.play()

    def play_sound_five(self):
        mixer.init()
        mixer.music.load("sounds/Gmaj.ogg")
        mixer.music.play()

    def play_sound_six(self):
        mixer.init()
        mixer.music.load("sounds/Am.ogg")
        mixer.music.play()

    def play_sound_seven(self):
        mixer.init()
        mixer.music.load("sounds/Bdim.ogg")
        mixer.music.play()

        #*** Database Code ***------------------------------
    def sql_delete_row(self):
        if self.model:
            self.model.removeRow(self.tableview.currentIndex().row())
        else:
            self.sql_tableview_model()

    def sql_add_row(self):
        if self.model:
            self.model.insertRows(self.model.rowCount(), 1)
        else:
            self.sql_tableview_model()

    def sql_tableview_model(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('KEYS.db')

        tableview = self.ui.tableView
        tableview.columnWidth(4)

        self.model = QtSql.QSqlTableModel()
        tableview.setModel(self.model)

        self.model.setTable('KEYS')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, 'I')
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "II")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "III")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "IV")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "V")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "VI")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "VII")
        tableview.hideColumn(0)


        #******* Initialize db winddow *********#
    def print_data(self):
        sqlite_file = 'KEYS.db'
        conn = sqlite3.connect(sqlite_file)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM KEYS ORDER BY ID")
        all_rows = cursor.fetchall()
        pprint(all_rows)

        conn.commit()
        conn.close()


        #******** Print db ********#
    def create_key_db(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('KEYS.db')
        db.open()

        query = QtSql.QSqlQuery()

        query.exec_("create table KEYS(ID int primary key, "
                    "I varchar(2),"
                    "II varchar(2),"
                    "III varchar(2),"
                    "IV varchar(2),"
                    "V varchar(2),"
                    "VI varchar(2),"
                    "VII varchar(2))")
        query.exec_("insert into KEYS values(1, 'Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb','F')")
        query.exec_("insert into KEYS values(2, 'Db', 'Eb','F', 'Gb', 'Ab', 'Bb', 'C')")
        query.exec_("insert into KEYS values(3, 'Ab', 'Bb', 'C', 'Db', 'Eb','F', 'G')")
        query.exec_("insert into KEYS values(4, 'Eb','F', 'G', 'Ab', 'Bb', 'C', 'D')")
        query.exec_("insert into KEYS values(5, 'Bb', 'C', 'D', 'Eb','F', 'G', 'A')")
        query.exec_("insert into KEYS values(6, 'F', 'G', 'A', 'Bb', 'C', 'D', 'E')")
        query.exec_("insert into KEYS values(7, 'C', 'D', 'E', 'F', 'G', 'A', 'B')")
        query.exec_("insert into KEYS values(8, 'G', 'A', 'B', 'C', 'D', 'E', 'F#')")
        query.exec_("insert into KEYS values(9, 'D', 'E', 'F#', 'G', 'A', 'B', 'C#')")
        query.exec_("insert into KEYS values(10, 'A', 'B', 'C#', 'D', 'E', 'F#', 'G#')")
        query.exec_("insert into KEYS values(11, 'E', 'F#', 'G#', 'A', 'B', 'C#', 'D#')")
        query.exec_("insert into KEYS values(12, 'B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#')")
        query.exec_("insert into KEYS values(13, 'F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#')")


    #********* play sound when keyboard key is pressed **********#
    def key_press_event(event):
        if event.key() == 65:
            print("hi")

if __name__=="__main__":
    MusicApp()


# def run():
#     widget = MusicApp()
#     widget.show()
#     sys.exit(app.exec_())
#
# run()
