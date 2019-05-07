import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, QShortcut
from PyQt5.uic import loadUi
from PyQt5 import QtSql, QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt
from main import Ui_MainWindow
import sqlite3
import os.path
from pprint import pprint as pp
from PyQt5.QtGui import QColor
from pygame import mixer
from PyQt5.QtCore import Qt
from table import Ui_Dialog
from time import time, sleep

mixer.init()
Gb = mixer.Sound("sounds/Gb.ogg")
Db = mixer.Sound("sounds/Db.ogg")
Ab = mixer.Sound("sounds/Ab.ogg")
Eb = mixer.Sound("sounds/Eb.ogg")
Bb = mixer.Sound("sounds/Bb.ogg")
F = mixer.Sound("sounds/F.ogg")
G = mixer.Sound("sounds/G.ogg")
D = mixer.Sound("sounds/D.ogg")
A = mixer.Sound("sounds/A.ogg")
E = mixer.Sound("sounds/E.ogg")
B = mixer.Sound("sounds/B.ogg")
f_sharp = mixer.Sound("sounds/Gb.ogg")
C = mixer.Sound("sounds/C.ogg")
Abm = mixer.Sound("sounds/Abm.ogg")
Ebm = mixer.Sound("sounds/Ebm.ogg")
Bbm = mixer.Sound("sounds/Bbm.ogg")
Fm = mixer.Sound("sounds/Fm.ogg")
Cm = mixer.Sound("sounds/Cm.ogg")
Gm = mixer.Sound("sounds/Gm.ogg")
Am = mixer.Sound("sounds/Am.ogg")
Em = mixer.Sound("sounds/Em.ogg")
Bm = mixer.Sound("sounds/Bm.ogg")
f_sharp_m = mixer.Sound("sounds/F#m.ogg")
c_sharp_m = mixer.Sound("sounds/C#m.ogg")
g_sharp_m = mixer.Sound("sounds/G#m.ogg")
d_sharp_m = mixer.Sound("sounds/D#m.ogg")
Dm = mixer.Sound("sounds/Dm.ogg")
Fdim = mixer.Sound("sounds/Fdim.ogg")
Cdim = mixer.Sound("sounds/Cdim.ogg")
Gdim =  mixer.Sound("sounds/Gdim.ogg")
Ddim = mixer.Sound("sounds/Ddim.ogg")
Adim = mixer.Sound("sounds/Adim.ogg")
Edim = mixer.Sound("sounds/Edim.ogg")
Bdim = mixer.Sound("sounds/Bdim.ogg")
f_sharp_dim = mixer.Sound("sounds/F#dim.ogg")
c_sharp_dim = mixer.Sound("sounds/C#dim.ogg")
g_sharp_dim = mixer.Sound("sounds/G#dim.ogg")
d_sharp_dim = mixer.Sound("sounds/D#dim.ogg")
a_sharp_dim = mixer.Sound("sounds/A#dim.ogg")

#------ seventh chords -------

