import AST.Nodo as Nodo


class Funcion(Nodo.Nodo):

    def __init__(self,tipo,nombre,parametros,sentencias,fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.tipo=tipo
        self.parametros=parametros
        self.sentencias=sentencias
