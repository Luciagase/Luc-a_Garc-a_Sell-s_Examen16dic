argumento="24z6 1x23 y369 89a 900b"

#función que crea una lista con una cadena de caracteres separados por espacios
def separar(argumento):
    lista=argumento.split(" ")
    return lista

#función extrae las letras de cada elemento de la lista
def extraer_letras(lista):
    lista_letras=[]
    for elemento in lista:
        letras=""
        for letra in elemento:
            if letra.isalpha():
                letras+=letra
        lista_letras.append(letras)
    return lista_letras

#función extrae los números de cada elemento de la lista
def extraer_numeros(lista):
    lista_numeros=[]
    for elemento in lista:
        numeros=""
        for numero in elemento:
            if numero.isdigit():
                numeros+=numero
        lista_numeros.append(numeros)
    return lista_numeros

#función que crea un diccionario con los elementos de la lista de letras como claves y los elementos de la lista de números como valores
def crear_diccionario(lista_letras,lista_numeros):
    diccionario={}
    for i in range(len(lista_letras)):
        diccionario[lista_letras[i]]=lista_numeros[i]
    return diccionario


#función que ordena el diccionario por claves
def ordenar_diccionario(diccionario):
    diccionario_ordenado=sorted(diccionario.items(), key=lambda x: x[0])
    return diccionario_ordenado


#función que extrae los valores del diccionario
def extraer_valores(diccionario_ordenado):
    lista_valores=[]
    for elemento in diccionario_ordenado:
        lista_valores.append(elemento[1])
    return lista_valores

#función que convierte los valores de la lista en números enteros
def convertir_a_enteros(lista_valores):
    lista_enteros=[]
    for elemento in lista_valores:
        lista_enteros.append(int(elemento))
    return lista_enteros

#función que opera los valores de la lista de enteros en orden + - * /
def operar(lista_enteros,n):
    resultado=lista_enteros[0]
    for i in range(1,len(lista_enteros)):
        if i==n:
            resultado+=lista_enteros[i]
        elif i==n+1:
            resultado-=lista_enteros[i]
        elif i==n+2:
            resultado*=lista_enteros[i]
        elif i==n+3:
            resultado/=lista_enteros[i]
    return resultado

if__name__=="__main__":
    lista=separar(argumento)