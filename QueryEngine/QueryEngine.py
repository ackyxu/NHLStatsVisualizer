import sqlite3
from sqlite3 import Error
class QueryEngine:
    def __init__(self, pathDB: str) -> None:

        try:
            self.conn = sqlite3.connect(pathDB)
            print("success")
     
        except Error as e:
            self.conn = None
            print("Cannot connect to the Database Given.  Error Log:")
            print(e)
            
    def __del__(self):
        self.CloseConnection()

    def performQuery(self, sql_query: str) -> dict | None:
        if(self.conn):
            self.conn.row_factory = sqlite3.Row
            cur = self.conn.cursor()
            cur.execute(sql_query)
            return [dict(row) for row in cur.fetchall()]
        else:
            self.noConnection()

    def noConnection(self):
        if(not self.conn):
            print("Error: There are currently no database connection established")

    def CloseConnection(self):
        if (self.conn):
            self.conn.close()
            print("Connection Closed")



