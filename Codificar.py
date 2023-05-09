#python Codificar.py Mensaje.txt 24


# Importar librerías necesarias
import sys

# Importar archivos necesarios
from Archivo import *
from Golay import Golay

def main():
    '''Codificar fichero de entrada con Golay24'''

    # Obtener nombre del fichero de entrada
    archivo = sys.argv[1]

    # Obtener tipo de Golay empleado
    tipo = int(sys.argv[2])

    # Leer bits del fichero
    bits = leer_fichero(archivo)

    # Cargar codigo
    codigo = Golay(tipo)

    # Codificar bits
    c = codigo.codificar(bits)

    print("Bits enviados: "+str(c))

    escribir_bits(c, "Bits_codificados_enviados.txt")

if __name__ == "__main__":
    main()