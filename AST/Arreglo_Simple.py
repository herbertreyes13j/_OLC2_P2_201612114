import AST.Nodo as Nodo


class ArregloSimple(Nodo.Nodo):

    def __init__(self, tipo, nombre, valor, fila, columna):
        self.nombre = nombre
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.tipo = tipo
