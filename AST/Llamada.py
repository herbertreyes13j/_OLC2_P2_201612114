import AST.Nodo as Nodo


class Llamada(Nodo.Nodo):

    def __init__(self, nombre,fila, columna,elementos=[]):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.elementos=elementos