import sys
import re
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

    with open('files/tcp-r', 'r') as file:
        for linea in file:

            # Busquedas en el archivo de transacciones recibidas
            with open('files/linea_tmp', 'w') as tmp_file:
                tmp_file.write(linea)
            
            desciso_busca = ejecuta('desciso -s files/linea_tmp')
            # Extraer el número de referencia ISO (DE 37)
            match = re.search(r'DE 37\s+"\d{12}', desciso_busca.stdout)
            REF_ISO = match.group().split('"')[1]
            # Extraer el Tipo de Mensaje
            match = re.search(r'MTI\s+"\K[0-9]{4}', desciso_busca.stdout)
            MTI = match.group().split('"')[1]
            # Extraer el Token C6 recibido
            match = re.search(r'DE 63\.C6\s+"! C600080 \K[a-zA-Z0-9]+', desciso_busca.stdout)
            if match:
                TC6_R = match.group().split('"')[1]
            else:
                TC6_R = "N/A"

            # Busquedas en el archivo de transacciones enviadas
            desciso_busca = ejecuta(f'desciso files/tcp-e -s -f"37=={REF_ISO}"')
            # Extraer el Token C6 enviado
            match = re.search(r'DE 63\.C6\s+"! C600080 \K[a-zA-Z0-9]+', desciso_busca.stdout)
            if match:
                TC6_E = match.group().split('"')[1]
            else:
                TC6_E = "N/A"

            # Comparacion de valores
            TC6_Igual = TC6_R == TC6_E

            #Guardar en el archivo
            resultado = f"{REF_ISO}\t{MTI}\t{TC6_R}\t{TC6_E}\t{TC6_Igual}"
            print(resultado)
            with open(OUTPUT_FILE, 'a') as file:
                file.write(resultado + '\n')

    # Remover archivos temporales
    if not DEBUG:
        ejecuta("rm files/tcp-r")
        ejecuta("rm files/tcp-e")
        ejecuta("rm files/linea_tmp")

if __name__ == "__main__":
    main()