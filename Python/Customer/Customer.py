
class Customer:

    def __init__(self, id, firstname, lastname, contactNum, email, password ):
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__contactNum = contactNum
        self.__email = email
        self.__password = password

    def getCustomerID(self):
        return self.__id

    def setCustomerID(self, id):
        self.__id = id

    def getFirstName(self):
        return self.__firstname

    def setFirstName(self, newName):
        self.__firstname = newName

    def getLastName(self):
        return self.__lastname

    def setLastName(self, newName):
        self.__lastname = newName

    def getContactNumber(self):
        return self.__contactNum

    def setContactNum(self, num):
        self.__contactNum = num

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password

    def getEmailAddress(self):
        return self.__email

    def setEmailAddress(self, email):
        self.__email = email
