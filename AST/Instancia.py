import AST.Nodo as Nodo
from Errores.N_Error import *
from TS.Tipos import *
from TS.Simbolo import *

class Instancia(Nodo.Nodo):

    def __init__(self, tipo, nombre,fila, columna,dimensioens=None):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.tipo = tipo
        self.dimensiones=dimensioens

    def analizar(self,TS,Errores):
        if TS.existestruct(self.tipo):
            Errores.insertar(N_Error("Semantico","Error instancia, no existe struct "+self.nombre,self.fila,self.columna))
            return TIPO_DATOS.ERROR

        if self.dimensiones is not None:
            dimensiones=len(self.dimensiones)
        else:
            dimensiones=0
        sim =Simbolo(self.tipo,self.nombre,"",TS.nombre,dimensiones)
        if not TS.push(sim):
            Errores.insertar(N_Error("Semantico",'Variable '+self.nombre+' ya esta definida',self.fila,self.columna))
            return TIPO_DATOS.ERROR

    def getC3D(self,TS):
        codigo=""
        codigo+=TS.makecomentario("Instancia de struct "+self.nombre+' de tipo '+self.tipo)
        temp = TS.getTemp()
        codigo += temp + '= array();\n'
        sim = TS.obtener(self.nombre)
        sim.posicion = temp
        return codigo


    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Instancia Struct'))
        grafica.edge(padre, nombrehijo)
        grafica.node('NodeN' + str(id(self)), label=(self.tipo))
        grafica.edge(nombrehijo, 'NodeN' + str(id(self)))
        grafica.node('NodeN2' + str(id(self)), label=(self.nombre))
        grafica.edge(nombrehijo, 'NodeN2' + str(id(self)))
        if self.dimensiones is not None:
            grafica.node('NodeS' + str(id(self)), label=('Dimensiones'))
            grafica.edge(nombrehijo, 'NodeS' + str(id(self)))
            for nodo in self.dimensiones:
                nodo.graficarasc('NodeS' + str(id(self)), grafica)
