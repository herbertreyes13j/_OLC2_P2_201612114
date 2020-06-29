import AST.Nodo as Nodo
from AST.Expresiones import *

class Asignacion(Nodo.Nodo):
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna

    def getC3D(self,TS,Global,Traductor):
        codigo=""
        return codigo;

    def graficarasc(self,padre,grafica):
        nombrehijo='Node'+str(id(self))
        grafica.node(nombrehijo,label=('Asignacion'))
        grafica.edge(padre,nombrehijo)
        grafica.node('Noden' + str(id(self)), label=(str(self.nombre)))
        grafica.edge(nombrehijo, 'Noden' + str(id(self)))

class AsignacionOp(Nodo.Nodo):
    def __init__(self, nombre,op, valor, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.op=op

    def getC3D(self,TS,Global,Traductor):
        codigo=""
        codigo+=Traductor.makecomentario("Asignacion tipo "+str(self.op)+' de variable '+self.nombre)
        hola = variable(self.nombre, self.fila, self.columna)
        codigo+=Traductor.makecomentario("Obteniendo posicion de variable")
        codigo+=hola.getPosicion(TS,Global,Traductor)
        pos=hola.temporal
        codigo+=Traductor.makecomentario("Obteniendo valor de expresion")
        codigo+=self.valor.getC3D(TS,Global,Traductor)

        if self.op=="=":
            codigo+=Traductor.changestack(hola.temporal,self.valor.temporal)
            return codigo
        else :
            codigo+=hola.getC3D(TS,Global,Traductor)
            temp=Traductor.getTemp()
            codigo+=Traductor.make3d(temp,hola.temporal,self.op.replace('=',""),self.valor.temporal)
            codigo+=Traductor.changestack(pos,temp)
            return codigo





        return codigo

    def graficarasc(self,padre,grafica):
        nombrehijo='Node'+str(id(self))
        grafica.node(nombrehijo,label=('Asignacion'))
        grafica.edge(padre,nombrehijo)
        grafica.node('Noden' + str(id(self)), label=(str(self.nombre)))
        grafica.edge(nombrehijo, 'Noden' + str(id(self)))
        grafica.node('Nodeo' + str(id(self)), label=(str(self.op)))
        grafica.edge(nombrehijo, 'Nodeo' + str(id(self)))
        self.valor.graficarasc(nombrehijo,grafica)

