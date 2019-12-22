# created by beyza at 2019-12-05 22:44.
# email : beyzakarali4743@gmail.com


from ControllerBMS.Bank import Bank
from ModelBMS.database import Database

class Credit:

#learn to export the object as a parameter.
    def __init__(self, usersCreditsInfo):
       self.__ID = usersCreditsInfo[0]
       self.__creditNo = usersCreditsInfo[1]
       self.__statementDay = usersCreditsInfo[2]
       self.__paymentDueDay = usersCreditsInfo[3]
       self.__limit = usersCreditsInfo[4]
       self.__creditAvaliable = usersCreditsInfo[5]
       #self.__bank = Bank()


    def setID(self, newID ):
        self.__ID = newID
        
    def setcreditNo(self, newcreditNo ):
        self.__creditNo = newcreditNo
    
    def setstatementDay(self, newstatementDay ):
        self.__statementDay = newstatementDay

    def setpaymentDueDay(self, newpaymentDueDay ):
        self.__paymentDueDay = newpaymentDueDay

    def setlimit(self, newlimit ):
        self.__limit= newlimit 

    def setcreditAvaliable(self, newcreditAvaliable ):
        self.__creditAvaliable= newcreditAvaliable   
    
    
    def setbank(self, newbank ):
        self.__bank = newbank     

    def getID(self):
        return self.__ID

    def getcreditNo(self):
        return self.__creditNo 
    
    def getstatementDay(self):
        return self.__statementDay

    def getpaymentDueDay(self):
        return self.__paymentDueDay 

    def getlimit(self):
        return self.__limit
         
    def getcreditAvaliable(self):
        return self.__creditAvaliable
    
    def getbank(self):
        return self.__bank     
    
    #Pull Credit information from the database.
    #
    def debtCredit(self):
        pass
    
    #Pull Credit information from the database.
    def wiewCreditDetails(self):
        pass

    @classmethod
    def setCredits(cls, userID):
        query = "SELECT * FROM credit INNER JOIN customer ON customerID = customer.ID WHERE customerID = %s"
        credits = Database.Query(Database, query, userID)
        clsCredits : Credit = []
        for credit in credits:
            clsCredits.append(cls(credit))
        return clsCredits
            


