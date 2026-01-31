import logging
import os
from pathlib import Path

# APONTANDO PARA PASTA RAIZ DO PROJETO
BASE_DIR = Path(__file__).resolve().parent.parent

# CRIANDO PASTA DE LOGS
LOG_DIR = BASE_DIR / "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# CONFIGURACOES DO LOGGING - (LOGS)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        # onde log vai aparecer - "salvar"
        handlers=[
            logging.FileHandler(LOG_DIR / "pipeline.log", encoding='utf-8'),
            logging.StreamHandler()
        ]
)

# FUNCAO PARA PEGAR O LOGGER
def get_logger(name):
    return logging.getLogger(name)

# CAMINHOS DO PROJETO
RAIZ_PROJETO = Path(__file__).parent.parent

# CAMINHO PARA BANCO DADOS E NOME DA TABELA DO BANCO SQLITE
CAMINHO_DB = RAIZ_PROJETO / "data" / "database" / "bitcoin.db"
NOME_TABELA_DB = "bitcoin_data"

# CONFIGURACOES DA PIPELINE EM SEGUNDOS
INTERVALO_COLETA_DADOS_SEGUNDOS = 30

URL_COINBASE = "https://api.coinbase.com/v2/prices/spot"