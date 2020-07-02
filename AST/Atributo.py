import AST.Nodo as Nodo
from TS.Simbolo import *
from Errores.N_Error import *

class Atributo(Nodo.Nodo):

    def __init__(self,tipo,nombre,fila, columna,dimensiones=[],isstruct=False):
        self.nombre = nombre
        self.tipo=tipo
        self.fila = fila
        self.columna = columna
        self.dimensiones=dimensiones
        self.isestruct=isstruct

    def analizar(self,TS,Errores):
        sim = Simbolo(self.tipo.tipo, self.nombre, "", TS.nombre)
        if not TS.push(sim):
            Errores.insertar(N_Error("Semantico", 'Variable ' + self.nombre + ' ya esta definida', self.fila,
                             self.columna))
            return
        sim.posicion=TS.getParametro()


    def getC3D(self,TS):
        codigo=""

        return codigo

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
