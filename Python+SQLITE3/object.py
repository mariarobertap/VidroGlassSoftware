

import sqlite3
import os
from sqlite3.dbapi2 import connect

class Item:

    def __init__(self):
        print("Objeto criado")

    def setItem2(self, conn, id, name):
        self.name = name
        self.id = id
        c = conn.cursor()
        c.execute("INSERT INTO item VALUES ("+ str(id) +",  '"+ name +"')")
        conn.commit()
        conn.close()

    def getItem(self, conn):
        if(self.id == None):
            print("Objeto Excluido")
            conn.close()
        else:
            print(str(self.id)+ self.name)
            c = conn.cursor()
            c.execute("SELECT * FROM item where id = "+ str(self.id) +"")
            print(c.fetchall())
            conn.commit()
            conn.close()
        

    def deleteItem(self, conn):
        c = conn.cursor()
        c.execute("DELETE FROM item WHERE id = "+ str(self.id) +"")
        print(c.fetchall())
        conn.commit()
        conn.close()
        self.name = None
        self.id = None

    def getAllItemsInTable(self, conn):
            c = conn.cursor()
            c.execute("SELECT * FROM item")
            print(c.fetchall())
            conn.commit()
            conn.close()

