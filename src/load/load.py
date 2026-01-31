import pandas as pd
import json
from pathlib import Path
from datetime import datetime

# dados_tratados - camada tranform
# dados_brutos_api - camada extract

def salvar_dados_multiplos_formatos(dados_tratados, dados_brutos_api):
    # 1. Localiza a raiz do projeto
    raiz_projeto = Path(__file__).parent.parent.parent
    
    # 2. Define os caminhos das camadas do Data Lake
    pasta_raw = raiz_projeto / "data" / "raw"        # Camada Bronze (Bruto)
    pasta_refined = raiz_projeto / "data" / "database" # Camada Gold (Processado)
    
    pasta_raw.mkdir(parents=True, exist_ok=True)
    pasta_refined.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    # --- CAMADA RAW (DADO BRUTO) ---
    # Salvamos o dicionário direto da API, sem passar pelo Pandas
    caminho_json_bruto = pasta_raw / f"extract_{timestamp}.json"
    with open(caminho_json_bruto, 'w', encoding='utf-8') as f:
        json.dump(dados_brutos_api, f, ensure_ascii=False, indent=2)

    # --- CAMADA REFINED (DADO TRATADO) ---
    df_pandas = pd.DataFrame(dados_tratados)
    nome_base = f"bitcoin_refined_{timestamp}"
    
    # Salvando formatos analíticos na pasta database ou refined
    df_pandas.to_csv(pasta_refined / f"{nome_base}.csv", index=False)
    df_pandas.to_parquet(pasta_refined / f"{nome_base}.parquet")
    
    print(f"✅ Camada RAW: Arquivo bruto salvo em: {pasta_raw}")
    print(f"✅ Camada REFINED: Arquivos CSV/Parquet salvos em: {pasta_refined}")