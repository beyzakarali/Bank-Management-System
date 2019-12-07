# created by beyza at 2019-12-05 22:44.
# email : beyzakarali4743@gmail.com



from Bank import Bank

class Credit:

#learn to export the object as a parameter.
    def __init__(self, ID = 0, creditNo = 0, statementDay = "", paymentDueDay = "", limit = 0, creditAvaliable = 0):
       self.__ID = ID
       self.__creditNo = creditNo
       self.__statementDay = statementDay
       self.__paymentDueDay = paymentDueDay
       self.__limit = limit
       self.__creditAvaliable = creditAvaliable
       self.__bank = Bank()


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

    
        
            


