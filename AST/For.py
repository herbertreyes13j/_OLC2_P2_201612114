import AST.Nodo as Nodo


class For(Nodo.Nodo):

    def __init__(self, Inicial,Condicion,Incremento,Sentencias,fila,columna):
        self.fila = fila
        self.columna = columna
        self.Incial=Inicial
        self.Condicion=Condicion
        self.Incremento=Incremento
        self.Sentencias=Sentencias