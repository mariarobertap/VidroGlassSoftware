import sqlite3
import os
from sqlite3.dbapi2 import connect


class Cliente:

    nome = None
    telefone = None
    cidade = None
    rua = None
    estado = None

    def __init__(self):
        print("Objeto [Cliente] criado")


    def CreateProdutoTable(self, conn):

        cur = conn.cursor()

        cur.execute("""CREATE TABLE item (
                id INTEGER,
                nome TEXT
        )""")

        conn.commit()

        conn.close()




    def setItem2(self, name, descricao, quantidade, valorUnit):
        conn = sqlite3.connect("produto.db")
        self.name = name
        self.quantidade = quantidade
        self.descricao = descricao
        self.valorUnit = valorUnit
        c = conn.cursor()
        c.execute(
            "INSERT INTO produto (name, descricao, quantidade, valorUnitario) VALUES ('"
            + name
            + "',  '"
            + descricao
            + "', "
            + quantidade
            + ", "
            + valorUnit
            + ")"
        )
        conn.commit()
        conn.close()

    def getItem(self, id):
        conn = sqlite3.connect("produto.db")
        print(str(self.id) + self.name)
        c = conn.cursor()
        c.execute("SELECT * FROM produto where id = " + str(id) + "")
        print(c.fetchall())
        conn.commit()
        conn.close()

    def deleteItem(self, id):
        conn = sqlite3.connect("produto.db")
        c = conn.cursor()
        c.execute("DELETE FROM produto WHERE id = " + str(id) + "")
        print(c.fetchall())
        conn.commit()
        conn.close()
        self.name = None
        self.id = None

    def getAllItemsInTable(self):
        conn = sqlite3.connect("produto.db")
        c = conn.cursor()
        c.execute("SELECT * FROM produto")
        print(c.fetchall())
        conn.commit()
        conn.close()
