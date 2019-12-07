# created by beyza at 2019-12-05 20:18.
# email : beyzakarali4743@gmail.com


class AccountActivity:
    def __init__(self ,ID = 0, name = "", amount = 0, date = "" ):
        self.__ID = ID
        self.__name = name
        self.__amount = amount
        self.__date = date
 

    def setID(self ,newID):
        self.__ID = newID

    def setname(self ,newname):
        self.__name = newname 

    def setamount(self ,newamount):
        self.__amount = newamount

    def setdate(self ,newdate):
        self.__date = newdate   

    def getID(self):
        return self.__ID 

    def getname(self):
        return self.__name

    def getamount(self):
        return self.__amount 

    def getdate(self):
        return self.__date    
    

    # get information on database 
    def wiewActivityDetails(self):
        pass

    # get information on database  
    #check payment and moneytransfer 
    def printReceipt(self):
        pass