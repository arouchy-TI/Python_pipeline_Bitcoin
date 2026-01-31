# Maestro da ETL
# 1 - importar as funcoes
from src.extraction.extraction import extrair_preco_bitcoin, extraindo_Cotacao
from src.transform.transform import tratar_dados_Bitcoin
from src.load.load import salvar_dados_multiplos_formatos
from src.database.repository import salvar_banco_local

def executar_pipeline_etl():
    print("Iniciando a pipeline ETL...")
    print("Extraindo dados da coinbase e Currency Freaks...")

    # 1 - arquivo extraction.py da pasta extraction
    dados_brutos_api = extrair_preco_bitcoin()
    taxa_conversao = extraindo_Cotacao()

    # 2 - arquivo transform.py da pasta transform
    dados_tratados = tratar_dados_Bitcoin(dados_brutos_api, taxa_conversao['rates']['BRL'])

    # 3 - arquivo load.py da pasta load
    print("Salvando dados...")
    salvar_dados_multiplos_formatos(dados_tratados, dados_brutos_api)

    print("Salvando dados no banco de dados local...")
    salvar_banco_local(dados_tratados)

    print("\n Pipeline ETL finalizada com sucesso!")

if __name__ == '__main__':
    executar_pipeline_etl()
