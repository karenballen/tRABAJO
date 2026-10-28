def invertir(arreglo):
    inicio = 0
    fin = len(arreglo) - 1

    while inicio < fin:
        temp = arreglo[inicio]
        arreglo[inicio] = arreglo[fin]
        arreglo[fin] = temp

        inicio += 1
        fin -= 1

    return arreglo

arreglo = [10, 20, 30, 40, 50]
print(invertir(arreglo))