import mysql.connector
import Customer
import base64

from DataRepresentation_Project import dbconfig as cfg

class CustomerDAO:
    connection = ""
    cursor = ''
    host = ''
    user = ''
    password = ''
    database = ''

    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']

    def getcursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def getAllCustomers(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM GolfStore.Customers"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)

    def getCustomerById(self, id):
        cursor = self.getcursor()
        sql = "SELECT * FROM GolfStore.Customers WHERE customerId LIKE %s"
        cursor.execute(sql, (id,))
        results = cursor.fetchone()
        print(results)

    def getCustomerByEmailAddress(self, email):
        cursor = self.getcursor()
        sql = "SELECT * FROM GolfStore.Customers WHERE emailAddress LIKE %s"
        cursor.execute(sql, (email,))
        results = cursor.fetchall()
        print(results)



    # def createCustomer(self, customerId, firstName, lastName, contactNum, email, password):
    #     b = base64.b64encode(bytes(password, 'utf-8'))  # bytes
    #     hashedPassword = b.decode('utf-8')  # convert bytes to string
    #     customer = Customer(customerId, firstName, lastName, contactNum, email, hashedPassword)
    #     return customer
    #
    # def addNewCustomer(self, customer):
    #     cursor = self.getcursor()
    #     sql="INSERT INTO GolfStore.Customers (customerId, firstName, lastName, contactNum, emailAddress, password)" \
    #         " values(%s, %s, %s, %s, %s, %s)"
    #     cursor.execute(sql, (customer.getCustomerID(), customer.getFirstName(), customer.getLastName(),
    #                          customer.getContactNumber(), customer.getEmailAddress(), customer.getPassword()))
    #     self.connection.commit()
    #     self.closeAll()

customerDAO = CustomerDAO()

if __name__ == "__main__":
    # customerDAO.getCustomerById(3)
    # customerDAO.getAllCustomers()
    # newCustomer = customerDAO.createCustomer(1, "Timmy", "Toon", '0879898989', "tt@tiles.com", "jndi3uen3e3n")
    # customerDAO.addNewCustomer(newCustomer)

    print("success")