a_sharp_m7b5 = mixer.Sound("sounds/sevenths/A#m7b5.ogg")
A7 = mixer.Sound("sounds/sevenths/A7.ogg")
Ab7 = mixer.Sound("sounds/sevenths/Ab7.ogg")
Abm7 = mixer.Sound("sounds/sevenths/Abm7.ogg")
Abmaj7 = mixer.Sound("sounds/sevenths/Abmaj7.ogg")
Am7 = mixer.Sound("sounds/sevenths/Am7.ogg")
Am7b5 = mixer.Sound("sounds/sevenths/Am7b5.ogg")
Amaj7 = mixer.Sound("sounds/sevenths/Amaj7.ogg")
B7 = mixer.Sound("sounds/sevenths/B7.ogg")
Bb7 = mixer.Sound("sounds/sevenths/Bb7.ogg")
Bbm7 = mixer.Sound("sounds/sevenths/Bbm7.ogg")
Bbmaj7 = mixer.Sound("sounds/sevenths/Bbmaj7.ogg")
Bmaj7 = mixer.Sound("sounds/sevenths/Bmaj7.ogg")
Bm7 = mixer.Sound("sounds/sevenths/Bm7.ogg")
Bm7b5 = mixer.Sound("sounds/sevenths/Bm7b5.ogg")
Bmaj7 = mixer.Sound("sounds/sevenths/Bmaj7.ogg")
c_sharp_m7 = mixer.Sound("sounds/sevenths/C#m7.ogg")
c_sharp_m7b5 = mixer.Sound("sounds/sevenths/C#m7b5.ogg")
C7 = mixer.Sound("sounds/sevenths/C7.ogg")
Cm7 = mixer.Sound("sounds/sevenths/Cm7.ogg")
Cm7b5 = mixer.Sound("sounds/sevenths/Cm7b5.ogg")
Cmaj7 = mixer.Sound("sounds/sevenths/Cmaj7.ogg")
d_sharp_m7 = mixer.Sound("sounds/sevenths/D#m7.ogg")
d_sharp_m7b5 = mixer.Sound("sounds/sevenths/D#m7b5.ogg")
D7 = mixer.Sound("sounds/sevenths/D7.ogg")
Db7 = mixer.Sound("sounds/sevenths/Db7.ogg")
Dbmaj7 = mixer.Sound("sounds/sevenths/Dbmaj7.ogg")
Dm7 = mixer.Sound("sounds/sevenths/Dm7.ogg")
Dm7b5 = mixer.Sound("sounds/sevenths/Dm7b5.ogg")
Dmaj7 = mixer.Sound("sounds/sevenths/Dmaj7.ogg")
E7 = mixer.Sound("sounds/sevenths/E7.ogg")
Eb7 = mixer.Sound("sounds/sevenths/Eb7.ogg")
Ebm7 = mixer.Sound("sounds/sevenths/Ebm7.ogg")
Ebmaj7 = mixer.Sound("sounds/sevenths/Ebmaj7.ogg")
Em7 = mixer.Sound("sounds/sevenths/Em7.ogg")
Em7b5 = mixer.Sound("sounds/sevenths/Em7b5.ogg")
Emaj7 = mixer.Sound("sounds/sevenths/Emaj7.ogg")
f_sharp7 = mixer.Sound("sounds/sevenths/F#7.ogg")
f_sharp_m7 = mixer.Sound("sounds/sevenths/F#m7.ogg")
f_sharp_m7b5 = mixer.Sound("sounds/sevenths/F#m7b5.ogg")
F7 = mixer.Sound("sounds/sevenths/F7.ogg")
Fm7 = mixer.Sound("sounds/sevenths/Fm7.ogg")
Fm7b5 = mixer.Sound("sounds/sevenths/Fm7b5.ogg")
Fmaj7 = mixer.Sound("sounds/sevenths/Fmaj7.ogg")
g_sharp_m7 = mixer.Sound("sounds/sevenths/G#m7.ogg")
g_sharp_m7b5 = mixer.Sound("sounds/sevenths/G#m7b5.ogg")
G7 = mixer.Sound("sounds/sevenths/G7.ogg")
Gbmaj7 = mixer.Sound("sounds/sevenths/Gbmaj7.ogg")
Gm7 = mixer.Sound("sounds/sevenths/Gm7.ogg")
Gm7b5 = mixer.Sound("sounds/sevenths/Gm7b5.ogg")
Gmaj7 = mixer.Sound("sounds/sevenths/Gmaj7.ogg")



