# created by beyza at 2019-11-30 01:34.
# email : beyzakarali4743@gmail.com


<<<<<<< HEAD
from PyQt5 import QtCore, QtGui, QtWidgets 

#ANA MENU butonunu teke düşür. Gereksiz buton
#widget alanını küçültürsek altta tek bir buton olabilir.
#passPrevWin fonksiyonunu kullan.

class Ui_Settings(object):

    def __init__(self, prevWin : QtWidgets.QMainWindow = None):
=======
from PyQt5 import QtCore, QtGui, QtWidgets

#Photos on the buttons are invisible.Therefore write text for now.Later fix it.

class Ui_Settings(object):
    
    #Back to mainmenu
    #Look at the parametres and fix problem
    def MainMenu(self):  
        self.winSettings.close()
        print("return -1")
        #return(-1)
        #self.winSettings.exit(-1) 

    # _Rutin_ setPointSize function 
    def pointSize(self,fontSize):
        self.font = QtGui.QFont()
        self.font.setPointSize(fontSize)
        return self.font
       

    def limitationForEft(self):
        self.textLabelEft.setText("MİN:100  MAX:100.000 ")
    

    def limitationForTransfer(self):
        self.textLabelTransfer.setText("MİN:100  MAX:100.000") 

    def limitationForPassword(self):
        self.textLabelPassword.setText(" -Boşluk olmamalı\n -MİN :8 Karakter \n -MAX :15 Karakter")  

    def limitationForUsername(self):
        self.textLabelUsername.setText("-Boşluk olmamalı\n-En az 1 rakam içermelidir\n       ÖRN:Mavi9  ") 


    def __init__(self):
>>>>>>> 97feb99639179da71d236ff06f4094d23efc4df9
        self.winSettings = QtWidgets.QMainWindow()
        self.setupUi(self.winSettings)
        self.winSettings.show()
<<<<<<< HEAD
        self.prevWin = prevWin

   
    def write(self):
        print("sınırlandırmalar var.")

    def passPrevWin(self):
        self.winSettings.close()
        self.prevWin.show()
        
      
=======
>>>>>>> 97feb99639179da71d236ff06f4094d23efc4df9

    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(500, 400)
        Settings.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget = QtWidgets.QWidget(Settings)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
<<<<<<< HEAD
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 501, 345))
=======
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 501, 391))
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
>>>>>>> 97feb99639179da71d236ff06f4094d23efc4df9
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(40, 35, 141, 21))
        self.label_2.setFont(self.pointSize(14))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(230, 30, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 131, 31))
        self.label_3.setFont(self.pointSize(14))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 100, 141, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 181, 31))
        self.label_4.setFont(self.pointSize(14))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 170, 141, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(270, 240, 61, 41))
        self.pushButton.setObjectName("pushButton")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.tab_2)
        self.commandLinkButton.setGeometry(QtCore.QRect(370, 320, 121, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
<<<<<<< HEAD
        #self.commandLinkButton.clicked.connect(self.MainMenu)
=======
        self.limitPasswordButton = QtWidgets.QPushButton(self.tab_2)
        self.limitPasswordButton.setGeometry(QtCore.QRect(400, 100, 31, 31))
        self.limitPasswordButton.setText("İ")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../FOTO/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.limitPasswordButton.setIcon(icon)
        self.limitPasswordButton.setIconSize(QtCore.QSize(35, 31))
        self.limitPasswordButton.setObjectName("limitPasswordButton")
        self.limitPasswordButton.clicked.connect(self.limitationForPassword)
        self.textLabelPassword = QtWidgets.QLabel(self.tab_2)
        self.textLabelPassword.setGeometry(QtCore.QRect(380, 120, 101, 91))
        self.textLabelPassword.setText("")
        self.textLabelPassword.setObjectName("textLabelPassword")
        self.textLabelPassword.setFont(self.pointSize(8))
       
>>>>>>> 97feb99639179da71d236ff06f4094d23efc4df9
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 30, 141, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(60, 20, 101, 51))
        self.label_8.setFont(self.pointSize(14))
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(230, 100, 141, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(40, 90, 121, 41))
        self.label_10.setFont(self.pointSize(14))
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(10, 170, 191, 31))
        self.label_12.setFont(self.pointSize(14))
        self.label_12.setObjectName("label_12")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 160, 61, 51))
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../FOTO/images (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 87))
        self.pushButton_3.setObjectName("pushButton_3")
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.tab_3)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(370, 320, 121, 41))
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
<<<<<<< HEAD
        self.pushButton_5.setGeometry(QtCore.QRect(200, 260, 75, 41))
