# created by buzun at 2019-12-03 18:25.
# email : batuuzun08@gmail.com


from ControllerBMS.Payment import Payment
from ControllerBMS.Credit import Credit
from ControllerBMS.Account import Account


class User:
    #Constuctor function
    #7 parametreden fazlası kötü
    #constructor için bilgileri dizi olarak vermek daha mantıklı
    def __init__(self, info = None):
        self.__ID = info[0][0]
        self.__AdminID = info[0][1]
        self.__firstName = info[0][2]
        self.__lastName = info[0][3]
        self.__TCno = info[0][4]
        self.__dateOfBirth = info[0][5]
        self.__email = info[0][6]
        self.__gender = info[0][7]
        self.__profilePhoto = info[0][8]
        self.__username = info[0][9]
        self.__password = info[0][10]
        self.__phoneNumber = info[0][11]

        #self.__payment = self.getPayments()
        #self.__account = self.getAccounts()
        #self.__credit = self.getCredit()
        


    def getDateOfBirth(self):
        year : str = self.__dateOfBirth.year
        month : str = self.__dateOfBirth.month
        day : str = self.__dateOfBirth.day
        
        date = year + month + day

        return date
    def getID(self):
        return self.__ID

    def getPayments(self):
        payment = Payment(self.getUsername())
        return payment

    def getAccounts(self):
        account = Account(self.getUsername())
        return account

    def getCredit(self):
        credit = Credit(self.getUsername())
        return credit

    def setFirstName(self, newName):
        self.__firstName = newName

    def setLastName(self, newName):
        self.__lastName = newName


    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password
    
    #implement to all set function
    
    def setTCno(self, TCno):
        self.__TCno = TCno


    def getFirstName(self):
        return self.__firstName
    #implement to all getter function




