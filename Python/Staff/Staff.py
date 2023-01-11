

class Staff:

    def __init__(self, id, firstname, lastname, position, email, password ):
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__position = position
        self.__email = email
        self.__password = password

    def getStaffID(self):
        return self.__id

    def setStaffID(self, id):
        self.__id = id

    def getFirstName(self):
        return self.__firstname

    def setFirstName(self, newName):
        self.__firstname = newName

    def getLastName(self):
        return self.__lastname

    def setLastName(self, newName):
        self.__lastname = newName

    def getPosition(self):
        return self.__position

    def setPosition(self, position):
        self.__position = position

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password

    def getEmailAddress(self):
        return self.__email

    def setEmailAddress(self, email):
        self.__email = email
