from src.transform.transform import tratar_dados_Bitcoin
from datetime import datetime

def testar_conversao_moeda():
    dados_falsos = {
        "data": {
            "amount": "50000.00",
            "base": "BTC",
            "currency": "USD"
        }
    }

    taxa_exemplo = 5.0
    resultado, = tratar_dados_Bitcoin(dados_falsos, taxa_exemplo)

    assert resultado["valor_dolar"] == 50000.00
    assert resultado["valor_real_brasileiro"] == 250000.00
    assert resultado["valor_bitcoin"] == "BTC"

    print("✅ Teste de conversao de moeda passou com sucesso!")

if __name__ == '__main__':
    testar_conversao_moeda()