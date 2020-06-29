import AST.Nodo as Nodo
import TS.Tipos as Tipos
import TS.Simbolo as Simbolo
from TS.TS import *

class Declaracion(Nodo.Nodo):

    def __init__(self, tipo, nombre, valor, fila, columna):
        self.nombre = nombre
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.tipo = tipo



    def getC3D(self,TS,Global,Traductor):
        codigo=""
        codigo+=Traductor.makecomentario("Declaracion de "+str(self.nombre))
        if self.valor==None:
            if self.tipo.tipo==Tipos.TIPO_DATOS.INT:
                val=0
            elif self.tipo.tipo==Tipos.TIPO_DATOS.FLOAT:
                val=0.0
            elif self.tipo.tipo==Tipos.TIPO_DATOS.CHAR:
                val='0'
        else:
            codigo+=self.valor.getC3D(TS,Global,Traductor)
            val=self.valor.temporal
        if TS is None:
            sim=Simbolo.Simbolo(self.tipo.tipo,self.nombre,Global.size,Global.nombre)
            Global.push(sim)
            codigo+=Traductor.changestack(sim.posicion,val)
        else:
            sim=Simbolo.Simbolo(self.tipo.tipo,self.nombre,TS.size,TS.nombre)
            TS.push(sim)
            temp=Traductor.getTemp()
            codigo+=Traductor.getfromP(temp,sim.posicion)
            codigo+=Traductor.changestack(temp,val)
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