=======
        self.pushButton_5.setGeometry(QtCore.QRect(210, 260, 75, 41))
>>>>>>> 97feb99639179da71d236ff06f4094d23efc4df9
        self.pushButton_5.setObjectName("pushButton_5")
        self.limitUsernameButton = QtWidgets.QPushButton(self.tab_3)
        self.limitUsernameButton.setGeometry(QtCore.QRect(400, 100, 31, 31))
        self.limitUsernameButton.setText("İ")
        self.limitUsernameButton.setIcon(icon)
        self.limitUsernameButton.setIconSize(QtCore.QSize(35, 31))
        self.limitUsernameButton.setObjectName("limitUsernameButton")
        self.limitUsernameButton.clicked.connect(self.limitationForUsername)
        self.textLabelUsername = QtWidgets.QLabel(self.tab_3)
        self.textLabelUsername.setGeometry(QtCore.QRect(370, 145, 151, 45))
        self.textLabelUsername.setText("")
        self.textLabelUsername.setObjectName("textLabelUsername")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 221, 41))
        self.label_6.setFont(self.pointSize(14))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.tab_4)
        self.comboBox.setGeometry(QtCore.QRect(280, 80, 161, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 180, 75, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.tab_4)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(370, 320, 121, 41))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setGeometry(QtCore.QRect(70, 20, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_5)
        self.label_14.setGeometry(QtCore.QRect(30, 70, 61, 31))
        self.label_14.setFont(self.pointSize(14))
        self.label_14.setObjectName("label_14")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_9.setGeometry(QtCore.QRect(180, 70, 151, 31))
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_15 = QtWidgets.QLabel(self.tab_5)
        self.label_15.setGeometry(QtCore.QRect(30, 130, 81, 31))
        self.label_15.setFont(self.pointSize(14))
        self.label_15.setObjectName("label_15")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_10.setGeometry(QtCore.QRect(180, 130, 151, 31))
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_17 = QtWidgets.QLabel(self.tab_5)
        self.label_17.setGeometry(QtCore.QRect(30, 190, 101, 31))
        self.label_17.setFont(self.pointSize(14))
        self.label_17.setObjectName("label_17")
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab_5)
        self.radioButton_3.setGeometry(QtCore.QRect(160, 200, 82, 21))
        self.radioButton_3.setFont(self.pointSize(11))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab_5)
        self.radioButton_4.setGeometry(QtCore.QRect(290, 200, 82, 21))
        self.radioButton_4.setFont(self.pointSize(11))
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 260, 75, 41))
        self.pushButton_4.setObjectName("pushButton_4")


        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(370, 350, 121, 41))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
<<<<<<< HEAD
        self.commandLinkButton_3.clicked.connect(self.passPrevWin)


=======
        self.limitEftButton = QtWidgets.QPushButton(self.tab_5)
        self.limitEftButton.setGeometry(QtCore.QRect(350, 70, 31, 31))
        self.limitEftButton.setText("İ")
        self.limitEftButton.setIcon(icon)
        self.limitEftButton.setIconSize(QtCore.QSize(35, 31))
        self.limitEftButton.setObjectName("limitEftButton")
        self.limitEftButton.clicked.connect(self.limitationForEft)
        self.limitTransferButton = QtWidgets.QPushButton(self.tab_5)
        self.limitTransferButton.setGeometry(QtCore.QRect(350, 130, 31, 31))
        self.limitTransferButton.setText("İ")
        self.limitTransferButton.setIcon(icon)
        self.limitTransferButton.setIconSize(QtCore.QSize(35, 31))
        self.limitTransferButton.setObjectName("limitTransferButton")
        self.limitTransferButton.clicked.connect(self.limitationForTransfer)
        self.textLabelEft = QtWidgets.QLabel(self.tab_5)
        self.textLabelEft.setGeometry(QtCore.QRect(390, 60, 101, 51))
        self.textLabelEft.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textLabelEft.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textLabelEft.setLineWidth(5)
        self.textLabelEft.setText("")
        self.textLabelEft.setObjectName("textLabelEft")
        self.textLabelEft.setFont(self.pointSize(7))
        self.textLabelTransfer = QtWidgets.QLabel(self.tab_5)
        self.textLabelTransfer.setGeometry(QtCore.QRect(390, 120, 101, 51))
        self.textLabelTransfer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textLabelTransfer.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textLabelTransfer.setLineWidth(1)
        self.textLabelTransfer.setText("")
        self.textLabelTransfer.setObjectName("textLabelTransfer")
        self.textLabelTransfer.setFont(self.pointSize(7))
