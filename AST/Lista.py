import AST.Nodo as Nodo


class Lista(Nodo.Nodo):

    def __init__(self, elementos,fila, columna):
        self.fila = fila
        self.columna = columna
        self.elementos=elementos
