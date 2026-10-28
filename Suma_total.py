def acumular(arreglo):
    suma = 0

    for numero in arreglo:
        suma += numero

    return suma

arreglo = [10, 20, 30, 40, 50]

print(acumular(arreglo))