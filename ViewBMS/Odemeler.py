
# created by beyza at 2019-11-30 01:33.
# email : beyzakarali4743@gmail.com


from PyQt5 import QtCore, QtGui, QtWidgets
from Bagis import Ui_Donation
from Fatura import Ui_Bill
from Vergi_Resmi import Ui_TaxOfficial

class Ui_Payments(object):
    def __init__(self):
        self.winPayments = QtWidgets.QMainWindow()
        self.setupUi(self.winPayments)
        self.winPayments.show()

    def DonationPage(self):
        self.winPayments.hide()
        self.win = Ui_Donation()

    def BillPage(self):
        self.winPayments.hide()
        self.win2 = Ui_Bill()
        
    def TaxOfficialPage(self):
        self.winPayments.hide()
        self.win = Ui_TaxOfficial()

    def setupUi(self, Payments):
        Payments.setObjectName("Payments")
        Payments.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(Payments)
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
        self.commandLinkButton.clicked.connect(self.BillPage)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(0, 240, 271, 41))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_2.clicked.connect(self.TaxOfficialPage)
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(0, 110, 185, 41))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_3.clicked.connect(self.DonationPage)
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(370, 350, 121, 41))
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
       # self.commandLinkButton_5.clicked.connect()
        Payments.setCentralWidget(self.centralwidget)

        self.retranslateUi(Payments)
        QtCore.QMetaObject.connectSlotsByName(Payments)
    
    def retranslateUi(self, Payments):
        _translate = QtCore.QCoreApplication.translate
        Payments.setWindowTitle(_translate("Odemler", "ÖDEMELER"))
        self.label.setText(_translate("Odemler", "ÖDEMELER"))
        self.commandLinkButton.setText(_translate("Odemler", "FATURA ÖDEME"))
        self.commandLinkButton_2.setText(_translate("Odemler", "VERGİLER VE RESMİ KURUMLAR"))
        self.commandLinkButton_3.setText(_translate("Odemler", "BAĞIŞ"))
        self.commandLinkButton_5.setText(_translate("Odemler", "ANA MENÜ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PAYMENTS = Ui_Payments()
    sys.exit(app.exec_())
