import AST.Nodo as Nodo


class AccesoStruct(Nodo.Nodo):

    def __init__(self, Atributo1,Atributo2,fila,columna):
        self.fila = fila
        self.columna = columna
        self.Atributo1=Atributo1
        self.Atributo2=Atributo2