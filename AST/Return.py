import AST.Nodo as Nodo


class Return(Nodo.Nodo):

    def __init__(self,fila,columna,Exp=None):
        self.fila = fila
        self.columna = columna
        self.EXP=Exp