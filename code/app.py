import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, QShortcut
from PyQt5.uic import loadUi
from PyQt5 import QtSql, QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt
from main import Ui_MainWindow
import sqlite3
import os.path
from pprint import pprint
from PyQt5.QtGui import QColor
from pygame import mixer
from PyQt5.QtCore import Qt
from table import Ui_Dialog




class MusicApp():
    """docstring for ."""
    def __init__(self):
        app = QApplication(sys.argv)
        self.MainWindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.table = Ui_Dialog()
        self.ui.setupUi(self.MainWindow)
        self.ui.comboBox.currentText()
        self.ui.one_chord.clicked.connect(self.play_sound_one)
        self.ui.two_chord.clicked.connect(self.play_sound_two)
        self.ui.three_chord.clicked.connect(self.play_sound_three)
        self.ui.four_chrod.clicked.connect(self.play_sound_four)
        self.ui.five_chord.clicked.connect(self.play_sound_five)
        self.ui.six_chord.clicked.connect(self.play_sound_six)
        self.ui.seven_chord.clicked.connect(self.play_sound_seven)
        self.ui.viewChords.clicked.connect(self.open_table)

        self.model = None
        self.ui.viewChords.clicked.connect(self.sql_tableview_model)
        self.ui.viewChords.clicked.connect(self.sql_add_row)
        self.ui.viewChords.clicked.connect(self.sql_delete_row)
        self.ui.viewChords.clicked.connect(self.create_key_db)
        self.MainWindow.show()
        sys.exit(app.exec_())


    def open_table(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def play_sound_one(self):
        mixer.init()
        combo = self.ui.comboBox.currentText()
        if combo == "Gb":
            mixer.music.load("sounds/soundsGb/Gb.ogg")
            mixer.music.play()
        elif combo == "Db":
            mixer.music.load("sounds/soundsDb/Db.ogg")
            mixer.music.play()
        elif combo == "Ab":
            mixer.music.load("sounds/soundsAb/Ab.ogg")
            mixer.music.play()
        elif combo == "Eb":
            mixer.music.load("sounds/soundsEb/Eb.ogg")
            mixer.music.play()
        elif combo == "Bb":
            mixer.music.load("sounds/soundsBb/Bb.ogg")
            mixer.music.play()
        elif combo == "F":
            mixer.music.load("sounds/soundsF/F.ogg")
            mixer.music.play()
        elif combo == "G":
            mixer.music.load("sounds/soundsG/G.ogg")
            mixer.music.play()
        elif combo == "D":
            mixer.music.load("sounds/soundsD/D.ogg")
            mixer.music.play()
        elif combo == "A":
            mixer.music.load("sounds/soundsA/A.ogg")
            mixer.music.play()
        elif combo == "E":
            mixer.music.load("sounds/soundsE/E.ogg")
            mixer.music.play()
        elif combo == "B":
            mixer.music.load("sounds/soundsB/B.ogg")
            mixer.music.play()
        elif combo == "F#":
            mixer.music.load("sounds/soundsF#/Gb.ogg")
            mixer.music.play()
        else:
            mixer.music.load("sounds/soundsC/C.ogg")
            mixer.music.play()

    def play_sound_two(self):
        mixer.init()
        combo = self.ui.comboBox.currentText()
        if combo == "Gb":
            mixer.music.load("sounds/soundsGb/Abm.ogg")
            mixer.music.play()
        elif combo == "Db":
            mixer.music.load("sounds/soundsDb/Ebm.ogg")
            mixer.music.play()
        elif combo == "Ab":
            mixer.music.load("sounds/soundsAb/Bbm.ogg")
            mixer.music.play()
        elif combo == "Eb":
            mixer.music.load("sounds/soundsEb/Fm.ogg")
            mixer.music.play()
        elif combo == "Bb":
            mixer.music.load("sounds/soundsBb/Cm.ogg")
            mixer.music.play()
        elif combo == "F":
            mixer.music.load("sounds/soundsF/Gm.ogg")
            mixer.music.play()
        elif combo == "G":
            mixer.music.load("sounds/soundsG/Am.ogg")
            mixer.music.play()
        elif combo == "D":
            mixer.music.load("sounds/soundsD/Em.ogg")
            mixer.music.play()
        elif combo == "A":
            mixer.music.load("sounds/soundsA/Bm.ogg")
            mixer.music.play()
        elif combo == "E":
            mixer.music.load("sounds/soundsE/F#m.ogg")
            mixer.music.play()
        elif combo == "B":
            mixer.music.load("sounds/soundsB/C#m.ogg")
            mixer.music.play()
        elif combo == "F#":
            mixer.music.load("sounds/soundsF#/Abm.ogg")
            mixer.music.play()
        else:
            mixer.music.load("sounds/soundsC/Dm.ogg")
            mixer.music.play()

    def play_sound_three(self):
        mixer.init()
        combo = self.ui.comboBox.currentText()
        if combo == "Gb":
            mixer.music.load("sounds/soundsGb/Bbm.ogg")
            mixer.music.play()
        elif combo == "Db":
            mixer.music.load("sounds/soundsDb/Fm.ogg")
            mixer.music.play()
        elif combo == "Ab":
            mixer.music.load("sounds/soundsAb/Cm.ogg")
            mixer.music.play()
        elif combo == "Eb":
            mixer.music.load("sounds/soundsEb/Gm.ogg")
            mixer.music.play()
        elif combo == "Bb":
            mixer.music.load("sounds/soundsBb/Dm.ogg")
            mixer.music.play()
        elif combo == "F":
            mixer.music.load("sounds/soundsF/Am.ogg")
            mixer.music.play()
        elif combo == "G":
            mixer.music.load("sounds/soundsG/Bm.ogg")
            mixer.music.play()
        elif combo == "D":
            mixer.music.load("sounds/soundsD/F#m.ogg")
            mixer.music.play()
        elif combo == "A":
            mixer.music.load("sounds/soundsA/C#m.ogg")
            mixer.music.play()
        elif combo == "E":
            mixer.music.load("sounds/soundsE/G#m.ogg")
            mixer.music.play()
        elif combo == "B":
            mixer.music.load("sounds/soundsB/D#m.ogg")
            mixer.music.play()
        elif combo == "F#":
            mixer.music.load("sounds/soundsF#/Bbm.ogg")
            mixer.music.play()
        else:
            mixer.music.load("sounds/soundsC/Em.ogg")
            mixer.music.play()

    def play_sound_four(self):
        mixer.init()
        combo = self.ui.comboBox.currentText()
        if combo == "Gb":
            mixer.music.load("sounds/soundsGb/B.ogg")
            mixer.music.play()
        elif combo == "Db":
            mixer.music.load("sounds/soundsDb/Gb.ogg")
            mixer.music.play()
        elif combo == "Ab":
            mixer.music.load("sounds/soundsAb/Db.ogg")
            mixer.music.play()
        elif combo == "Eb":
            mixer.music.load("sounds/soundsEb/Ab.ogg")
            mixer.music.play()
        elif combo == "Bb":
            mixer.music.load("sounds/soundsBb/Eb.ogg")
            mixer.music.play()
        elif combo == "F":
            mixer.music.load("sounds/soundsF/Bb.ogg")
            mixer.music.play()
        elif combo == "G":
            mixer.music.load("sounds/soundsG/C.ogg")
            mixer.music.play()
        elif combo == "D":
            mixer.music.load("sounds/soundsD/G.ogg")
            mixer.music.play()
        elif combo == "A":
            mixer.music.load("sounds/soundsA/D.ogg")
            mixer.music.play()
        elif combo == "E":
            mixer.music.load("sounds/soundsE/A.ogg")
            mixer.music.play()
        elif combo == "B":
            mixer.music.load("sounds/soundsB/E.ogg")
            mixer.music.play()
        elif combo == "F#":
            mixer.music.load("sounds/soundsF#/B.ogg")
            mixer.music.play()
        else:
            mixer.music.load("sounds/soundsC/F.ogg")
            mixer.music.play()

    def play_sound_five(self):
        mixer.init()
        combo = self.ui.comboBox.currentText()
        if combo == "Gb":
            mixer.music.load("sounds/soundsGb/Db.ogg")
            mixer.music.play()
        elif combo == "Db":
            mixer.music.load("sounds/soundsDb/Ab.ogg")
            mixer.music.play()
        elif combo == "Ab":
            mixer.music.load("sounds/soundsAb/Eb.ogg")
            mixer.music.play()
        elif combo == "Eb":
            mixer.music.load("sounds/soundsEb/Bb.ogg")
            mixer.music.play()
        elif combo == "Bb":
            mixer.music.load("sounds/soundsBb/F.ogg")
            mixer.music.play()
        elif combo == "F":
            mixer.music.load("sounds/soundsF/C.ogg")
            mixer.music.play()
        elif combo == "G":
            mixer.music.load("sounds/soundsG/D.ogg")
            mixer.music.play()
        elif combo == "D":
            mixer.music.load("sounds/soundsD/A.ogg")
            mixer.music.play()
        elif combo == "A":
            mixer.music.load("sounds/soundsA/E.ogg")
            mixer.music.play()
        elif combo == "E":
            mixer.music.load("sounds/soundsE/B.ogg")
            mixer.music.play()
        elif combo == "B":
            mixer.music.load("sounds/soundsB/F#.ogg")
            mixer.music.play()
        elif combo == "F#":
            mixer.music.load("sounds/soundsF#/Db.ogg")
            mixer.music.play()
        else:
            mixer.music.load("sounds/soundsC/G.ogg")
            mixer.music.play()

    def play_sound_six(self):
        mixer.init()
        combo = self.ui.comboBox.currentText()
        if combo == "Gb":
            mixer.music.load("sounds/soundsGb/Ebm.ogg")
            mixer.music.play()
        elif combo == "Db":
            mixer.music.load("sounds/soundsDb/Bbm.ogg")
            mixer.music.play()
        elif combo == "Ab":
            mixer.music.load("sounds/soundsAb/Fm.ogg")
            mixer.music.play()
        elif combo == "Eb":
            mixer.music.load("sounds/soundsEb/Cm.ogg")
            mixer.music.play()
        elif combo == "Bb":
            mixer.music.load("sounds/soundsBb/Gm.ogg")
            mixer.music.play()
        elif combo == "F":
            mixer.music.load("sounds/soundsF/Dm.ogg")
            mixer.music.play()
        elif combo == "G":
            mixer.music.load("sounds/soundsG/Em.ogg")
            mixer.music.play()
        elif combo == "D":
            mixer.music.load("sounds/soundsD/Bm.ogg")
            mixer.music.play()
        elif combo == "A":
            mixer.music.load("sounds/soundsA/F#m.ogg")
            mixer.music.play()
        elif combo == "E":
            mixer.music.load("sounds/soundsE/C#m.ogg")
            mixer.music.play()
        elif combo == "B":
            mixer.music.load("sounds/soundsB/G#m.ogg")
            mixer.music.play()
        elif combo == "F#":
            mixer.music.load("sounds/soundsF#/Ebm.ogg")
            mixer.music.play()
        else:
            mixer.music.load("sounds/soundsC/Am.ogg")
            mixer.music.play()

    def play_sound_seven(self):
        mixer.init()
        combo = self.ui.comboBox.currentText()
        if combo == "Gb":
            mixer.music.load("sounds/soundsGb/Fdim.ogg")
            mixer.music.play()
        elif combo == "Db":
            mixer.music.load("sounds/soundsDb/Cdim.ogg")
            mixer.music.play()
        elif combo == "Ab":
            mixer.music.load("sounds/soundsAb/Gdim.ogg")
            mixer.music.play()
        elif combo == "Eb":
            mixer.music.load("sounds/soundsEb/Ddim.ogg")
            mixer.music.play()
        elif combo == "Bb":
            mixer.music.load("sounds/soundsBb/Adim.ogg")
            mixer.music.play()
        elif combo == "F":
            mixer.music.load("sounds/soundsF/Edim.ogg")
            mixer.music.play()
        elif combo == "G":
            mixer.music.load("sounds/soundsG/F#dim.ogg")
            mixer.music.play()
        elif combo == "D":
            mixer.music.load("sounds/soundsD/C#dim.ogg")
            mixer.music.play()
        elif combo == "A":
            mixer.music.load("sounds/soundsA/G#dim.ogg")
            mixer.music.play()
        elif combo == "E":
            mixer.music.load("sounds/soundsE/D#dim.ogg")
            mixer.music.play()
        elif combo == "B":
            mixer.music.load("sounds/soundsB/A#dim.ogg")
            mixer.music.play()
        elif combo == "F#":
            mixer.music.load("sounds/soundsF#/Fdim.ogg")
            mixer.music.play()
        else:
            mixer.music.load("sounds/soundsC/Bdim.ogg")
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

        tableview = self.table.tableView
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
    #Ctrl A - J will handle this feature


if __name__=="__main__":
    MusicApp()
