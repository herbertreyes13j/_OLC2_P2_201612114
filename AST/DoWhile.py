import AST.Nodo as Nodo


class DoWhile(Nodo.Nodo):

    def __init__(self, EXP,SENTENCIAS,fila,columna):
        self.fila = fila
        self.columna = columna
        self.EXP=EXP
        self.SENTENCIAS=SENTENCIAS