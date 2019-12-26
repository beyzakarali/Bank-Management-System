# created by beyza at 2019-12-05 20:09.
# email : beyzakarali4743@gmail.com

from ControllerBMS.AccountActivity import AccountActivity
from ModelBMS.database import Database

class Account:
    #Learn to export the object as a parametres.
    def __init__(self, usersAccountsInfo):
        self.__ID = usersAccountsInfo[0]
        self.__accountNo = usersAccountsInfo[1]
        self.__iban = usersAccountsInfo[2]
        self.__balance = usersAccountsInfo[3]
        self.__bankId = usersAccountsInfo[4]
        self.__userId = usersAccountsInfo[6] 
        
        #self.__activity = AccountActivity()

    def setID(self ,newID):
        self.__ID = newID

    def setAccountNo (self ,newaccountNo ):
        self.__accountNo  = newaccountNo 

    def setIban (self ,newıban ):
        self.__ıban  = newıban

    def setBalance (self ,newbalance ):
        self.__balance  = newbalance 

    def setBankId (self ,newbankId ):
        self.__bankId  = newbankId    

    def setUserId (self ,newuserId ):
        self.__userId  = newuserId    

    def setActivity (self ,newactivity ):
        self.__activity = newactivity            
             

    def getID(self):
        return self.__ID

    def getAccountNo (self):
        return self.__accountNo 

    def getIban (self):
        return self.__iban    
    
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


    def getUsersAccounts(self, bank):
        pass

    @classmethod
    def setAccounts(cls, userID):
        query = "SELECT * FROM account INNER JOIN customer ON customerID = customer.ID WHERE customerID = %s"
        accounts = Database.Query(Database, query, userID)
        clsAccounts : Account = []
        for account in accounts:
            clsAccounts.append(cls(account))
        return clsAccounts
