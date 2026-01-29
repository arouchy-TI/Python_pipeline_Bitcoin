import sqlite3
import pandas as pd
import os
from config.settings import CAMINHO_DB, NOME_TABELA_DB

def consultar_dados():
    conexao = sqlite3.connect(str(CAMINHO_DB))

    query = f"SELECT * FROM {NOME_TABELA_DB} ORDER BY data_atual DESC LIMIT 10;"
    df = pd.read_sql_query(query, conexao)
    conexao.close()

    print(f"\n Ultimos 5 registro na tabela: {NOME_TABELA_DB}")
    print(df)

if __name__ == '__main__':
    consultar_dados()