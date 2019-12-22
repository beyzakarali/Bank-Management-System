# created by beyza at 2019-12-01 01:54.
# email : beyzakarali4743@gmail.com


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from ViewBMS.BMS import Ui_BMS
from ViewBMS.KayitOl import Ui_SignUp
from ControllerBMS.UserCls import User

    



#Giriş sayfası GUI
class Ui_LogIn(object):
    #Yapıcı fonksiyon
    def __init__(self):
        print("Giris.py __init__ ")
        self.winLogin = QtWidgets.QMainWindow()
        self.setupUi(self.winLogin)
        self.winLogin.show()
        self.onlineUser = User


    #def createUser(self, informationsOfUser):
    #    self.onlineUser = User(informationsOfUser)
    #    return self.onlineUser
        
    #Anamenü sayfasına aktarma
    def BMSPage (self, user : User): 
        self.winLogin.hide()
        self.win = Ui_BMS(user)

    #Kayıt sayfasına aktarma
    def LoginPage (self):
        self.winLogin.hide()
        self.win = Ui_SignUp(self.winLogin)

    #Hata giriş pop-up
    def showErrorDialog(self):
        msg = QMessageBox()
        msg.setWindowTitle("HATA")
        msg.setText("Hatalı giriş!")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Retry)
        msg.setDefaultButton(QMessageBox.Retry)
        msg.setInformativeText("Lütfen tekrar deneyin.")
        x = msg.exec_()

    #username and password entered from interface
    def getUsernamePassword(self):
        return self.lineEdit.text(), self.lineEdit_2.text()

    def authentication(self):
        username, password = self.getUsernamePassword()
        
        userInfo = self.onlineUser.getUserInformations(User, username, password)
        self.onlineUser = User.createUser(userInfo)
        self.onlineUser.createUsersPayments()
        self.onlineUser.createUsersAccounts()
        self.onlineUser.createUsersCredit()

        self.BMSPage(self.onlineUser)
        
        


######################### SAYFA DÜZENİ ###########################
#Pyuic5 generator ile otomatik oluşturulmuştur.
                   
    #Giris sayfası yapısı    
    def setupUi(self, LOGIN):
        LOGIN.setObjectName("LOGIN")
        LOGIN.setEnabled(True)
        LOGIN.resize(500, 400)
        LOGIN.setMinimumSize(QtCore.QSize(500, 400))
        LOGIN.setMaximumSize(QtCore.QSize(500, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        LOGIN.setFont(font)
        LOGIN.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.centralwidget = QtWidgets.QWidget(LOGIN)
        self.centralwidget.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 230, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(49, 49, 49);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 260, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 230, 141, 20))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 260, 141, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        
        #Enter ile giris.
        self.lineEdit_2.returnPressed.connect(self.authentication)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 350, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.label_5.setObjectName("label_5")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(270, 340, 185, 41))
        self.commandLinkButton.setStyleSheet("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 300, 51, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 50, 511, 301))
        self.label_2.setStyleSheet("background-color: rgb(49, 49, 49);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../FOTO/security-icon-information-10.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.label_4.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.label_5.raise_()
        self.commandLinkButton.raise_()
        LOGIN.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LOGIN)
        self.statusbar.setObjectName("statusbar")
        LOGIN.setStatusBar(self.statusbar)

        self.retranslateUi(LOGIN)
        QtCore.QMetaObject.connectSlotsByName(LOGIN)
        LOGIN.setTabOrder(self.lineEdit, self.lineEdit_2)
        LOGIN.setTabOrder(self.lineEdit_2, self.pushButton)
        LOGIN.setTabOrder(self.pushButton, self.commandLinkButton)

        self.lineEdit_2.returnPressed.connect(self.authentication)
        self.commandLinkButton.clicked.connect(self.LoginPage)
        self.pushButton.clicked.connect(self.authentication)


    def retranslateUi(self, LOGIN):
        _translate = QtCore.QCoreApplication.translate
        LOGIN.setWindowTitle(_translate("LOGIN", "LOGIN"))
        self.label.setText(_translate("LOGIN", "     BANK MANAGEMENT SYSTEM"))
        self.label_3.setText(_translate("LOGIN", "Kullanıcı Adı:"))
        self.label_4.setText(_translate("LOGIN", "Şifre :"))
        self.label_5.setText(_translate("LOGIN", "Henüz kayıtlı değilseniz"))
        self.commandLinkButton.setText(_translate("LOGIN", "TIKLAYIN"))
        self.pushButton.setText(_translate("LOGIN", "GİR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LOGIN = Ui_LogIn()
    sys.exit(app.exec_())
