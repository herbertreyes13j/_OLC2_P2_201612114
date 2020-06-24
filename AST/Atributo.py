import AST.Nodo as Nodo


class Atributo(Nodo.Nodo):

    def __init__(self,tipo,nombre,fila, columna,dimensiones=[]):
        self.nombre = nombre
        self.tipo=tipo
        self.fila = fila
        self.columna = columna
        self.dimensiones=dimensiones

    def analizar(self,TS):
        pass
    def getC3D(self):
        pass

    def graficarasc(self, padre, grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Atributo'))
        grafica.edge(padre, nombrehijo)
        if self.tipo is not None:
            grafica.node('Nodet' + str(id(self)), label=(str(self.tipo.tipo.name)))
            grafica.edge(nombrehijo, 'Nodet' + str(id(self)))
        grafica.node('Noden' + str(id(self)), label=(str(self.nombre)))
        grafica.edge(nombrehijo, 'Noden' + str(id(self)))
        if len(self.dimensiones) >0:
            grafica.node('Noded' + str(id(self)), label=('Dimensiones'))
            grafica.edge(nombrehijo, 'Noded' + str(id(self)))
        for node in self.dimensiones:
            node.graficarasc('Noded' + str(id(self)), grafica)
