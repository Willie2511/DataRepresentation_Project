import mysql.connector

from DataRepresentation_Project import dbconfig as cfg


class StaffDAO:

    connection=""
    cursor=''
    host=''
    user=''
    password=''
    database=''

    def __init__(self):
        self.host= cfg.mysql['host']
        self.user= cfg.mysql['user']
        self.password= cfg.mysql['password']
        self.database= cfg.mysql['database']

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


    def getAllStaff(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM GolfStore.Staff"
        cursor.execute(sql)
        results = cursor.fetchall()
        self.closeAll()
        return results

    def getStaffById(self, id):
        cursor = self.getcursor()
        sql = "SELECT * FROM GolfStore.Staff WHERE staffId LIKE %s"
        cursor.execute(sql, (id,))
        results = cursor.fetchone()
        self.closeAll()
        return results

    def getStaffByEmailAddress(self, email):
        cursor = self.getcursor()
        sql = "SELECT * FROM GolfStore.Staff WHERE emailAddress LIKE %s"
        cursor.execute(sql, (email,))
        results = cursor.fetchall()
        self.closeAll()
        return results

    def getStaffByPosition(self, position):
        cursor = self.getcursor()
        sql = "SELECT * FROM GolfStore.Staff WHERE position LIKE %s"
        cursor.execute(sql, (position,))
        results = cursor.fetchall()
        self.closeAll()
        return results

staffDAO = StaffDAO()

if __name__ == "__main__":
    # staffDAO.getStaffById(1)
    # staffDAO.getStaffByEmailAddress("markclancey@cgl.staff.com")
    staffDAO.getStaffByPosition("Customer Service")
    print("success")

