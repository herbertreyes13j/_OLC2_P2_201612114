import AST.Nodo as Nodo


class Atributo(Nodo.Nodo):

    def __init__(self,tipo,nombre,fila, columna,dimensiones=[]):
        self.nombre = nombre
        self.tipo=tipo
        self.fila = fila
        self.columna = columna
        self.dimensiones=dimensiones
