import AST.Nodo as Nodo


class Funcion(Nodo.Nodo):

    def __init__(self,tipo,nombre,parametros,sentencias,fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.tipo=tipo
        self.parametros=parametros
        self.sentencias=sentencias

    def getC3D(self):
        pass

    def analizar(self,TS):
        pass

    def graficarasc(self,padre,grafica):
        nombrehijo='Node'+str(id(self))
        grafica.node(nombrehijo,label=('Funcion'))
        grafica.edge(padre,nombrehijo)
        grafica.node('Nodet'+str(id(self)),label=(str(self.tipo.tipo.name)))
        grafica.edge(nombrehijo,'Nodet'+str(id(self)))
        grafica.node('Noden' + str(id(self)), label=(str(self.nombre)))
        grafica.edge(nombrehijo, 'Noden' + str(id(self)))
        grafica.node('Nodep' + str(id(self)), label=('Parametros'))
        grafica.edge(nombrehijo, 'Nodep' + str(id(self)))
        for node in self.parametros:
            node.graficarasc('Nodep' + str(id(self)),grafica)
        grafica.node('Nodes' + str(id(self)), label=('Sentencias'))
        grafica.edge(nombrehijo, 'Nodes' + str(id(self)))
        for node in self.sentencias:
            node.graficarasc('Nodes' + str(id(self)),grafica)