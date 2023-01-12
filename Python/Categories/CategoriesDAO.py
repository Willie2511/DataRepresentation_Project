import mysql.connector

from DataRepresentation_Project import dbconfig as cfg

class CategoriesDAO:
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

    def getAllCategories(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM GolfStore.categories"
        cursor.execute(sql)
        results = cursor.fetchall()
        self.closeAll()
        return results

    def getCategoryById(self, id):
        cursor = self.getcursor()
        sql = "SELECT * FROM GolfStore.categories WHERE Id LIKE %s"
        cursor.execute(sql, (id,))
        results = cursor.fetchone()
        self.closeAll()
        return results

categoryDAO = CategoriesDAO()
if __name__ == "__main__":
    # categoryDAO.getAllCategories()
    categoryDAO.getCategoryById(2)



