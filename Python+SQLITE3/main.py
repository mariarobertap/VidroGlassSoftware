
import sqlite3
import os
from sqlite3.dbapi2 import connect
from object import Item
 

def CreateProdutoTable(conn):
    cur = conn.cursor()

    cur.execute("""CREATE TABLE item (
            id INTEGER,
            nome TEXT
    )""")

    conn.commit()

    conn.close()
   
def ConnectDatabase():
    conn = sqlite3.connect('produto.db')

    return conn

def DataBaseExist(db):
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


def main():
    item = Item()

    if DataBaseExist('produto.db'):
        print("database existe")
        connection =  ConnectDatabase()
        item.setItem2(connection, 5, "Vou ser exluido")
        connection =  ConnectDatabase()
        item.getItem(connection)
        connection =  ConnectDatabase()
        item.deleteItem(connection)
        connection =  ConnectDatabase()
        item.getItem(connection)
        connection =  ConnectDatabase()
        item.setItem2(connection, 6, "Morango")
        connection =  ConnectDatabase()
        item.getAllItemsInTable(connection)

      
    else:
       connection =  ConnectDatabase()
       CreateProdutoTable(connection)

main()  