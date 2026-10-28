def moverCeros(arreglo):
    idxNoCero = 0

    for i in range(len(arreglo)):
        if arreglo[i] != 0:
            arreglo[idxNoCero] = arreglo[i]
            idxNoCero += 1

    for i in range(idxNoCero, len(arreglo)):
        arreglo[i] = 0

    return arreglo

arreglo = [0, 1, 0, 3, 12]

print(moverCeros(arreglo))