import AST.Nodo as Nodo


class AccesoStruct(Nodo.Nodo):

    def __init__(self, Atributo1,Atributo2,fila,columna):
        self.fila = fila
        self.columna = columna
        self.Atributo1=Atributo1
        self.Atributo2=Atributo2

    def analizar(self,TS,Errores):
        pass

    def getC3D(self,TS):
        pass

    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Arreglo'))
        grafica.edge(padre, nombrehijo)
        self.Atributo1.graficarasc(nombrehijo,grafica)
        self.Atributo2.graficarasc(nombrehijo,grafica)
