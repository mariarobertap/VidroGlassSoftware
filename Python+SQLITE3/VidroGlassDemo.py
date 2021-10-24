import sqlite3
import os
from sqlite3.dbapi2 import connect
from produto import Produto

produto = Produto()


def CreateClienteTable():
    conn = ConnectDatabase()
    cur = conn.cursor()

    cur.execute(
        """CREATE TABLE cliente (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            telefone INTEGER

    )"""
    )

    conn.commit()

    conn.close()


def CreateProdutoTable():
    conn = ConnectDatabase()
    cur = conn.cursor()

    cur.execute(
        """CREATE TABLE produto (
            id INTEGER PRIMARY KEY,
            name TEXT,
            descricao TEXT,
            quantidade INTEGER,
            valorUnitario REAL
    )"""
    )

    conn.commit()

    conn.close()


def ConnectDatabase():
    conn = sqlite3.connect("produto.db")

    return conn


def DataBaseExist(db):
    if not os.path.isfile(db):
        return False
    sz = os.path.getsize(db)

    # file is empty, give benefit of the doubt that its sqlite
    # New sqlite3 files created in recent libraries are empty!
    if sz == 0:
        return True

    # SQLite database file header is 100 bytes
    if sz < 100:
        return False

    # Validate file header
    with open(db, "rb") as fd:
        header = fd.read(100)

    return header[:16] == b"SQLite format 3\x00"


def CadastrarProduto():
    os.system("cls")
    name = input("Escolha um nome: ")
    descricao = input("Escolha uma descricao: ")
    quantidade = input("Escolha uma quantidade: ")
    valor = input("Escolha um valor: ")
    produto.setItem2(name, descricao, quantidade, valor)


def MenuProduto():

    while True:

        print("1-Cadastrar produto:")
        print("2-Editar Produto")
        print("3-Ecluir Produto")
        print("4-Visualizar todos os produto")
        print("5-Voltar")
        opcao = input("Escolha uma opcao")

        if opcao == "1":
            CadastrarProduto()
        elif opcao == "4":
            os.system("cls")
            produto.getAllItemsInTable()
        elif opcao == "5":
            return


def MenuCliente():
    print("Cadastrar cliente:")
    print("Editar cliente")
    print("Ecluir cliente")
    print("Visualizar cliente")
    opcao = input("Escolha uma opcao")


def MenuSistema():

    print("1 - PRODUTO")
    print("2 - CLIENTE")
    print("2 - GERAR NOTA")

    opcao = input("Escolha uma opcao")

    if opcao == "1":
        MenuProduto()
    elif opcao == "2":
        MenuCliente()


def main():

    if DataBaseExist("produto.db"):
        print("database existe")
        MenuSistema()
    else:
        CreateProdutoTable()
        CreateClienteTable()
        MenuSistema()


main()
