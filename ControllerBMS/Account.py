# created by beyza at 2019-12-05 20:09.
# email : beyzakarali4743@gmail.com

from AccountActivity import AccountActivity

class Account:
    #Learn to export the object as a parametres.
    def __init__(self, ID =0 ,accountNo =0 ,ıban = 0, balance = 0, bankId = 0, userId = 0, ):
        self.__ID = ID
        self.__accountNo = accountNo
        self.__ıban = ıban
        self.__balance = balance
        self.__bankId = bankId
        self.__userId = userId 
        self.__activity = AccountActivity()

    def setID(self ,newID):
        self.__ID = newID

    def setaccountNo (self ,newaccountNo ):
        self.__accountNo  = newaccountNo 

    def setıban (self ,newıban ):
        self.__ıban  = newıban

    def setbalance (self ,newbalance ):
        self.__balance  = newbalance 

    def setbankId (self ,newbankId ):
        self.__bankId  = newbankId    

    def setuserId (self ,newuserId ):
        self.__userId  = newuserId    

    def setactivity (self ,newactivity ):
        self.__activity = newactivity            
             

    def getID(self):
        return self.__ID

    def getaccountNo (self):
        return self.__accountNo 

    def getıban (self):
        return self.__ıban    
    
    def getbalance (self):
        return self.__balance  
    
    def getbankId (self):
        return self.__bankId
    
    def getuserId (self):
        return self.__userId   
    
    def getactivity (self):
        return self.__activity  


    #Pull account information from the database and make a list.
    def AccountActivity(self):
        pass
