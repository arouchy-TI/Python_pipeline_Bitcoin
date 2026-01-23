import pandas as pd
import sqlite3
from pathlib import Path
from config.settings import CAMINHO_DB, NOME_TABELA_DB

def salvar_banco_local(dados_tratados, nome_tabela=NOME_TABELA_DB):
    df = pd.DataFrame(dados_tratados)
    caminho_db = CAMINHO_DB
    conexao = sqlite3.connect(caminho_db)
    df.to_sql(nome_tabela, conexao, if_exists='append', index=False)
    conexao.close()

    print(f"Dados salvos no banco de dados local em: {caminho_db}, tabela: {nome_tabela}")