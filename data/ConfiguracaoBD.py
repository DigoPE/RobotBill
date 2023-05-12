import mysql.connector

class ConexaoDB():

    def __init__(self):
        self.host = 'localhost'
        self.database = 'billdb'
        self.user = 'root'
        self.passwd = '1234'
        self.mydb = None

    def conectarDB(self):
        self.mydb = mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            passwd=self.passwd
        )

    def executaQueryDB(self, query):
        if not self.mydb or not self.mydb.is_connected():
            self.conectarDB()

        cursor = self.mydb.cursor()
        cursor.execute(query)
        resultado = cursor.fetchall()
        cursor.close()

        return resultado

    def fechaConexaoDB(self):
        if self.mydb and self.mydb.is_connected():
            self.mydb.close()

