import mysql.connector

def conectar ():
    conexao = mysql.connector.connect(
        host= "127.0.0.1",
        user = "root",
        password = "root",
        database = "saep"
    )

    cursor = conexao.cursor(dictionary=True)

    return conexao, cursor