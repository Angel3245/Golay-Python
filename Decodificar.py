#python Decodificar.py Bits_codificados_recibidos.txt 24


# Importar librerías necesarias
import sys

# Importar archivos necesarios
from Archivo import *
from Golay import Golay

def main():
    '''Decodificar flujo de bits del fichero de entrada con Golay24'''

    # Obtener nombre del fichero de entrada
    archivo = sys.argv[1]

    # Obtener tipo de Golay empleado
    tipo = int(sys.argv[2])

    # Leer bits del fichero
    bits = leer_bits(archivo)

    # Cargar codigo
    codigo = Golay(tipo)

    # Decodificar bits
    u = codigo.decodificar(bits)

    print("Bits decodificados: " + str(u))

    msg = ''
    
    # Convertir bits a char para formar el texto recibido
    for i in range(0,len(u),8):
        charbits = u[i:i+8]
        outchar = chr(int(charbits,2))
        msg += outchar

    print("Palabra recibida: "+msg)

    escribir_fichero(u, "Mensaje_decodificado.txt")

if __name__ == "__main__":
    main()