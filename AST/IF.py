import AST.Nodo as Nodo


class IF(Nodo.Nodo):

    def __init__(self, EXP,SENTENCIAS_V,fila,columna,SENTENCIAS_F=[]):
        self.fila = fila
        self.columna = columna
        self.EXP=EXP
        self.SENTENCIAS_V=SENTENCIAS_V
        self.SENTENCIAS_F=SENTENCIAS_F