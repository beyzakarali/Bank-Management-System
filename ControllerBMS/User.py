# created by buzun at 2019-12-03 18:25.
# email : batuuzun08@gmail.com


from ControllerBMS import Payment, Credit, Account

class User:

    #Constuctor function
    def __init__(self, firstName = "", lastName = "", dateOfBirth= "", cityOfBirth= ""
                    , address= "", profilePhoto= "", TCno= 0, phoneNumber= 0, password= ""):
        #what is the python id? 
        #static 
        self.__ID = id
        self.__firstName = firstName
        self.__lastName = lastName
        self.__dateOfBirth = dateOfBirth
        self.__cityOfBirth = cityOfBirth
        self.__address = address
        self.__profilePhoto = profilePhoto
        self.__TCno = TCno
        self.__phoneNumber = phoneNumber
        self.__password = password
        self.__payment = Payment()
        self.__account = Account()
        self.__credit = Credit()
        #generate static id variable, then use setID function.
        #class tipinde nesne dizisi üretme nasıl yapılır.

    def setFirstName(self, newName):
        self.__firstName = newName
    def setLastName(self, newName):
        self.__lastName = newName
    
    #implement to all set function
    
    def setTCno(self, TCno):
        self.__TCno = TCno


    def getFirstName(self):
        return self.__firstName
    #implement to all getter function





