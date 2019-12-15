# created by beyza at 2019-12-05 22:44.
# email : beyzakarali4743@gmail.com



class Payment:
    def __init__(self ,ID = 0, paymentName = "", amount = 0 ):
        self.__ID = ID
        self.__paymentName = paymentName
        self.__amount = amount

    def setID(self ,newID):
        self.__ID = newID

    def setpaymentName(self ,newpaymentName):
        self.__paymentName = newpaymentName

    def setamount(self ,newamount):
        self.__amount = newamount

    def getID(self):
        return self.__ID

    def getpaymentName(self):
        return self.__paymentName 

    def getamount(self):
        return self.__amount   

    #Pull payment information from the database.
    def billPayment(self):
        pass
    
    def trafficPayment(self):
        pass
  
    #_Warning_ This function is new(not in the class diagram)
    #Pull payment information from the database.
    def donation(self):
        pass


 

          


    

