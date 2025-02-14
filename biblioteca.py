import os
import subprocess

# Biblioteca

# Variables globales
YEAR          = 2025             # Año Fijo
BIT_INVALIDA  = "NaN"
DEBUG         = False            # Bandera que decide si es DEBUG o no


## @brief Le dice al usuario que no debe ejecutar la biblioteca directamente
def main():
    print("""
Esta es una biblioteca
No debe ser ejecutada directamente
Uso:

from biblioteca import *
          """)

## @brief Imprime informacion util de DEBUG
#  @param msg Recibe la cadena a imprimir
#  @param DEBUG Bandera que indica si el programa esta en DEBUG o no
def debug_log(msg):
    if DEBUG:
        print(f"[DEBUG]: {msg}")

## @brief Ejecuta un comando en Linux
#  @param comando Recibe el comando a ejecutar en linux.
#  @return Si se usa en una asignación, retorna la salida del comando. De lo contrario, solo lo ejecuta.
def ejecuta(comando):
    debug_log(f'[EJECUTA]: {comando}')
    # Ejecutar el comando
    resultado = subprocess.run(comando, shell=True, text=True, capture_output=True)

    # Si el comando se usa como una expresión, devolvemos su salida
    if resultado.stdout.strip() or resultado.stderr.strip():
        return resultado.stdout.strip()

    # Si no se usa como expresión, no devuelve nada (como el comportamiento original)
    return None

## @brief Obtiene fecha en formato Mes a partir de MMDD
#  @param MMDD fecha en formato MMDD , ejemplo: 1227
def obtener_mes(MMDD):
    MESES=("Ene", "Feb", "Mar", "Abr" , "May", "Jun" , "Jul"  , "Ago", "Sep" ,"Oct" ,"Nov" ,"Dic")
    
    MM = MMDD[0:2]

    if ( int(MM) >= 1 and int(MM) <= 12 ):
        return MESES[int(MM) - 1]
    else:
        return BIT_INVALIDA

## @brief Obtiene el nombre de la carpeta en formato YYDD a partir del Mes
#  @param MES fecha en formato Mes , ejemplo: Abr 
def obtener_YYYY_Mes(MES):
    
    if (MES == BIT_INVALIDA) :
        return MES
    else:
        return str(YEAR) + "_" + MES

if __name__=="__main__":
    main()



