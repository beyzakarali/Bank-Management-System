# created by beyza at 2019-12-05 20:18.
# email : beyzakarali4743@gmail.com


from PyQt5.QtWidgets import QMessageBox
import datetime

class AccountActivity:
    def __init__(self , activityInfo ):
        self.__ID = activityInfo[0]
        self.__name = activityInfo[1]
        self.__amount = activityInfo[2]
        self.__date = activityInfo[3]
 

    def setID(self ,newID):
        self.__ID = newID

    def setHame(self ,newname):
        self.__name = newname 

    def setAmount(self ,newamount):
        self.__amount = newamount

    def setDate(self ,newdate):
        self.__date = newdate   

    def getID(self):
        return self.__ID 

    def getName(self):
        return self.__name

    def getAmount(self):
        return self.__amount 

    def getDate(self):
        return self.__date    
    
    @staticmethod
    def getCurrentDate():
        return datetime.datetime.now()
        
    # get information on database 
    def wiewActivityDetails(self):
        pass

    
    def createActivity(self):
        pass

    def printReceipt(self):
        title = "---MAKBUZ---"
        text = self.getName()
        informativeText = "Hesabınızdan " + self.getDate() + "tarihinde,"
        + self.getAmount() + "₺ çekilmiştir."

        self.showInformationDialog(title, text, informativeText)


    #Hata giriş pop-up
    @staticmethod
    def showInformationDialog(title, text, informativeText):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.setInformativeText(informativeText)
        x = msg.exec_()