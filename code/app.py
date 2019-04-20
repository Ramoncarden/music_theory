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

mixer.init()
Gb = mixer.Sound("sounds/soundsGb/Gb.ogg")
Db = mixer.Sound("sounds/soundsDb/Db.ogg")
Ab = mixer.Sound("sounds/soundsAb/Ab.ogg")
Eb = mixer.Sound("sounds/soundsEb/Eb.ogg")
Bb = mixer.Sound("sounds/soundsBb/Bb.ogg")
F = mixer.Sound("sounds/soundsF/F.ogg")
G = mixer.Sound("sounds/soundsG/G.ogg")
D = mixer.Sound("sounds/soundsD/D.ogg")
A = mixer.Sound("sounds/soundsA/A.ogg")
E = mixer.Sound("sounds/soundsE/E.ogg")
B = mixer.Sound("sounds/soundsB/B.ogg")
f_sharp = mixer.Sound("sounds/soundsF#/Gb.ogg")
C = mixer.Sound("sounds/soundsC/C.ogg")
Abm = mixer.Sound("sounds/soundsGb/Abm.ogg")
Ebm = mixer.Sound("sounds/soundsDb/Ebm.ogg")
Bbm = mixer.Sound("sounds/soundsAb/Bbm.ogg")
Fm = mixer.Sound("sounds/soundsEb/Fm.ogg")
Cm = mixer.Sound("sounds/soundsBb/Cm.ogg")
Gm = mixer.Sound("sounds/soundsF/Gm.ogg")
Am = mixer.Sound("sounds/soundsG/Am.ogg")
Em = mixer.Sound("sounds/soundsD/Em.ogg")
Bm = mixer.Sound("sounds/soundsA/Bm.ogg")
f_sharp_m = mixer.Sound("sounds/soundsE/F#m.ogg")
c_sharp_m = mixer.Sound("sounds/soundsB/C#m.ogg")
g_sharp_m = mixer.Sound("sounds/soundsE/G#m.ogg")
d_sharp_m = mixer.Sound("sounds/soundsB/D#m.ogg")
Dm = mixer.Sound("sounds/soundsC/Dm.ogg")
Fdim = mixer.Sound("sounds/soundsGb/Fdim.ogg")
Cdim = mixer.Sound("sounds/soundsDb/Cdim.ogg")
Gdim =  mixer.Sound("sounds/soundsAb/Gdim.ogg")
Ddim = mixer.Sound("sounds/soundsEb/Ddim.ogg")
Adim = mixer.Sound("sounds/soundsBb/Adim.ogg")
Edim = mixer.Sound("sounds/soundsF/Edim.ogg")
Bdim = mixer.Sound("sounds/soundsC/Bdim.ogg")
f_sharp_dim = mixer.Sound("sounds/soundsG/F#dim.ogg")
c_sharp_dim = mixer.Sound("sounds/soundsD/C#dim.ogg")
g_sharp_dim = mixer.Sound("sounds/soundsA/G#dim.ogg")
d_sharp_dim = mixer.Sound("sounds/soundsE/D#dim.ogg")
a_sharp_dim = mixer.Sound("sounds/soundsB/A#dim.ogg")




