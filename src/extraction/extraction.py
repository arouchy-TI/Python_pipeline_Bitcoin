import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from config.settings import URL_COINBASE, get_logger

# inicializando logger
logger = get_logger(__name__)

# Logica do Ambiente - Localiza a raiz do projeto (subindo 2 níveis de src/extraction/)
raiz_projeto = Path(__file__).resolve().parent.parent.parent
caminho_env = raiz_projeto / ".env"
load_dotenv(dotenv_path=caminho_env)

# Força o carregamento do arquivo específico
load_dotenv(dotenv_path=caminho_env)

def extraindo_Informacoes():
    """
        Consome Api coinbase obter preco bitcoin
    """
    url = URL_COINBASE
    logger.info(f"Inicializando requisicao para Coin Base: {url}")

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        logger.info(f"Dados da bitocoin extraido com sucesso")
        return resposta.json()

    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao conectar com a coinBase: {e}")
        return None

def extraindo_Cotacao():
    """
        Consome Api currencyFreaks para obter taxas de cambio
    """
    api_key = os.getenv("CURRENCY_API_KEY")
    
    if not api_key:
        logger.critical(f'Chave de API ausente no arquivo: {caminho_env}')
        raise ValueError('Currency Api Key nao encontradano arquivo .env')

    url = f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey={api_key}"
    
    try:
        logger.info("solicitando cotacao de cambio (Currency Freaks)...")
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()

        logger.info("Informacoes obtidas com sucesso")
        return resposta.json()
    
    except Exception as e:
        logger.error(f'falha na extracao de cotacao: {e}')
        return None

# --- BLOCO DE TESTE (EXECUÇÃO DIRETA) ---
# Esta linha verifica se o arquivo está sendo executado diretamente (não importado)
if __name__ == "__main__":
    logger.info("Iniciando execução de teste do módulo extraction.py")
    
    # Chamamos as funções e guardamos o resultado nas variáveis
    dados_coinbase = extraindo_Informacoes()
    dados_cotacao = extraindo_Cotacao()
    
    # Mostramos o resultado no log e no terminal para conferir
    if dados_coinbase:
        logger.info(f"Sucesso Coinbase! Resultado: {dados_coinbase}")
    
    if dados_cotacao:
        logger.info(f"Sucesso Cotação! Resultado: {dados_cotacao}")
        
    logger.info("Fim da execução de teste.")