import AST.Nodo as Nodo


class Puntero(Nodo.Nodo):

    def __init__(self,tipo,nombre,valor,fila, columna,dimensiones=[],pointercount=0):
        self.nombre = nombre
        self.tipo=tipo
        self.fila = fila
        self.columna = columna
        self.dimensiones=dimensiones
        self.valor=valor
        self.pointercount=pointercount