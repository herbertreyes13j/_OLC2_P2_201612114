import AST.Nodo as Nodo
from AST.Lista import *
from TS.Simbolo import *
from Errores.N_Error import *
from TS.Tipos import *

class Arreglo(Nodo.Nodo):

    def __init__(self, tipo, nombre, valor,dimensiones,fila, columna):
        self.nombre = nombre
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.tipo = tipo
        self.dimensiones=dimensiones

    def analizar(self,TS,Errores):
        sim = Simbolo(self.tipo.tipo, self.nombre, "", TS.nombre)
        if not TS.push(sim):
            Errores.insertar(N_Error("Semantico",'Variable '+self.nombre+' ya esta definida'),self.fila,self.columna)
            return TIPO_DATOS.ERROR
        if not isinstance(self.valor,Lista):
            Errores.insertar(N_Error("Semantico", 'Solo se puede asignar tipo list a arreglo'), self.fila,
                             self.columna)
            return TIPO_DATOS.ERROR

        tipo=self.valor.analizar(TS,Errores)
        if tipo==TIPO_DATOS.ERROR:
            return TIPO_DATOS.ERROR

        for nodo in self.dimensiones:
            tipo=nodo.analizar(TS,Errores)
            if tipo==TIPO_DATOS.ERROR:
                return TIPO_DATOS.ERROR

    def getC3D(self,TS):
        codigo=""
        codigo+=TS.makecomentario("DECLARACION DE ARREGLO "+self.nombre)
        temp=TS.getTemp()
        codigo+=self.valor.getC3D(TS)
        codigo+=temp+'='+self.valor.temporal+';\n'
        sim = TS.obtener(self.nombre)
        sim.posicion=temp

        return codigo

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

