# created by buzun at 2019-12-03 18:25.
# email : batuuzun08@gmail.com
# edited by beyza at 2019-12-05 20:07.


class Bank:
    def __init__(self, ID = "", bankName = 0, phoneNumber = 0):
        self.__ID = id
        self.__bankName = bankName
        self.__phoneNumber = phoneNumber


    #getter and setter function
    def  setID(self, newID):
        self.__ID = newID

    def setbankName(self, newbankName):
        self.__bankName = newbankName

    def setphoneNumber(self, newphoneNumber):
        self.__phoneNumber = newphoneNumber
    
    def  getID(self):
        return self.__ID     

    def getbankName(self):
        return self.__bankName   

    def getphoneNumber(self):
        return self.__phoneNumber 

    # read database 
    # account activities
    # user info 
    def viewAllDetails(self):
        pass
