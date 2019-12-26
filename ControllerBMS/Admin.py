# created by buzun at 2019-12-03 19:49.
# email : batuuzun08@gmail.com
# edited by beyza at 2019-12-05 20:02.

from ControllerBMS.UserCls import User



class Admin:
    #learn to export object as a parameter.
    def __init__(self, adminInfo):
        self.__ID = adminInfo[0]
        self.__userName = adminInfo[1]
        self.__password = adminInfo[2]
        self.onlineUser = User

    #getter and setter functions

    def setID(self, newID):
        self.__ID = newID

    def setuserName(self, newuserName):
        self.__userName = newuserName

    def setpassword(self, newpassword):
        self.__password = newpassword

    def setuser(self, newuser):
        self.__user = newuser

    def getID(self):
        return self.__ID

    def getuserName(self):
        return self.__userName

    def getpassword(self):
        return self.__password

    def getuser(self):
        return self.__user

    #Pull the entire list of users in database.
    def viewAllUser(self):
        pass

    #compare the parameters in the database and return user.
    def logIn(self, userName, password):
        pass
