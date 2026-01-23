# Maestro da ETL
# 1 - importar as funcoes
from src.extraction.extraction import extraindo_Informacoes, extraindo_Cotacao
from src.transform.transform import tratar_dados_Bitcoin
from src.load.load import salvar_dados_multiplos_formatos
from src.database.repository import salvar_banco_local

def executar_pipeline_etl():
    print("Iniciando a pipeline ETL...")
    print("Extraindo dados da coinbase e Currency Freaks...")

    dados_brutos = extraindo_Informacoes()
    json_cotacao = extraindo_Cotacao()

    dados_tratados = tratar_dados_Bitcoin(dados_brutos, json_cotacao['rates']['BRL'])

    print("Salvando dados...")
    salvar_dados_multiplos_formatos(dados_tratados, dados_brutos)

    print("Salvando dados no banco de dados local...")
    salvar_banco_local(dados_tratados)

    print("\n Pipeline ETL finalizada com sucesso!")

if __name__ == '__main__':
    executar_pipeline_etl()
