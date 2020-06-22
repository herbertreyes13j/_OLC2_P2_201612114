import AST.Nodo as Nodo


class Atributo(Nodo.Nodo):

    def __init__(self,tipo,nombre,fila, columna,dimensiones=[],pointercount=0):
        self.nombre = nombre
        self.tipo=tipo
        self.fila = fila
        self.columna = columna
        self.dimensiones=dimensiones
        self.pointercount=pointercount
