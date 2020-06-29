import AST.Nodo as Nodo


class Arreglo(Nodo.Nodo):

    def __init__(self, tipo, nombre, valor,dimensiones,fila, columna):
        self.nombre = nombre
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.tipo = tipo
        self.dimensiones=dimensiones

    def getC3D(self,TS,Global,Traductor):
        pass

    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Arreglo'))
        grafica.edge(padre, nombrehijo)
        grafica.node('Nodet' + str(id(self)), label=(str(self.tipo.tipo.name)))
        grafica.edge(nombrehijo, 'Nodet' + str(id(self)))

        grafica.node('Noden' + str(id(self)), label=(str(self.nombre)))
        grafica.node('Nodec' + str(id(self)), label=('dimensiones'))
        grafica.edge(nombrehijo, 'Nodec' + str(id(self)))
        for nodo in self.dimensiones:
            nodo.graficarasc('Nodec' + str(id(self)),grafica)
        grafica.edge(nombrehijo, 'Noden' + str(id(self)))
        if self.valor is not None:
            self.valor.graficarasc(nombrehijo, grafica)

