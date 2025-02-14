import sys
import os
import subprocess
from biblioteca import *

def main():
    # Verificar que se pasaron 2 argumentos además del nombre del script
    if len(sys.argv) != 4:
        print("Uso: python main.py <banco> <tcp-num> <fecha en formato MMDD>")
        sys.exit(1)

    # Obtener los argumentos
    BANCO   = sys.argv[1]
    TCP_NUM = sys.argv[2]
    MMDD    = sys.argv[3] 

    # Obtener valores
    MES     = obtener_mes(MMDD)
    YYYY_Mes= obtener_YYYY_Mes(MES) 

    # Crear direcciones de las bitacoras
    BITACORA_DIR = f"/bitacoras/{YYYY_Mes}/autemi-{BANCO}/"
    OUTPUT_FILE  = f"files/C6_{BANCO}_{TCP_NUM}.{MMDD}"

    print(BITACORA_DIR)
    print(OUTPUT_FILE)

    comando = f'grep C600080 "{BITACORA_DIR}tcp{TCP_NUM}-e.{MMDD}" > files/tcp-e 2>/dev/null'
    subprocess.run(comando, shell=True, check=True)
    print(comando)


if __name__ == "__main__":
    main()