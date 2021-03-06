# PASO 1: Importar el módulo "mysql.connector" previamente ¡INSTALADO!
import mysql.connector

data = []

class MyDatabase:
    def open_connection(self):
        connection = mysql.connector.connect( 
            host="localhost",                    
            user="root", 
            passwd="", 
            database="db_demo")
        return connection

    def insert_db(self, nombre, edad, genero):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_usuarios(NOMBRE, EDAD, GENERO) VALUES (%s,%s,%s)"
        data = (nombre, edad, genero)
        cursor.execute(query, data)
        my_connection.commit()
        print("Usuario registrado exitosamente!")
        my_connection.close()       

    def read_db(self):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "SELECT NOMBRE, EDAD, GENERO FROM TBL_USUARIOS"
        cursor.execute(query)
        registro = 0
        for fila in cursor:
            data.append(fila) 
            print('DATA (BackEnd): ' + str(registro) +" - "+ str(data[registro]))
            registro = registro + 1 
            
        my_connection.close()     