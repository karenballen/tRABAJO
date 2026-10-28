def numeroFaltante(arreglo):
    N = len(arreglo) + 1

    sumaIdeal = N * (N + 1) // 2

    sumaReal = 0
    for numero in arreglo:
        sumaReal += numero

    faltante = sumaIdeal - sumaReal

    return faltante


arreglo = [1, 2, 4, 5]

print(numeroFaltante(arreglo))