>>>>>>> 97feb99639179da71d236ff06f4094d23efc4df9
        self.tabWidget.addTab(self.tab_5, "")
        Settings.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Settings)
        self.statusbar.setObjectName("statusbar")
        Settings.setStatusBar(self.statusbar)

        self.retranslateUi(Settings)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Settings)
        Settings.setTabOrder(self.tabWidget, self.lineEdit)
        Settings.setTabOrder(self.lineEdit, self.limitPasswordButton)
        Settings.setTabOrder(self.limitPasswordButton, self.lineEdit_2)
        Settings.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        Settings.setTabOrder(self.lineEdit_3, self.pushButton)
        Settings.setTabOrder(self.pushButton, self.commandLinkButton)
        Settings.setTabOrder(self.commandLinkButton, self.lineEdit_5)
        Settings.setTabOrder(self.lineEdit_5, self.limitUsernameButton)
        Settings.setTabOrder(self.limitUsernameButton, self.lineEdit_6)
        Settings.setTabOrder(self.lineEdit_6, self.pushButton_3)
        Settings.setTabOrder(self.pushButton_3, self.pushButton_5)
        Settings.setTabOrder(self.pushButton_5, self.commandLinkButton_5)
        Settings.setTabOrder(self.commandLinkButton_5, self.comboBox)
        Settings.setTabOrder(self.comboBox, self.pushButton_2)
        Settings.setTabOrder(self.pushButton_2, self.limitEftButton)
        Settings.setTabOrder(self.limitEftButton, self.lineEdit_9)
        Settings.setTabOrder(self.lineEdit_9, self.limitTransferButton)
        Settings.setTabOrder(self.limitTransferButton, self.lineEdit_10)
        Settings.setTabOrder(self.lineEdit_10, self.radioButton_3)
        Settings.setTabOrder(self.radioButton_3, self.radioButton_4)
        Settings.setTabOrder(self.radioButton_4, self.pushButton_4)
        Settings.setTabOrder(self.pushButton_4, self.commandLinkButton_3)
        Settings.setTabOrder(self.commandLinkButton_3, self.commandLinkButton_2)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "AYARLAR"))
        self.label_2.setText(_translate("Settings", "Mevcut Şifreniz"))
        self.label_3.setText(_translate("Settings", "Yeni Şifreniz"))
        self.label_4.setText(_translate("Settings", "Yeni Şifreniz (Tekrar)"))
        self.pushButton.setText(_translate("Settings", "ONAYLA"))
        self.commandLinkButton.setText(_translate("Settings", "ANA MENÜ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Settings", "Şifre Değiştime"))
        self.label_8.setText(_translate("Settings", "Mail adres"))
        self.label_10.setText(_translate("Settings", "Kullanıcı Adı"))
        self.label_12.setText(_translate("Settings", "Fotoğraf Güncelleme"))
        self.commandLinkButton_5.setText(_translate("Settings", "ANA MENÜ"))
        self.pushButton_5.setText(_translate("Settings", "GÜNCELLE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Settings", "Bilgi Güncelleme"))
        self.label_6.setText(_translate("Settings", "Sileceğiniz Hesabı Seçiniz"))
        self.comboBox.setItemText(0, _translate("Settings", "Mevcut Hesap"))
        self.pushButton_2.setText(_translate("Settings", "SİL"))
        self.commandLinkButton_2.setText(_translate("Settings", "ANA MENÜ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Settings", "Hesap Silme"))
        self.label_13.setText(_translate("Settings", "Günlük Limitlerinizi Belirleyiniz"))
        self.label_14.setText(_translate("Settings", "EFT"))
        self.label_15.setText(_translate("Settings", "HAVALE"))
        self.label_17.setText(_translate("Settings", "E-TİCARET"))
        self.radioButton_3.setText(_translate("Settings", "Açık"))
        self.radioButton_4.setText(_translate("Settings", "Kapalı"))
        self.pushButton_4.setText(_translate("Settings", "ONAYLA"))
        self.commandLinkButton_3.setText(_translate("Settings", "ANA MENÜ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Settings", "Limit Ayarları"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SETTİNG= Ui_Settings()
    sys.exit(app.exec_())
