import AST.Nodo as Nodo


class Etiqueta(Nodo.Nodo):

    def __init__(self,nombre,fila,columna):
        self.fila = fila
        self.columna = columna
        self.nombre=nombre

class Goto(Nodo.Nodo):

    def __init__(self,nombre,fila,columna):
        self.fila = fila
        self.columna = columna
        self.nombre=nombre