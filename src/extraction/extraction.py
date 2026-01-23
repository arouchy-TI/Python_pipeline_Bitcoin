import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from config.settings import URL_COINBASE

# Localiza a raiz do projeto (subindo 2 níveis de src/extraction/)
raiz_projeto = Path(__file__).resolve().parent.parent.parent
caminho_env = raiz_projeto / ".env"

# Força o carregamento do arquivo específico
load_dotenv(dotenv_path=caminho_env)

def extraindo_Informacoes():
    url = URL_COINBASE
    resposta = requests.get(url)
    return resposta.json()

def extraindo_Cotacao():
    api_key = os.getenv("CURRENCY_API_KEY")
    
    if not api_key:
        print(f"⚠️ Aviso: load_dotenv falhou em {caminho_env}")
        print("Tentando leitura manual do .env...")

    if not api_key:
        raise ValueError(f"API Key nao encontrada! Verifique se o arquivo {caminho_env} existe e contem CURRENCY_API_KEY=...")
        
    url = f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey={api_key}"
    resposta = requests.get(url)
    return resposta.json()