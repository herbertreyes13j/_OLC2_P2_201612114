import AST.Nodo as Nodo


class Switch(Nodo.Nodo):

    def __init__(self, EXP,Casos,fila, columna,Default=None):
        self.fila = fila
        self.columna = columna
        self.EXP=EXP
        self.Casos=Casos
        self.Default=Default

class Casos(Nodo.Nodo):
    def __init__(self,Exp,Sentencias,fila,columna):
        self.fila=fila
        self.columna=columna
        self.Exp=Exp
        self.sentencias=Sentencias

class Default(Nodo.Nodo):
    def __init__(self,Sentencias,fila,columna):
        self.fila=fila
        self.columna=columna
        self.sentencias=Sentencias