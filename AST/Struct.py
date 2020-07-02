import AST.Nodo as Nodo


class Struct(Nodo.Nodo):

    def __init__(self, nombre, atributos,fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.atributos=atributos


    def analizar(self,TS,Errores):
        pass
    def getC3D(self,TS):
        pass

    def graficarasc(self,padre,grafica):
        pass