# ₿ Bitcoin Data Lake - Pipeline ETL Profissional

Este projeto implementa uma pipeline de dados automatizada que coleta cotações de Bitcoin, realiza conversão de câmbio em tempo real e armazena os dados seguindo o conceito de **Arquitetura de Medalhão (Data Lake)**.

## 🚀 Estrutura do Projeto
- **`data/raw`**: Camada Bronze (Dados brutos em JSON direto da API).
- **`data/database`**: Camada Gold (Dados tratados em CSV, Parquet e SQLite).
- **`src/`**: Código modularizado (Extração, Transformação e Carga).
- **`tests/`**: Testes unitários para garantir a integridade dos cálculos.
- **`config/`**: Centralização de parâmetros e variáveis de ambiente.

## 🛠️ Tecnologias Utilizadas
- **Python 3.9+**
- **Pandas** (Tratamento de dados)
- **SQLite** (Armazenamento relacional)
- **Requests** (Consumo de APIs)
- **Pytest** (Qualidade de código)

## 🔧 Como Rodar
1. Instale as dependências: `pip install -r requirements.txt`
2. Configure seu `.env` com a API Key.
3. Inicie o orquestrador: `python orchestrator.py`