#Función de la secuencia de Tribonacci
def tribonacci(n):
    lista=[0,0,1]
    for i in range(3,n):
        lista.append(lista[i-3]+lista[i-2]+lista[i-1])
    return lista[n-1]

print(tribonacci(5))

if __name__ == "__main__":
    print(tribonacci(5))
    