keys_name = [['Gb', 'Abm', 'Bbm', 'Cb', 'Db', 'Ebm','Fdim'],
    ['Db', 'Ebm','Fm', 'Gb', 'Ab', 'Bbm', 'Cdim'],
    ['Ab', 'Bbm', 'Cm', 'Db', 'Eb','Fm', 'Gdim'],
    ['Eb','Fm', 'Gm', 'Ab', 'Bb', 'Cm', 'Ddim'],
    ['Bb', 'Cm', 'Dm', 'Eb','F', 'Gm', 'Adim'],
    ['F', 'Gm', 'Am', 'Bb', 'C', 'Dm', 'Edim'],
    ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim'],
    ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'F#dim'],
    ['D', 'Em', 'F#m', 'G', 'A', 'Bm', 'C#dim'],
    ['A', 'Bm', 'C#m', 'D', 'E', 'F#m', 'G#dim'],
    ['E', 'F#m', 'G#m', 'A', 'B', 'C#m', 'D#dim'],
    ['B', 'C#m', 'D#m', 'E', 'F#', 'G#m', 'A#dim'],
    ['F#', 'G#m', 'A#m', 'B', 'C#', 'D#m', 'E#dim']]

#variable sound name
keys_chords = [['Gb', 'Abm', 'Bbm', 'B', 'Db', 'Ebm','Fdim'],
    ['Db', 'Ebm','Fm', 'Gb', 'Ab', 'Bbm', 'Cdim'],
    ['Ab', 'Bbm', 'Cm', 'Db', 'Eb','Fm', 'Gdim'],
    ['Eb','Fm', 'Gm', 'Ab', 'Bb', 'Cm', 'Ddim'],
    ['Bb', 'Cm', 'Dm', 'Eb','F', 'Gm', 'Adim'],
    ['F', 'Gm', 'Am', 'Bb', 'C', 'Dm', 'Edim'],
    ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim'],
    ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'f_sharp_dim'],
    ['D', 'Em', 'f_sharp_m', 'G', 'A', 'Bm', 'c_sharp_dim'],
    ['A', 'Bm', 'c_sharp_m', 'D', 'E', 'f_sharp_m', 'g_sharp_dim'],
    ['E', 'f_sharp_m', 'g_sharp_m', 'A', 'B', 'c_sharp_m', 'd_sharp_dim'],
    ['B', 'c_sharp_m', 'd_sharp_m', 'E', 'f_sharp', 'g_sharp_m', 'a_sharp_dim'],
    ['f_sharp', 'Abm', 'Bbm', 'B', 'Db', 'Ebm', 'Fdim']]


# -------- seventh chords ---------

keys_seventh_name = [['Gbmaj7', 'Abm7', 'Bbm7', 'Bmaj7', 'Db7', 'Ebm7','Fm7b5'],
    ['Dbmaj7', 'Ebm7','Fm7', 'Gbmaj7', 'Ab7', 'Bbm7', 'Cm7b5'],
    ['Abmaj7', 'Bbm7', 'Cm7', 'Dbmaj7', 'Eb7','Fm7', 'Gm7b5'],
    ['Ebmaj7','Fm7', 'Gm7', 'Abmaj7', 'Bb7', 'Cm7', 'Dm7b5'],
    ['Bbmaj7', 'Cm7', 'Dm7', 'Ebmaj7','F7', 'Gm7', 'Am7b5'],
    ['Fmaj7', 'Gm7', 'Am7', 'Bbmaj7', 'C7', 'Dm7', 'Em7b5'],
    ['Cmaj7', 'Dm7', 'Em7', 'Fmaj7', 'G7', 'Am7', 'Bm7b5'],
    ['Gmaj7', 'Am7', 'Bm7', 'Cmaj7', 'D7', 'Em7', 'F#m7b5'],
    ['Dmaj7', 'Em7', 'F#m7', 'Gmaj7', 'A7', 'Bm7', 'C#m7b5'],
    ['Amaj7', 'Bm7', 'C#m7', 'Dmaj7', 'E7', 'F#m7', 'G#m7b5'],
    ['Emaj7', 'F#m7', 'G#m7', 'Amaj7', 'B7', 'C#m7', 'D#m7b5'],
    ['Bmaj7', 'C#m7', 'D#m7', 'Emaj7', 'F#7', 'G#m7', 'A#m7b5'],
    ['F#maj7', 'G#m7', 'A#m7', 'Bmaj7', 'C#7', 'D#m7', 'E#m7b5']]

