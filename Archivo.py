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