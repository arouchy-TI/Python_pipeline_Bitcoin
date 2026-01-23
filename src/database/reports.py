import sqlite3
import pandas as pd
from pathlib import Path

def gerar_relatorios_precos():
    raiz_projeto = Path(__file__).parent.parent.parent
    caminho_db = raiz_projeto / "data" / "database" / "bitcoin.db"

    conexao = sqlite3.connect(str(caminho_db))

    # QUERYS
    query_media_precos = """
        SELECT
            AVG(valor_real_brasileiro) as media_brl FROM bitcoin_data;
    """

    query_extremos_precos = """
        SELECT
            MAX(valor_real_brasileiro) as max_brl,
            MIN(valor_real_brasileiro) as min_brl    
        FROM bitcoin_data;
    """

    query_valor_dolar = """
        SELECT
            MAX(valor_dolar) as max_usd,
            MIN(valor_dolar) as min_usd
        FROM bitcoin_data;
    """
    query_utlimo_preco_bitcoin = """
        SELECT
            valor_real_brasileiro AS ultimo_preco_bitcoin,
            data_atual            AS utima_atualizacao
        FROM bitcoin_data
        WHERE valor_bitcoin = 'BTC'
        ORDER BY data_atual DESC
        LIMIT 5;
    """
    query_maior_preco_registrado = """
        SELECT
            valor_real_brasileiro AS maior_preco_bitcoin,
            data_atual            AS ultima_atualizacao
        FROM bitcoin_data
        WHERE valor_bitcoin = 'BTC'
        ORDER BY valor_real_brasileiro DESC, data_atual DESC
        LIMIT 3;
    """
    query_menor_preco_registrado = """
        SELECT
            valor_real_brasileiro AS menor_preco_bitcoin,
            data_atual            AS ultima_atualizacao    
        FROM bitcoin_data
        WHERE valor_bitcoin = 'BTC'
        ORDER BY valor_real_brasileiro ASC, data_atual DESC
        LIMIT 3;
    """

    print("\n Relatorio Macro")
    print("----------------")
    print(pd.read_sql_query(query_media_precos, conexao))
    print("----------------")
    print(pd.read_sql_query(query_extremos_precos, conexao))
    print("----------------")
    print(pd.read_sql_query(query_valor_dolar, conexao))
    print("----------------")
    print(pd.read_sql_query(query_utlimo_preco_bitcoin, conexao))
    print("----------------")
    print(pd.read_sql_query(query_maior_preco_registrado, conexao))
    print("----------------")
    print(pd.read_sql_query(query_menor_preco_registrado, conexao))
    conexao.close()

if __name__ == '__main__':
    gerar_relatorios_precos()