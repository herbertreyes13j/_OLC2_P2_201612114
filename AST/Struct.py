import AST.Nodo as Nodo


class Struct(Nodo.Nodo):

    def __init__(self, nombre, atributos,fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.atributos=atributos
