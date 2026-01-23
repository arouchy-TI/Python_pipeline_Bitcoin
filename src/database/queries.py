import sqlite3
import pandas as pd
import os

def consultar_dados():
    caminho_db = os.path.join(os.getcwd(), "data", "database", "bitcoin.db")
    conexao = sqlite3.connect(caminho_db)

    query = "SELECT * FROM bitcoin_data ORDER BY data_atual DESC LIMIT 10;"
    df = pd.read_sql_query(query, conexao)
    conexao.close()

    print("\n Ultimos 5 registro no banco de dados: ")
    print(df)

if __name__ == '__main__':
    consultar_dados()