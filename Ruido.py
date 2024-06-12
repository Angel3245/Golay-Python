# Copyright (C) 2023  Jose Ángel Pérez Garrido
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Use: python Ruido.py Bits_codificados_enviados.txt 


# Importar librerías necesarias
import random
import sys

# Importar archivos necesarios
from Archivo import *

def aleatorizar(bitstring, p=0.05):
    '''Introduce cambios aleatorios en la secuencia de los bits recibidos para simular ruido en el canal'''
    resultado = ''
    for bit in bitstring:
        if random.uniform(0,1) <= p:
            if bit == '0':
                bit = '1'
            else:
                bit = '0'
        resultado += bit
    return resultado

def main():
    '''Aleatorizar bits de una secuencia de bits para simular ruido en un canal'''

    # Obtener nombre del fichero de entrada
    archivo = sys.argv[1]

    # Leer bits del fichero
    bits = leer_bits(archivo)

    print("Bits antes de ruido: "+str(bits))
    # Aleatorizar bits
    bits = aleatorizar(bits)
    print("Bits despues de ruido: "+str(bits))

    escribir_bits(bits, "Bits_codificados_recibidos.txt")

if __name__ == "__main__":
    main()