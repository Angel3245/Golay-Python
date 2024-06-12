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
def leer_fichero(archivo_entrada):
    '''Leer bytes de un archivo y transformarlos a bits dado su nombre'''
    with open(archivo_entrada, 'rb') as archivo:
        # Leer bytes
        bytestream = archivo.read()
        bitstream = ''
        
        # Para cada byte obtener sus bits
        for byte in bytestream:
            binary = '{0:08b}'.format(byte)
            bitstream += binary
    return bitstream

def leer_bits(archivo_entrada):
    '''Leer flujo de bits de un archivo dado su nombre'''
    with open(archivo_entrada, 'r') as archivo:
        return archivo.read()
    
def escribir_bits(matriz, archivo_salida):
    '''Escribir flujo de bits en un archivo dado su nombre'''
    with open(archivo_salida, 'w') as archivo:
        # Para cada vector de la matriz
        for vector in matriz:
            # Escribir bytes en el archivo
            archivo.write(str(vector))

def escribir_fichero(bits,archivo_salida):
    '''Convertir bits a bytes y escribir en un archivo dado su nombre'''
    with open(archivo_salida, 'wb') as archivo:
        # Para cada byte obtener sus bits
        bytes = int(bits, 2).to_bytes((len(bits) + 7) // 8, byteorder='big')

        # Escribir bytes en el archivo
        archivo.write(bytes)