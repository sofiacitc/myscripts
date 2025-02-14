# Biblioteca

# Variables globales
YEAR            = 2025             # Año Fijo
BIT_INVALIDA    = "NaN"

def main():
    print("""
Esta es una biblioteca
No debe ser ejecutada directamente
Uso:

from biblioteca import *
          """)
    
def obtener_mes(MMDD):
    MESES=("Ene", "Feb", "Mar", "Abr" , "May", "Jun" , "Jul"  , "Ago", "Sep" ,"Oct" ,"Nov" ,"Dic")
    
    MM = MMDD[0:2]

    if ( int(MM) >= 1 and int(MM) <= 12 ):
        return MESES[int(MM) - 1]
    else:
        return BIT_INVALIDA
    
def obtener_YYYY_Mes(MES):
    
    if (MES == BIT_INVALIDA) :
        return MES
    else:
        return str(YEAR) + "_" + MES

if __name__=="__main__":
    main()



