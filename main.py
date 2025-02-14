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

    # Manejar errores
    if YYYY_Mes == BIT_INVALIDA:
        print("Se ha introducido una fecha no valida")
        return -1

    # Crear direcciones de las bitacoras
    BITACORA_DIR = f"/bitacoras/{YYYY_Mes}/autemi-{BANCO}/"
    OUTPUT_FILE  = f"files/C6_{BANCO}_{TCP_NUM}.{MMDD}"

    debug_log(f'Dirección de la bitacora a escanear: {BITACORA_DIR}')
    debug_log(f'Direccion del archivo de salida: {OUTPUT_FILE}')

    print(f"Buscando dentro de {BITACORA_DIR}")

    # Guardamos las transacciones con Token C6, enviados y recibidos
    ejecuta(f'grep C600080 "{BITACORA_DIR}tcp{TCP_NUM}-e.{MMDD}" > files/tcp-e 2>/dev/null')
    ejecuta(f'grep C600080 "{BITACORA_DIR}tcp{TCP_NUM}-r.{MMDD}" > files/tcp-r 2>/dev/null')

    # Imprime cabecera de la tabla
    ejecuta(f'echo -e "REF_ISO\t\tMTI\tTC6_R\t\t\tTC6_E\t\t\tTC6_Igual" > "{OUTPUT_FILE}"')

if __name__ == "__main__":
    main()