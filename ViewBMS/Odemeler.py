
# created by beyza at 2019-11-30 01:33.
# email : beyzakarali4743@gmail.com


from PyQt5 import QtCore, QtGui, QtWidgets
from ViewBMS.Bagis import Ui_Donation
from ViewBMS.Fatura import Ui_Bill
from ViewBMS.Vergi_Resmi import Ui_TaxOfficial




class Ui_Payments(object):

    def __init__(self, prevWin : QtWidgets.QMainWindow = None):
        self.winPayments = QtWidgets.QMainWindow()
        self.setupUi(self.winPayments)
        self.winPayments.show()
        self.prevWin = prevWin

    def DonationPage(self):
        self.winPayments.hide()
        self.win = Ui_Donation()

    def passPrevWin(self):
        self.winPayments.close()
        self.prevWin.show()

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
        self.centralwidget.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, -20, 291, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(360, 340, 121, 41))
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 140, 220, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.verticalLayout.addWidget(self.commandLinkButton_3)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout.addWidget(self.commandLinkButton)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.verticalLayoutWidget)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.verticalLayout.addWidget(self.commandLinkButton_2)
        Payments.setCentralWidget(self.centralwidget)

        self.retranslateUi(Payments)
        QtCore.QMetaObject.connectSlotsByName(Payments)
        Payments.setTabOrder(self.commandLinkButton_3, self.commandLinkButton)
        Payments.setTabOrder(self.commandLinkButton, self.commandLinkButton_2)
        Payments.setTabOrder(self.commandLinkButton_2, self.commandLinkButton_5)

        self.commandLinkButton.clicked.connect(self.BillPage)
        self.commandLinkButton_2.clicked.connect(self.TaxOfficialPage)
        self.commandLinkButton_3.clicked.connect(self.DonationPage)
        self.commandLinkButton_5.clicked.connect(self.passPrevWin)
        

    def retranslateUi(self, Payments):
        _translate = QtCore.QCoreApplication.translate
        Payments.setWindowTitle(_translate("Payments", "ÖDEMELER"))
        self.label.setText(_translate("Payments", "ÖDEMELER"))
        self.commandLinkButton_5.setText(_translate("Payments", "GERİ DÖN"))
        self.commandLinkButton_3.setText(_translate("Payments", "BAĞIŞ"))
        self.commandLinkButton.setText(_translate("Payments", "FATURA ÖDEME"))
        self.commandLinkButton_2.setText(_translate("Payments", "VERGİLER VE RESMİ KURUMLAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Payments = Ui_Payments()
    sys.exit(app.exec_())