class SoundApp():
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
        # self.btnClose.clicked.connect(print_hi)
        # table.btnClose.clicked.connect(self.print_hi)

        self.model = None
        self.ui.viewChords.clicked.connect(self.sql_tableview_model)
        # self.ui.viewChords.clicked.connect(self.sql_add_row)
        # self.ui.viewChords.clicked.connect(self.sql_delete_row)
        self.ui.viewChords.clicked.connect(self.create_key_db)
        self.MainWindow.show()
        sys.exit(app.exec_())


    def open_table(self):
        self.window = QtWidgets.QDialog()
        self.table = Ui_Dialog()
        self.table.setupUi(self.window)
        self.window.show()

    def print_hi(self):
        print("hello")

    def play_sound_one(self):
        combo = self.ui.comboBox.currentText()
        if combo == "Gb":
            mixer.Sound.play(Gb)
        elif combo == "Db":
            mixer.Sound.play(Db)
        elif combo == "Ab":
            mixer.Sound.play(Ab)
        elif combo == "Eb":
            mixer.Sound.play(Eb)
        elif combo == "Bb":
            mixer.Sound.play(Bb)
        elif combo == "F":
            mixer.Sound.play(F)
        elif combo == "G":
            mixer.Sound.play(G)
        elif combo == "D":
            mixer.Sound.play(D)
        elif combo == "A":
            mixer.Sound.play(A)
        elif combo == "E":
            mixer.Sound.play(E)
        elif combo == "B":
            mixer.Sound.play(B)
        elif combo == "F#":
            mixer.Sound.play(f_sharp)
        else:
            mixer.Sound.play(C)

    def play_sound_two(self):
        combo = self.ui.comboBox.currentText()
        if combo == "Gb":
            mixer.Sound.play(Abm)
        elif combo == "Db":
            mixer.Sound.play(Ebm)
        elif combo == "Ab":
            mixer.Sound.play(Bbm)
        elif combo == "Eb":
            mixer.Sound.play(Fm)
        elif combo == "Bb":
            mixer.Sound.play(Cm)
        elif combo == "F":
            mixer.Sound.play(Gm)
        elif combo == "G":
            mixer.Sound.play(Am)
        elif combo == "D":
            mixer.Sound.play(Em)
        elif combo == "A":
            mixer.Sound.play(Bm)
        elif combo == "E":
            mixer.Sound.play(f_sharp_m)
        elif combo == "B":
            mixer.Sound.play(c_sharp_m)
        elif combo == "F#":
            mixer.Sound.play(Abm)
        else:
            mixer.Sound.play(Dm)

    def play_sound_three(self):
        combo = self.ui.comboBox.currentText()
        if combo == "Gb":
            mixer.Sound.play(Bbm)
        elif combo == "Db":
            mixer.Sound.play(Fm)
        elif combo == "Ab":
            mixer.Sound.play(Cm)
        elif combo == "Eb":
            mixer.Sound.play(Gm)
        elif combo == "Bb":
            mixer.Sound.play(Dm)
        elif combo == "F":
            mixer.Sound.play(Am)
        elif combo == "G":
            mixer.Sound.play(Bm)
        elif combo == "D":
            mixer.Sound.play(f_sharp_m)
        elif combo == "A":
            mixer.Sound.play(c_sharp_m)
        elif combo == "E":
            mixer.Sound.play(g_sharp_m)
        elif combo == "B":
            mixer.Sound.play(d_sharp_m)
        elif combo == "F#":
            mixer.Sound.play(Bbm)
        else:
            mixer.Sound.play(Em)

    def play_sound_four(self):
        combo = self.ui.comboBox.currentText()
        if combo == "Gb":
            mixer.Sound.play(B)
        elif combo == "Db":
            mixer.Sound.play(Gb)
        elif combo == "Ab":
            mixer.Sound.play(Db)
        elif combo == "Eb":
            mixer.Sound.play(Ab)
        elif combo == "Bb":
            mixer.Sound.play(Eb)
        elif combo == "F":
            mixer.Sound.play(Bb)
        elif combo == "G":
            mixer.Sound.play(C)
        elif combo == "D":
            mixer.Sound.play(G)
        elif combo == "A":
            mixer.Sound.play(D)
        elif combo == "E":
            mixer.Sound.play(A)
        elif combo == "B":
            mixer.Sound.play(E)
        elif combo == "F#":
            mixer.Sound.play(B)
        else:
            mixer.Sound.play(F)

    def play_sound_five(self):
        combo = self.ui.comboBox.currentText()
        if combo == "Gb":
            mixer.Sound.play(Db)
        elif combo == "Db":
            mixer.Sound.play(Ab)
        elif combo == "Ab":
            mixer.Sound.play(Eb)
        elif combo == "Eb":
            mixer.Sound.play(Bb)
        elif combo == "Bb":
            mixer.Sound.play(F)
        elif combo == "F":
            mixer.Sound.play(C)
        elif combo == "G":
            mixer.Sound.play(D)
        elif combo == "D":
            mixer.Sound.play(A)
        elif combo == "A":
            mixer.Sound.play(E)
        elif combo == "E":
            mixer.Sound.play(B)
        elif combo == "B":
            mixer.Sound.play(f_sharp)
        elif combo == "F#":
            mixer.Sound.play(Db)
        else:
            mixer.Sound.play(G)

    def play_sound_six(self):
        combo = self.ui.comboBox.currentText()
        if combo == "Gb":
            mixer.Sound.play(Ebm)
        elif combo == "Db":
            mixer.Sound.play(Bbm)
        elif combo == "Ab":
            mixer.Sound.play(Fm)
        elif combo == "Eb":
            mixer.Sound.play(Cm)
        elif combo == "Bb":
            mixer.Sound.play(Gm)
        elif combo == "F":
            mixer.Sound.play(Dm)
        elif combo == "G":
            mixer.Sound.play(Em)
        elif combo == "D":
            mixer.Sound.play(Bm)
        elif combo == "A":
            mixer.Sound.play(f_sharp_m)
        elif combo == "E":
            mixer.Sound.play(c_sharp_m)
        elif combo == "B":
            mixer.Sound.play(g_sharp_m)
        elif combo == "F#":
            mixer.Sound.play(Ebm)
        else:
            mixer.Sound.play(Am)

    def play_sound_seven(self):
        combo = self.ui.comboBox.currentText()
        if combo == "Gb":
            mixer.Sound.play(Fdim)
        elif combo == "Db":
            mixer.Sound.play(Cdim)
        elif combo == "Ab":
            mixer.Sound.play(Gdim)
        elif combo == "Eb":
            mixer.Sound.play(Ddim)
        elif combo == "Bb":
            mixer.Sound.play(Adim)
        elif combo == "F":
            mixer.Sound.play(Edim)
        elif combo == "G":
            mixer.Sound.play(f_sharp_dim)
        elif combo == "D":
            mixer.Sound.play(c_sharp_dim)
        elif combo == "A":
            mixer.Sound.play(g_sharp_dim)
        elif combo == "E":
            mixer.Sound.play(d_sharp_dim)
        elif combo == "B":
            mixer.Sound.play(a_sharp_dim)
        elif combo == "F#":
            mixer.Sound.play(Fdim)
        else:
            mixer.Sound.play(Bdim)

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
    SoundApp()
