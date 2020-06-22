import AST.Nodo as Nodo


class Struct(Nodo.Nodo):

    def __init__(self, nombre, atributos,fila, columna,instancias=[]):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.atributos=atributos
        self.instancias=instancias
