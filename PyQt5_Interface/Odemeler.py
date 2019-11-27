# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ödemeler.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Bağış import Ui_Bagis
from Fatura import Ui_Fatura
from Vergi_Resmi import Ui_Vergi_Resmi

class Ui_Odemler(object):

    def Bagis_page(self):
        self.win =  QtWidgets.QMainWindow()
        self.ui = Ui_Bagis()
        self.ui.setupUi(self.win)
        #Odemler.hide()
        self.win.show()

    def Fatura_page(self):
        self.win =  QtWidgets.QMainWindow()
        self.ui = Ui_Fatura()
        self.ui.setupUi(self.win)
       # Odemler.hide()
        self.win.show()
        
    def Vergi_page(self):
        self.win =  QtWidgets.QMainWindow()
        self.ui = Ui_Vergi_Resmi()
        self.ui.setupUi(self.win)
       # Odemler.hide()
        self.win.show()

    def setupUi(self, Odemler):
        Odemler.setObjectName("Odemler")
        Odemler.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(Odemler)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, -20, 291, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(0, 170, 185, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(self.Fatura_page)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(0, 240, 271, 41))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_2.clicked.connect(self.Vergi_page)
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(0, 110, 185, 41))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_3.clicked.connect(self.Bagis_page)
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(370, 350, 121, 41))
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
       # self.commandLinkButton_5.clicked.connect()
        Odemler.setCentralWidget(self.centralwidget)

        self.retranslateUi(Odemler)
        QtCore.QMetaObject.connectSlotsByName(Odemler)
    
    def retranslateUi(self, Odemler):
        _translate = QtCore.QCoreApplication.translate
        Odemler.setWindowTitle(_translate("Odemler", "ÖDEMELER"))
        self.label.setText(_translate("Odemler", "ÖDEMELER"))
        self.commandLinkButton.setText(_translate("Odemler", "FATURA ÖDEME"))
        self.commandLinkButton_2.setText(_translate("Odemler", "VERGİLER VE RESMİ KURUMLAR"))
        self.commandLinkButton_3.setText(_translate("Odemler", "BAĞIŞ"))
        self.commandLinkButton_5.setText(_translate("Odemler", "GERİ DÖN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Odemler = QtWidgets.QMainWindow()
    ui = Ui_Odemler()
    ui.setupUi(Odemler)
    Odemler.show()
    sys.exit(app.exec_())
