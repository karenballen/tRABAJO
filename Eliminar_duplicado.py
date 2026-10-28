def eliminarDuplicados(cabeza):
    actual = cabeza

    while actual is not None and actual.siguiente is not None:

        if actual.dato == actual.siguiente.dato:
            actual.siguiente = actual.siguiente.siguiente

        else:
            actual = actual.siguiente

    return cabeza