#variable sound names
keys_chords_seventh = [['Gbmaj7', 'Abm7', 'Bbm7', 'Bmaj7', 'Db7', 'Ebm7','Fm7b5'],
    ['Dbmaj7', 'Ebm7','Fm7', 'Gbmaj7', 'Ab7', 'Bbm7', 'Cm7b5'],
    ['Abmaj7', 'Bbm7', 'Cm7', 'Dbmaj7', 'Eb7','Fm7', 'Gm7b5'],
    ['Ebmaj7','Fm7', 'Gm7', 'Abmaj7', 'Bb7', 'Cm7', 'Dm7b5'],
    ['Bbmaj7', 'Cm7', 'Dm7', 'Ebmaj7','F7', 'Gm7', 'Am7b5'],
    ['Fmaj7', 'Gm7', 'Am7', 'Bbmaj7', 'C7', 'Dm7', 'Em7b5'],
    ['Cmaj7', 'Dm7', 'Em7', 'Fmaj7', 'G7', 'Am7', 'Bm7b5'],
    ['Gmaj7', 'Am7', 'Bm7', 'Cmaj7', 'D7', 'Em7', 'f_sharp_m7b5'],
    ['Dmaj7', 'Em7', 'f_sharp_m7', 'Gmaj7', 'A7', 'Bm7', 'c_sharp_m7b5'],
    ['Amaj7', 'Bm7', 'c_sharp_m7', 'Dmaj7', 'E7', 'f_sharp_m7', 'g_sharp_m7b5'],
    ['Emaj7', 'f_sharp_m7', 'g_sharp_m7', 'Amaj7', 'B7', 'c_sharp_m7', 'd_sharp_m7b5'],
    ['Bmaj7', 'c_sharp_m7', 'd_sharp_m7', 'Emaj7', 'f_sharp7', 'g_sharp_m7', 'a_sharp_m7b5'],
    ['Gbmaj7', 'Abm7', 'Bbm7', 'Bmaj7', 'Db7', 'Ebm7', 'Fm7b5']]



class MainWindow(QMainWindow):
    """docstring for Music App"""
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Set up variables
        self.seventh_flag = False
        self.current_song = []
        self.current_playable = []
        self.combo = self.ui.comboBox.currentText()
        self.ui.seventh_chord.setCheckable(True)


        self.ui.one_chord.clicked.connect(self.play_sound_one)
        self.ui.two_chord.clicked.connect(self.play_sound_two)
        self.ui.three_chord.clicked.connect(self.play_sound_three)
        self.ui.four_chrod.clicked.connect(self.play_sound_four)
        self.ui.five_chord.clicked.connect(self.play_sound_five)
        self.ui.six_chord.clicked.connect(self.play_sound_six)
        self.ui.seven_chord.clicked.connect(self.play_sound_seven)
        self.ui.viewChords.clicked.connect(self.open_table)
        self.ui.comboBox.currentTextChanged.connect(self.on_combobox_changed)
        self.ui.seventh_chord.toggled.connect(self.on_pushButtonSetBase_toggled)
        self.ui.recButton.clicked.connect(self.record)
        self.ui.playButton.clicked.connect(self.playback)
        #initialize combo comboBox
        self.on_combobox_changed()


        self.key_dlg = QtWidgets.QDialog()
        self.table = Ui_Dialog()
        self.table.setupUi(self.key_dlg)
        self.table.btnClose.clicked.connect(self.key_dlg.close)

        self.model = None

    #set stylesheet




    def open_table(self):
        self.sql_tableview_model()
        self.key_dlg.show()
        self.key_dlg.exec_()

        # self.window = QtWidgets.QDialog()
        # self.table = Ui_Dialog()
        # self.table.setupUi(self.window)
        # self.window.show()


    #change order of loading chords




    @QtCore.pyqtSlot(bool)  #<<== the missing link
    def on_pushButtonSetBase_toggled(self,checked):
        if checked:
            self.seventh_flag = True
            print(self.seventh_flag)
            self.change_seven()
        else:
            self.seventh_flag = False
            self.change_chord()
            print(self.seventh_flag)

