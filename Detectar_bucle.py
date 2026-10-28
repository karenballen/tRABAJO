def detectarBucle(cabeza):
    lento = cabeza
    rapido = cabeza

    while rapido is not None and rapido.siguiente is not None:
        lento = lento.siguiente
        rapido = rapido.siguiente.siguiente

        if lento == rapido:
            return True

    return False