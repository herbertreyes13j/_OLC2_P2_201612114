import AST.Nodo as Nodo


class Break(Nodo.Nodo):

    def __init__(self,fila, columna):
        self.fila = fila
        self.columna = columna

class Continue(Nodo.Nodo):

    def __init__(self,fila, columna):
        self.fila = fila
        self.columna = columna