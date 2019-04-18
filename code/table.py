# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(756, 548)
        self.btnClose = QtWidgets.QPushButton(Dialog)
        self.btnClose.setGeometry(QtCore.QRect(320, 500, 113, 32))
        self.btnClose.setObjectName("btnClose")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setEnabled(True)
        self.tableView.setGeometry(QtCore.QRect(15, 10, 731, 481))
        self.tableView.setShowGrid(True)
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnClose.setText(_translate("Dialog", "Close"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    table = Ui_Dialog()
    table.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
