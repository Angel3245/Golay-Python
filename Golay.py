# Importar librerías necesarias
import sys

# Importar archivos necesarios
from Archivo import *

class Golay:
    def __init__(self, tipo=24):
        self.I12= [[1,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,1]]

        self.A = [[0,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,0,1,1,1,0,0,0,1,0],
                [1,1,0,1,1,1,0,0,0,1,0,1],
                [1,0,1,1,1,0,0,0,1,0,1,1],
                [1,1,1,1,0,0,0,1,0,1,1,0],
                [1,1,1,0,0,0,1,0,1,1,0,1],
                [1,1,0,0,0,1,0,1,1,0,1,1],
                [1,0,0,0,1,0,1,1,0,1,1,1],
                [1,0,0,1,0,1,1,0,1,1,1,0],
                [1,0,1,0,1,1,0,1,1,1,0,0],
                [1,1,0,1,1,0,1,1,1,0,0,0],
                [1,0,1,1,0,1,1,1,0,0,0,1]]
    
        # Eliminamos la ultima columna de la matriz A para G23
        self.A_prima = [[0,1,1,1,1,1,1,1,1,1,1],
                        [1,1,1,0,1,1,1,0,0,0,1],
                        [1,1,0,1,1,1,0,0,0,1,0],
                        [1,0,1,1,1,0,0,0,1,0,1],
                        [1,1,1,1,0,0,0,1,0,1,1],
                        [1,1,1,0,0,0,1,0,1,1,0],
                        [1,1,0,0,0,1,0,1,1,0,1],
                        [1,0,0,0,1,0,1,1,0,1,1],
                        [1,0,0,1,0,1,1,0,1,1,1],
                        [1,0,1,0,1,1,0,1,1,1,0],
                        [1,1,0,1,1,0,1,1,1,0,0],
                        [1,0,1,1,0,1,1,1,0,0,0]]

        # Establecer parámetros del código
        self.n = 12 # Longitud de palabra
        self.p = 2 # Palabras binarias (p = 2)

        # Tipo de Golay utilizado (24 o 23)
        self.tipo = tipo
     
        if not(self.tipo in [24,23]):
            return ValueError('El tipo de Golay seleccionado ('+self.tipo+') no es un tipo válido.')
        
        # Calcular matriz generadora
        self.G24 = self.concatenar(self.I12,self.A)
        self.G23 = self.concatenar(self.I12,self.A_prima)

    def get_columna(self,matriz, n):
        '''Devuelve la columna n de una matriz'''
        A_col = [[0] * len(matriz[0])]
        for k in range(len(self.A[0])):
            A_col[0][k] = self.A[n][k]
        return A_col
    
    def eliminar_columna(self, matriz, col):
        '''Devuelve la matriz eliminando la columna col'''
        return [list(x) for x in zip(*[d for i,d in enumerate(zip(*matriz)) if not i == col])]

    def sumar(self,A,B):
        '''Devuelve el resultado de la suma de dos vectores A y B'''
        long = len(A[0])
        C = [[0]*long]
        for index in range(long):
            C[0][index] = A[0][index] ^ B[0][index]
        return C
    
    def multiplicar(self, A, B):
        '''Devuelve el resultado de la multiplicación de la matriz A por la matriz B'''

        # La matriz resultado C esta compuesta por el numero de filas de A y el numero de columnas de B
        filas = len(A)
        columnas = len(B[0])

        # Crear matriz C de 0s
        C = [[0 for k in range(columnas)] for i in range(filas)]

        # Iterar por fila de A
        for i in range(filas):
        
            # Iterar por columna de B
            for j in range(columnas):
        
                # Iterar por fila de B
                for k in range(len(B)):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % self.p

        return C

    def transpuesta(self,matriz):
        '''Calcula la transpuesta de una matriz'''
        filas = len(matriz[0])
        columnas = len(matriz)
        transpuesta = [[0 for k in range(columnas)] for i in range(filas)]

        for i in range(filas):
            for j in range(columnas):
                transpuesta[i][j] = matriz[j][i]
        return transpuesta

    def concatenar(self,A,B):
        '''Devuelve la matriz (A|B) de orden (n x (i + j)) dadas las matrices A de orden (n x i) y B de orden (n x j)'''
        num_filas = len(A)
        toret = [0] * num_filas
        for fila in range(num_filas):
            toret[fila] = A[fila] + B[fila]
        return toret
    
    def aplanar(self,vector):
        '''Aplana los elementos del vector y devuelve una cadena de bits'''
        return ''.join([str(j) for j in vector[0]])

    def rellenar(self,datos):
        '''Rellenar datos recibidos con 1s para que el numero de bits sea múltiplo de n. Añadir prefijo indicando numero de 1s añadido'''
        prefijo, relleno = '',''
        tamano = len(datos)
        resto = tamano % self.n
        if resto != 0:
            tamano_relleno = self.n - resto
            prefijo = '{0:012b}'.format(tamano_relleno)
            relleno = '1' * tamano_relleno
        return prefijo + datos + relleno
    
    def get_vector(self,palabra):
        '''Convierte una palabra compuesta por una cadena de bits a un vector'''
        vector = [[]]
        for char in palabra:
            vector[0].append(int(char))
        return vector
    
    def anadir_peso_impar(self, r):
        '''Añadir un 0 ó un 1 a la palabra recibida r de forma que la palabra ri (i = 0 ó 1) tenga peso impar'''
        # Calcular el peso de r
        peso = r.count('1')

        # Añadir bit
        r+=str((peso+1)%self.p)

        return r
    
    def codificar(self, datos):
        '''Divide los datos en palabras de 12 bits y codifica cada palabra mediante el código Golay'''
        # Rellenar datos a codificar para asegurar multiplo de n
        datos = self.rellenar(datos)
        
        # Inicializar list para almacenar los datos codificados
        codificado_list = []

        for i in range(0,len(datos),self.n):
            palabra = datos[i:i+self.n]
            vector = self.get_vector(palabra)

            # Calcular vector codigo
            if(self.tipo == 24):
                c = self.multiplicar(vector,self.G24)
            elif(self.tipo == 23):
                c = self.multiplicar(vector,self.G23)

            for bit in c[0]:
                codificado_list.append(bit)

        return codificado_list
    
    def algoritmo_decodificacion(self, r):
        '''Aplicamos el algoritmo de decodificación 5.1.2'''
        error = None

        #(i) Se calcula el síndrome s de la palabra recibida
        vector_r = self.get_vector(r)

        #print(vector_r)

        # Calcular la transpuesta de la matriz generadora
        Gt = self.transpuesta(self.G24)

        # Dividir vector en dos partes de 12 bits y sumar sindromes
        s = self.multiplicar(vector_r,Gt) # primer sindrome

        #(ii) Si w(s) ≤ 3, entonces el vector error es e = (s,0)
        w_s = sum(s[0]) #Peso del sindrome

        if w_s <= 3:
            error = [s[0] + [0] * 12] #(s,0)
            print("La palabra "+r+" tiene un error (s,0): ("+str(s[0])+",0)")
        
        #(iii) Si w(s + ai) ≤ 2 para alguna fila ai de la matriz A, entonces el vector error es e = (s + ai,ui)
        else:
            for j in range(12):
                sum_vec = self.sumar(s,self.get_columna(self.A,j)) #s + ai
                peso_sum = sum(sum_vec[0]) #w(s + ai)
                if peso_sum <= 2:
                    error = [sum_vec[0] + self.I12[j]] #(s + ai,ui)
                    print("La palabra "+r+" tiene un error (s + ai,ui): ("+str(sum_vec[0])+","+str(self.I12[j])+")")
                    break

            #(iv) Se calcula el segundo síndrome de la palabra r, sA.
            if error == None:
                sA = self.multiplicar(s, self.transpuesta(self.A)) # segundo sindrome
                w_sA = sum(sA[0])

                #(v) Si w(sA) ≤ 3, entonces el vector error es e = (0,sA).
                if w_sA <= 3:
                    error = [[0] * 12 + sA[0]]
                    print("La palabra "+r+" tiene un error (0,sA): (0,"+str(sA[0])+")")

                #(vi) Si w(sA+ai) ≤ 2 para alguna fila ai de la matriz A, entonces el vector error es e = (ui,sA + ai).
                for j in range(12):
                    sum_vec = self.sumar(sA,self.get_columna(self.A,j)) #sA + ai
                    peso_sum = sum(sum_vec[0]) #w(sA + ai)
                    if peso_sum <= 2:
                        error = [self.I12[j] + sum_vec[0]]
                        print("La palabra "+r+" tiene un error (ui,sA + ai): ("+str(self.I12[j])+","+str(sum_vec[0])+")")
                        break

        #(vii) Si todavía no se ha determinado el vector error e, solicitar una retransmisión pues se han producido más de tres errores.
        if error == None:
            raise Exception("No se ha podido decodificar la palabra "+r+". Error al menos triple")

        else:
            # Palabra Golay corregida = (vector recibido) - (vector error)
            return self.sumar(vector_r,error)

    def decodificar(self, datos):
        '''Se decodifican los datos llamando aplicando el algoritmo correspondiente dependiendo del tipo de Golay y después se elimina el relleno'''
        if(self.tipo == 24):
            u = self.decodificar24(datos)

        elif(self.tipo == 23):
            u = self.decodificar23(datos)

        # Leemos el prefijo para comprobar cuantos bits de relleno existen
        prefijo = u[:12]

        # Eliminamos el prefijo y los bits de relleno
        u = u[12:-int(prefijo,2)]

        return u
    
    def decodificar24(self, datos):
        '''Decodifica los bits recibidos mediante el codigo de Golay24.'''
        
        resultado = ''

        #Para cada palabra binaria r recibida de longitud 24
        for i in range(0,len(datos),24):
            r = datos[i:i+24]

            try:
                # Como G24 es un código sistemático, el símbolo fuente es la primera mitad de la palabra corregida
                resultado += self.aplanar(self.algoritmo_decodificacion(r))[:12]
            
            # Si no se pudo decodificar la palabra
            except Exception as e:
                # Añadimos el espacio de 0 correspondientes al vector que se debe retransmitir
                resultado += str(0) * 12
                print(e)
                
        return resultado

    def decodificar23(self, datos):
        '''Decodifica los bits recibidos mediante el codigo de Golay23.'''
        resultado = ''

        #Para cada palabra binaria r recibida de longitud 23
        for i in range(0,len(datos),23):
            r = datos[i:i+23]

            try:
                # (i) Añadir un 0 ó un 1 a la palabra recibida r de forma que la palabra ri (i = 0 ó 1) tenga peso impar.
                ri = self.anadir_peso_impar(r)

                # (ii) Descodificar la palabra ri utilizando el algoritmo 5.1.2 como una palabra código c' de G24
                c_prima = self.aplanar(self.algoritmo_decodificacion(ri))

                # (iii) La palabra r se descodifica como la palabra código c de G23 obtenida suprimiendo el último dígito de la palabra c'
                c_prima = c_prima[:-1]

                # Como G24 es un código sistemático, el símbolo fuente es la primera mitad de la palabra corregida
                resultado += c_prima[:12]

            # Si no se pudo decodificar la palabra
            except Exception as e:
                # Añadimos el espacio de 0 correspondientes al vector que se debe retransmitir
                resultado += str(0) * 12
                print(e)
                
        return resultado