from datetime import datetime

def tratar_dados_Bitcoin(dados_brutos, taxa_conversao):
    # Convertendo o preço da Coinbase para float
    valor_usd = float(dados_brutos['data']['amount'])
    
    # Convertendo a taxa da API de câmbio para float
    taxa = float(taxa_conversao)
    
    valor_brl = valor_usd * taxa
    
    dados_processados = [{
        "valor_usd": valor_usd,
        "valor_real_brasileiro": valor_brl,
        "moeda_origem": dados_brutos['data']['base'],
        "moeda_destino": dados_brutos['data']['currency'],
        "data_atual": datetime.now()
    }]
    
    return dados_processados