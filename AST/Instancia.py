import AST.Nodo as Nodo


class Instancia(Nodo.Nodo):

    def __init__(self, tipo, nombre,fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.tipo = tipo

    def analizar(self,TS,Errores):
        pass

    def getC3D(self,TS):
        pass

    def graficarasc(self,padre,grafica):
        pass
