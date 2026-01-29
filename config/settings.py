import logging
import os
from pathlib import Path

# criando pasta logs na raiz
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_DIR / "pipeline.log", encoding='utf-8'),
            logging.StreamHandler()
        ]
)

def get_logger(name):
    return logging.getLogger(name)

# CAMINHOS DO PROJETO
RAIZ_PROJETO = Path(__file__).parent.parent
CAMINHO_DB = RAIZ_PROJETO / "data" / "database" / "bitcoin.db"

# CONFIGURACOES DA PIPELINE
INTERVALO_COLETA_DADOS_SEGUNDOS = 30
NOME_TABELA_DB = "bitcoin_data"

URL_COINBASE = "https://api.coinbase.com/v2/prices/spot"