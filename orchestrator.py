import time
import subprocess
import sys
import os
from config.settings import INTERVALO_COLETA_DADOS_SEGUNDOS

def rodar_job():
    intervalo = INTERVALO_COLETA_DADOS_SEGUNDOS
    print(f"Iniciando orquestrador de jobs com intervalo de {intervalo} segundos...")
    print("Pressione Ctrl+C para parar.")
    
    raiz_projeto = os.path.dirname(os.path.abspath(__file__)) 
    env_personalizada = os.environ.copy()
    env_personalizada["PYTHONPATH"] = raiz_projeto

    try:
        while True:
            subprocess.run([sys.executable, "-m", "src.main"],
                            cwd=raiz_projeto,
                            env=env_personalizada
                            )
            print(f"Aguardando {intervalo} segundos para o proximo job...")
            time.sleep(intervalo)

    except KeyboardInterrupt:
        print("Orquestrador de jobs parado pelo usuário.")

if __name__ == "__main__":
    rodar_job()