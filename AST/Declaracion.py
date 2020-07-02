import AST.Nodo as Nodo
import TS.Tipos as Tipos
import TS.Simbolo as Simbolo
from Errores.N_Error import *
from TS.Tipos import *
from TS.TS import *

class Declaracion(Nodo.Nodo):

    def __init__(self, tipo, nombre, valor, fila, columna):
        self.nombre = nombre
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.tipo = tipo

    def analizar(self,TS,Errores):
        #Buscando si variable ya esta declarada
        sim = Simbolo.Simbolo(self.tipo.tipo, self.nombre, "", TS.nombre)
        if not TS.push(sim):
            Errores.insertar(N_Error("Semantico",'Variable '+self.nombre+' ya esta definida',self.fila,self.columna))
            return

        if self.valor is not None:
            tipo=self.valor.analizar(TS,Errores)
            if tipo==TIPO_DATOS.ERROR:
                return TIPO_DATOS.ERROR


    def getC3D(self,TS):
        codigo=""
        codigo+=TS.makecomentario("Declaracion de "+str(self.nombre))
        if self.valor==None:
            if self.tipo.tipo==Tipos.TIPO_DATOS.INT:
                val=0
            elif self.tipo.tipo==Tipos.TIPO_DATOS.FLOAT:
                val=0.0
            elif self.tipo.tipo==Tipos.TIPO_DATOS.CHAR:
                val='0'
        else:
            codigo+=self.valor.getC3D(TS)
            temp = TS.getTemp()
            if self.tipo.tipo == TIPO_DATOS.INT:
                tipo = "int"
            elif self.tipo.tipo == TIPO_DATOS.CHAR:
                tipo = "char"
            elif self.tipo.tipo == TIPO_DATOS.FLOAT or self.tipo.tipo == TIPO_DATOS.DOUBLE:
                tipo = "double"
            codigo += temp + '= (' + tipo + ')' + str(self.valor.temporal) + ';\n'
            val=temp
        temp = TS.getTemp()
        codigo += temp + '=' + str(val) + ';\n'

        sim=TS.obtener(self.nombre)
        sim.posicion=temp
        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo='Node'+str(id(self))
        grafica.node(nombrehijo,label=('Declaracion'))
        grafica.edge(padre,nombrehijo)
        grafica.node('Nodet'+str(id(self)),label=(str(self.tipo.tipo.name)))
        grafica.edge(nombrehijo,'Nodet'+str(id(self)))
        grafica.node('Noden' + str(id(self)), label=(str(self.nombre)))
        grafica.edge(nombrehijo, 'Noden' + str(id(self)))
        if self.valor is not None:
            self.valor.graficarasc(nombrehijo,grafica)


