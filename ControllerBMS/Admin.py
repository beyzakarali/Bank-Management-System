# created by buzun at 2019-12-03 19:49.
# email : batuuzun08@gmail.com

from ControllerBMS.UserCls import User



class Admin:
    #paremetre olarak nesne vermeyi öğren.
    def __init__(self, userName = "", password = 0):
        self.__ID = id
        self.__userName = userName
        self.__password = password
        self.__user = User()

    #getter and setter functions

    def getID(self):
        return self.__ID

    #veritabanından tüm kullanıcıları listeleyecek.
    def viewAllUser(self):
        pass

    #gelen parametreleri veritabanında karşılaştırıp user döndürecek.
    def logIn(self, userName, password):
        pass

        



