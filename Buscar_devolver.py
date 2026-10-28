def buscar(arreglo, valor):
    for i in range(len(arreglo)):
        if arreglo[i] == valor:
            return i
    return -1

arreglo = [10, 20, 30, 40, 50]
valor = 30

print(buscar(arreglo, valor))