# created by beyza at 2019-12-05 22:44.
# email : beyzakarali4743@gmail.com


from ModelBMS.database import Database

class Payment:
    def __init__(self , paymentInfo):
        self.__ID = paymentInfo[0]
        self.__paymentName = paymentInfo[1]
        self.__amount = paymentInfo[2]

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


    @classmethod
    def setPayments(cls, userID):
        query = "SELECT payments.ID, payments.PaymentName, payments.Amount FROM `customer` INNER JOIN payments on customer.ID = payments.CustomerId WHERE customer.ID = %s"
        payments = Database.Query(Database, query, userID)
        clsPayments : Payment = []
        for payment in payments:
            clsPayments.append(cls(payment))
        
        return clsPayments
 

          


    