#TODO set default value to C
    def on_combobox_changed(self):
        current_selection = []
        self.combo = self.ui.comboBox.currentIndex()
        if self.seventh_flag == True:
            self.change_seven()
        else:
            self.change_chord()

    def change_chord(self):
        self.ui.label_1.setText(keys_name[self.combo][0])
        self.ui.label_2.setText(keys_name[self.combo][1])
        self.ui.label_3.setText(keys_name[self.combo][2])
        self.ui.label_4.setText(keys_name[self.combo][3])
        self.ui.label_5.setText(keys_name[self.combo][4])
        self.ui.label_6.setText(keys_name[self.combo][5])
        self.ui.label_7.setText(keys_name[self.combo][6])

    def change_seven(self):
        self.ui.label_1.setText(keys_seventh_name[self.combo][0])
        self.ui.label_2.setText(keys_seventh_name[self.combo][1])
        self.ui.label_3.setText(keys_seventh_name[self.combo][2])
        self.ui.label_4.setText(keys_seventh_name[self.combo][3])
        self.ui.label_5.setText(keys_seventh_name[self.combo][4])
        self.ui.label_6.setText(keys_seventh_name[self.combo][5])
        self.ui.label_7.setText(keys_seventh_name[self.combo][6])

#TODO change how sounds are played
#UPdate current Key

    def play_sound_one(self):
        self.current_song.append((time(), 0))
        if self.seventh_flag == False:
            play_chord = keys_chords[self.combo][0] + ".play()"
            exec(play_chord)
        else:
            play_chord = keys_chords_seventh[self.combo][0] + ".play()"
            exec(play_chord)


    def play_sound_two(self):
        self.current_song.append((time(), 1))
        if self.seventh_flag == False:
            play_chord = keys_chords[self.combo][1] + ".play()"
            exec(play_chord)
        else:
            play_chord = keys_chords_seventh[self.combo][1] + ".play()"
            exec(play_chord)


    def play_sound_three(self):
        self.current_song.append((time(), 2))
        if self.seventh_flag == False:
            play_chord = keys_chords[self.combo][2] + ".play()"
            exec(play_chord)
        else:
            play_chord = keys_chords_seventh[self.combo][2] + ".play()"
            exec(play_chord)


    def play_sound_four(self):
        self.current_song.append((time(), 3))
        if self.seventh_flag == False:
            play_chord = keys_chords[self.combo][3] + ".play()"
            exec(play_chord)
        else:
            play_chord = keys_chords_seventh[self.combo][3] + ".play()"
            exec(play_chord)


    def play_sound_five(self):
        self.current_song.append((time(), 4))
        if self.seventh_flag == False:
            play_chord = keys_chords[self.combo][4] + ".play()"
            exec(play_chord)
        else:
            play_chord = keys_chords_seventh[self.combo][4] + ".play()"
            exec(play_chord)


    def play_sound_six(self):
        self.current_song.append((time(), 5))
        if self.seventh_flag == False:
            play_chord = keys_chords[self.combo][5] + ".play()"
            exec(play_chord)
        else:
            play_chord = keys_chords_seventh[self.combo][5] + ".play()"
            exec(play_chord)


    def play_sound_seven(self):
        self.current_song.append((time(), 6))
        if self.seventh_flag == False:
            play_chord = keys_chords[self.combo][6] + ".play()"
            exec(play_chord)
        else:
            play_chord = keys_chords_seventh[self.combo][6] + ".play()"
            exec(play_chord)


