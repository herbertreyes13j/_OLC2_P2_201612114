import AST.Nodo as Nodo
from Errores.N_Error import *
from TS.Tipos import *

class Struct(Nodo.Nodo):

    def __init__(self, nombre, atributos,fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.atributos=atributos



    def analizar(self,TS,Errores):
        temporal={}
        for nodo in self.atributos:
            if nodo.nombre in temporal:
                Errores.insertar(N_Error("Semantico","Nombre de atributo "+nodo.nombre+' repetido en struct '+self.nombre,
                                         self.fila,self.columna))
                return TIPO_DATOS.ERROR
            temporal[nodo.nombre]=nodo

    def getC3D(self,TS):
        codigo=""
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo = 'Node' + str(id(self))
        grafica.node(nombrehijo, label=('Struct'))
        grafica.edge(padre, nombrehijo)
        grafica.node('NodeN' + str(id(self)), label=(self.nombre))
        grafica.edge(nombrehijo, 'NodeN' + str(id(self)))
        grafica.node('NodeS' + str(id(self)), label=('Atributos'))
        grafica.edge(nombrehijo, 'NodeS' + str(id(self)))
        for nodo in self.atributos:
            nodo.graficarasc('NodeS' + str(id(self)), grafica)