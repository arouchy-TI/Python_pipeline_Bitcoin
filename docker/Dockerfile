FROM python:3.10-slim

WORKDIR /app

# 1. Copia o arquivo de requisitos para dentro do container
COPY requirements.txt .

# 2. Instala as bibliotecas (isso resolve o erro do 'requests')
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copia o restante dos arquivos do projeto
COPY . .

# 4. Executa o orquestrador
CMD ["python", "orchestrator.py"]