#***** Record Code ******#

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_R:
            self.record()
        elif e.key() == Qt.Key_P:
            self.playback()
        else:
            e.ignore()
        e.accept()


    def record(self):
        self.current_song = []
        self.current_playable = []


    def convert_time(self):
        prev = self.current_song[0][0]
        for event in self.current_song:
            self.current_playable.append((event[0] - prev, event[1]))
            prev = event[0]
        print("converting", self.current_playable)
        sleep(5)
        # self.playback()

    def playback(self):
        if not self.current_playable:
            self.convert_time()
        for item in self.current_playable:
            sleep(item[0])
            #GEt name of chord

            # item[1].play()
            play_chord = keys_chords[self.combo][item[1]] + ".play()"
            exec(play_chord)
            print(item[1], keys_name[self.combo][item[1]])
        print(self.current_song)
        pp(self.current_playable)

    # def keyPressEvent(self, event):
    #     if type(event) == QtGui.QKeyEvent:
    #         if event.key() == QtCore.Qt.Key_A:





        #*** Database Code ***------------------------------
    # def sql_delete_row(self):
    #     if self.model:
    #         self.model.removeRow(self.tableview.currentIndex().row())
    #     else:
    #         self.sql_tableview_model()
    #
    # def sql_add_row(self):
    #     if self.model:
    #         self.model.insertRows(self.model.rowCount(), 1)
    #     else:
    #         self.sql_tableview_model()

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
    # def print_data(self):
    #     sqlite_file = 'KEYS.db'
    #     conn = sqlite3.connect(sqlite_file)
    #     cursor = conn.cursor()
    #
    #     cursor.execute("SELECT * FROM KEYS ORDER BY ID")
    #     all_rows = cursor.fetchall()
    #     pprint(all_rows)
    #
    #     conn.commit()
    #     conn.close()


        #******** Print db ********#
    # def create_key_db(self):
    #     db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    #     db.setDatabaseName('KEYS.db')
    #     db.open()
    #
    #     query = QtSql.QSqlQuery()
    #
    #     query.exec_("create table KEYS(ID int primary key, "
    #                 "I varchar(2),"
    #                 "II varchar(2),"
    #                 "III varchar(2),"
    #                 "IV varchar(2),"
    #                 "V varchar(2),"
    #                 "VI varchar(2),"
    #                 "VII varchar(2))")
    #     query.exec_("insert into KEYS values(1, 'Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb','F')")
    #     query.exec_("insert into KEYS values(2, 'Db', 'Eb','F', 'Gb', 'Ab', 'Bb', 'C')")
    #     query.exec_("insert into KEYS values(3, 'Ab', 'Bb', 'C', 'Db', 'Eb','F', 'G')")
    #     query.exec_("insert into KEYS values(4, 'Eb','F', 'G', 'Ab', 'Bb', 'C', 'D')")
    #     query.exec_("insert into KEYS values(5, 'Bb', 'C', 'D', 'Eb','F', 'G', 'A')")
    #     query.exec_("insert into KEYS values(6, 'F', 'G', 'A', 'Bb', 'C', 'D', 'E')")
    #     query.exec_("insert into KEYS values(7, 'C', 'D', 'E', 'F', 'G', 'A', 'B')")
    #     query.exec_("insert into KEYS values(8, 'G', 'A', 'B', 'C', 'D', 'E', 'F#')")
    #     query.exec_("insert into KEYS values(9, 'D', 'E', 'F#', 'G', 'A', 'B', 'C#')")
    #     query.exec_("insert into KEYS values(10, 'A', 'B', 'C#', 'D', 'E', 'F#', 'G#')")
    #     query.exec_("insert into KEYS values(11, 'E', 'F#', 'G#', 'A', 'B', 'C#', 'D#')")
    #     query.exec_("insert into KEYS values(12, 'B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#')")
    #     query.exec_("insert into KEYS values(13, 'F#', 'G#', 'A#', 'B', 'C#', 'D#', 'E#')")


    #********* play sound when keyboard key is pressed **********#
    #Ctrl A - J will handle this feature


if __name__=="__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
