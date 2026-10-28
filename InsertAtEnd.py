class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


def InsertAtEnd(cabeza, valor):
    nuevoNodo = Nodo(valor)

    if cabeza is None:
        cabeza = nuevoNodo
    else:
        actual = cabeza

        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevoNodo

    return cabeza


cabeza = None

cabeza = InsertAtEnd(cabeza, 10)
cabeza = InsertAtEnd(cabeza, 20)
cabeza = InsertAtEnd(cabeza, 30)