import AST.Nodo as Nodo
from AST.Expresiones import *
from TS.Simbolo import *

class Asignacion(Nodo.Nodo):
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna

    def analizar(self,TS,Errores):
        hola = variable(self.nombre,self.fila,self.columna)
        tipo=hola.analizar(TS,Errores)
        if tipo==TIPO_DATOS.ERROR:
            return TIPO_DATOS.ERROR


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

    def analizar(self,TS,Errores):
        hola = variable(self.nombre,self.fila,self.columna)
        tipo=hola.analizar(TS,Errores)
        if tipo==TIPO_DATOS.ERROR:
            return TIPO_DATOS.ERROR

        tipo=self.valor.analizar(TS,Errores)
        if tipo==TIPO_DATOS.ERROR:
            return TIPO_DATOS.ERROR


    def getC3D(self,TS):
        codigo=""
        codigo+=TS.makecomentario("Asignacion tipo "+str(self.op)+' de variable '+self.nombre)
        hola =TS.obtener(self.nombre)


        codigo+=self.valor.getC3D(TS)
        temp=TS.getTemp()
        if hola.tipo==TIPO_DATOS.INT:
            tipo="int"
        elif hola.tipo==TIPO_DATOS.CHAR:
            tipo="char"
        elif hola.tipo==TIPO_DATOS.FLOAT or hola.tipo.tipo==TIPO_DATOS.DOUBLE:
            tipo="double"
        codigo+=temp+'= ('+tipo+')'+str(self.valor.temporal)+';\n'
        if self.op=="=":

            codigo+=hola.posicion+'='+temp+';\n'
            return codigo
        else :
            codigo+=TS.make3d(hola.posicion,hola.posicion,self.op.replace('=',""),temp)
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

