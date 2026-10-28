def invertirLista(cabeza):
    prev = None
    actual = cabeza
    sig = None

    while actual is not None:
        sig = actual.siguiente

        actual.siguiente = prev

        prev = actual
        actual = sig

    return prev