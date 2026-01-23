import os
from pathlib import Path

# CAMINHOS DO PROJETO
RAIZ_PROJETO = Path(__file__).parent.parent
CAMINHO_DB = RAIZ_PROJETO / "data" / "database" / "bitcoin.db"

# CONFIGURACOES DA PIPELINE
INTERVALO_COLETA_DADOS_SEGUNDOS = 30
NOME_TABELA_DB = "bitcoin_data"

URL_COINBASE = "https://api.coinbase.com/v2/prices/spot"