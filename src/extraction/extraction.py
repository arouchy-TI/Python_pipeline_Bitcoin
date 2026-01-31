# CAMA DE EXTRACAO DO ETL
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from config.settings import URL_COINBASE, get_logger

# inicializando logger
logger = get_logger(__name__)

# Logica do Ambiente - Localiza a raiz do projeto (subindo 3 níveis de src/extraction/)
raiz_projeto = Path(__file__).resolve().parent.parent.parent
caminho_env = raiz_projeto / ".env"
load_dotenv(dotenv_path=caminho_env)

def extrair_preco_bitcoin():
    """
        Consome Api coinbase obter preco bitcoin - convertida para float futuramente 
    """
    url = URL_COINBASE
    logger.info(f"Inicializando requisicao para Coin Base: {url}")

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        logger.info(f"Dados da bitocoin extraido com sucesso")
        return resposta.json()

    # tratando erros de requisicao http
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao conectar com a coinBase: {e} ")
        return None

def extraindo_Cotacao():
    """
        Consome Api currencyFreaks para obter taxas de cambio
    """
    api_key = os.getenv("CURRENCY_API_KEY")
    
    # verificacao defensiva
    # se api key = 404 ou string vazia
    if not api_key:
        logger.critical(f'Chave de API ausente no arquivo: {caminho_env}')
        raise ValueError('Currency Api Key nao encontradano arquivo .env')

    url = f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey={api_key}"
    
    try:
        logger.info("solicitando cotacao de cambio (Currency Freaks)...")
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()

        # extraindo taxa de cambio
        logger.info("Informacoes obtidas com sucesso")
        return resposta.json()
    
    # tratando todos os tipos de erros 
    except Exception as e:
        logger.error(f'falha na extracao de cotacao: {e} ')
        return None

