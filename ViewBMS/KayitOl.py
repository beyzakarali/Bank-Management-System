
#Telefon numarası eklenecek.

from PyQt5 import QtCore, QtGui, QtWidgets
from ModelBMS.database import Database as db

NEXT_TAB = 1

class Ui_Record(object):
    def __init__(self, prevWin = None):
        self.winRecord = QtWidgets.QMainWindow()
        self.setupUi(self.winRecord)
        self.winRecord.show()
        self.prevWin = prevWin

    #Giris sayfasına aktarma
    def Giris_page (self):
        print("giris page....")
        self.winRecord.hide()
        self.win = Ui_LOGIN()

    def changeTab(self):
        index = self.tabWidget.currentIndex()
        self.tabWidget.setCurrentIndex(index + NEXT_TAB)

    def insertUser(self):
        #eğer başarılı olursa giris_page çalıştır.
        userInfo = self.getUserInfo()
        for i in userInfo:
            print(i)
        db.Query(db, 
        "INSERT INTO customer(AdminId, Name, Surname, TCNo, DateOfBirth, Mail, Gender, ProfilePhoto, Username, Password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        , userInfo)
        print("insertUser function....")
        self.Giris_page()

    def getUserInfo(self):
        userInfo = []
        userInfo.append("2")
        userInfo.append(self.lineEdit.text())
        userInfo.append(self.lineEdit_2.text())
        userInfo.append(self.lineEdit_3.text())

         #yıl-ay-gün | yıl.ay.gün formatıyla olmalı
        userInfo.append(self.lineEdit_4.text())

        userInfo.append(self.lineEdit_5.text())
        userInfo.append(self.getGender())
        userInfo.append("photoname")
        userInfo.append(self.lineEdit_6.text())
        if self.lineEdit_7.text() == self.lineEdit_8.text():
            userInfo.append(self.lineEdit_7.text())

        return userInfo

    def getGender(self):
        if self.radioButton.isChecked() == True:
            return "K"
        else:
            return "E"


    def setupUi(self, Record):
        Record.setObjectName("Record")
        Record.resize(500, 400)
        Record.setMinimumSize(QtCore.QSize(500, 400))
        self.centralwidget = QtWidgets.QWidget(Record)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 400))
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.tabWidget.setMinimumSize(QtCore.QSize(500, 400))
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabWidget.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.tabWidget.setIconSize(QtCore.QSize(100, 100))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setMinimumSize(QtCore.QSize(500, 400))
        self.tab.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tab.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(200, 20, 113, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 20, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 60, 113, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 100, 113, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 140, 113, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(30, 180, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 180, 113, 20))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
       
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.tab)
        self.commandLinkButton.setGeometry(QtCore.QRect(390, 330, 101, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(self.changeTab)
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setGeometry(QtCore.QRect(200, 220, 82, 21))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_2.setGeometry(QtCore.QRect(320, 220, 82, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(30, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setMinimumSize(QtCore.QSize(500, 400))
        self.tab_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tab_3.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.tab_3.setObjectName("tab_3")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 160, 113, 20))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(20, 200, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(180, 200, 113, 20))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(20, 240, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(180, 240, 113, 20))
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 10, 181, 121))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../FOTO/images (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(270, 264))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 290, 75, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.insertUser)
      
        self.tabWidget.addTab(self.tab_3, "")
        Record.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Record)
        self.statusbar.setObjectName("statusbar")
        Record.setStatusBar(self.statusbar)
        self.actionmoney1 = QtWidgets.QAction(Record)
        self.actionmoney1.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../.designer/money.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionmoney1.setIcon(icon1)
        self.actionmoney1.setObjectName("actionmoney1")

        self.retranslateUi(Record)
        self.tabWidget.setCurrentIndex(0)
        
        Record.setTabOrder(self.tabWidget, self.lineEdit)
        Record.setTabOrder(self.lineEdit, self.lineEdit_2)
        Record.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        Record.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        Record.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        Record.setTabOrder(self.lineEdit_5, self.radioButton)
        Record.setTabOrder(self.radioButton, self.radioButton_2)
       
        Record.setTabOrder(self.commandLinkButton, self.pushButton_2)
        Record.setTabOrder(self.pushButton_2, self.lineEdit_6)
        Record.setTabOrder(self.lineEdit_6, self.lineEdit_7)
        Record.setTabOrder(self.lineEdit_7, self.lineEdit_8)
        Record.setTabOrder(self.lineEdit_8, self.pushButton_3)
        

    def retranslateUi(self, Record):
        _translate = QtCore.QCoreApplication.translate
        Record.setWindowTitle(_translate("Record", "KAYIT SAYFASI"))
        self.label.setText(_translate("Record", "Ad  "))
        self.label_2.setText(_translate("Record", "Soyad "))
        self.label_3.setText(_translate("Record", "T.C. No"))
        self.label_4.setText(_translate("Record", "Doğum Tarihi"))
        self.label_5.setText(_translate("Record", "Email"))
       
        self.commandLinkButton.setText(_translate("Record", "İLERLE"))
        self.radioButton.setText(_translate("Record", "Kadın"))
        self.radioButton_2.setText(_translate("Record", "Erkek"))
        self.label_7.setText(_translate("Record", "Cinsiyet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Record", "KİŞİSEL BİLGİLER"))
        self.label_6.setText(_translate("Record", "Kullanıcı Adı"))
        self.label_8.setText(_translate("Record", "Şifre"))
        self.label_9.setText(_translate("Record", "Tekrar Şifre"))
        self.pushButton_3.setText(_translate("Record", "KAYDOL"))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Record", "KAYIT"))
        self.actionmoney1.setText(_translate("Record", "money1"))
        self.actionmoney1.setToolTip(_translate("Record", "image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RECORD = Ui_Record()
    sys.exit(app.exec_())
