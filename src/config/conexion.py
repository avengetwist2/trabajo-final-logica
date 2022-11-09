import sqlite3
import os

class Conexion:
    db_name = os.getcwd().split('src')[0] + 'src\config\database.db'
    #print(db_name)
    def __init__(self):
        pass

    def run_query(self, query, parameters=()):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, parameters)
                conn.commit()
            return result
        except Exception as ex:
            print(ex)

