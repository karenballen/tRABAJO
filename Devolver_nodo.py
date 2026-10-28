def nodoDesdeFinal(cabeza, N):
    rapido = cabeza
    lento = cabeza

    if N <= 0:
        return None

    for i in range(N):
        if rapido is None:
            return None
        rapido = rapido.siguiente

    while rapido is not None:
        rapido = rapido.siguiente
        lento = lento.siguiente

    return lento