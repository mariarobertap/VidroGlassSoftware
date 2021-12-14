import sqlite3
import os
from sqlite3.dbapi2 import connect
from Cliente import Cliente


class Database:

    

    def __init__(self):
        self.clienteTable = Cliente()
        self.StartDatabase()
    
    def CreateClienteTable(self):
        conn = self.ConnectDatabase()
        cur = conn.cursor()

        cur.execute(
            """CREATE TABLE cliente (
                id INTEGER PRIMARY KEY,
                name TEXT,
                telefone TEXT,
                cidade TEXT,
                rua TEXT,
                estado TEXT
        )"""
        )

        conn.commit()
        print("[Database.py][CreateClienteTable]: Cliente table created :)")
        conn.close()

    
    def insertInto(self, name, telefone, cidade, rua, estado):
        conn = sqlite3.connect("produto.db")

        c = conn.cursor()
        c.execute(
            "INSERT INTO cliente (name, telefone, cidade, rua, estado) VALUES ('"
            + name
            + "',  '"
            + telefone
            + "', '"
            + cidade
            + "', '"
            + rua
            + ")"
            + "', '"
            + estado
            + "')"
        )
        conn.commit()
        print("[Database.py][insertInto]: Insert concluido com sucesso")
        conn.close()

    def getItem(self):
        conn = sqlite3.connect("produto.db")
        c = conn.cursor()
        c.execute("SELECT * FROM cliente")
        rows = c.fetchall()    
        print(c.fetchall())
        conn.commit()
        conn.close()
        return rows

    def updateClient(self, id, name, telefone, cidade, rua, estado):
        conn = sqlite3.connect("produto.db")
        c = conn.cursor()
        c.execute(
            "UPDATE cliente SET name ='"
            + name
            + "', telefone = '"
            + telefone
            + "', cidade ='"
            + cidade
            + "', rua = '"
            + rua
            + "',estado = '"
            + estado
            + "'"
            + "WHERE id = '"
            + str(id)
            + "'"
        )
          
        print(c.fetchall())
        conn.commit()
        conn.close()

        

    def StartDatabase(self):
        if self.DataBaseExist('produto.db'):
            print("database existe")
        else:
            self.CreateClienteTable() 

    def ConnectDatabase(self):
        conn = sqlite3.connect('produto.db')

        return conn

    def DataBaseExist(self, db):

        if not os.path.isfile(db): return False
        sz = os.path.getsize(db)

        # file is empty, give benefit of the doubt that its sqlite
        # New sqlite3 files created in recent libraries are empty!
        if sz == 0: return True

        # SQLite database file header is 100 bytes
        if sz < 100: return False

        # Validate file header
        with open(db, 'rb') as fd: header = fd.read(100)    

        return (header[:16] == b'SQLite format 3\x00')

