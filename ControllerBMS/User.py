# created by buzun at 2019-12-03 18:25.
# email : batuuzun08@gmail.com
# edited by beyza at 2019-12-05 19:52.


from Payment import Payment
from Credit import Credit
from Account import Account


class User:

    #Constuctor function
    def __init__(self, firstName = "", lastName = "", dateOfBirth= "", cityOfBirth= ""
                    , address= "", profilePhoto= "", TCno= 0, phoneNumber= 0, password= ""):
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
        

     
     #implement to all set function
    def setID (self,newID):
        self.__ID = newID

    def setFirstName(self, newName):
        self.__firstName = newName

    def setLastName(self, newName):
        self.__lastName = newName

    def setdateOfBirth(self, newdateOfBirth):
        self.__dateOfBirth = newdateOfBirth

    def setcityOfBirth(self, newcityOfBirth):
        self.__cityOfBirth = newcityOfBirth  

    def setaddress (self, newaddress ):
        self.__address  = newaddress 

    def setprofilePhoto (self, newprofilePhoto ):
        self.__profilePhoto = newprofilePhoto      

    def setTCno(self, newTCno):
        self.__TCno = newTCno    

    def setphoneNumber (self, newphoneNumber ):
        self.__phoneNumber = newphoneNumber    

    def setpassword (self, newpassword ):
        self.__password = newpassword  

    def setpayment (self, newpayment  ):
        self.__payment  = newpayment         
    
    def setaccount (self, newaccount  ):
        self.__account  = newaccount 

    def setcredit (self, newcredit  ):
        self.__credit = newcredit     

     #implement to all getter function

    def getID (self):
        return self.__ID 

    def getFirstName(self):
        return self.__firstName

    def getdateOfBirth(self):
        return self.__dateOfBirth 

    def getcityOfBirth(self):
        return self.__cityOfBirth  

    def getLastName(self):
        return self.__lastName 

    def getaddress (self):
        return self.__address 

    def getprofilePhoto (self):
        return self.__profilePhoto 

    def getTCno(self):
        return self.__TCno       

    def getphoneNumber (self):
        return self.__phoneNumber

    def getpassword (self):
        return self.__password      
    
    def getpayment (self):
        return self.__payment   
    
    def getaccount (self):
        return self.__account

    def getcredit (self):
        return self.__credit  

   




