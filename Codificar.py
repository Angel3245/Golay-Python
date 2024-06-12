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

# Use: python Codificar.py Mensaje.txt 24


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