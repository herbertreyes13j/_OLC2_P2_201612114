import AST.Nodo as Nodo


class Arreglo(Nodo.Nodo):

    def __init__(self, tipo, nombre, valor,dimensiones,fila, columna):
        self.nombre = nombre
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.tipo = tipo
        self.dimensiones=dimensiones

